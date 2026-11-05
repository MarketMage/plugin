#!/usr/bin/env python3
"""Writes each skill's references/costs.md from the actors' live Store pricing, and copies the
shared references into the skills. The judgement files (`judgement*.md`) go only to the skills whose
skills.json entry has `"judgement"`: `true` for all of them, or a list of the ones the skill reads (a skill
that doesn't judge gets only what it names, for example the tone). Every other shared file goes to every
skill, and a file a skill no longer gets is removed from its references. Run after any price change:

    python3 scripts/sync-references.py

It reads the public actor details from api.apify.com (no sign-in). An actor that isn't public yet
has no public details: its pricing comes from `scripts/pending-pricing.json`, a snapshot read from
the private actor with the Apify CLI (`--refresh-pending`, signed in as the actor's owner), and its
table says the prices are pending publication. Once the actor is public, the live price replaces
the snapshot, and CI's check fails until costs.md is regenerated.

Prices come from the pricing entry in force now (the latest `pricingInfos` entry whose `startedAt`
is in the past). A future-dated entry is shown as "from <date>": its new events are listed with that
date and its price changes noted, so a scheduled change is never quoted early.

With --check it writes nothing and exits 1 when a costs.md is out of date (run in CI). A file
written before a scheduled price started still passes after the start date (it already shows it
"from <date>"); a pricing entry added since the file was written fails it. Set
SYNC_REFERENCES_NOW to an ISO date to check as of another day.
"""
from __future__ import annotations

import datetime
import json
import os
import pathlib
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
# The shipped plugin folder, from the marketplace's plugins[0].source (the one source of truth);
# everything else in the repo stays out of it.
sys.path.insert(0, str(ROOT / 'scripts'))
from plugin_dir import plugin_dir  # noqa: E402

PLUGIN = plugin_dir(ROOT)
SKILLS = json.loads((ROOT / 'scripts' / 'skills.json').read_text())
SHARED = ROOT / 'scripts' / 'shared'
PENDING = ROOT / 'scripts' / 'pending-pricing.json'
TIERS = [('FREE', 'Free'), ('BRONZE', 'Bronze'), ('SILVER', 'Silver'), ('GOLD', 'Gold+')]


def wanted(name: str, spec: dict) -> bool:
    """Whether the shared file `name` goes to this skill: a judgement file only as skills.json says
    (`"judgement": true` for all of them, or a list of names); every other shared file to every skill."""
    if not name.startswith('judgement'):
        return True
    flag = spec.get('judgement')
    return flag is True or (isinstance(flag, list) and name in flag)


def public_actor(name: str) -> dict | None:
    try:
        with urllib.request.urlopen(f'https://api.apify.com/v2/acts/cleanpull~{name}', timeout=30) as r:
            return json.loads(r.read())['data']
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def private_actor(name: str) -> dict:
    """The owner's view of a private actor, through the signed-in Apify CLI (never reads the token)."""
    r = subprocess.run(['npx', '-y', 'apify-cli@1.10.0', 'api', 'GET', f'/v2/acts/cleanpull~{name}'],
                       capture_output=True, text=True, timeout=300)
    d = json.loads(r.stdout)
    d = d.get('data', d)
    return {
        'title': d['title'],
        'defaultRunOptions': {'memoryMbytes': d['defaultRunOptions'].get('memoryMbytes')},
        'pricingInfos': d['pricingInfos'],
    }


def actor(name: str, pending: dict, refresh: bool) -> dict:
    a = public_actor(name)
    if a is not None:
        pending.pop(name, None)
        return a
    if refresh or name not in pending:
        if '--check' in sys.argv:
            raise SystemExit(f'{name}: not public and not in {PENDING.name}; run with --refresh-pending')
        pending[name] = private_actor(name)
    return {**pending[name], 'pending': True}


def money(v: float) -> str:
    per_k = v * 1000
    return f'${per_k:,.2f}' if per_k >= 0.1 else f'${per_k:,.3f}'


def started(p: dict) -> datetime.datetime:
    v = p.get('startedAt') or p.get('createdAt') or '1970-01-01T00:00:00Z'
    return datetime.datetime.fromisoformat(v.replace('Z', '+00:00'))


def utcnow() -> datetime.datetime:
    # SYNC_REFERENCES_NOW (ISO date) stands in for the clock, for testing the --check rule.
    v = os.environ.get('SYNC_REFERENCES_NOW')
    if v:
        return datetime.datetime.fromisoformat(v.replace('Z', '+00:00')).astimezone(datetime.timezone.utc)
    return datetime.datetime.now(datetime.timezone.utc)


def created(p: dict) -> datetime.datetime:
    v = p.get('createdAt') or p.get('startedAt') or '1970-01-01T00:00:00Z'
    return datetime.datetime.fromisoformat(v.replace('Z', '+00:00'))


def pricing_now(a: dict, as_of: datetime.datetime) -> tuple[dict, dict | None]:
    """The pricing in force at `as_of` (the latest entry whose startedAt has passed), and the next
    future-dated entry if one is scheduled. A scheduled change is never quoted before its date."""
    infos = sorted(a['pricingInfos'], key=started)
    past = [p for p in infos if started(p) <= as_of] or infos[:1]
    future = [p for p in infos if started(p) > as_of]
    return past[-1], (future[0] if future else None)


def check_times(actors: list[dict], now: datetime.datetime) -> list[datetime.datetime]:
    """The moments a costs.md could have been generated at and still be right: now, or any time
    since the newest pricing entry was created. A file written before a scheduled entry started
    stays valid after it starts (it already quoted it "from <date>"), so CI doesn't turn red on
    the day by itself; a pricing entry added after the file was written always fails the check."""
    newest = max((created(p) for a in actors for p in a['pricingInfos']), default=now)
    times = {now, min(newest, now)}
    for a in actors:
        for p in a['pricingInfos']:
            if newest <= started(p) <= now:
                times.add(started(p) - datetime.timedelta(seconds=1))
                times.add(started(p))
    return sorted(t for t in times if newest <= t <= now or t == now)


def tier_prices(e: dict) -> list[float]:
    tiered = e.get('eventTieredPricingUsd') or {}
    return [tiered.get(t, {}).get('tieredEventPriceUsd', e.get('eventPriceUsd', 0)) for t, _ in TIERS]


def table(name: str, a: dict, as_of: datetime.datetime) -> str:
    current, future = pricing_now(a, as_of)
    events = current['pricingPerEvent']['actorChargeEvents']
    lines = [f'### `cleanpull/{name}`: {a["title"]}', '']
    if a.get('pending'):
        lines += [
            '**Pending:** this actor is not public yet. Its prices below are the ones set on it, and apply once it is published. '
            'Until then, runs of it fail with "Actor not found": say the job is coming soon and offer the skill\'s other steps.',
            '',
        ]
    lines += [
        f'Default memory {a["defaultRunOptions"].get("memoryMbytes")} MB. Prices per 1,000 events, by Apify plan:',
        '',
        '| Event | What it is | ' + ' | '.join(t for _, t in TIERS) + ' |',
        '| --- | --- | ' + ' | '.join('---' for _ in TIERS) + ' |',
    ]
    for key, e in events.items():
        main = ' (main)' if e.get('isPrimaryEvent') else ''
        lines.append(f'| `{key}`{main} | {e["eventTitle"]} | ' + ' | '.join(money(p) for p in tier_prices(e)) + ' |')
    if future:
        date = started(future).date().isoformat()
        new = future['pricingPerEvent']['actorChargeEvents']
        for key, e in new.items():
            if key not in events:
                lines.append(f'| `{key}` | {e["eventTitle"]} (from {date}; not charged before) | '
                             + ' | '.join(money(p) for p in tier_prices(e)) + ' |')
        changed = [k for k in new if k in events and tier_prices(new[k]) != tier_prices(events[k])]
        gone = [k for k in events if k not in new]
        notes = []
        for k in changed:
            was, now = tier_prices(events[k]), tier_prices(new[k])
            moved = [f'{money(n)} on {t}' for (_, t), w, n in zip(TIERS, was, now) if w != n]
            kept = [t for (_, t), w, n in zip(TIERS, was, now) if w == n]
            notes.append(f'`{k}` becomes ' + ', '.join(moved) + (f' ({", ".join(kept)} unchanged)' if kept else ''))
        notes += [f'`{k}` is no longer charged' for k in gone]
        added = any(k not in events for k in new)
        lines += ['', f'**From {date}:** ' + ('; '.join(notes) + '. ' if notes else '')
                  + (f'The events marked "from {date}" start then. ' if added else '')
                  + ('Other prices stay the same. ' if not notes else '')
                  + f'Before {date}, quote the current prices.']
    return '\n'.join(lines)


def start_command() -> str:
    text = (PLUGIN / 'skills' / 'start' / 'SKILL.md').read_text()
    front, body = text.split('\n---\n', 1)
    body = body.replace('`references/', '`${CLAUDE_PLUGIN_ROOT}/skills/start/references/')
    # The command shares the skill's name (/marketmage:start), and Claude sees the command's
    # description, not the skill's: give it the skill's own, so "what is this?", "hi" or
    # "is this a scam?" reach it.
    import yaml  # PyYAML (pip install pyyaml)
    desc = yaml.safe_load(front.removeprefix('---\n'))['description']
    return ('---\ndescription: ' + json.dumps(desc, ensure_ascii=False) + '\n---\n\n'
            '<!-- Generated from skills/start/SKILL.md by scripts/sync-references.py: edit the skill, not this file. -->\n'
            + body)


def main() -> None:
    check = '--check' in sys.argv
    stale: list[str] = []
    cache: dict[str, dict] = {}
    pending = json.loads(PENDING.read_text()) if PENDING.exists() else {}
    before = json.dumps(pending, sort_keys=True)
    refresh = '--refresh-pending' in sys.argv
    for skill, spec in SKILLS.items():
        actors = spec['runs'] + spec['pricesOnly']
        refs = PLUGIN / 'skills' / skill / 'references'
        refs.mkdir(parents=True, exist_ok=True)
        for f in sorted(SHARED.glob('*.md')):
            if not wanted(f.name, spec):
                if (refs / f.name).exists():
                    if check:
                        stale.append(f'{PLUGIN.name}/skills/{skill}/references/{f.name} (not wanted)')
                    else:
                        (refs / f.name).unlink()
                continue
            if check:
                if not (refs / f.name).exists() or (refs / f.name).read_text() != f.read_text():
                    stale.append(f'{PLUGIN.name}/skills/{skill}/references/{f.name}')
            else:
                shutil.copy(f, refs / f.name)
        parts = [
            '# Costs',
            '',
            'From the actors\' Store pricing (regenerate with `scripts/sync-references.py`; CI fails when it is out of date).',
            'Estimate with the Bronze column: the paid-plan price (Silver and Gold pay less), so no paid-plan user pays more than you said.',
            'Where the Free column differs, free-plan users pay that price: quote it too, in the same line ("about USD 0.09; USD 0.17 on Apify\'s free plan"), so they never pay more than you said either.',
            'Every run also has a start event of $0.00005 per GB of memory.',
            '',
        ]
        for name in actors:
            if name not in cache:
                cache[name] = actor(name, pending, refresh)
        now = utcnow()

        def render(as_of: datetime.datetime) -> str:
            return '\n'.join(parts + [x for name in actors for x in (table(name, cache[name], as_of), '')])

        if check:
            have = (refs / 'costs.md').read_text() if (refs / 'costs.md').exists() else None
            if have is None or all(have != render(t) for t in check_times([cache[n] for n in actors], now)):
                stale.append(f'{PLUGIN.name}/skills/{skill}/references/costs.md')
        else:
            (refs / 'costs.md').write_text(render(now))
            print(skill, ', '.join(actors))
    # /marketmage:start: a plugin command takes the name before the skill of the same name, so the
    # command carries the start skill's own text (references pointed at the skill's folder).
    command = start_command()
    target = PLUGIN / 'commands' / 'start.md'
    if check:
        if not target.exists() or target.read_text() != command:
            stale.append(f'{PLUGIN.name}/commands/start.md')
    else:
        target.parent.mkdir(exist_ok=True)
        target.write_text(command)
    if check and json.dumps(pending, sort_keys=True) != before:
        stale.append(PENDING.name)
    elif not check:
        PENDING.write_text(json.dumps(pending, indent=1) + '\n')
        # The multi-turn evals' recorded first turns carry copies of these files: bring them up to date too.
        subprocess.run([sys.executable, str(pathlib.Path(__file__).with_name('eval_history.py')), 'refresh'], check=True)
    if check:
        if stale:
            print('Out of date (run scripts/sync-references.py):', ', '.join(stale))
            sys.exit(1)
        print('references up to date')


if __name__ == '__main__':
    main()
