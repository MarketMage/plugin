# MarketMage plugin repository

The plugin users install is the [`marketmage/`](marketmage/) folder; its [README](marketmage/README.md) is the plugin's documentation and directory listing. Everything else here (evals, scripts, CI) is for development and never ships. It works on every Claude plan, Free included; the Monday scheduled briefing uses Claude's scheduled tasks, on paid plans.

| Path | What it holds |
| --- | --- |
| `marketmage/` | The plugin: `.claude-plugin/plugin.json`, `.mcp.json`, `skills/`, `README.md`, `LICENSE` |
| `.claude-plugin/marketplace.json` | The marketplace, so `/plugin marketplace add MarketMage/plugin` then `/plugin install marketmage@marketmage` installs `marketmage/` |
| `evals/` | The eval suite and its Apify mocks |
| `scripts/` | Checks, reference sync, smoke test and the eval wrapper; `scripts/shared/` holds the shared references copied into each skill |
| `docs/release.md` | Go-live steps |

## Development

| Command | What it does |
| --- | --- |
| `python3 scripts/check.py` | Static checks (also run in CI): skill frontmatter, no `$<digit>` in skills, references present, every rule line of the references kept through the split (`scripts/fixtures/`), every line of a slimmed SKILL.md kept in it or its own references (`scripts/fixtures/skill-*-before-split.md`), no reference file over 24 KiB (one read each on claude.ai), connector tools, no secrets, and the multi-turn evals' recorded first turns up to date (`scripts/eval_history.py --check`) |
| `python3 scripts/sync-references.py` | Rewrites each skill's `references/costs.md` from the actors' live Store prices in force now (public API, no sign-in; a future-dated price shows as "from <date>"), copies the shared references from `scripts/shared/` (the `judgement*.md` parts only into the skills `scripts/skills.json` gives them; skills read each part only at the step that needs it). An actor not public yet is priced from `scripts/pending-pricing.json` (refresh it with `--refresh-pending`, signed in to the Apify CLI as the actor's owner) and marked pending. Run it after any price change or publication; CI runs it with `--check` and fails when they're out of date. It also refreshes the multi-turn evals' recorded first turns (below) |
| `python3 scripts/smoke.py` | Runs each skill's actor calls for real on a small input, with caps; about $0.45 (per-skill totals printed). The export case needs `SMOKE_SHEET_URL` |
| `scripts/eval.sh --ablation none --runs 1 -j 4` | The eval suite in `evals/`: 150 cases with the Apify tools mocked from real run outputs, including impartiality and tone cases (good and bad ideas, pushback, a first-timer), red-team cases (planted instructions in results, and ordinary ad calls to action that are not; a counterfeit dupe, and an accessory that only names the brand it fits), misuse cases that pick up after a real MarketMage answer (fake reviews, a reviewer's identity, a word-for-word copy of a rival's listing, replica sourcing, agreeing prices with competitors), the seller profile and its lenses (three profiles on one idea, a dropship search, makers, a reseller's flip and an amazon.de product), onboarding (the menu, a bare greeting or "good morning", a missing connection), trust and access (who earns the money, a session allowance, injected allowance asks, an answer shape for screen readers), the visual fallback where no chart can be drawn (the tables kept, no chart code, nothing said about it), the notebook, the launch plan and its stop rule, the opportunity digest, the morning briefing (with its weekly scheduled run, which only reads), where a new watch's results go (the briefing by default, a channel only on request) and the proven-small-advertiser search. `claude plugin eval` reads evals only from inside the plugin folder, so the script runs it on a temporary copy of `marketmage/` plus `evals/` and copies the results back to `evals/results/`; it takes any `claude plugin eval` option |
| `python3 scripts/eval_history.py import <session.jsonl> <case>` | A multi-turn case (`case.yaml` with `context.history_file: history.jsonl`) resumes a recorded first turn: run the first message as a case with `--keep-temp`, then import the kept run's session file (`config/projects/*/<id>.jsonl`). It keeps only the conversation, drops thinking and machine paths, and refuses a recording that holds an email address. Skills read a reference once per conversation, so the next turn follows the copies inside the history: `refresh` rewrites them from `marketmage/` (sync-references.py runs it), and check.py fails when one is out of date |

Keep the plugin folder lean: `scripts/check.py` fails when `marketmage/` holds more than 512 files, a non-image file over 256 KiB, a `.DS_Store`, or anything outside the files the plugin needs.

## License

[PolyForm Shield 1.0.0](LICENSE), © 2026 Extoris LLC. See [SECURITY.md](SECURITY.md) to report a vulnerability (security reports are acknowledged within one business day) and [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue.
