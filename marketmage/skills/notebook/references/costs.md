# Costs

From the actors' Store pricing (regenerate with `scripts/sync-references.py`; CI fails when it is out of date).
Estimate with the Bronze column: the paid-plan price (Silver and Gold pay less), so no paid-plan user pays more than you said.
Where the Free column differs, free-plan users pay that price: at the approval, quote its high end too, in the same line ("Usually USD 0.05–0.09 (up to USD 0.17 on Apify's free plan); it can't go over USD 0.50"), so they never pay more than you said either. These prices are for that one approval line before a yes (`running.md`, "Before any run"), never for cost lines elsewhere.
Every run also has a start event of $0.00005 per GB of memory.

## Range and ceiling

The approval line gives a range and a ceiling: "Usually USD 0.20–0.35; it can't go over USD 1." (`running.md`, "Before any run", items 4 to 6.)
- **High end:** the counted worst case, each event at its Bronze price × the count the input can return (change events included where the read repeats one this account made). **Low end:** what the read usually charges: the results such input usually returns, no change events. Item 5's USD 0.25 bound for a go-ahead in the message compares the high end, never the ceiling.
- **Ceiling:** about 3× the high end (the free-plan figure when higher), rounded up to the next of USD 0.15, 0.25, 0.50, 0.75, 1, 1.50, 2, 2.50, 3, then the next whole dollar; at least USD 0.50 for a multi-step check (two or more runs on one yes, or a check's rounds); never above a budget or allowance the user gave. It is the spending limit: one run's `maxTotalChargeUsd` is the ceiling; several runs on one yes split it in proportion to their high ends. Well above what the job should cost, so a job finishes instead of stopping part-way (owner's rule of 9 Nov 2026: a supplier read capped near its estimate stopped after 1 of 7 ideas).
- **No yes needed** (high end USD 0.05 or less): no line is said; the cap is about 3× the high end, at least USD 0.01.
- **Watches** keep their monthly estimate and their own Max cost per run (`watchlists.md`); this ceiling is for one-off checks.

- **This skill:** each notebook call is capped at USD 0.01 and needs no yes once the user has opted in.

## Prices

### `cleanpull/marketmage-notebook`: MarketMage Notebook: Saved Ideas & Seller Profile

Default memory 128 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `notebook-read` (main) | Notebook read | $0.20 | $0.20 | $0.20 | $0.20 |
| `notebook-entries-read` | Extra entry read | $0.010 | $0.010 | $0.010 | $0.010 |
| `notebook-write` | Notebook write | $0.30 | $0.30 | $0.30 | $0.30 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
