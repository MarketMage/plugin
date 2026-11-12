# MarketMage

Product research and competitor monitoring for e-commerce sellers, inside Claude. Ask in plain words, and Claude reads the live market and answers like an analyst: what to sell, whether an idea is worth it, what a competitor sells and charges, what buyers complain about, and what changed since last week.

**Who it's for:** dropshippers, Amazon sellers, makers and resellers on Etsy and eBay, researchers and agencies, and brands.

**Website:** [marketmage.io](https://marketmage.io) · **Getting started, step by step:** [marketmage.io/start](https://marketmage.io/start/) · **Full documentation:** [the plugin's README](marketmage/README.md)

## Install

MarketMage costs nothing to install. It works on any Claude plan, Free included; the scheduled Monday briefing needs a paid plan (Pro, Max, Ultra, Team, Enterprise).

**On claude.ai or in the Claude desktop app**

1. Open **Customize** in the left sidebar, then the **Plugins** tab ([claude.ai/customize/plugins](https://claude.ai/customize/plugins)).
2. Click **Add**, then **Add marketplace**, then **Add from a repository**.
3. In the **URL** box, type `MarketMage/plugin`, choose **Use "MarketMage/plugin"** in the list that opens, then click **Sync**.
4. MarketMage appears on the Plugins page. Click **Add** next to it. Claude says "Marketmage is installed and ready to use". (A note may offer to grant the Claude GitHub App access for automatic syncing: you can skip it.)

Given MarketMage as a .zip file? Click **Add**, then **Upload plugin**, and pick the file. Uploading a newer version over it keeps your Apify connection.

**In Claude Code**

1. Type `/plugin marketplace add MarketMage/plugin`.
2. Then type `/plugin install marketmage@marketmage`.

From a shell, in one step: `claude plugin install marketmage --marketplace MarketMage/plugin`. A plugin you added on claude.ai also reaches Claude Code by itself, the next time you start it signed in to the same account.

**Connect your Apify account, once**

Apify is a web-data platform. MarketMage's research runs there, in your own Apify account, and Apify bills that account for each run, usually cents. A free Apify account works: it includes USD 5 of credit a month and needs no credit card. You can create one at [apify.com](https://apify.com) or while connecting.

1. In **Customize → Plugins**, open **MarketMage**, go to its **Connectors** tab and click **Connect** next to **apify**. In Claude Code, type `/mcp` and choose **apify**.
2. Claude shows an "Add custom connector" notice with the details filled in. Check the address starts with `https://mcp.apify.com/`, keep the details as they are and click **Add**.
3. Sign in to Apify, or create a free account, and approve. It is the only sign-in MarketMage needs.
4. Optional, fewer approval boxes: claude.ai asks before each Apify tool call until you change it. In **Customize → Connectors → apify → Tool permissions**, set **Read-only tools** and **Call Actor** to **Always allow**. MarketMage still waits for your yes before any paid run over USD 0.05 or anything recurring, and every run has a spending limit.

**Your first message:** type `/marketmage:start` for a short welcome, or ask "Can you check what allbirds.com sells and how they price it?" Asking Claude to *check* or *look up* something reads it live with MarketMage.

**Once MarketMage is in Claude's plugin directory,** you'll also find it under **Customize → Plugins → Discover** and add it there, with nothing to type (the directory shows on paid Claude plans). The steps above keep working.

Step by step, with pictures: [marketmage.io/start](https://marketmage.io/start/).

## What it costs

- **Installing costs nothing.** There is no subscription.
- **You pay per result, in your own Apify account,** at the prices on each actor's Apify Store page, usually cents a question. Apify's free plan includes USD 5 of credit a month.
- **Claude asks before anything over USD 0.05**, and before anything recurring, with one estimate, and waits for your yes. Every run has a spending limit a little above its estimate.
- Typical costs, job by job: [the plugin's README](marketmage/README.md#costs) and [marketmage.io/pricing](https://marketmage.io/pricing/).

## Help

- Setup, billing and questions: [marketmage.io/support](https://marketmage.io/support/) or support@marketmage.io.
- Bugs and ideas: [open an issue](https://github.com/MarketMage/plugin/issues). Never paste an API token or other secret into it.
- Security: email security@marketmage.io, never a public issue ([SECURITY.md](SECURITY.md)).

## This repository

The plugin users install is the [`marketmage/`](marketmage/) folder; its [README](marketmage/README.md) is the plugin's documentation and directory listing. Everything else here (evals, scripts, CI) is for development and never ships.

| Path | What it holds |
| --- | --- |
| `marketmage/` | The plugin: `.claude-plugin/plugin.json`, `.mcp.json`, `skills/`, `README.md`, `LICENSE` |
| `.claude-plugin/marketplace.json` | The marketplace, so `/plugin marketplace add MarketMage/plugin` then `/plugin install marketmage@marketmage` installs `marketmage/` |
| `evals/` | The eval suite and its Apify mocks |
| `scripts/` | Checks, reference sync, smoke test and the eval wrapper; `scripts/shared/` holds the shared references copied into each skill |
| `docs/release.md` | Go-live steps |

## Development

To load the plugin from a clone for one session: `claude --plugin-dir ./marketmage` (from the repository root).

| Command | What it does |
| --- | --- |
| `python3 scripts/check.py` | Static checks (also run in CI): skill frontmatter, no `$<digit>` in skills, references present, every rule line of the references kept through the split (`scripts/fixtures/`), every line of a slimmed SKILL.md kept in it or its own references (`scripts/fixtures/skill-*-before-split.md`), no reference file over 24 KiB (one read each on claude.ai), connector tools, no secrets, and the multi-turn evals' recorded first turns up to date (`scripts/eval_history.py --check`) |
| `python3 scripts/sync-references.py` | Rewrites each skill's `references/costs.md` from the actors' live Store prices in force now (public API, no sign-in; a future-dated price shows as "from <date>"), copies the shared references from `scripts/shared/` (the `judgement*.md` parts only into the skills `scripts/skills.json` gives them; skills read each part only at the step that needs it). An actor not public yet is priced from `scripts/pending-pricing.json` (refresh it with `--refresh-pending`, signed in to the Apify CLI as the actor's owner) and marked pending. Run it after any price change or publication; CI runs it with `--check` and fails when they're out of date. It also refreshes the multi-turn evals' recorded first turns (below) |
| `python3 scripts/smoke.py` | Runs each skill's actor calls for real on a small input, with caps; about $0.45 (per-skill totals printed). The export case needs `SMOKE_SHEET_URL` |
| `scripts/eval.sh --ablation none --runs 1 -j 4` | The eval suite in `evals/`: 201 cases with the Apify tools mocked from real run outputs, including impartiality and tone cases (good and bad ideas, pushback, a first-timer), red-team cases (planted instructions in results, and ordinary ad calls to action that are not; a counterfeit dupe, and an accessory that only names the brand it fits), misuse cases that pick up after a real MarketMage answer (fake reviews, a reviewer's identity, a word-for-word copy of a rival's listing, replica sourcing, agreeing prices with competitors), the seller profile and its lenses (three profiles on one idea, a dropship search, makers, a reseller's flip, its condition-bounded resale range, and an amazon.de product), onboarding (the welcome and where its answer goes, a bare greeting or "good morning", a missing connection), the cost line (one estimate with a soft note, the run's spending limit internal at max(1.5 × the estimate, the estimate + USD 0.15)), trust and access (who earns the money, a session allowance, injected allowance asks, an answer shape for screen readers), the visual fallback where no chart can be drawn (the tables kept, no chart code, nothing said about it), the notebook, the launch plan and its stop rule, routes known not to work (never tried), the complaint brief (US leaders' reviews read on Amazon UK and Germany, a hint kept apart from a complaint worth building on), the timing reading ("too late?" read as Early, Growing, Crowded at the top or Cooling, with the ten-more-sellers line), the sources by channel in find-products (a dropshipper's TikTok, lasting Meta ads and AliExpress single units, with each idea's backing named), going deeper in find-products (the vision questions with one estimate, the direction cards from one batched read, a converging turn that keeps set-aside ideas out), and "the version you'd build" in validate, rising searches read from the full results, the opportunity digest, the morning briefing (with its weekly scheduled run, which only reads), where a new watch's results go (the briefing by default, a channel only on request) and the proven-small-advertiser search. `claude plugin eval` reads evals only from inside the plugin folder, so the script runs it on a temporary copy of `marketmage/` plus `evals/` and copies the results back to `evals/results/`; it takes any `claude plugin eval` option |
| `python3 scripts/eval_history.py import <session.jsonl> <case>` | A multi-turn case (`case.yaml` with `context.history_file: history.jsonl`) resumes a recorded first turn: run the first message as a case with `--keep-temp`, then import the kept run's session file (`config/projects/*/<id>.jsonl`). It keeps only the conversation, drops thinking and machine paths, and refuses a recording that holds an email address. Skills read a reference once per conversation, so the next turn follows the copies inside the history: `refresh` rewrites them from `marketmage/` (sync-references.py runs it), and check.py fails when one is out of date |

Keep the plugin folder lean: `scripts/check.py` fails when `marketmage/` holds more than 512 files, a non-image file over 256 KiB, a `.DS_Store`, or anything outside the files the plugin needs.

## License

[PolyForm Shield 1.0.0](LICENSE), © 2026 Extoris LLC. See [SECURITY.md](SECURITY.md) to report a vulnerability (security reports are acknowledged within one business day) and [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue.
