---
name: spy-store
description: Analyse a competitor's online store - catalogue size, price range, discounts, best sellers, new arrivals, the promotions it shows now (sales, codes, free-shipping threshold) and its recent launches, how well its product pages are built, and the apps and marketing tools it runs on (Shopify themes and apps, email, reviews, ads, payments). Use when someone gives a store's domain and asks what it sells, how it prices or promotes, what is selling or new, or what tech it uses. Works best on Shopify stores; other platforms get a product sample, promotions and the tech stack. Not for watching a store's promotions over time (use promo-watch) or for a fix list on one product page (use listing-audit).
---

# Spy on a store

Profile one competitor's store and say what a rival seller can learn from it. Read `references/running.md` first (costs, caps, tools, secrets). Prices are in `references/costs.md`.

`references/running.md` is the core; its parts are read only at their step (its first lines say when): `references/running-results.md` once results are in, before using them; `references/running-runs.md` also before a status message stands in for rows; `references/running-runs.md` before a data-provider read, when a run doesn't succeed, or when this chat already holds a run; `references/running-abroad.md` outside the US; `references/running-asks.md` when the user asks who runs this, offers an allowance, pastes a secret or asks for something MarketMage won't do.
- `references/known-limits.md`: routes established not to work, each with what to use instead: read in the same batch as `references/running.md`, before choosing any source (a store, a marketplace, a country, a keyword); never try a route it lists. `references/plain-words.md` (the words the user sees, for every answer) is read in that same batch.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. Ask only for

- **The store's domain:** `brand.com`.
- **Optional:** the part they care about (pricing, best sellers, new products, promotions, page quality, tools).

## 2. Runs

Start with the tech scan. It is cheap, and it tells you whether the store is on Shopify.

| Step | Actor | Input | Cost on paid plans |
| --- | --- | --- | --- |
| Tech stack | `cleanpull/tech-stack-detector` | `domains: ["brand.com"]`, `maxPagesPerDomain: 1` | **USD 0.003** |
| Shopify catalogue | `cleanpull/shopify-store-scraper` | `stores: ["brand.com"]`, `maxProductsPerStore: 250`, `storeSummary: true`, `bestSellerRank: true`, `bestSellerDepth: 20` | 250 × USD 0.0008 + USD 0.003 summary ≈ **USD 0.20** |
| Not Shopify | `cleanpull/any-store-product-monitor` | `sitemaps: ["brand.com"]`, `maxProductsPerSitemap: 30`, `includeVariants: false` | 30 × USD 0.0015 ≈ **USD 0.05** |
| Promotions and launches | `cleanpull/promotions-monitor` | `stores: ["brand.com"]`, `launchWindowDays: 30`, `maxLaunchesPerStore: 25` | USD 0.001 page check + USD 0.002 per promotion or launch row: usually **USD 0.02 to 0.06** |
| Product page quality | `cleanpull/listing-quality-checker` | `productUrls`: their top 1 to 3 best sellers' pages (from the catalogue run); if the user gives their own page to compare, put theirs in `productUrls` and the store's pages in `competitorUrls` | **USD 0.005 a page** |

- **Before the catalogue run:** give the one estimate and get a yes. Offer the promotions read with it, in the same estimate (the full profile, tech + 250 products + promotions: up to about USD 0.25 (with a spending limit)). Offer the page audit when the user cares how the store sells online, or wants to compare their own page.
- **Not Shopify:** if the tech scan says another platform, quote only the Any Store sample (about USD 0.05) and the promotions read (about USD 0.02) as the profile (about USD 0.07 with the tech scan), and leave the Shopify line out.
- **What actually sells (Shopify, offered by name):** `includeStock: true` adds published stock per variant (USD 0.0005 a product, about USD 0.125 for 250), and **from a second read a day or more later** units sold since the last read, sales per day and days of stock left, where the store publishes stock. Run it with `monitorName: "spy-<domain>"` so a later read, in this chat or another, compares with it; say the sales figures come with that second read.
- **A small store from the proven small advertisers search** (`ads-watch`, its store size already read): skip the tech scan when it's known to be Shopify, read the whole catalogue with `maxProductsPerStore: 50` (its `publishedProductsCount` × USD 0.0008 + USD 0.003 summary, about USD 0.02 for 20 products), and lead the answer with what they sell beside the advertised product and how they price it: that is the shape of a store the user could build.
- **Large Shopify stores:** offer `maxProductsPerStore: 1000` (its estimate at the yes: about USD 0.80) only if the user wants the whole catalogue. The summary's `productCount` and `catalogueComplete` say how much was read.

## 3. Read the results

- **Tech stack:** `ecommerce`, `marketingAutomation`, `payments`, `analytics`, `advertising`, and the Shopify `apps` and `theme` in the store summary. Name the tools a rival could copy: reviews, email and SMS, upsells, loyalty.
- **Store summary** (`recordType: "store"`):
  - `productCount`;
  - `priceMin`, `priceMedian` and `priceMax`;
  - `onSaleShare` and `averageDiscountPercent`: a discount-led store, or full price;
  - `inStockShare`;
  - `topProductTypes` and `topVendors`;
  - `bestSellers`.
- **Not Shopify (the Any Store sample):** there is no store summary row. From the 30 rows, work out and give: the price range and median (`price`), the share on sale (`onSale`), the share in stock (`inStock`), and the brands (`brand`). Say it is a 30-page sample of the sitemap, not the whole catalogue. Offer `maxProductsPerSitemap: 100` (its estimate at the yes: about USD 0.15) for a fuller picture, or `urlFilter` to read one category.
- **Promotions** (`recordType: "promotion"`): `type`, `text`, `code`, `threshold` and `thresholdCurrency`, `percentOff`, `confidence`, and on Shopify `markdown` (`sharePercent` of the newest products below compare-at price, `maxPercentOff`). Codes are only those the site prints. Bars drawn only by scripts aren't read.
- **Launches** (`recordType: "launch"`): `title`, `launchedAt`, `price`, `relaunch`. On Shopify they're dated by the store; elsewhere a one-off read shows none (launches need two runs).
- **Page audit:** `score`, `grade` and `topFixes`; what their page does well that the user's could copy (structured data for Google, images, shipping and returns markup).
- **Stock and sales** (with `includeStock`, from the second read): per product `unitsSoldSinceLastRun`, `salesPerDay`, `daysOfStockLeft`. Lead "what sells" with these when present; they're estimates from published stock, so a restock between reads hides sales.
- **Products** (read with `get-dataset-items`, `fields: "recordType,title,productType,priceMin,priceMax,onSale,available,publishedAt,bestSellerRank,url"`; the store summary is the row with `recordType: "store"`; read it in full): new arrivals (the latest `publishedAt`), the best-seller order (`bestSellerRank`), and price clusters.

## 4. Answer

- **A short profile:** what they sell, at what price, and how they sell (discounts, codes, free-shipping threshold, bundles, apps).
- **The visual moment, after the profile** (`references/running-results.md`, "Explaining results": "One visual, where it helps"; only where you can draw one, and otherwise nothing about it is said; never in the first answer to this skill's new reads, only in a follow-up turn: the full detail or list, a chart the user asks for, a deeper turn): **the catalogue by type**, one horizontal bar per product type in `topProductTypes` (its `products` count, at most 8), labelled with the name and the count, with the share on sale (`onSaleShare`) and the median price (`priceMedian`) in the title. Not for the 30-page sample of a store that isn't Shopify (it has no store summary). Caption: the store's domain, its `productCount` products and the date read. The same figures are given in one line of the answer as well.
- **Their top 5 sellers** and their newest 5 products (or launches).
- **What's on now:** the running promotion and the threshold, compared with the user's if known.
- **Three takeaways** for the user: a price gap, a product gap, a tactic or tool worth trying.
- **Going deeper: what it opens up for you** (the elevation layer). The answer's offer line, once per conversation, is "Want more on any part, or shall we go deeper on what this opens up for you?" On a yes: one question first, only when it isn't clear yet ("Would you rather match them, outflank them, or learn from how they sell?"); then 2 or 3 openings, each tied to one fact read in this chat, about 50 words each: a product they've advertised for 35 days or more (when their ads were read with `ads-watch`: proven, so worth checking with `validate`), a range on deep discount (`onSaleShare`, `averageDiscountPercent`, or a markdown: a soft spot), a gap in their catalogue or prices, or what buyers complain about in their shop's reviews (the `reviews-watch` read of their product pages, offered with its estimate when not read). Never an opening without its fact, and no verdict on it; then a one-line "Where we are" when something is ruled in or out, and one Next step. A read it needs gets its one estimate at the yes, and nothing else is said about cost.
- **Offer next steps:** watch this store's promotions and launches with `promo-watch`, its prices and new products with `price-watch` (whole-store mode), see and watch the ads it runs with `ads-watch`, compare catalogues with `gaps`, or export the catalogue with `export`. For more than one of these on the same store, offer them as one digest (`references/watchlists.md`, "One request, one digest").
