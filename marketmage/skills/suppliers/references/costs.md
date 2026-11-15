# Costs

From the actors' Store pricing (regenerate with `scripts/sync-references.py`; CI fails when it is out of date).
Estimate with the Bronze column: the paid-plan price (Silver and Gold pay less), so no paid-plan user pays more than you said.
Where the Free column differs, free-plan users pay that price: at the approval, quote its figure too, in the same line ("This costs about USD 0.09 (about USD 0.17 on Apify's free plan), occasionally a little more if I need to dig deeper to answer you"), so they never pay more than you said either. These prices are for that one approval line before a yes (`running.md`, "Before any run"), never for cost lines elsewhere.
Every run also has a start event of $0.00005 per GB of memory.

## Estimate and spending limit

The approval line gives one estimate with a soft note: "This costs about USD 0.35, occasionally a little more if I need to dig deeper to answer you." No range, no ceiling and no spending-limit figure is said (`running.md`, "Before any run", items 4 to 6).
- **The estimate:** the counted worst case of what is planned (its high end), each event at its Bronze price × the count the input can return (change events included where the read repeats one this account made). Item 5's USD 0.25 bound for a go-ahead in the message compares the estimate, never the spending limit.
- **The spending limit (internal, never said):** max(1.5 × the estimate, the estimate + USD 0.15), from the estimate as said at the approval (the free-plan figure when higher), rounded up to the cent (said USD 0.17: limit USD 0.32); never above a budget or allowance the user gave. One run's `maxTotalChargeUsd` is the limit; several runs on one yes: each floored run gets its floor first (below), and the rest is split across the others in proportion to their high ends; when the floors together come to more than the limit, the limit is raised to their sum. It sits above the estimate so a job finishes instead of stopping part-way (owner's rule of 9 Nov 2026: a supplier read capped near its estimate stopped after 1 of 7 ideas; kept internal by the owner's change of 10 Nov 2026).
- **Floors** (per-search reserves the actor holds before it starts; a cap under one stops a read part-way): `supplier-price-finder`, its high end + USD 0.02 per idea per Alibaba source (AliExpress is read with `aliexpress-scraper`, which reserves nothing ahead, so its cap is the formula's share with no floor); `marketplace-search-scanner`, its high end + USD 0.02 per keyword per service marketplace (eBay, Etsy, Walmart, Target, Best Buy, Home Depot, Lowe's).
- **No yes needed** (estimate USD 0.05 or less): no line is said; the cap follows the same formula from the run's own high end.
- **Watches** keep their monthly estimate and their own Max cost per run (`watchlists.md`); this limit is for one-off checks.

- **This skill:** 3 ideas on Made-in-China plus AliExpress's top 3 each with their product pages (`aliexpress-scraper`, never more than 3) about USD 0.11 (about USD 0.13 on the free plan), spending limit USD 0.28; the single-unit check on 3 ideas (AliExpress's top 3 each, with their product pages) about USD 0.04 (about USD 0.06 on the free plan), spending limit USD 0.21; one idea on Made-in-China alone (about USD 0.025) or the single-unit check on one idea (about USD 0.013, USD 0.02 on the free plan) needs no yes (limits never said).
- **Floor:** a `supplier-price-finder` cap always leaves USD 0.02 per idea per Alibaba source above the high end: the actor reserves it before each search, and a cap near the estimate stopped a read after 1 of 7 ideas. When the formula gives less, the floor is the limit. The AliExpress read reserves nothing: its cap is the formula's.

## Prices

### `cleanpull/supplier-price-finder`: Supplier Price Finder: Wholesale & Landed Cost

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `product-summary` (main) | Product summary | $5.00 | $5.00 | $4.50 | $4.00 |
| `offer` | Supplier offer | $2.00 | $2.00 | $1.80 | $1.60 |
| `residential-request` | Request through residential proxy (add-on) | $7.00 | $7.00 | $7.00 | $7.00 |
| `provider-record` | Provider record | $3.00 | $3.00 | $2.70 | $2.40 |
| `provider-search` | Provider search | $20.00 | $20.00 | $20.00 | $20.00 |

### `cleanpull/aliexpress-scraper`: AliExpress Scraper: Real Dropshipping Prices

Default memory 512 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `listing` (main) | Product | $1.40 | $0.70 | $0.63 | $0.56 |
| `product-details` | Product page details | $5.00 | $3.50 | $3.15 | $2.80 |
| `review` | Review | $0.90 | $0.45 | $0.40 | $0.36 |

**From 2026-11-25:** `listing` becomes $1.50 on Free, $1.00 on Bronze, $0.90 on Silver, $0.80 on Gold+; `review` becomes $1.20 on Free, $0.90 on Bronze, $0.81 on Silver, $0.72 on Gold+. Before 2026-11-25, quote the current prices: the per-run estimates in the skills use them and run slightly low from that date (the spending limit covers the difference).

### `cleanpull/marketmage-notebook`: MarketMage Notebook: Saved Ideas & Seller Profile

Default memory 128 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `notebook-read` (main) | Notebook read | $0.20 | $0.20 | $0.20 | $0.20 |
| `notebook-entries-read` | Extra entry read | $0.010 | $0.010 | $0.010 | $0.010 |
| `notebook-write` | Notebook write | $0.30 | $0.30 | $0.30 | $0.30 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
