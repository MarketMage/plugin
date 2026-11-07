# Costs

From the actors' Store pricing (regenerate with `scripts/sync-references.py`; CI fails when it is out of date).
Estimate with the Bronze column: the paid-plan price (Silver and Gold pay less), so no paid-plan user pays more than you said.
Where the Free column differs, free-plan users pay that price: quote it too, in the same line ("about USD 0.09; USD 0.17 on Apify's free plan"), so they never pay more than you said either.
Every run also has a start event of $0.00005 per GB of memory.

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
