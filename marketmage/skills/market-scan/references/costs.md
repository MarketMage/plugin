# Costs

From the actors' Store pricing (regenerate with `scripts/sync-references.py`; CI fails when it is out of date).
Estimate with the Bronze column: the paid-plan price (Silver and Gold pay less), so no paid-plan user pays more than you said.
Where the Free column differs, free-plan users pay that price: quote it too, in the same line ("about USD 0.09; USD 0.17 on Apify's free plan"), so they never pay more than you said either.
Every run also has a start event of $0.00005 per GB of memory.

### `cleanpull/marketplace-search-scanner`: Marketplace Search Scanner: Amazon, eBay, Etsy

Default memory 512 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `keyword-summary` (main) | Keyword summary | $3.00 | $3.00 | $2.70 | $2.40 |
| `listing` | Listing | $0.50 | $0.50 | $0.45 | $0.40 |
| `search-page` | Amazon search page | $2.00 | $2.00 | $1.80 | $1.60 |
| `residential-page` | Amazon page from home-network addresses | $12.00 | $12.00 | $12.00 | $12.00 |
| `market-change` | Market change | $1.00 | $1.00 | $0.90 | $0.80 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `provider-record` | Provider record | $6.00 | $3.00 | $2.70 | $2.40 |
| `provider-search` | Provider search | $30.00 | $15.00 | $15.00 | $15.00 |

### `cleanpull/watch-digest`: Watch Digest: Price, Stock & Rank Changes

Default memory 128 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `digest` (main) | Digest | $5.00 | $5.00 | $4.50 | $4.00 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `item-watched` | Item watched | $0.25 | $0.25 | $0.22 | $0.20 |

### `cleanpull/alerts-sender`: Alerts Sender: Email, Slack, Discord & Teams

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `alert-delivered` (main) | Message delivered | $1.00 | $1.00 | $0.90 | $0.80 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |

### `cleanpull/marketmage-notebook`: MarketMage Notebook: Saved Ideas & Seller Profile

Default memory 128 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `notebook-read` (main) | Notebook read | $0.20 | $0.20 | $0.20 | $0.20 |
| `notebook-entries-read` | Extra entry read | $0.010 | $0.010 | $0.010 | $0.010 |
| `notebook-write` | Notebook write | $0.30 | $0.30 | $0.30 | $0.30 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
