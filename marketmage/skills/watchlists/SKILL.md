---
name: watchlists
description: List, read, pause, resume, change or stop the user's MarketMage watchlists - the price, MAP, rank, reviews, promotions, marketplace, ads and listing watches this plugin saved in their Apify account (tasks and schedules named cw-...) - and show their latest digest of changes, a history chart of a watched product, or what each client's watches cost over a period. Use when someone asks what they are watching with MarketMage, what one of their watches found, for a product's price or rank history, for a per-client cost report, or to pause, change or delete one. Not for other Apify tasks or schedules, and not for a briefing of what's new across everything since the last visit (use briefing).
---

# Watchlists

Manage the watchlists that `price-watch`, `rank-watch`, `map-watch`, `reviews-watch`, `promo-watch`, `market-scan`, `ads-watch` and `listing-audit` created. The kinds, names and actors are in the table at the top of `references/watchlists.md`. Read `references/watchlists.md` (the tools and steps) and `references/running.md` (the secrets rule). Prices are in `references/costs.md`.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## List

- **Read** `apify-api-read` on `/v2/actor-tasks` (`{"limit": 50, "desc": true}`) and `/v2/schedules` (`{"limit": 50}`), paging with `offset` (50, 100…) while a page is full: the list carries each task's name and IDs, not its input, and a larger page can still exceed what the tool returns.
- **Keep** tasks named `cw-...`, the schedules that run them, and each one's export schedule if it has one (`cw-export-` plus the task name without `cw-`, created by the `export` skill). Show the export with its watchlist: tab, time, and cost a month.
- **For each, show:**
  - the name and kind (price, rank, MAP, reviews, promotions, market, ads, listing, TikTok, charts, trends or undercuts; a Watch Digest task can mix kinds: name each part; an opportunity digest, `cw-opps-`, mixes trends, charts and TikTok, and a launch-week watch, `cw-launch-`, prices, ranks and reviews);
  - item counts, from `get-actor-task` input lists:

    | Kind | Input lists |
    | --- | --- |
    | price | `productUrls`, `amazonAsins`, `shopifyStores` |
    | rank | `rankKeywords` × `rankAsins` |
    | reviews | `reviewProductUrls`, `reviewAsins`, `reviewTrustpilotDomains` |
    | promotions | `promotionStores` |
    | market | `marketKeywords` × (`marketAmazonMarketplaces` and each of eBay, Etsy, Walmart, Target, Best Buy in `marketSources`) |
    | MAP | `products` |
    | ads | `adAdvertisers` (+ `adKeywords`, `adGoogleAdvertiserIds`, `adMetaPageIds`) × `adPlatforms` |
    | listing | `productUrls` |
    | TikTok | `tiktokKeywords` (× `tiktokMaxProductsPerKeyword` products) |
    | charts | `chartCategories` × `chartTypes` × `chartMarketplaces` |
    | trends | `trendsTerms` (in `trendsGeo`) |
    | undercuts | `competitorStores` (against `yourStore`) |
  - the cadence, in words from the cron expression;
  - whether it's enabled, and the next run;
  - its **Max cost per run** (`maxRunCostUsd`);
  - the estimated monthly cost, worked out from the input with the formulas in the skill for its kind (`price-watch`, `rank-watch`, `map-watch`, `reviews-watch`, `promo-watch`, `market-scan`, `ads-watch`, `listing-audit`; TikTok, charts and the opportunity digest's Trends terms in `find-products`, step 5; undercuts in `gaps`, step 6).
- **The total:** end the list with the enabled watches' monthly total, export schedules included ("Your 6 watches: about USD 4.20 a month"). On Apify's free plan (or when the plan isn't known), when the total is over USD 5, say that once the month's USD 5 is used Apify blocks runs until the next cycle, and offer weekly cadence or merging watches on the same stores into one digest (`references/watchlists.md`, "One request, one digest").
- **A dashboard, offered in one line** (`references/running.md`, "Explaining results": "Things people keep, offered"): after the list (or a week across every watch) with 2 or more watches, where this Claude can make an artifact: "Want a page you can reopen with all your watches?" On a yes, an artifact with each watch's latest state from the reads just made, its cadence and monthly cost, and a history chart per watched product where the runs were read ("A history chart", with the same rules). It shows the readings of the day it was made and says that date; asking again refreshes it. Offered once in a chat; never made unasked.
- **A label:** when the user asks for one client's or brand's watches ("only Acme's"), keep the tasks whose short name or title starts with that label (`references/watchlists.md`, "Naming"), and say how many others were left out. Watches made without a label stay in the full list; offer a label for new ones.
- **None found:** say so and offer `price-watch`, `rank-watch` or `reviews-watch`.

## What changed

- **Get the last run:** `apify-api-read` on `/v2/actor-tasks/<taskId>/runs` with `{"limit": 1, "desc": true}` (its first item; no items means the watch hasn't run yet: say when its schedule first runs it). Never `/runs/last`: it fails for a watch that hasn't run. A run that didn't succeed may have no `DIGEST.md`: `references/running.md`, "Running" ("Only a record that is there").
- **Watch Digest:**
  - read `DIGEST.md` from its `defaultKeyValueStoreId` with `get-key-value-store-record`;
  - for detail, read the dataset with `get-dataset-items` and `fields: "recordType,source,opportunity,what,title,keyword,detail,url"`.
  - Rows with `recordType: "digest"` hold the counts, each watcher's status and the delivery status.
  - The digest's sources are `stores`, `amazon`, `ranks`, `shopify`, `reviews`, `promotions`, `market`, `ads`, `tiktok`, `charts` and `trends`: explain each part as its skill says (`reviews-watch`, `promo-watch`, `market-scan`, `ads-watch`, step "Reading … later"; TikTok, charts and trends in `find-products`, step 6).
  - **Opportunities this week:** when `DIGEST.md` opens with this section (changes carrying `opportunity`: `searches`, `charts`, `tiktok`), lead with it, in its order: new rising searches and breakouts, then new chart entries, then TikTok products selling faster; then the rest by watcher. Read it as `find-products`, step 6 says, and end on one next move on the strongest with its price in the same line ("Next step: validate 'dog lick mat', about USD 0.14"), never "I'll give you the cost".
  - **Alert settings** (`alertBelowRating`, `alertPriceDropPercent`, `alertRankMilestonesOnly`) narrow only the message sent; read the dataset for every change, and say how many the message left out when it matters.
- **Barcode (MAP):**
  - read the dataset;
  - products with `changes` or `mapViolations` are the news;
  - `firstCheck: true` rows are the baseline.
  - Give the check time from each record's `scrapedAt`, and, past 10 violations, the 10 worst with the full list on request or in a sheet (`map-watch`, step 2).
  - An Amazon offer below or near MAP names no seller: offer the listing's sellers as `map-watch`, step 2 says (about USD 0.004 an ASIN), with a yes.
  - A task description that lists authorised dealers ("Authorised dealers: …"): tag each violation as `map-watch`, step 2, "Dealer tags" says. Draft MAP notices on request, as that step says.
- **Older ads watchlists on Ad Library Monitor itself** (`cw-ads-…` tasks whose actor isn't Watch Digest): read the dataset; `recordType: "change"` rows (`change`: `new` or `stopped`) are the news. New ads watchlists use Watch Digest.
- **Catalog Matcher (undercuts, `cw-gaps-`):** read the summary rows in full (`recordType: "summary"`: `undercuts`, `newUndercuts`, `medianPriceIndex`, `matched`), then the changed rows with `fields: "recordType,catalogue,yourTitle,theirTitle,yourPrice,theirPrice,priceGapPercent,undercut,changes,theirUrl"`; rows whose `changes` include `undercut` (with `gapPercent`) are the news. `RUN_SUMMARY` gives `storeRuns`, `storeReadsCostUsd` and any rival skipped for its share. Explain it as `gaps` step 7 says.
- **Listing Quality Checker (listing):** read the dataset; `audit` rows with `changedChecks` (a check that moved, with its fix) and `change` rows (`removed`) are the news. A run that returns nothing means no page changed (`RUN_SUMMARY` outcome `NO_CHANGES`).
- **Explain it like an expert:**
  - the biggest moves first;
  - what they mean for the user;
  - any watcher that failed or stopped early, with its reason.
- **Several runs:** for "this week", use `/v2/actor-tasks/<taskId>/runs` with `{"limit": 7, "desc": true}` and summarise across them.

## This week, across every watch

When the user asks what changed across all their watches ("my week", "what happened this week"):
- list the `cw-` tasks as above, then read each one's runs of the last 7 days (`/v2/actor-tasks/<taskId>/runs`, `{"limit": 7, "desc": true}`) and, for each run, its digest or dataset as above. Reading costs nothing.
- **One summary, by theme, not by watch:** opportunities (from any digest's "Opportunities this week" section, first), prices (the biggest moves and stock-outs), ranks (milestones), reviews (new low ratings, rating moves), promotions and launches (a new product reported by both a store watcher and a promotions watcher is one launch, listed and counted once), markets (new entrants, price-band moves), ads (new and stopped), listings (score changes), TikTok (fastest sellers), charts (new entries and climbers), MAP (new violations). At most 10 rows a theme; skip a theme with nothing.
- **Then:** watches that failed or stopped early this week, with the reason; and the week's cost, per watch and in total:
  - **Watch Digest runs bill in parts:** a digest run's own charge covers only the digest and the items watched; each watcher (store pages, Amazon, ranks, reviews…) and the delivery run as their own runs, billed there. So a digest run's figure alone undercounts.
  - **The exact figure** (for example when an agency rebills a client): for each digest run, read its `RUN_SUMMARY` (`watchers[].runId` and `delivery.runId`), then each of those runs with `get-actor-run`, and add their charges to the digest run's. **A run's charge** is its `chargedEventCounts` × the event prices in that run's own `pricingInfo` (`pricingPerEvent.actorChargeEvents.<event>.eventPriceUsd`), the prices on the run's date, which is how Watch Digest itself prices its watcher runs. Only a run without `pricingInfo` is priced from `costs.md` (today's prices: say so). Never `usageTotalUsd`: for these pay-per-event actors it is Apify's platform usage, not what the run charged. Reading runs is free. Barcode, Listing Quality Checker and Catalog Matcher tasks bill in their own run.
  - **The quick figure:** the watch's estimate (from its kind's formula) × the runs that week, said as an estimate ("about USD 0.21, estimated from 7 runs"). Use it when the user wants an overview, and offer the exact sum.
- End with the one change worth acting on first, and why.

## A history chart

When the user asks to see a product's history ("30 days of price and BSR on B0X", "chart the Buy Box", "put it next to Keepa"), offer a chart and draw it on a yes:
- **The data, in this order:**
  - the rows of their history sheet (the `export` skill's appended changes), pasted, uploaded as a CSV, or opened through a connected Google Drive;
  - otherwise the watch's earlier runs: `/v2/actor-tasks/<taskId>/runs` with `{"limit": 50, "desc": true}` (paging with `offset` for longer), and each run's dataset with `get-dataset-items` and `fields: "recordType,what,changeType,title,from,to,detail,url,at,watcherIssues"`, keeping that product's rows (by its ASIN or URL) and each run's `digest` row (its `watcherIssues`), with the run's `status` from the runs list. Reading earlier runs is free: say so. Apify keeps a run's results only for its plan's retention period, so runs further back may be gone; the history sheet keeps them for good, and offer it for next time when it isn't set up.
- **What a digest holds:** changes only, and only moves at or above the watch's threshold (`minPriceChangePercent`, 2% unless the task sets another; BSR moves of 10% or more). A **SUCCEEDED** run whose watcher for that product ran (no entry for that watcher in the digest row's `watcherIssues`) and has no row for the product means nothing moved past the threshold, so the line carries the last value forward to the next change, drawn as a **step line** (flat, then a step on the change date). A run that isn't SUCCEEDED, or whose watcher for that kind failed, stopped or didn't run (an entry in `watcherIssues`; on runs from before it, a `RUN_SUMMARY` `watchers[]` status other than SUCCEEDED), is **not** a reading: leave a gap in the line over those dates and name them under the chart ("no reading 12–14 Oct: the Amazon watcher failed"). The first value is the earliest change's `from`. Say in one line under the chart: the number of runs read, the first and last dates, that flat stretches mean no move past the threshold (smaller moves aren't recorded), and any gaps.
- **The chart:** `what: "Price"` as a price line, `"Best Sellers Rank"` as a BSR line on its own axis (lower is better: say so, or turn the axis upside down), and `"Buy Box"` changes as labelled markers on the date they happened (the winner's name, with the price where it moved). One product per chart; several products as small charts side by side.
- **How:** first, an inline visual in the reply where you can draw one (`references/running.md`, "Explaining results": "One visual, where it helps"), with the artifact below offered in one line for a chart they want to keep or share, and made on a yes ("Things people keep, offered"). Where no inline visual can be drawn (Claude Code included), a chart the user asked for ("chart it") is made, as before: an artifact in this chat where Claude can make one (a chart the user can open and share), or a chart image or file where artifacts aren't available; otherwise a dated table of the changes; when they asked only for the history, the chart is offered in one line and made on a yes. Never invent points between real readings. The dated changes stay in a table under any chart (one row per change or missed reading, never a row per day with the last value filled in), and in the screen-reader or no-tables shape the history is told in dated sentences with no chart.
- Then one line of reading: the biggest move and when, and, for the Buy Box, how often it changed hands.

## A cost report per client

When the user asks what each client, brand or label cost over a period ("what did each client cost in October?", "Bondi Paws' bill this month"), for an invoice:
- **The period:** the dates the user names, in their time zone; "last month" is the last calendar month. Say the dates back in the answer.
- **The watches:** list the `cw-` tasks and schedules ("List"), and group them by label. **The label is the prefix before the first colon in the watch's title** (the task input's `title`, or the task description after "MarketMage: "): "Acme: competitor prices" → Acme (`references/watchlists.md`, "Naming", writes it there and first in the short name). A short name alone never makes a label: `cw-price-competitors` or `cw-rank-eye-mask`, with a title such as "Competitor prices" and no prefix, has none, even though its short name has a first word. Or group them as the user says. Export schedules (`cw-export-…`) go with their watch. Watches without a label go under "No label" with their cost, never shared out among clients and never given a client name made up from the short name; then offer once to put them under a client ("Which client are cw-price-competitors and cw-rank-eye-mask for?"), and add the label to their titles on a yes.
- **The runs in the period:** for each task, `/v2/actor-tasks/<taskId>/runs` with `{"limit": 50, "desc": true}`, paging with `offset` until a run started before the period; keep the runs that started in it, failed and aborted ones included, since a stopped run still charged what it read.
- **Each run's cost, the exact method** ("This week, across every watch": the digest run plus its watcher and delivery runs from `RUN_SUMMARY`, each priced from its `chargedEventCounts` × its own `pricingInfo` event prices; `costs.md` only for a run without `pricingInfo`; never `usageTotalUsd`).
- **A digest run with no `RUN_SUMMARY`** (it failed, was aborted or timed out before writing it; for a run that didn't succeed, its store's key list shows whether the record is there before any read: `references/running.md`, "Running", "Only a record that is there"): its watchers may still have run and charged. Find them: for each watcher kind in the task's input (`productUrls` → `cleanpull~any-store-product-monitor`, `amazonAsins` → `cleanpull~amazon-product-scraper`, rank keywords → `cleanpull~amazon-keyword-rank-tracker`, `shopifyStores` → `cleanpull~shopify-store-scraper`, reviews → `cleanpull~reviews-monitor`, `promotionStores` → `cleanpull~promotions-monitor`, marketplace searches → `cleanpull~marketplace-search-scanner`, ads → `cleanpull~ad-library-monitor`, TikTok → `cleanpull~tiktok-shop-sales-tracker`, charts → `cleanpull~amazon-bestsellers-tracker`, Trends → `cleanpull~google-trends-scraper`), `get-actor-run-list` with that `actorId` and `desc: true`, paging with `offset`, and keep the runs that started between the digest run's `startedAt` and its `finishedAt`; a watcher run's `INPUT` record (`get-key-value-store-record` on its `defaultKeyValueStoreId`) has `monitorName: "digest-<the task's monitorName>"`, which tells it from another watch's run in the same minutes. Do the same for `cleanpull~alerts-sender` (delivery) when one ran in that window. Price them as above, and say that run's figure was found by its time window. When they can't be found or read, give the digest run's own charge and mark that run's figure as an estimate ("may miss its watcher runs"); never call the total exact then. Barcode, Listing Quality Checker and Catalog Matcher runs bill in their own run. Export runs bill in their own run too (USD 0.0001 a row): `get-actor-run-list` with `actorId: "cleanpull~google-sheets-sync"`, keeping the runs in the period whose `INPUT` record's `taskId` is the watch's.
- **Many runs** (a daily digest is about 30 a month, each with a few watcher runs): say how many reads it takes, all free, and read them in parallel batches. For a quick figure first, the estimate × runs (as in "This week") is fine, said as an estimate, with the exact sum offered.
- **The answer, ready to paste into an invoice:** a table with one row per label: watches, runs, cost in USD (two decimals), and a total row. Then, per label, one line per watch on request. Say which figures are exact and which are estimates, and that Apify's own usage page (`https://console.apify.com/billing`) is the bill of record. In a currency the user works in, give it beside USD with the rate and its date.
- **As a spreadsheet, offered in one line** (`references/running.md`, "Explaining results": "Things people keep, offered"): an xlsx file where this Claude makes files (Cowork), or a Google Sheet through a connected Google Drive; otherwise the table as CSV text to paste. `export` writes a run's dataset, not this computed table, so it isn't the route here.
- Reading runs costs nothing; say so before the reads.

## A client brief

When the user asks for a client-ready brief (from a digest, a week of changes, a cost report or a `spy-store` profile): the headline, the three moves that matter with their reason and cost, and one table, in the client's name and without MarketMage's internal names (`cw-…`, run IDs). Then offer it in the form they want, using whatever this Claude can make: a Google Doc through a connected Google Drive, a PDF or Word file, or a document or page in this chat that they can copy. When none of these is available here, give it as clean text with headings, ready to paste into their own template. Their logo and colours come from them; never fetch a client's brand assets.

## Change

- **Pause:** `update-schedule` with `isEnabled: false`, for the watchlist's schedule and its export schedule if any.
- **Resume, or a new cadence:** show the monthly cost it means and get a yes first, then `update-schedule` with `isEnabled: true`, or the new cron expression and time zone. Do the same for its export schedule, keeping it 30 minutes after.
- **Items:**
  - `get-actor-task`, edit only the item lists;
  - New items are read whole on their first run (their baseline: a Shopify store's 250 products about USD 0.20, an ad item up to USD 0.15, a reviews product about USD 0.013, a TikTok keyword about USD 0.06, a 100-rank chart about USD 0.15). Show **two figures**: the next run with the baseline, and a typical run after it (and its monthly cost). Get a yes first.
  - Set `maxRunCostUsd` to cover the baseline run (`references/watchlists.md`, "Reading, pausing and changing"), and lower it to the typical figure once the baseline has run: offer that the next time the user reads this watch. Or, with a yes, run the baseline now with `call-actor` and keep the typical figure on the task.
  - `update-actor-task` with the whole input, keeping every `ENCRYPTED_VALUE:` field unchanged.
  - Then read the task again with `get-actor-task` and check every encrypted field is still there (`references/running.md`, "Secrets"). If one is gone, say which channel and give the Console link.
- **Delivery settings:** never in chat. Give `https://console.apify.com/actors/tasks/<taskId>/input` with the steps in `references/watchlists.md`, "Where the user pastes a setting".
- **Adding reviews, promotions, marketplace searches or ads to an existing Watch Digest task:** raise `maxRunCostUsd` by the room their kind needs (`references/watchlists.md`, step 3), or the digest will skip that watcher. Newly added ad items need **USD 0.18** of room for their first run (their baseline), then about USD 0.05.
- **Stop:** after the user confirms by name, pause its schedule and its export schedule with `update-schedule` (`isEnabled: false`): a paused watch runs and costs nothing.
- **Delete:** the plugin has no delete tool. Pause first (as in Stop), then give the exact links with the IDs filled in, and the steps, as `references/watchlists.md`, "Deleting" sets out: `https://console.apify.com/schedules/<scheduleId>` for each schedule, then `https://console.apify.com/actors/tasks/<taskId>`.
- **Email:** never set from chat, and never an address from context: the user enters the address, the sender and the key together on the task's input page (Watch Digest refuses an address without them); say what email needs and offer the free options first (`references/watchlists.md`, step 7).

Never change or delete a task or schedule whose name doesn't start with `cw-`. Those belong to the user's other work.
