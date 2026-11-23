---
name: watchlists
description: List, read, pause, resume, change or stop the user's MarketMage watchlists - the price, MAP, rank, reviews, promotions, marketplace, ads and listing watches this plugin saved in their Apify account (tasks and schedules named cw-...) - and show their latest digest of changes, a history chart of a watched product, or what each client's watches cost over a period. Use when someone asks what they are watching with MarketMage, what one of their watches found, for a product's price or rank history, for a per-client cost report, or to pause, change or delete one. Not for other Apify tasks or schedules, and not for a briefing of what's new across everything since the last visit (use briefing).
---

Files named `shared/<name>.md` here are in the plugin's shared folder, `../../shared/` from this skill's folder; every other file named here or in them (`costs.md`, and this skill's own parts) is in this skill's own `references/` folder.

# Watchlists

Manage the watchlists that `price-watch`, `rank-watch`, `map-watch`, `reviews-watch`, `promo-watch`, `market-scan`, `ads-watch` and `listing-audit` created. The kinds, names and actors are in the table at the top of `shared/watchlists.md`. Read `shared/watchlists.md` (the tools and steps) and `shared/running.md` (the secrets rule). Prices are in `references/costs.md`.

`shared/running.md` is the core; its parts are read only at their step (its first lines say when): `shared/running-results.md` once results are in, before using them; `shared/running-runs.md` also before a status message stands in for rows; `shared/running-runs.md` before a slower read, when a run doesn't succeed, or when this chat already holds a run; `shared/running-abroad.md` outside the US; `shared/running-asks.md` when the user asks who runs this, offers an allowance, pastes a secret or asks for something MarketMage won't do.
- `shared/known-limits.md`: routes established not to work, each with what to use instead: read in the same batch as `shared/running.md`, before choosing any source (a store, a marketplace, a country, a keyword); never try a route it lists. `shared/plain-words.md` (the words the user sees, for every answer) is read in that same batch.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`shared/running.md`, "Running").

## List

- **Read** `apify-api-read` on `/v2/actor-tasks` (`{"limit": 50, "desc": true}`) and `/v2/schedules` (`{"limit": 50}`), paging with `offset` (50, 100…) while a page is full: the list carries each task's name and IDs, not its input, and a larger page can still exceed what the tool returns.
- **Keep** tasks named `cw-...` and the schedules that run them.
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
- **The total, only when it matters:** work out the enabled watches' monthly total and say it ("Your 6 watches: about USD 4.20 a month") only when the user asks what their watches cost, or in the free-plan line: on Apify's free plan (or when the plan isn't known), when the total is over USD 5, say that once the month's USD 5 is used Apify blocks runs until the next cycle, and offer weekly cadence or merging watches on the same stores into one digest (`shared/watchlists.md`, "One request, one digest").
- **A dashboard, offered in one line** (`shared/running-results.md`, "Explaining results": "Things people keep, offered"): after the list (or a week across every watch) with 2 or more watches, where this Claude can make an artifact: "Want a page you can reopen with all your watches?" On a yes, an artifact with each watch's latest state from the reads just made, its cadence and monthly cost, and a history chart per watched product where the runs were read ("A history chart", with the same rules). It shows the readings of the day it was made and says that date; asking again refreshes it. Offered once in a chat; never made unasked.
- **A label:** when the user asks for one client's or brand's watches ("only Acme's"), keep the tasks whose short name or title starts with that label (`shared/watchlists.md`, "Naming"), and say how many others were left out. Watches made without a label stay in the full list; offer a label for new ones.
- **None found:** say so and offer `price-watch`, `rank-watch` or `reviews-watch`.

## What changed

- **Get the last run:** `apify-api-read` on `/v2/actor-tasks/<taskId>/runs` with `{"limit": 1, "desc": true}` (its first item; no items means the watch hasn't run yet: say when its schedule first runs it). Never `/runs/last`: it fails for a watch that hasn't run. A run that didn't succeed may have no `DIGEST.md`: `shared/running.md`, "Running" ("Only a record that is there").
- **Watch Digest:**
  - read `DIGEST.md` from its `defaultKeyValueStoreId` with `get-key-value-store-record`;
  - for detail, read the dataset with `get-dataset-items` and `fields: "recordType,source,opportunity,what,title,keyword,detail,url"`.
  - Rows with `recordType: "digest"` hold the counts and each watcher's status.
  - The digest's sources are `stores`, `amazon`, `ranks`, `shopify`, `reviews`, `promotions`, `market`, `ads`, `tiktok`, `charts` and `trends`: explain each part as its skill says (`reviews-watch`, `promo-watch`, `market-scan`, `ads-watch`, step "Reading … later"; TikTok, charts and trends in `find-products`, step 6).
  - **Opportunities this week:** when `DIGEST.md` opens with this section (changes carrying `opportunity`: `searches`, `charts`, `tiktok`), lead with it, in its order: new rising searches and breakouts, then new chart entries, then TikTok products selling faster; then the rest by watcher. Read it as `find-products`, step 6 says, and end on one next move on the strongest, with no price ("Next step: validate 'dog lick mat'."); its estimate comes when the user takes it up and it needs a yes.
- **Barcode (MAP):**
  - read the dataset;
  - products with `changes` or `mapViolations` are the news;
  - `firstCheck: true` rows are the baseline.
  - Give the check time from each record's `scrapedAt`, and, past 10 violations, the 10 worst with the full list on request or in a sheet (`map-watch`, step 2).
  - An Amazon offer below or near MAP names no seller: offer the listing's sellers as `map-watch`, step 2 says, run on a yes.
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
- **Then:** watches that failed or stopped early this week, with the reason. The week's cost, per watch and in total, only when the user asks for it ("what did my watches cost this week?"):
  - **Watch Digest runs bill in parts:** a digest run's own charge covers only the digest and the items watched; each watcher (store pages, Amazon, ranks, reviews…) runs as its own run, billed there. So a digest run's figure alone undercounts.
  - **The exact figure** (for example when an agency rebills a client): for each digest run, read its `RUN_SUMMARY` (`watchers[].runId`), then each of those runs with `get-actor-run`, and add their charges to the digest run's. **A run's charge** is its `chargedEventCounts` × the event prices in that run's own `pricingInfo` (`pricingPerEvent.actorChargeEvents.<event>.eventPriceUsd`), the prices on the run's date, which is how Watch Digest itself prices its watcher runs. Only a run without `pricingInfo` is priced from `costs.md` (today's prices: say so). Never `usageTotalUsd`: for these pay-per-event actors it is Apify's platform usage, not what the run charged. Reading runs is free. Barcode, Listing Quality Checker and Catalog Matcher tasks bill in their own run.
  - **The quick figure:** the watch's estimate (from its kind's formula) × the runs that week, said as an estimate ("about USD 0.21, estimated from 7 checks"). Use it when the user wants an overview, and offer the exact sum.
- End with the one change worth acting on first, and why.

## A history chart

When the user asks to see a product's history ("30 days of price and BSR on B0X", "chart the Buy Box", "put it next to Keepa"), offer a chart and draw it on a yes:
- **The data, in this order:**
  - the watch's earlier runs: `/v2/actor-tasks/<taskId>/runs` with `{"limit": 50, "desc": true}` (paging with `offset` for longer), and each run's dataset with `get-dataset-items` and `fields: "recordType,what,changeType,title,from,to,detail,url,at,watcherIssues"`, keeping that product's rows (by its ASIN or URL) and each run's `digest` row (its `watcherIssues`), with the run's `status` from the runs list. Reading earlier runs is free: say so. Apify keeps a run's results only for its plan's retention period, so runs further back may be gone: say so when the chart stops short.
- **What a digest holds:** changes only, and only moves at or above the watch's threshold (`minPriceChangePercent`, 2% unless the task sets another; BSR moves of 10% or more). A **SUCCEEDED** run whose watcher for that product ran (no entry for that watcher in the digest row's `watcherIssues`) and has no row for the product means nothing moved past the threshold, so the line carries the last value forward to the next change, drawn as a **step line** (flat, then a step on the change date). A run that isn't SUCCEEDED, or whose watcher for that kind failed, stopped or didn't run (an entry in `watcherIssues`; on runs from before it, a `RUN_SUMMARY` `watchers[]` status other than SUCCEEDED), is **not** a reading: leave a gap in the line over those dates and name them under the chart ("no reading 12–14 Oct: the Amazon watcher failed"). The first value is the earliest change's `from`. Say in one line under the chart: the number of runs read, the first and last dates, that flat stretches mean no move past the threshold (smaller moves aren't recorded), and any gaps.
- **The chart:** `what: "Price"` as a price line, `"Best Sellers Rank"` as a BSR line on its own axis (lower is better: say so, or turn the axis upside down), and `"Buy Box"` changes as labelled markers on the date they happened (the winner's name, with the price where it moved). One product per chart; several products as small charts side by side.
- **How:** first, an inline visual in the reply where you can draw one (`shared/running-results.md`, "Explaining results": "One visual, where it helps"), with the artifact below offered in one line for a chart they want to keep or share, and made on a yes ("Things people keep, offered"). Where no inline visual can be drawn (Claude Code included), a chart the user asked for ("chart it") is made, as before: an artifact in this chat where Claude can make one (a chart the user can open and share), or a chart image or file where artifacts aren't available; otherwise a dated table of the changes; when they asked only for the history, the chart is offered in one line and made on a yes. Never invent points between real readings. The dated changes stay in a table under any chart (one row per change or missed reading, never a row per day with the last value filled in), and in the screen-reader or no-tables shape the history is told in dated sentences with no chart.
- Then one line of reading: the biggest move and when, and, for the Buy Box, how often it changed hands.

## A cost report per client

When the user asks what each client, brand or label cost over a period ("what did each client cost in October?", "Bondi Paws' bill this month"), for an invoice:
- **The period:** the dates the user names, in their time zone; "last month" is the last calendar month. Say the dates back in the answer.
- **The watches:** list the `cw-` tasks and schedules ("List"), and group them by label. **The label is the prefix before the first colon in the watch's title** (the task input's `title`, or the task description after "MarketMage: "): "Acme: competitor prices" → Acme (`shared/watchlists.md`, "Naming", writes it there and first in the short name). A short name alone never makes a label: `cw-price-competitors` or `cw-rank-eye-mask`, with a title such as "Competitor prices" and no prefix, has none, even though its short name has a first word. Or group them as the user says. Watches without a label go under "No label" with their cost, never shared out among clients and never given a client name made up from the short name; then offer once to put them under a client ("Which client are cw-price-competitors and cw-rank-eye-mask for?"), and add the label to their titles on a yes.
- **The runs in the period:** for each task, `/v2/actor-tasks/<taskId>/runs` with `{"limit": 50, "desc": true}`, paging with `offset` until a run started before the period; keep the runs that started in it, failed and aborted ones included, since a stopped run still charged what it read.
- **Each run's cost, the exact method** ("This week, across every watch": the digest run plus its watcher runs from `RUN_SUMMARY`, each priced from its `chargedEventCounts` × its own `pricingInfo` event prices; `costs.md` only for a run without `pricingInfo`; never `usageTotalUsd`).
- **A digest run with no `RUN_SUMMARY`** (it failed, was aborted or timed out before writing it; for a run that didn't succeed, its store's key list shows whether the record is there before any read: `shared/running.md`, "Running", "Only a record that is there"): its watchers may still have run and charged. Find them: for each watcher kind in the task's input (`productUrls` → `cleanpull~any-store-product-monitor`, `amazonAsins` → `cleanpull~amazon-product-scraper`, rank keywords → `cleanpull~amazon-keyword-rank-tracker`, `shopifyStores` → `cleanpull~shopify-store-scraper`, reviews → `cleanpull~reviews-monitor`, `promotionStores` → `cleanpull~promotions-monitor`, marketplace searches → `cleanpull~marketplace-search-scanner`, ads → `cleanpull~ad-library-monitor`, TikTok → `cleanpull~tiktok-shop-sales-tracker`, charts → `cleanpull~amazon-bestsellers-tracker`, Trends → `cleanpull~google-trends-scraper`), `get-actor-run-list` with that `actorId` and `desc: true`, paging with `offset`, and keep the runs that started between the digest run's `startedAt` and its `finishedAt`; a watcher run's `INPUT` record (`get-key-value-store-record` on its `defaultKeyValueStoreId`) has `monitorName: "digest-<the task's monitorName>"`, which tells it from another watch's run in the same minutes. Price them as above, and say that run's figure was found by its time window. When they can't be found or read, give the digest run's own charge and mark that run's figure as an estimate ("may miss its watcher runs"); never call the total exact then. Barcode, Listing Quality Checker and Catalog Matcher runs bill in their own run.
- **Many runs** (a daily digest is about 30 a month, each with a few watcher runs): say how many reads it takes, all free, and read them in parallel batches. For a quick figure first, the estimate × runs (as in "This week") is fine, said as an estimate, with the exact sum offered.
- **The answer, ready to paste into an invoice:** a table with one row per label: watches, runs, cost in USD (two decimals), and a total row. Then, per label, one line per watch on request. Say which figures are exact and which are estimates, and that Apify's own usage page (`https://console.apify.com/billing`) is the bill of record. In a currency the user works in, give it beside USD with the rate and its date.
- **As a spreadsheet, offered in one line** (`shared/running-results.md`, "Explaining results": "Things people keep, offered"): an xlsx file where this Claude makes files (Cowork), or a Google Sheet through a connected Google Drive; otherwise the table as CSV text to paste.
- Reading runs costs nothing; say so before the reads.

## A client brief

When the user asks for a client-ready brief (from a digest, a week of changes, a cost report or a `spy-store` profile): the headline, the three moves that matter with their reason and cost, and one table, in the client's name and without MarketMage's internal names (`cw-…`, run IDs). Then offer it in the form they want, using whatever this Claude can make: a Google Doc through a connected Google Drive, a PDF or Word file, or a document or page in this chat that they can copy. When none of these is available here, give it as clean text with headings, ready to paste into their own template. Their logo and colours come from them; never fetch a client's brand assets.

## Change

- **Pause:** `update-schedule` with `isEnabled: false`, for the watchlist's schedule.
- **Resume, or a new cadence:** show the monthly cost it means and get a yes first, then `update-schedule` with `isEnabled: true`, or the new cron expression and time zone.
- **Items:**
  - `get-actor-task`, edit only the item lists, and never add, change or remove any other field;
  - New items are read whole on their first run (their baseline: a Shopify store's 250 products about USD 0.20, an ad item up to USD 0.15, a reviews product about USD 0.013, a TikTok keyword about USD 0.06, a 100-rank chart about USD 0.15). Show **two figures**: the next run with the baseline, and a typical run after it (and its monthly cost). Get a yes first.
  - Set `maxRunCostUsd` to cover the baseline run (`shared/watchlists.md`, "Reading, pausing and changing"), and lower it to the typical figure once the baseline has run: offer that the next time the user reads this watch. Or, with a yes, run the baseline now with `call-actor` and keep the typical figure on the task.
  - `update-actor-task` with the whole input, keeping every other field as it was, `ENCRYPTED_VALUE:` fields unchanged.
  - Then read the task again with `get-actor-task` and check every encrypted field is still there (`shared/running-asks.md`, "Secrets"). If one is gone, say which saved setting it was (its label) and give the Console link, never asking for it in chat.
- **Adding reviews, promotions, marketplace searches or ads to an existing Watch Digest task:** raise `maxRunCostUsd` by the room their kind needs (`shared/watchlists.md`, step 3), or the digest will skip that watcher. Newly added ad items need **USD 0.18** of room for their first run (their baseline), then about USD 0.05.
- **Stop:** after the user confirms by name, pause its schedule with `update-schedule` (`isEnabled: false`): a paused watch runs and costs nothing.
- **Delete:** the plugin has no delete tool. Pause first (as in Stop), then give the exact links with the IDs filled in, and the steps, as `shared/watchlists.md`, "Deleting" sets out: `https://console.apify.com/schedules/<scheduleId>` for each schedule, then `https://console.apify.com/actors/tasks/<taskId>`.
- **Results somewhere else** (a spreadsheet, email or a chat app): say plainly, in one line, that this version reports the changes in their briefing in Claude (`shared/watchlists.md`, step 6), and promise nothing more. A key, password or link they paste is never used (`shared/running-asks.md`, "Secrets").

Never change or delete a task or schedule whose name doesn't start with `cw-`. Those belong to the user's other work.
