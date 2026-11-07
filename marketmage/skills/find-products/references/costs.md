# Costs

From the actors' Store pricing (regenerate with `scripts/sync-references.py`; CI fails when it is out of date).
Estimate with the Bronze column: the paid-plan price (Silver and Gold pay less), so no paid-plan user pays more than you said.
Where the Free column differs, free-plan users pay that price: at the approval estimate, quote it too, in the same line ("up to about USD 0.09 (USD 0.17 on Apify's free plan), capped"), so they never pay more than you said either. These prices are for that one estimate before a yes (`running.md`, "Before any run"), never for cost lines elsewhere.
Every run also has a start event of $0.00005 per GB of memory.

### `cleanpull/amazon-bestsellers-tracker`: Amazon Best Sellers Scraper & Rank Tracker

Default memory 1024 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `chart-item` (main) | Product row | $1.50 | $1.50 | $1.35 | $1.20 |
| `item-change` | Change | $2.00 | $2.00 | $1.80 | $1.60 |
| `item-checked` | Unchanged product checked | $0.10 | $0.10 | $0.090 | $0.080 |
| `chart-summary` | Chart summary | $2.00 | $2.00 | $1.80 | $1.60 |
| `product-details` | Product details | $4.00 | $4.00 | $3.60 | $3.20 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |

### `cleanpull/tiktok-shop-sales-tracker`: TikTok Shop Scraper & Sales Tracker: Units per Day

Default memory 1024 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `product` (main) | Product | $3.00 | $2.00 | $1.80 | $1.60 |
| `product-checked` | Unchanged product (Changes only) | $0.50 | $0.50 | $0.45 | $0.40 |
| `product-details` | Product details | $1.00 | $1.00 | $0.90 | $0.80 |
| `source-summary` | Summary | $1.00 | $1.00 | $0.90 | $0.80 |

### `cleanpull/google-trends-scraper`: Google Trends Scraper & API

Default memory 4096 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `term-result` (main) | Term result | $1.00 | $1.00 | $0.90 | $0.80 |
| `comparison-result` | Comparison result | $1.50 | $1.50 | $1.30 | $1.10 |
| `calibrated-term` | Calibrated term | $10.00 | $10.00 | $9.00 | $8.00 |
| `trending-item` | Trending item | $1.00 | $1.00 | $0.90 | $0.80 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |

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

### `cleanpull/ad-library-monitor`: Ad Library Monitor: Facebook, Google & TikTok Ads

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `watch-item-checked` (main) | Watch item checked | $1.00 | $1.00 | $0.90 | $0.80 |
| `ad` | Ad | $1.50 | $1.50 | $1.35 | $1.20 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `library-request` | Ad library request | $7.00 | $3.50 | $3.25 | $3.00 |

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

### `cleanpull/amazon-product-scraper`: Amazon Product Scraper: Buy Box, Offers & BSR

Default memory 1024 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `product` (main) | Product | $3.00 | $3.00 | $2.70 | $2.40 |
| `product-offers` | Every seller's offer | $1.00 | $1.00 | $0.90 | $0.80 |
| `local-market` | Product read outside the US | $3.00 | $3.00 | $2.70 | $2.40 |
| `product-checked` | Product checked, unchanged | $0.50 | $0.50 | $0.45 | $0.40 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |

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

### `cleanpull/reviews-monitor`: Reviews Monitor: Shopify, Amazon & Trustpilot

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `rating-summary` (main) | Product rating summary | $3.00 | $3.00 | $2.70 | $2.40 |
| `review` | Review | $0.50 | $0.50 | $0.45 | $0.40 |
| `product-checked` | Product checked | $0.50 | $0.50 | $0.45 | $0.40 |
| `residential-request` | Request through home-network addresses | $6.00 | $6.00 | $6.00 | $6.00 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `provider-record` | Provider record | $6.00 | $3.00 | $2.70 | $2.40 |
| `provider-search` | Provider search | $6.00 | $3.00 | $3.00 | $3.00 |

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
