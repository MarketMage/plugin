# Watchlists: saved tasks and schedules

A watchlist is one saved Apify task and one schedule that runs it.

| Kind | Task name | Actor |
| --- | --- | --- |
| Prices, stock, Shopify stores | `cw-price-…` | `cleanpull/watch-digest` |
| Amazon keyword ranks | `cw-rank-…` | `cleanpull/watch-digest` |
| Reviews | `cw-reviews-…` | `cleanpull/watch-digest` |
| Promotions and launches | `cw-promo-…` | `cleanpull/watch-digest` |
| Marketplace searches | `cw-market-…` | `cleanpull/watch-digest` |
| MAP by barcode | `cw-map-…` | `cleanpull/barcode-price-checker` |
| Competitor ads | `cw-ads-…` | `cleanpull/watch-digest` |
| Listing health | `cw-listing-…` | `cleanpull/listing-quality-checker` |
| TikTok Shop sales per day | `cw-tiktok-…` | `cleanpull/watch-digest` |
| Amazon chart moves | `cw-charts-…` | `cleanpull/watch-digest` |
| Opportunities this week (Trends rising searches, chart new entries, TikTok speeding up) | `cw-opps-…` | `cleanpull/watch-digest` |
| Launch week (the leaders' prices, ranks and reviews) | `cw-launch-…` | `cleanpull/watch-digest` |
| Undercuts on Shopify rivals | `cw-gaps-…` | `cleanpull/catalog-matcher` |

Watch Digest is the default because it makes one digest a run, which the `briefing` and `watchlists` skills read in Claude; one Watch Digest task may mix kinds (for example prices and reviews), named for its main kind. Listing Quality Checker, Barcode Price Checker and Catalog Matcher make no digest: their results stay in the run's dataset in Apify, and the `watchlists` skill reads them.

The user owns both in their own Apify account and pays for each run at the prices in `costs.md`.

**One request, one digest.** When one request covers several kinds for the same stores, brands or products (for example a "competitor watch": their prices, promotions and launches, and ads), offer them as **one Watch Digest task**, named for its main kind, instead of a task per kind: one schedule, one digest per run, one monthly figure, and one digest fee (USD 0.005 a run) instead of one per task. Its input carries each kind's lists (`productUrls` or `shopifyStores`, `promotionStores`, `adAdvertisers`…). With ads in it, always pass `adPlatforms` (it includes TikTok by default), leaving TikTok out when the user's market is outside the EU, the UK and Switzerland. Quote it as one figure: each kind's per-run formula from its skill, with the digest fee counted once; its `maxRunCostUsd` adds each kind's room (step 3). Offer separate tasks only when the user wants different cadences (prices daily, ads weekly). MAP, listing-health and undercut watches run on their own actors and stay separate tasks.

## Naming

- **Task name:** `cw-<kind>-<short-name>`, for example `cw-price-competitors` or `cw-rank-water-bottles`. Use lower case, digits and dashes, 3 to 63 characters.
- **The same short name goes in the input's `monitorName`** (`watchlistName` for Marketplace Search Scanner run on its own). Runs with the same monitor name compare against each other, so never reuse a name for a different list.
- **Schedule name:** the task name.
- **Description:** start with "MarketMage:" so the `watchlists` skill can find it.
- **A client or brand label:** when the user watches for several clients or brands (an agency, a portfolio), put the label first in the short name, in the `monitorName` and in the title: `cw-price-acme-competitors`, `monitorName: "acme-competitors"`, "Acme: competitor prices". The `watchlists` and `briefing` skills can then read one label's watches alone ("only Acme's"). Ask for the label once when the user mentions clients; never invent one. The `watchlists` skill sums a label's runs into a cost report for a period ("A cost report per client").
- **One Claude project per client:** for an agency, offer the pattern once, in one line: a Claude project per client whose instructions hold the client's name and label, its domains and marketplace, its currency and the watch naming ("Label: acme. Domains: acme.com.au. Marketplace: Amazon AU, AUD."). Every chat in that project then starts with the right client, and the label keeps its watches, briefing and costs apart. The watches stay in the Apify account connected to Claude, whichever project starts them.

## Creating one

1. **Agree the cadence.** Daily at a time the user names, in their time zone, is the default; weekly is the cheaper option. Turn it into a 5-field cron expression with an IANA time zone.
   - **Never faster than hourly.** Hourly (or every few hours) fits one watch: the user's **own** Amazon ASINs' Buy Box (`price-watch`, "Your own Buy Box, hourly"). Store pages, Shopify stores, rivals' listings, promotions, reviews, ranks, ads and markets are read at most daily, unless the user gives a reason a faster read serves (a launch day, a flash sale they're tracking), and then only for that period, back to daily after it. Keep schedules and volumes to what the research needs.
   - **Stagger the start times.** When several watches are created now with no exact time from the user, start them 10 to 15 minutes apart (`0 8`, `15 8`, `30 8`…): runs that start together count against the account's memory limit together ("When a run goes wrong", in `running-runs.md`), and a scheduled start Apify refuses for memory may simply not run that time. A time the user named is kept as they said it; when it matches another `cw-` schedule's minute, offer the 15-minute offset in one line, and only change it with their yes.
2. **Show the monthly cost first, once, as the approval** (`running.md`, "Before any run"): per-run cost × runs a month (30 daily, 4 or 5 weekly, 720 hourly), plus the first run. The first run reads everything at full price; later runs mostly pay the lower "checked, unchanged" price. Get a clear yes.
   - **The running total, worked out before the yes, said only when it matters:** list the user's `cw-` tasks and schedules ("Reading, pausing and changing"), read each enabled one's input with `get-actor-task` (all free; in one parallel batch, reusing any input already read in this chat; never quote task inputs, whose secret fields come back encrypted), work out its monthly estimate with its kind's formula (the `watchlists` skill, "List"), or, when that would take long, use its `maxRunCostUsd` ÷ 1.5 × runs a month as an upper estimate. With no other watch, the new one's figure is the total. Say the total ("With this one, your watches total about USD <x> a month.") only in the free-plan line below, or when the user asks; otherwise the new watch's own figure is the one estimate.
   - **Apify's free plan:** when the user is on it, or hasn't said, and that total plus this first run goes over USD 5, say so plainly in the same line: the free plan includes USD 5 of usage a month, and once it's used Apify blocks the account's runs until the next monthly cycle, so the watches (and one-off checks) go quiet until then. The USD 5 also covers anything else they run on Apify. Then offer what fits: weekly instead of daily, fewer items, one digest instead of several (above), or a paid plan. Never decide for them.
3. **Create the task** with `create-actor-task`: the actor, the name, the input without any secret, and a title and description.
   - **Bound every scheduled run:** put `maxRunCostUsd` in the input, at about 1.5× the typical per-run estimate (at least USD 0.02), and tell the user the figure. Scheduled runs have no spending limit of their own (the task and schedule tools cannot set one), so this input is what stops a run that grows: Watch Digest holds the whole digest (its watchers included) to it, and the other actors stop starting items when the next could pass it.
   - **Leave room for one item's worst case** with reviews, promotions, marketplace searches, Amazon rank keywords or ads: their actors start an item only when its worst case still fits, and Watch Digest doesn't start such a watcher at all when its share can't cover one item. Add to the 1.5× figure: USD 0.04 for reviews (shop products or ASINs; USD 0.03 when the watcher has only Trustpilot businesses, whose worst case is USD 0.0235), USD 0.03 for promotions, USD 0.06 for Amazon marketplace searches, USD 0.20 for eBay, Etsy, Walmart, Target or Best Buy searches (one search's worst case is USD 0.166), for Amazon rank keywords one keyword's worst case: (`maxResults` ÷ 16, rounded up) pages × USD 0.008 + USD 0.001 per ASIN (USD 0.025 at 48 results, about USD 0.073 at 144), and for ads USD 0.18 per watchlist on the first run (the baseline) and about USD 0.05 after it (Watch Digest gives an ad item already read whole its steady-state share). Amazon ASINs outside the US: add USD 0.003 per ASIN to the per-run figure itself (the local-market read, every run). Product pages on Walmart, Target, Best Buy, eBay or Etsy: add USD 0.003 per such page and USD 0.015 per such marketplace, since the store watcher reads a marketplace's pages in one job that starts only when all of them fit. A digest that skipped a watcher says so in its "Not checked" section, with the figure that would fit.
4. **Run it once now** with `call-actor` (same actor and input, with a cap). That records the baseline, so the first scheduled run already reports changes. Show what it found.
   - **Unless the watch skill says the first scheduled run records it:** `map-watch` after a first check, and `price-watch` for Walmart, Target, Best Buy, eBay and Etsy pages `price-check` read the same day. Items not covered still get this run.
   - **Its run lists only Watch Digest's own events** (the digest and items watched): each watcher's reads run as that actor's own run, billed there. So a low charge on the digest's run doesn't mean the baseline was skipped: check the `digest` row's `baselineItems` and the watchers' statuses instead.
   - **The first run reads everything at the full price,** so in this run's input set `maxRunCostUsd` to the first-run cap (the same figure as `maxTotalChargeUsd`). Otherwise the task's lower per-run figure would stop the baseline part-way. The task keeps the per-run figure.
5. **Create the schedule** with `create-schedule`:
   - a task action naming the task;
   - the cron expression and time zone;
   - `isEnabled: true`.
6. **Where the results go: your briefing in Claude.** Say it in one line: "your briefing in Claude, on request or on a Monday schedule": the digests stay in the user's Apify account, the `briefing` skill turns every watch's changes into a few decisions when they ask ("catch me up", free to read), and after their first briefing it offers to run every Monday on its own as a Claude scheduled task. Nothing is sent anywhere else, and the task's input carries no delivery settings.
   - **Knowing it ran:** the `briefing` names any watch whose recent runs failed or that didn't run when its schedule said, and the `watchlists` skill does the same when the user asks what changed.
7. **Confirm** in one short block: the name, what it watches, when it runs, its Max cost per run, and where the results go.
8. **Notebook:** if the user keeps one and the watch is for an idea in it, add a watch entry linked to that idea (`notebook.md`).

## Words the user sees

- **then the task:** `https://console.apify.com/actors/tasks/<taskId>`;

   | --- | --- | --- | --- |


## Reading, pausing and changing

- **List:** `apify-api-read` on `/v2/actor-tasks` with `{"limit": 50, "desc": true}` and `/v2/schedules` with `{"limit": 50}` (the list carries each task's name and IDs, not its input; a larger page can still exceed what the tool returns). If a page comes back full (50 items, or `total` above what you have), read the next with `offset` 50, 100… until you have them all. Keep the ones whose names start with `cw-`.
- **Latest result:** `apify-api-read` on `/v2/actor-tasks/<taskId>/runs` with `{"limit": 1, "desc": true}`: its first item is the last run, and no items means it hasn't run yet (never `/runs/last`, which fails then).
  - For Watch Digest, read `DIGEST.md` from its key-value store with `get-key-value-store-record`.
    - Exactly: take `defaultKeyValueStoreId` from that run, then `get-key-value-store-record` with `{"keyValueStoreId": "<defaultKeyValueStoreId>", "recordKey": "DIGEST.md"}`. Never call it without `keyValueStoreId`. For a run that didn't succeed, read it only if its store lists it (`running.md`, "Running": "Only a record that is there").
  - For Barcode, Listing Quality Checker and Catalog Matcher, read the dataset with `get-dataset-items`.
- **Pause:** `update-schedule` with `isEnabled: false` (no cost; confirm it is paused). The plugin can't delete either: the user deletes them at `https://console.apify.com/schedules`.
- **Resume or change cadence:** first show the monthly cost at the new cadence and get a yes, then `update-schedule` with `isEnabled: true` or the new cron expression.
- **Change what it watches:** read the task with `get-actor-task`, change only the item lists, and pass the whole input back to `update-actor-task`, keeping every other field as it is, `ENCRYPTED_VALUE:` fields included (`running-asks.md`, "Secrets"): the plugin never adds, changes or removes a field it doesn't manage.
  - New items start their history at the next run.
  - New items are read whole on their first run (their baseline), at first-run prices. Show two figures: **the next run, with the new items' baseline**, and **a typical run after it**, each per run and the typical one a month. Get a yes.
  - Set `maxRunCostUsd` to the baseline figure (about 1.5× the next run's estimate, with the room in step 3) so the baseline isn't cut, and say you'll lower it to the typical figure (about 1.5× a typical run, with the same room) once the baseline has run: do that the next time the user reads the watch, or when they ask. Alternatively, with the user's yes, run the baseline now with `call-actor` as in step 4, and keep the typical figure on the task.
- **Stop:** pause the schedule with `update-schedule` (`isEnabled: false`) after the user confirms by name: a paused watch costs nothing. To remove it for good, the user deletes the schedule and the task in the Console ("Deleting" below).

## Deleting

The plugin has no delete tool for tasks or schedules. When the user asks to delete one, say so in one line, then give the exact links with the IDs filled in (from `create-actor-task`, `get-actor-task`, `/v2/actor-tasks` or `/v2/schedules`), never only "the Console":
- **the schedule first,** if the watch has one: `https://console.apify.com/schedules/<scheduleId>`;
- **then the task:** `https://console.apify.com/actors/tasks/<taskId>`;
- on each page, open the page's **⋯** (more actions) menu, choose **Delete**, and confirm with **Delete** in the dialog.

A task without a schedule never runs on its own and costs nothing while it waits: say so, so the user knows nothing is charged before they get to it. Pause its schedule first when it has one (as in "Stop"), so nothing runs in between.
