---
name: promo-watch
description: Read or monitor the promotions competitor online stores show - sitewide sales, discount codes, free-shipping thresholds, bundles, gifts, sign-up offers and markdown depth - and their new products and collections with launch dates, once or on a schedule that reports what started, ended and launched. Works on Shopify and other store platforms. Use when someone asks what sales or codes a competitor is running, their free-shipping threshold, what they launched recently, or wants to be told when a competitor starts or ends a promotion. Not for a full profile of a store's catalogue, pricing and tools (use spy-store).
---

# Promotions and launches

What competitors are promoting and launching, now or over time. Read these first:
- `references/running.md`: costs, caps, tools, secrets;
- `references/running.md` is the core; its parts are read only at their step (its first lines say when): `references/running-results.md` once results are in, before using them; `references/running-runs.md` also before a status message stands in for rows; `references/running-runs.md` before a data-provider read, when a run doesn't succeed, or when this chat already holds a run; `references/running-abroad.md` outside the US; `references/running-asks.md` when the user asks who runs this, offers an allowance, pastes a secret or asks for something MarketMage won't do.
- `references/known-limits.md`: routes established not to work, each with what to use instead: read in the same batch as `references/running.md`, before choosing any source (a store, a marketplace, a country, a keyword); never try a route it lists. `references/plain-words.md` (the words the user sees, for every answer) is read in that same batch.
- `references/watchlists.md`: scheduling;
- `references/costs.md`: the prices.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. Ask only for

- **The stores:** domains, or a country site (`brand.com/us/`).
- **Optional:**
  - extra pages of those stores: a sale page (its crossed-out prices give the markdown), a new-arrivals page (`pages`, up to 10 a store);
  - which promotions matter (`promotionTypes`: `sitewide-sale`, `sale`, `code`, `free-shipping`, `bundle`, `gift`, `signup-offer`, `markdown`; all by default);
  - launches only, or promotions only.
- **Once or ongoing.** If ongoing, how often.

## 2. One-off check

- **Run** `cleanpull/promotions-monitor` with `stores`, `pages`, `promotionTypes`, and for launches `launchWindowDays` (7 by default; 30 for "this month") and `maxLaunchesPerStore` (25 by default). For promotions only, `includeLaunches: false`; for launches only, `promotionTypes: []`.
- **Cost (paid plans):** USD 0.001 per page checked (a home page with its Shopify feeds, or an extra page) + USD 0.002 per promotion or launch row.
  - A store typically gives 3 to 15 rows: about **USD 0.02 a store**, at most USD 0.001 + (`maxLaunchesPerStore` + about 10 promotions) × 0.002 ≈ USD 0.07.
  - A store that can't be read is listed in the run summary and not charged; a few need residential reads (USD 0.006 each).
  - **Example:** 5 stores ≈ USD 0.10, at most USD 0.35: "up to about USD 0.35 (with a spending limit). Go ahead?", and get a yes.
- **Read** with `get-dataset-items`:
  - promotions: `fields: "recordType,store,type,text,code,threshold,thresholdCurrency,percentOff,amountOff,confidence,foundIn,markdown,pageUrl"`;
  - launches: `fields: "recordType,store,kind,title,url,launchedAt,relaunch,confidence,source,price,compareAtPrice,currency"`;
  - `RUN_SUMMARY`: per store the platform, pages read, and any page not read, with the reason.

## 3. Explain it like an expert

- **Per store, one line:** the headline offer (sitewide %, code, threshold), then launches.
- **Free-shipping thresholds** set the basket: compare them with the user's own and with the store's median price (a USD 75 threshold on a USD 30 median pushes buyers to three items).
- **Codes** are only those the site prints (in an announcement bar, a banner, a header). Codes sent by email, in pop-ups after a click, or in a cart aren't seen.
- **Markdowns** on Shopify: `markdown.sharePercent` of the newest products below their compare-at price, and `maxPercentOff`. A high share all year is a pricing model (inflated compare-at prices), not a sale.
- **Confidence:** `high` from an announcement bar, header or the store's own data; `medium` elsewhere on the page or in image alt text: say "seen on the page" for those.
- **Launches:** on Shopify, dated by the store (`source: "shopify-feed"`); `relaunch: true` means an old product re-published. On other platforms launches need two runs (a baseline, then new product links), so a one-off check shows none there: say so.
- **Not read:** bars drawn only by scripts (Kith and Nike in tests), and Amazon, Walmart and Target.
- **Then what it means for the user:** match or beat a threshold, time their own promotion, or note a competitor's slow sellers being discounted.

## 4. Ongoing (a watchlist)

- **The task:** `cleanpull/watch-digest`, named `cw-promo-<name>`, with:
  - `promotionStores` (any platform, at most 200);
  - `monitorName: "<name>"` and `title`;
  - `maxRunCostUsd` (see below).

  Watch Digest watches all promotion types and launches. For only some types, or extra sale pages, use the one-off check instead.
- **What the digests report:** promotions that started, promotions that ended (only after two runs without them, so rotating banners don't count), launches, and a free-shipping threshold that moved.
- **Cost per run:**
  - digest USD 0.005;
  - stores × USD 0.00025;
  - USD 0.001 per store's page check;
  - USD 0.002 per promotion started or ended and per launch;
  - USD 0.001 per message once a channel is added.
  - **The first run** records every running promotion (and the last day's Shopify launches) as the baseline: about USD 0.02 a store.
  - **Example:** 10 stores daily, about 3 changes a day: 0.005 + 10 × 0.00025 + 10 × 0.001 + 3 × 0.002 ≈ **USD 0.024 a run, about USD 0.70 a month**; the first run ≈ USD 0.22. Weekly is about USD 0.10 a month.
- **`maxRunCostUsd`:** 1.5× the typical run + USD 0.03 (room for one store's worst case). For the example, about USD 0.07.
- **Steps:** follow `references/watchlists.md`: monthly and first-run cost, a yes, the task, the baseline run (with `maxRunCostUsd` raised to the first-run cap in that run's input), the schedule, and where the results go: "your briefing in Claude, on request or on a Monday schedule"; the Console link for a channel only when the user asks for Slack, Discord, Teams, a webhook or email (step 7).

## 5. Reading a promotions digest later

Lead with sitewide sales and new codes that started, then ended promotions (with their last sighting), then launches. Say what each means for the user's pricing or calendar that week.

**A store also in a price watch** (`shopifyStores`, in this digest or another `cw-` watch): its launches also come as "New product" from the store watcher. List each new product once, under launches, with its price from the store watcher, and count it once.
