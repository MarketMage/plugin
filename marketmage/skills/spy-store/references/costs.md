# Costs

From the actors' Store pricing (regenerate with `scripts/sync-references.py`; CI fails when it is out of date).
Estimate with the Bronze column: the paid-plan price (Silver and Gold pay less), so no paid-plan user pays more than you said.
Where the Free column differs, free-plan users pay that price: quote it too, in the same line ("about USD 0.09; USD 0.17 on Apify's free plan"), so they never pay more than you said either.
Every run also has a start event of $0.00005 per GB of memory.

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

### `cleanpull/tech-stack-detector`: Tech Stack Detector: Website Technology Lookup

Default memory 1024 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `domain-result` (main) | Domain result | $3.00 | $2.00 | $1.80 | $1.60 |
| `domain-checked` | Domain checked | $0.50 | $0.50 | $0.45 | $0.40 |
| `tech-change` | Technology change | $5.00 | $5.00 | $4.50 | $4.00 |
| `extra-request` | Extra page or script | $0.30 | $0.30 | $0.27 | $0.24 |
| `browser-render` | Browser render | $5.00 | $5.00 | $4.50 | $4.00 |
| `history-snapshot` | History snapshot | $2.00 | $2.00 | $1.80 | $1.60 |
| `subdomain-discovery` | Subdomain discovery | $1.00 | $1.00 | $0.90 | $0.80 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |

### `cleanpull/any-store-product-monitor`: Price Tracker & Stock Monitor for Any Online Store

Default memory 1024 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `product` (main) | Product | $1.50 | $1.50 | $1.35 | $1.20 |
| `product-checked` | Product checked, unchanged | $0.50 | $0.50 | $0.45 | $0.40 |
| `residential-read` | Product from a protected store | $4.00 | $4.00 | $4.00 | $4.00 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `provider-record` | Provider record | $6.00 | $3.00 | $2.70 | $2.40 |
| `provider-search` | Provider search | $30.00 | $15.00 | $15.00 | $15.00 |

### `cleanpull/promotions-monitor`: Competitor Promotions & New Products Monitor

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `promotion` (main) | Promotion or launch | $2.00 | $2.00 | $1.80 | $1.60 |
| `page-checked` | Page checked | $1.00 | $1.00 | $0.90 | $0.80 |
| `residential-request` | Request through residential addresses | $6.00 | $6.00 | $6.00 | $6.00 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |

### `cleanpull/listing-quality-checker`: Listing Quality Checker: Product Page Audit & Score

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `audit` (main) | Page audit | $5.00 | $5.00 | $4.50 | $4.00 |
| `page-checked` | Page checked, unchanged | $0.60 | $0.60 | $0.55 | $0.50 |
| `residential-page` | Page through residential addresses | $7.00 | $7.00 | $7.00 | $7.00 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
