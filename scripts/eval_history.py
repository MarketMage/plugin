#!/usr/bin/env python3
"""Earlier turns for multi-turn evals (`evals/<case>/history.jsonl`, resumed through case.yaml's
`context.history_file`).

A history is a recorded first turn: a real eval run of the first message with the Apify tools mocked, so
the skill is already loaded and its references already read when the case's own prompt arrives. Because
skills read a reference only once per conversation, the copies of the plugin's files inside a history are
what Claude follows in the next turn. So they must be the current text:

  scripts/eval_history.py import <session.jsonl> <case> [<case>...]
      keep only the conversation from a kept eval run's session file (`--keep-temp`, then
      config/projects/*/<id>.jsonl), drop thinking, attachments and machine paths, and write it to
      each case; then refresh it.
  scripts/eval_history.py refresh
      rewrite every plugin file inside every history (a skill's body, each Read of a SKILL.md or a
      reference) from the files in marketmage/ as they are now. Run it after sync-references.py.
  scripts/eval_history.py --check
      fail when a history is out of date or holds anything private (check.py runs this).

Private means an email address, a home or temp path (/Users/<name>, /home/<name>, C:\\Users, /tmp,
/private/var/folders), a token (Apify, Anthropic, GitHub, email-service, Slack, Bearer) or an account ID
(userId, accountId, username= in a URL). import refuses a session that holds any of them and writes
nothing; refresh writes nothing while one is present. API message IDs (msg_...) are replaced with
msg_evalNNNN in order of first use, so records of one message stay grouped; requestId is dropped.

Only the plugin's files are refreshed: the recorded assistant text (for example prices quoted from
costs.md) stays as recorded and drifts when those files change; re-record when that matters. A Read that
used offset or limit is left as recorded.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from plugin_dir import plugin_dir  # noqa: E402

PLUGIN = plugin_dir()
BASE = '/eval/marketmage'  # where the plugin's files appear to live in a history
KEEP = {'user', 'assistant'}
DROP_KEYS = {'toolUseResult', 'promptId', 'gitBranch', 'entrypoint', 'permissionDecision', 'turnCompanion',
             'sourceToolAssistantUUID', 'requestId'}
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
# Addresses that are part of the plugin's own text or of the mocked data, not anyone's personal address.
EMAIL_OK = re.compile(r'@(marketmage\.io|cleanpull(-[a-z0-9]+)?\.(com|io)|example\.(com|org)|[a-z0-9-]+\.iam\.gserviceaccount\.com)$')
PRIVATE = {
    'a home path': re.compile(r'/(?:Users|home)/[^/\s"\\]+|[A-Za-z]:(?:\\)+Users'),
    'a temp path': re.compile(r'/private/var/folders|/var/folders/|(?<![\w.])/(?:private/)?tmp/'),
    'a token': re.compile(r'apify_api_[A-Za-z0-9]{10,}|sk-ant-[A-Za-z0-9_-]{10,}|gh[pousr]_[A-Za-z0-9]{20,}|'
                          r're_[A-Za-z0-9]{20,}|SG\.[A-Za-z0-9_-]{20,}|hooks\.slack\.com/services/T(?!0+/)[A-Z0-9]{8,}/|'
                          r'Bearer\s+[A-Za-z0-9._-]{16,}'),
    'an account ID': re.compile(r'userId\s*[=:]|"userId"|accountId\s*[=:]|"accountId"|[?&](?:username|user)='),
}
PLUGIN_PATH = re.compile(r'(/[^\s"\'`]*?)/(skills/[a-z-]+/(?:SKILL\.md|references/[a-z0-9-]+\.md)|skills/[a-z-]+)')


def histories():
    return sorted((ROOT / 'evals').glob('*/history.jsonl'))


def skill_body(skill: str) -> str:
    text = plugin_text(f'skills/{skill}/SKILL.md')
    m = re.match(r'---\n.*?\n---\n', text, re.S)
    return text[m.end():].lstrip('\n') if m else text


def read_format(rel: str) -> str:
    """The text Claude Code's Read tool returns for a whole file: numbered lines, tab-separated."""
    lines = plugin_text(rel).split('\n')
    if lines and lines[-1] == '':
        lines.pop()
    return '\n'.join(f'{n}\t{line}' for n, line in enumerate(lines, 1))


class MissingFile(Exception):
    pass


def plugin_text(rel: str) -> str:
    try:
        return (PLUGIN / rel).read_text()
    except FileNotFoundError:
        raise MissingFile(f'reads {BASE}/{rel}, which no longer exists; re-record it') from None


def rebase(text: str) -> str:
    return PLUGIN_PATH.sub(lambda m: f'{BASE}/{m.group(2)}', text)


def walk_strings(obj, fn):
    if isinstance(obj, str):
        return fn(obj)
    if isinstance(obj, list):
        return [walk_strings(x, fn) for x in obj]
    if isinstance(obj, dict):
        return {k: walk_strings(v, fn) for k, v in obj.items()}
    return obj


def refreshed(records: list[dict]) -> list[dict]:
    reads = {}  # tool_use_id -> plugin-relative path read
    msg_ids = {}  # recorded API message ID -> msg_evalNNNN
    out = []
    for rec in records:
        rec = json.loads(json.dumps(rec))
        rec.pop('requestId', None)
        mid = rec['message'].get('id')
        if isinstance(mid, str) and mid.startswith('msg_'):
            if mid not in msg_ids:
                msg_ids[mid] = mid if re.fullmatch(r'msg_eval\d{4}', mid) else f'msg_eval{len(msg_ids) + 1:04d}'
            rec['message']['id'] = msg_ids[mid]
        content = rec['message'].get('content')
        if rec['type'] == 'assistant' and isinstance(content, list):
            for block in content:
                if block.get('type') == 'tool_use' and block.get('name') == 'Read':
                    args = block.get('input', {})
                    path = args.get('file_path', '')
                    if path.startswith(BASE + '/') and 'offset' not in args and 'limit' not in args:
                        reads[block['id']] = path[len(BASE) + 1:]
        if rec['type'] == 'user' and isinstance(content, list):
            for block in content:
                if block.get('type') == 'tool_result' and block.get('tool_use_id') in reads:
                    block['content'] = read_format(reads[block['tool_use_id']])
                m = None
                if block.get('type') == 'text' and rec.get('isMeta'):
                    m = re.match(r'Base directory for this skill: \S+/skills/([a-z-]+)\n\n', block['text'])
                if m:
                    block['text'] = m.group(0) + skill_body(m.group(1))
        out.append(rec)
    return out


def load(path: pathlib.Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def dump(records: list[dict]) -> str:
    return ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records)


def emails(text: str) -> list[str]:
    return [e for e in EMAIL.findall(text) if not EMAIL_OK.search(e)]


def private(text: str) -> list[str]:
    """What private data the text holds, by kind (never the matched value itself)."""
    found = [f'{len(emails(text))} email address(es)'] if emails(text) else []
    found += [f'{len(rx.findall(text))}x {kind}' for kind, rx in PRIVATE.items() if rx.search(text)]
    return found


def import_session(src: pathlib.Path, cases: list[str]) -> None:
    kept, parent = [], None
    for rec in load(src):
        if rec.get('type') not in KEEP or rec.get('isSidechain'):
            continue
        content = rec.get('message', {}).get('content')
        if isinstance(content, list):
            content = [b for b in content if b.get('type') not in ('thinking', 'redacted_thinking')]
            if not content:
                continue
            rec['message']['content'] = content
        for key in DROP_KEYS:
            rec.pop(key, None)
        rec['cwd'] = '/eval/cwd'
        rec['parentUuid'] = parent
        parent = rec['uuid']
        kept.append(walk_strings(rec, rebase))
    try:
        text = dump(refreshed(kept))
    except MissingFile as e:
        sys.exit(f'{src}: {e}')
    found = private(text)
    if found:
        sys.exit(f'{src}: holds {", ".join(found)}; nothing written. Record a run without it, or remove it first')
    for case in cases:
        out = ROOT / 'evals' / case / 'history.jsonl'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text)
        print(f'wrote {out.relative_to(ROOT)} ({len(kept)} records)')


# The private-data gate's own test, run with every --check: each line must be refused, each safe line kept.
# (Built from parts so this file holds no token-shaped string itself.)
MUST_REFUSE = ['/Users/' + 'someone/Documents/x', '/home/' + 'runner/work/x', 'C:' + '\\\\Users\\\\x',
               '/private/var/' + 'folders/ab/T/marketmage-eval.XYZ', 'cwd /' + 'tmp/x', 'apify_' + 'api_' + 'A' * 24,
               'sk-' + 'ant-' + 'a' * 20, 'gh' + 'p_' + 'a' * 30, 'Bearer ' + 'a' * 20,
               'console.apify.com/account?' + 'userId=ZyX987', '{"' + 'userId": "x"}', 'someone@' + 'gmail.com',
               'x@' + 'cleanpull.attacker.com']
MUST_KEEP = ['/eval/marketmage/skills/start/SKILL.md', 'their username on the store', 'sheets@cleanpull.com',
             'cleanpull-sheets-1@proj.iam.gserviceaccount.com', 'https://marketmage.io/acceptable-use']


def selftest() -> list[str]:
    bad = [f'private-data gate misses: {s!r}' for s in MUST_REFUSE if not private(s)]
    return bad + [f'private-data gate wrongly refuses: {s!r}' for s in MUST_KEEP if private(s)]


def main(argv: list[str]) -> int:
    if argv[:1] == ['import'] and len(argv) >= 3:
        import_session(pathlib.Path(argv[1]), argv[2:])
        return 0
    if argv in (['refresh'], ['--check']):
        stale = selftest()
        for path in histories():
            text = path.read_text()
            try:
                new = dump(refreshed(load(path)))
            except MissingFile as e:
                stale.append(f'{path.relative_to(ROOT)}: {e}')
                continue
            except (json.JSONDecodeError, KeyError, TypeError) as e:
                stale.append(f'{path.relative_to(ROOT)}: not a valid history ({type(e).__name__}: {e}); re-record it')
                continue
            found = private(text) + private(new)
            if found:
                stale.append(f'{path.relative_to(ROOT)}: holds {", ".join(sorted(set(found)))}; remove it and re-record')
                continue
            if new != text:
                if argv == ['refresh']:
                    path.write_text(new)
                    print(f'refreshed {path.relative_to(ROOT)}')
                else:
                    stale.append(f'{path.relative_to(ROOT)}: out of date; run scripts/eval_history.py refresh')
        if stale:
            print('\n'.join(stale))
            return 1
        if argv == ['--check']:
            print(f'histories up to date ({len(histories())})')
        return 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
