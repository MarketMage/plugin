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

- **This skill:** a one-off ads read of 2 brands on Google, Meta and TikTok at 30 ads: usually USD 0.20–0.32, ceiling USD 1. Proven small advertisers (steps 1 and 3, two runs): usually USD 0.06–0.11 (up to USD 0.13 on the free plan), ceiling USD 0.50, split about USD 0.33 and 0.17.
- **Watches:** their monthly estimate and their own Max cost per run, as this skill and `watchlists.md` set out.

## Prices

### `cleanpull/ad-library-monitor`: Ad Library Monitor: Facebook, Google & TikTok Ads

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `watch-item-checked` (main) | Watch item checked | $1.00 | $1.00 | $0.90 | $0.80 |
| `ad` | Ad | $1.50 | $1.50 | $1.35 | $1.20 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `library-request` | Ad library request | $7.00 | $3.50 | $3.25 | $3.00 |

### `cleanpull/watch-digest`: Watch Digest: Price, Stock & Rank Changes

Default memory 128 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `digest` (main) | Digest | $5.00 | $5.00 | $4.50 | $4.00 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `item-watched` | Item watched | $0.25 | $0.25 | $0.22 | $0.20 |

### `cleanpull/shopify-store-scraper`: Shopify Scraper: Products, Stock & Sales Estimates

Default memory 1024 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `product-result` (main) | Product | $0.80 | $0.80 | $0.70 | $0.60 |
| `product-change` | Product change | $1.00 | $1.00 | $0.90 | $0.80 |
| `product-checked` | Unchanged product checked | $0.15 | $0.15 | $0.13 | $0.12 |
| `stock-tracking` | Stock and sales tracking | $0.50 | $0.50 | $0.45 | $0.40 |
| `market-price` | Price in another market | $0.30 | $0.30 | $0.27 | $0.24 |
| `store-summary` | Store summary | $3.00 | $3.00 | $2.70 | $2.40 |
| `comparison-result` | Cross-store comparison | $1.00 | $1.00 | $0.90 | $0.80 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |

### `cleanpull/alerts-sender`: Alerts Sender: Email, Slack, Discord & Teams

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `alert-delivered` (main) | Message delivered | $1.00 | $1.00 | $0.90 | $0.80 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
