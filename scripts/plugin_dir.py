#!/usr/bin/env python3
"""The shipped plugin folder: `.claude-plugin/marketplace.json`'s plugins[0].source, checked to be a
relative folder inside this repository. One place for every script (check.py, sync-references.py and
eval.sh, which runs `python3 scripts/plugin_dir.py` to print it)."""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def plugin_dir(root: pathlib.Path = ROOT) -> pathlib.Path:
    manifest = root / '.claude-plugin' / 'marketplace.json'
    try:
        source = json.loads(manifest.read_text())['plugins'][0]['source']
    except (OSError, ValueError, KeyError, IndexError, TypeError) as err:
        sys.exit(f'{manifest.relative_to(root)}: no plugins[0].source ({err})')
    if not isinstance(source, str) or source.startswith('/'):
        sys.exit(f'{manifest.relative_to(root)}: plugins[0].source must be a relative folder in this repository, not {source!r}')
    path = (root / source).resolve()
    if root not in path.parents or not (path / '.claude-plugin' / 'plugin.json').is_file():
        sys.exit(f'{manifest.relative_to(root)}: plugins[0].source {source!r} is not a plugin folder inside this repository')
    return path


if __name__ == '__main__':
    print(plugin_dir())
