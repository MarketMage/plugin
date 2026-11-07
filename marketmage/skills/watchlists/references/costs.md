# Costs

From the actors' Store pricing (regenerate with `scripts/sync-references.py`; CI fails when it is out of date).
Estimate with the Bronze column: the paid-plan price (Silver and Gold pay less), so no paid-plan user pays more than you said.
Where the Free column differs, free-plan users pay that price: quote it too, in the same line ("about USD 0.09; USD 0.17 on Apify's free plan"), so they never pay more than you said either.
Every run also has a start event of $0.00005 per GB of memory.

### `cleanpull/watch-digest`: Watch Digest: Price, Stock & Rank Changes

Default memory 128 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `digest` (main) | Digest | $5.00 | $5.00 | $4.50 | $4.00 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `item-watched` | Item watched | $0.25 | $0.25 | $0.22 | $0.20 |

### `cleanpull/barcode-price-checker`: Barcode Price Checker: UPC & EAN Price Compare

Default memory 1024 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `product-result` (main) | Product with offers | $3.00 | $3.00 | $2.70 | $2.40 |
| `google-request` | Google Shopping search | $4.00 | $4.00 | $3.60 | $3.20 |
| `product-change` | Product with changes | $2.00 | $2.00 | $1.80 | $1.60 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `provider-record` | Provider record | $6.00 | $3.00 | $2.70 | $2.40 |
| `provider-search` | Provider search | $40.00 | $20.00 | $20.00 | $20.00 |

### `cleanpull/amazon-keyword-rank-tracker`: Amazon Keyword Rank Tracker: Organic & Sponsored

Default memory 512 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `search-page` (main) | Search page | $2.00 | $2.00 | $1.80 | $1.60 |
| `residential-page` | Search page from home-network addresses | $6.00 | $6.00 | $6.00 | $6.00 |
| `rank` | Product rank | $1.00 | $1.00 | $0.90 | $0.80 |
| `result` | Search result | $0.50 | $0.50 | $0.45 | $0.40 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `provider-record` | Provider record | $3.00 | $3.00 | $2.70 | $2.40 |
| `provider-search` | Provider search | $15.00 | $15.00 | $15.00 | $15.00 |

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

### `cleanpull/amazon-product-scraper`: Amazon Product Scraper: Buy Box, Offers & BSR

Default memory 1024 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `product` (main) | Product | $3.00 | $3.00 | $2.70 | $2.40 |
| `product-offers` | Every seller's offer | $1.00 | $1.00 | $0.90 | $0.80 |
| `local-market` | Product read outside the US | $3.00 | $3.00 | $2.70 | $2.40 |
| `product-checked` | Product checked, unchanged | $0.50 | $0.50 | $0.45 | $0.40 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |

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

### `cleanpull/promotions-monitor`: Competitor Promotions & New Products Monitor

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `promotion` (main) | Promotion or launch | $2.00 | $2.00 | $1.80 | $1.60 |
| `page-checked` | Page checked | $1.00 | $1.00 | $0.90 | $0.80 |
| `residential-request` | Request through residential addresses | $6.00 | $6.00 | $6.00 | $6.00 |
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

### `cleanpull/ad-library-monitor`: Ad Library Monitor: Facebook, Google & TikTok Ads

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `watch-item-checked` (main) | Watch item checked | $1.00 | $1.00 | $0.90 | $0.80 |
| `ad` | Ad | $1.50 | $1.50 | $1.35 | $1.20 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
| `library-request` | Ad library request | $7.00 | $3.50 | $3.25 | $3.00 |

### `cleanpull/listing-quality-checker`: Listing Quality Checker: Product Page Audit & Score

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `audit` (main) | Page audit | $5.00 | $5.00 | $4.50 | $4.00 |
| `page-checked` | Page checked, unchanged | $0.60 | $0.60 | $0.55 | $0.50 |
| `residential-page` | Page through residential addresses | $7.00 | $7.00 | $7.00 | $7.00 |
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

### `cleanpull/tiktok-shop-sales-tracker`: TikTok Shop Scraper & Sales Tracker: Units per Day

Default memory 1024 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `product` (main) | Product | $3.00 | $2.00 | $1.80 | $1.60 |
| `product-checked` | Unchanged product (Changes only) | $0.50 | $0.50 | $0.45 | $0.40 |
| `product-details` | Product details | $1.00 | $1.00 | $0.90 | $0.80 |
| `source-summary` | Summary | $1.00 | $1.00 | $0.90 | $0.80 |

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

### `cleanpull/catalog-matcher`: Catalog Matcher: Competitor Product Matching & Price Gaps

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `matched-pair` (main) | Matched pair | $2.00 | $2.00 | $1.80 | $1.60 |
| `gap-row` | Gap | $0.10 | $0.10 | $0.090 | $0.080 |
| `pair-checked` | Pair or gap checked, unchanged | $0.050 | $0.050 | $0.045 | $0.040 |
| `catalogue-compared` | Competitor catalogue compared | $50.00 | $50.00 | $50.00 | $50.00 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |

### `cleanpull/alerts-sender`: Alerts Sender: Email, Slack, Discord & Teams

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `alert-delivered` (main) | Message delivered | $1.00 | $1.00 | $0.90 | $0.80 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
