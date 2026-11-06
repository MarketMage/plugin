---
name: price-watch
description: Set up a scheduled watchlist that reports price, sale, stock, Buy Box and Best Sellers Rank changes on competitors' product pages (any online store), Amazon listings and whole Shopify stores (new and removed products, price moves, discounts), as one digest per run. It saves the watch in the user's Apify account as a task with its own daily or weekly schedule, and the user's MarketMage briefing in Claude reads its digests. Use when someone wants to be told when competitor prices, sales or stock change, or asks to watch or monitor product pages, Amazon listings or Shopify stores every day or week. For a one-off comparison use price-check; for Amazon keyword ranks use rank-watch.
---

# Price watch

Create a watchlist: one Watch Digest task and a schedule that runs it. Read these first:
- `references/running.md`: costs, caps, tools, and the secrets rule;
- `references/running.md` is the core; its parts are read only at their step (its first lines say when): `references/running-results.md` once results are in, before using them; `references/running-runs.md` before a data-provider read, when a run doesn't succeed, or when this chat already holds a run; `references/running-abroad.md` outside the US; `references/running-asks.md` when the user asks who runs this, offers an allowance, pastes a secret or asks for something MarketMage won't do.
- `references/watchlists.md`: the steps and naming;
- `references/costs.md`: the prices.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. Ask only for

- **What to watch**, any mix of:
  - product page URLs from any online store, as `productUrls`;
  - Amazon ASINs or URLs, as `amazonAsins`, with `amazonMarketplace`. Each ASIN is watched for its Buy Box (winner and price), price, stock, sellers joining or leaving, rating, and **Best Sellers Rank (BSR)**: Amazon's sales rank in the product's category, where a lower number means more recent sales; a move of 10% or more is reported;
  - whole Shopify stores by domain, as `shopifyStores`, with `maxProductsPerStore` (default 1,000; suggest 250 to start). When a store has more products than the cap, removed products aren't reported (a capped read can't tell removed from not reached): say so, and offer the store's full size when removals matter.
  - **Which 250, in one line when the store may have more:** the store's product feed lists its most recently published products first, so a cap of 250 reads the 250 newest. A launch is published at the top of that list, so **new launches are seen**; older products past the 250th aren't watched for price, stock or sales. A product re-published by the store comes back at the top: if an earlier run read it, it's compared with that last reading, so a price or stock move it reports can be months old; if no run read it before, it shows as new. A store that blocks its feed is read from its sitemap instead, in the sitemap's order, which isn't newest first: then launches past the cap can be missed (the run doesn't say which source it used). For the whole catalogue, raise the cap to the store's size (each further 250 products is one more item, USD 0.00025, plus their product reads).
- **How often:** daily at a time, or weekly.
- **Optional:**
  - the smallest price move worth reporting (`minPriceChangePercent`, for example 2);
  - whether to send a digest even when nothing changed (`sendWhenNoChanges`);
  - only real price cuts in the message (`alertPriceDropPercent`, for example 10; store products and Shopify stores; `references/watchlists.md`, "Alerts");
  - for Shopify stores, sales per day (`shopifyIncludeStock: true`): stock per variant and, from the second run, units sold and sales per day where the store publishes stock, at USD 0.0005 more per product read, every run (250 products ≈ USD 0.125 a run, about USD 3.75 a month daily, USD 0.55 weekly). Say the cost plainly; weekly is usually enough.

- **One request for several kinds** (a "competitor watch": prices, promotions and launches, ads for the same stores): offer one digest task for all of them (`references/watchlists.md`, "One request, one digest").
- **Amazon's delivery location:** Amazon is read as a signed-out shopper in the marketplace's own country, at Amazon's default delivery location (no postcode). Say it in one line when you set up an ASIN watch: the Buy Box and price can differ from what the user sees signed in at their own address.

## 2. Cost, per run (paid plans)

```
digest                              USD 0.005
+ items × USD 0.00025                  (item = product page, ASIN, or 250 products of a Shopify store)
+ store pages:   unchanged USD 0.0005, new or changed USD 0.0015
+ Amazon ASINs:  unchanged USD 0.0005, new or changed USD 0.003
                 outside the US (amazon.de, .co.uk, .co.jp…): + USD 0.003 per ASIN, every run (local-market read)
+ Shopify:       unchanged USD 0.00015 per product, change USD 0.001, first read USD 0.0008 per product
                 with shopifyIncludeStock: + USD 0.0005 per product, every run
+ Walmart, Target, Best Buy, eBay or Etsy pages: USD 0.003 each on top (provider record, every run)
                 + USD 0.015 per such marketplace per run (provider search)
+ delivery (once a channel is added): USD 0.001 per message
```

- **The first run** reads everything at the new or changed price. Later runs are mostly unchanged.
- **Amazon outside the US:** every ASIN read on a non-US marketplace adds USD 0.003 on every run, checks included, so an unchanged amazon.de ASIN costs USD 0.0035 and a changed one USD 0.006. Example: 10 amazon.de ASINs daily ≈ 0.005 + 10 × 0.00025 + 10 × 0.0035 ≈ USD 0.043 a run, about USD 1.28 a month. Fold it into `maxRunCostUsd`.
- **Walmart, Target, Best Buy, eBay and Etsy product pages** come through CleanPull's marketplace data service (nothing to set up): each page read costs its USD 0.003 record on every run, changed or not, and each of those marketplaces USD 0.015 a run. Example: 5 Walmart pages daily add 5 × 0.003 + 0.015 = USD 0.03 a run, about USD 0.90 a month. The digest takes a few minutes longer.
- **eBay links from Europe and the UK:** an ebay.de, ebay.co.uk or ebay.es item link is read as the same item on ebay.com (Any Store Product Monitor 0.2.5), at the eBay page price above; its price keeps the listing's own currency, never converted. eBay sold prices aren't available: only the current listing price.
- **Worked example:** 20 store pages and 10 ASINs, daily. The first run is about USD 0.08. A typical day is 0.005 + 30 × 0.00025 + 30 × 0.0005 ≈ **USD 0.03**, or about **USD 0.83 a month**.
- **Weekly** costs about a seventh: the worked example is about USD 0.13 a month. Offer it when daily moves don't matter.
- Show the user the first-run and monthly figures, and get a clear yes.

### Your own Buy Box, hourly

For the user's **own** ASINs, when they want to know quickly when they lose the Buy Box, an hourly watch is the one schedule faster than daily (`references/watchlists.md`, step 1). Only their own ASINs: rivals' listings stay daily.
- **What arrives:** set `changeTypes: ["buy-box"]` on this watch, so it reports only Buy Box changes on those ASINs: the Buy Box changing hands or being suppressed. With `sendWhenNoChanges: false` (the default), a message comes only on a run where that happened; price, stock, seller, rating and BSR moves are left out of this watch's digest (watcher problems are still reported). If they also want those, they belong on their daily watch, or, when they ask for them hourly, leave `changeTypes` out (every change type, with `minPriceChangePercent` keeping small price moves out) and say a price or BSR move then also sends one.
- **Cost:** 720 runs a month, so the digest fee leads: per run 0.005 + ASINs × (0.00025 + 0.0005). Example: 5 own ASINs hourly ≈ 0.005 + 5 × 0.00075 ≈ USD 0.009 a run, **about USD 6.30 a month**; every 4 hours (180 runs), about USD 1.58; daily, about USD 0.26. Show the hourly and 4-hourly figures and let them choose.

## 3. Create it

Follow `references/watchlists.md`, "Creating one":
- **Task:** `create-actor-task` for `cleanpull/watch-digest`, named `cw-price-<name>`, with this input:
  - `title`;
  - `monitorName: "<name>"`;
  - the item lists;
  - `minPriceChangePercent` and `sendWhenNoChanges`;
  - `alertPriceDropPercent` and `shopifyIncludeStock` if agreed;
  - `maxRunCostUsd`: about 1.5× the typical per-run cost (with the USD 0.003 per non-US ASIN in it), at least USD 0.02, plus, with Walmart, Target, Best Buy, eBay or Etsy pages, USD 0.003 per such page and USD 0.015 per such marketplace (see `references/watchlists.md`).

  No channel fields.
- **Same-day marketplace pages:** Walmart, Target, Best Buy, eBay and Etsy product pages that `price-check` read in this conversation today (rows returned) are not read again now (about USD 0.0045 a page and USD 0.015 a marketplace saved): the first scheduled run records their baseline (no changes for them that run). Say so in one plain sentence instead of paying for another read now, for example "The first scheduled run records these pages' prices, so their first change report comes with the run after it; today's prices are the ones you just saw." Run the baseline below with the other items only (that run's input without those pages; the task keeps them all), and skip it when nothing else is left. The task's `maxRunCostUsd`, with its room for these pages, already covers their first read. Every other item gets the baseline run.
- **Baseline run:** `call-actor` on `cleanpull/watch-digest` with the same input and a cap of about 1.5× the first-run estimate.
  - Poll until it's done.
  - Read `DIGEST.md` and the `digest` row (`watchers`, `baselineItems`).
  - Report how many items are now watched, and any watcher that failed, with its reason.
- **Schedule:** `create-schedule` with the task action and the cron expression in the user's time zone.
- **History, for ASIN watches:** a watch's history is read back at most 7 runs at a time, so for the last 30 or 90 days of price, Buy Box and BSR offer a **history sheet**: the `export` skill's export schedule after each run, appending each run's changes to a Google Sheet (`incremental: true`), at USD 0.0001 a row (a few cents a month). One line: "Keep a history sheet of these changes? (about USD <rows a month × 0.0001> a month)". From that sheet or the last runs, Claude can draw a price, BSR and Buy Box chart on request, free (`watchlists` skill, "A history chart").
- **Delivery:** the results go to "your briefing in Claude, on request or on a Monday schedule" (`references/watchlists.md`, step 7); don't offer or ask about a channel. **Only when the user asks for Slack, Discord, Teams, a webhook or email,** set it up as a follow-up: Slack, Discord, Teams or a webhook (free; the Slack steps and one channel per watch set in step 7), or email through the user's own sending service (step 7: what email needs, the free options first, and the address never taken from context). Give the Console link to add it: `https://console.apify.com/actors/tasks/<taskId>/input`. No delivery field is set from chat: for email, the user enters the address, the sender and the key together on that page (Watch Digest refuses an address without them, and every scheduled run would fail).

## 4. Reading a digest later

The `watchlists` skill reads the latest digest. When you explain one:
- group by watcher;
- lead with the biggest price moves and stock-outs;
- say what each means: a competitor undercutting, a rival out of stock (a chance to raise price or advertise), the Buy Box lost.
- **One line per new product:** when the same store is in `shopifyStores` and `promotionStores` (one digest, or a price watch and a promo watch), a launch shows twice: a "New product" from the store watcher and a launch from the promotions watcher. Report it once, with the launch (its date) and the price from the store watcher, and never count it twice in a total. A `relaunch` is an old product re-published, not a new one.
- **A history chart, on request** ("show me 30 days of price and BSR on B0X", "chart it"): see the `watchlists` skill, "A history chart" (an inline visual where one can be drawn; an artifact when the user wants to keep it).
