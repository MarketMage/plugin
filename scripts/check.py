#!/usr/bin/env python3
"""Static checks for the plugin (run in CI and before every commit):

- every skill has a SKILL.md whose `name` matches its folder and whose description fits;
- no SKILL.md contains `$<digit>` or `$ARGUMENTS` (Claude Code replaces those with the skill's
  arguments, so a price like "$0.005" would be mangled; write "USD 0.005");
- every skill has its references (every non-judgement file in scripts/shared/ and `costs.md`, and the
  `judgement*.md` files skills.json gives it, each of which its SKILL.md must point to);
- the split references still hold every line of the old ones (scripts/fixtures/*-before-split.md);
- the connector is https and its tools= list is exactly the allow-list below (no per-actor tools: they take
  no spending cap, so every run goes through call-actor);
- each skill's actors in skills.json are exactly the `cleanpull/<name>` actors its SKILL.md names;
- every "For you: <label>" in the skills and shared references is one of the four fixed labels,
  and no drifted label form appears;
- the shipped folder (marketplace.json's plugins[0].source, now marketmage/) holds only the plugin's
  files, at most 512, none of them a system file or a non-image over 256 KiB, with its README and LICENSE;
- no file holds something that looks like a real secret.
"""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
from urllib.parse import parse_qs, urlparse

try:
    import yaml  # PyYAML: frontmatter is parsed as Claude Code parses it, so invalid YAML fails here
except ImportError:
    sys.exit('check.py needs PyYAML: pip install pyyaml')

ROOT = pathlib.Path(__file__).resolve().parent.parent
# The shipped plugin folder, from the marketplace's plugins[0].source (the one source of truth);
# everything else in the repo stays out of it.
sys.path.insert(0, str(ROOT / 'scripts'))
from plugin_dir import plugin_dir  # noqa: E402

PLUGIN = plugin_dir(ROOT)
SHIP = PLUGIN.relative_to(ROOT).as_posix()  # the shipped folder, as messages name it
errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


skills = json.loads((ROOT / 'scripts' / 'skills.json').read_text())
SHARED = ROOT / 'scripts' / 'shared'
JUDGEMENT = sorted(f.name for f in SHARED.glob('judgement*.md'))
COMMON = sorted(f.name for f in SHARED.glob('*.md') if not f.name.startswith('judgement'))

# The split references keep every rule word for word: each non-blank line of the references as
# they were before the split (scripts/fixtures/<name>-before-split.md) must still be a line of
# some file in scripts/shared/. Only file names in backticks may differ (a section moved to a
# smaller file). When a rule is reworded on purpose, refresh the fixture in the same commit.
FILE_NAME = re.compile(r'`[a-z][a-z-]*\.md`')


def norm(line: str) -> str:
    return FILE_NAME.sub('`F.md`', line.strip())


shared_lines = {norm(line) for f in SHARED.glob('*.md') for line in f.read_text().splitlines()}
for fixture in sorted((ROOT / 'scripts' / 'fixtures').glob('*-before-split.md')):
    for n, line in enumerate(fixture.read_text().splitlines(), 1):
        if line.strip() and norm(line) not in shared_lines:
            fail(f'{fixture.name}:{n}: this line of the old reference is in no file in scripts/shared/: {line.strip()[:80]}')

for cmd in sorted((PLUGIN / 'commands').glob('*.md')):
    m = re.match(r'^---\n(.*?)\n---\n', cmd.read_text(), re.S)
    try:
        front = yaml.safe_load(m.group(1)) if m else None
    except yaml.YAMLError as e:
        fail(f'{SHIP}/commands/{cmd.name}: frontmatter is not valid YAML: {str(e).splitlines()[0]}')
        continue
    if not isinstance(front, dict) or not isinstance(front.get('description'), str):
        fail(f'{SHIP}/commands/{cmd.name}: frontmatter has no description string')
    elif len(front['description']) > 500:
        # claude.ai's plugin upload refuses a command description over 500 characters.
        fail(f'{SHIP}/commands/{cmd.name}: description is {len(front["description"])} characters; claude.ai allows 500')

manifest = json.loads((PLUGIN / '.claude-plugin' / 'plugin.json').read_text())
if len(manifest.get('description', '')) > 500:
    # claude.ai's plugin upload refuses a plugin description over 500 characters.
    fail(f'{SHIP}/.claude-plugin/plugin.json: description is {len(manifest["description"])} characters; claude.ai allows 500')

for name in skills:
    d = PLUGIN / 'skills' / name
    md = d / 'SKILL.md'
    if not md.exists():
        fail(f'{SHIP}/skills/{name}: no SKILL.md')
        continue
    text = md.read_text()
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        fail(f'{SHIP}/skills/{name}: no frontmatter')
        continue
    try:
        front = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        fail(f'{SHIP}/skills/{name}: SKILL.md frontmatter is not valid YAML: {str(e).splitlines()[0]}')
        continue
    if not isinstance(front, dict) or not isinstance(front.get('description'), str):
        fail(f'{SHIP}/skills/{name}: SKILL.md frontmatter has no description string')
        continue
    if front.get('name') != name:
        fail(f'{SHIP}/skills/{name}: frontmatter name is {front.get("name")!r}')
    if not 50 <= len(front.get('description', '')) <= 1024:
        fail(f'{SHIP}/skills/{name}: description length {len(front.get("description", ""))}')
    for bad in re.findall(r'\$(?:\d|ARGUMENTS)', text):
        fail(f'{SHIP}/skills/{name}: SKILL.md contains {bad!r}, which Claude Code replaces with arguments')
    flag = skills[name].get('judgement')
    judged = JUDGEMENT if flag is True else [f for f in JUDGEMENT if isinstance(flag, list) and f in flag]
    if isinstance(flag, list):
        for f in sorted(set(flag) - set(JUDGEMENT)):
            fail(f'{SHIP}/skills/{name}: skills.json lists {f}, which is not in scripts/shared/')
    for ref in COMMON + ['costs.md'] + judged:
        if not (d / 'references' / ref).exists():
            fail(f'{SHIP}/skills/{name}: missing references/{ref} (run scripts/sync-references.py)')
    # Every pointer resolves: each reference file named in the SKILL.md or in any of the skill's
    # own references (`references/<file>.md`, or a backticked `<file>.md` that is a shared
    # reference or costs.md) must be in this skill's own references/. The one scope: a skill that
    # gets no judgement part skips the common references' pointers into the judgement parts
    # (those passages are for the judgement skills: the profile, confidence, the answer structure).
    known = {f.name for f in SHARED.glob('*.md')} | {'costs.md'}
    have = {f.name for f in (d / 'references').glob('*.md')}
    pointers: dict[str, set[str]] = {}
    for src in [md] + sorted((d / 'references').glob('*.md')):
        key = 'SKILL.md' if src == md else src.name
        pointers[key] = set()
        for n, line in enumerate(src.read_text().splitlines(), 1):
            named = set(re.findall(r'references/([a-z][a-z-]*\.md)', line))
            named |= {f for f in re.findall(r'`([a-z][a-z-]*\.md)`', line) if f in known}
            for ref in sorted(named):
                if not judged and key in COMMON and ref in JUDGEMENT:
                    continue
                pointers[key].add(ref)
                if ref not in have:
                    where = 'SKILL.md' if src == md else f'references/{src.name}'
                    fail(f'{SHIP}/skills/{name}: {where}:{n} points to {ref}, which is not in its references/')
    # Every judgement part a skill gets is reachable from its SKILL.md through those pointers,
    # so it knows when to read each one.
    seen, todo = set(), ['SKILL.md']
    while todo:
        for ref in pointers.get(todo.pop(), ()):
            if ref not in seen:
                seen.add(ref)
                todo.append(ref)
    for ref in judged:
        if ref not in seen:
            fail(f'{SHIP}/skills/{name}: gets references/{ref} but no pointer from its SKILL.md leads to it')
    if flag is True and 'references/judgement.md' not in text:
        fail(f'{SHIP}/skills/{name}: a judgement skill must point to references/judgement.md')

for cmd in sorted((PLUGIN / 'commands').glob('*.md')):
    for bad in re.findall(r'\$(?:\d|ARGUMENTS)', cmd.read_text()):
        fail(f'{SHIP}/commands/{cmd.name} contains {bad!r}, which Claude Code replaces with arguments')

mcp = json.loads((PLUGIN / '.mcp.json').read_text())['mcpServers']['apify']
url = urlparse(mcp['url'])
if url.scheme != 'https':
    fail(f'{SHIP}/.mcp.json: the URL must be https')
tools = set(parse_qs(url.query).get('tools', [''])[0].split(','))
# No per-actor tools: Apify's per-actor tools take no spending cap (maxTotalChargeUsd), so call-actor,
# which carries it, is the only way the plugin starts a run. call-actor resolves any actor by name
# and validates the input against the actor's own input schema, so nothing else is needed.
ALLOWED = {
    'call-actor', 'get-actor-run', 'get-actor-run-list', 'get-dataset-items',
    'get-key-value-store-record', 'abort-actor-run',
    'create-actor-task', 'get-actor-task', 'update-actor-task',
    'create-schedule', 'get-schedule', 'update-schedule',
    'apify-api-read',
}
if tools:
    for extra in sorted(tools - ALLOWED):
        fail(f'{SHIP}/.mcp.json: {extra} is not on the allow-list')
    for missing in sorted(ALLOWED - tools):
        fail(f'{SHIP}/.mcp.json: {missing} is on the allow-list but not in tools=')
    for actor_tool in sorted(t for t in tools if '/' in t):
        fail(f'{SHIP}/.mcp.json: {actor_tool} is a per-actor tool, which carries no spending cap; runs go through call-actor')

for name, spec in skills.items():
    md = PLUGIN / 'skills' / name / 'SKILL.md'
    if md.exists():
        named = set(re.findall(r'cleanpull/([a-z-]+)', md.read_text()))
        if named != set(spec['runs']):
            fail(f'{SHIP}/skills/{name}: skills.json "runs" lists {sorted(spec["runs"])}, SKILL.md names {sorted(named)}')
        if set(spec['pricesOnly']) & named:
            fail(f'{SHIP}/skills/{name}: an actor is in both "runs" and "pricesOnly"')

# The For you verdict is one of four fixed strings (judgement.md, rule 7). Every "For you: <label>"
# the skills and shared references write must be one of them word for word, and the drifted forms
# seen in live answers must not appear outside the line that lists them as forbidden.
LABELS = ('a strong fit', 'a fit, with one fix', 'a long shot', 'not this one')
DRIFT = re.compile(r"there.s room, with one fix|fits, with one thing to fix|with one thing to fix first"
                   r"|\ba fit with one fix\b|\bfit, with a fix\b|\ba fit with a fix\b", re.I)
label_files = sorted((ROOT / 'scripts' / 'shared').glob('*.md')) + sorted((PLUGIN / 'skills').glob('*/SKILL.md')) \
    + sorted((PLUGIN / 'commands').glob('*.md'))
for f in label_files:
    for n, line in enumerate(f.read_text().splitlines(), 1):
        for m in re.finditer(r'For you: (?:\*\*)?([a-z][^\n]{0,40})', line):
            if not m.group(1).startswith(LABELS):
                fail(f'{f.relative_to(ROOT)}:{n}: "For you: {m.group(1)[:30]}" is not one of the fixed labels {LABELS}')
        if 'Never a paraphrase' not in line:
            for m in DRIFT.finditer(line):
                fail(f'{f.relative_to(ROOT)}:{n}: "{m.group(0)}" is a drifted For you label; use one of {LABELS}')

# The shipped folder: users get all of it and nothing else. The directory holds a plugin for a
# reviewer when it has more than 512 files or a non-image file over 256 KiB, and blocks .DS_Store
# and similar system files. When git is available, the files counted are those git tracks plus new
# files it doesn't ignore (a .DS_Store that .gitignore covers never ships); without git, every file
# in the folder counts.
SHIPPED_TOP = {'.claude-plugin', '.mcp.json', 'skills', 'commands', 'README.md', 'LICENSE'}
SYSTEM_FILES = {'.DS_Store', 'Thumbs.db', 'desktop.ini', '__MACOSX'}
IMAGE_OR_FONT = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.woff', '.woff2', '.ttf', '.otf'}
try:
    tracked = subprocess.run(['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard', '--', str(PLUGIN.relative_to(ROOT))], cwd=ROOT, capture_output=True, check=True).stdout
    shipped = [ROOT / p for p in tracked.decode().split('\0') if p and (ROOT / p).is_file()]
except (OSError, subprocess.CalledProcessError):
    shipped = []
if not shipped:
    shipped = [f for f in PLUGIN.rglob('*') if f.is_file()]
if len(shipped) > 512:
    fail(f'{SHIP}/: {len(shipped)} files; the directory holds a plugin with more than 512 for a reviewer')
for f in shipped:
    rel = f.relative_to(PLUGIN)
    if rel.parts[0] not in SHIPPED_TOP:
        fail(f'{SHIP}/{rel}: not part of the plugin; keep dev files outside {SHIP}/')
    if SYSTEM_FILES & set(rel.parts):
        fail(f'{SHIP}/{rel}: system file; remove it')
    elif f.suffix.lower() not in IMAGE_OR_FONT and f.stat().st_size > 256 * 1024:
        fail(f'{SHIP}/{rel}: over 256 KiB; the directory holds it for a reviewer')
for need in ('.claude-plugin/plugin.json', 'README.md', 'LICENSE'):
    if not (PLUGIN / need).is_file():
        fail(f'{SHIP}/{need}: missing')

SECRET = re.compile(r'(apify_api_[A-Za-z0-9]{20,}|re_[A-Za-z0-9]{20,}|SG\.[A-Za-z0-9_-]{20,}|hooks\.slack\.com/services/T(?!0+/)[A-Z0-9]{8,}/)')
for f in ROOT.rglob('*'):
    if f.is_file() and '.git' not in f.parts and 'results' not in f.parts and f.suffix in {'.md', '.json', '.jsonl', '.py', '.yml', '.yaml'}:
        if SECRET.search(f.read_text(errors='ignore')):
            fail(f'{f.relative_to(ROOT)}: looks like it holds a secret')

# Multi-turn evals resume a recorded first turn (evals/<case>/history.jsonl). Skills read a reference
# once per conversation, so the copies of the plugin's files inside a history are what the next turn
# follows: they must be today's text (scripts/eval_history.py refresh), and hold no email address.
history = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'eval_history.py'), '--check'], capture_output=True, text=True)
if history.returncode != 0:
    lines = [line for line in history.stdout.splitlines() if line]
    tail = ' | '.join(history.stderr.strip().splitlines()[-3:])
    errors.extend(lines or [f'scripts/eval_history.py --check failed (exit {history.returncode}): {tail or "no output"}'])
    if lines and tail:
        errors.append(f'scripts/eval_history.py stderr: {tail}')
for case in sorted((ROOT / 'evals').glob('*/case.yaml')):
    m = re.search(r'history_file:\s*(\S+)', case.read_text())
    if m and not (case.parent / m.group(1)).is_file():
        fail(f'{case.relative_to(ROOT)}: history_file {m.group(1)} does not exist')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'ok: {len(skills)} skills, {len(tools)} connector tools')
