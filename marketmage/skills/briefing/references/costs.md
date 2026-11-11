# Costs

From the actors' Store pricing (regenerate with `scripts/sync-references.py`; CI fails when it is out of date).
Estimate with the Bronze column: the paid-plan price (Silver and Gold pay less), so no paid-plan user pays more than you said.
Where the Free column differs, free-plan users pay that price: at the approval, quote its figure too, in the same line ("This costs about USD 0.09 (about USD 0.17 on Apify's free plan), occasionally a little more if I need to dig deeper to answer you"), so they never pay more than you said either. These prices are for that one approval line before a yes (`running.md`, "Before any run"), never for cost lines elsewhere.
Every run also has a start event of $0.00005 per GB of memory.

## Estimate and spending limit

The approval line gives one estimate with a soft note: "This costs about USD 0.35, occasionally a little more if I need to dig deeper to answer you." No range, no ceiling and no spending-limit figure is said (`running.md`, "Before any run", items 4 to 6).
- **The estimate:** the counted worst case of what is planned (its high end), each event at its Bronze price × the count the input can return (change events included where the read repeats one this account made). Item 5's USD 0.25 bound for a go-ahead in the message compares the estimate, never the spending limit.
- **The spending limit (internal, never said):** max(1.5 × the estimate, the estimate + USD 0.15), from the estimate as said at the approval (the free-plan figure when higher), rounded up to the cent (said USD 0.17: limit USD 0.32); never above a budget or allowance the user gave. One run's `maxTotalChargeUsd` is the limit; several runs on one yes split it in proportion to their high ends. It sits above the estimate so a job finishes instead of stopping part-way (owner's rule of 9 Nov 2026: a supplier read capped near its estimate stopped after 1 of 7 ideas; kept internal by the owner's change of 10 Nov 2026).
- **No yes needed** (estimate USD 0.05 or less): no line is said; the cap follows the same formula from the run's own high end.
- **Watches** keep their monthly estimate and their own Max cost per run (`watchlists.md`); this limit is for one-off checks.

- **This skill:** reading watches' digests starts no run; the notebook read is capped at USD 0.01. Watches use their monthly estimate and their own Max cost per run.

## Prices

### `cleanpull/marketmage-notebook`: MarketMage Notebook: Saved Ideas & Seller Profile

Default memory 128 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `notebook-read` (main) | Notebook read | $0.20 | $0.20 | $0.20 | $0.20 |
| `notebook-entries-read` | Extra entry read | $0.010 | $0.010 | $0.010 | $0.010 |
| `notebook-write` | Notebook write | $0.30 | $0.30 | $0.30 | $0.30 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |

### `cleanpull/watch-digest`: Watch Digest: Price, Stock & Rank Changes

Default memory 128 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `digest` (main) | Digest | $5.00 | $5.00 | $4.50 | $4.00 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `item-watched` | Item watched | $0.25 | $0.25 | $0.22 | $0.20 |
