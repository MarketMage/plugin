---
name: rank-watch
description: Check or monitor where Amazon products rank for search keywords - organic and sponsored position, page, who outranks them - once, or on a schedule that reports rank moves and milestones (entered the top 10, reached page 1, ad started or stopped). Ongoing tracking is saved in the user's Apify account as a task with its own daily or weekly schedule. Use when a seller asks where their listing ranks for a keyword, who outranks them, or wants their keyword ranks tracked every day or week.
---

# Rank watch

Amazon keyword ranks, now or over time. Read these first:
- `references/running.md`: costs, caps, tools, secrets;
- `references/watchlists.md`: scheduling;
- `references/costs.md`: the prices.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. Ask only for

- **The keywords,** as shoppers type them (at most 300 per watchlist).
- **The ASINs** to find for each keyword (theirs, and any competitors to compare). When different products have different keywords (a catalogue: each product's own search terms), ask for them **as sets**, product or product group → its keywords, and keep them apart (step 3, "One watcher per set").
- **The marketplace:** US by default.
- **Once or ongoing.** If ongoing, how often: daily or weekly.

## 2. One-off check

- **Run** `cleanpull/amazon-keyword-rank-tracker` with `keywords`, `asins`, `marketplace` and `maxResults: 48` (page 1).
  - Offer `maxResults: 144` when a product isn't on page 1: up to 9 pages at 16 results a page (3 at 48), so its worst case is 9 × USD 0.008 + USD 0.001 per ASIN ≈ **USD 0.073 per keyword**; quote up to that, and cap it at 1.5× (about USD 0.11), never under one keyword's worst case, or the tracker won't start the keyword.
  - `stopWhenFound: true` saves pages.
- **Cost per keyword:** per search page read, USD 0.002 (`search-page`) and, in the US, USD 0.006 more for the ad read (`residential-page`), so **USD 0.008 a page**; plus USD 0.001 per product rank. **Pages per keyword:** Amazon shows 16 to about 60 results a page, and the actor reads up to `maxResults` ÷ 16 pages (rounded up), so `maxResults: 48` reads **1 to 3 pages** (`stopWhenFound` stops sooner when every ASIN is found). Quote the range: one keyword and 1 ASIN on page 1 ≈ **USD 0.01, up to USD 0.025** (3 × 0.008 + 0.001; a real check on "wireless earbuds" read 3 pages for USD 0.025); 10 keywords ≈ USD 0.09, up to USD 0.25. **Cap** at 1.5× the top of the range (one keyword: USD 0.04), and never under one keyword's full worst case: the tracker starts a keyword only when that keyword's worst case still fits what is left of the cap, counting every page it may read (`maxResults` ÷ 16, rounded up) at USD 0.008, ads or not, plus USD 0.001 per ASIN; at `maxResults: 48`, **USD 0.025 for one ASIN**. So a cap under that (even USD 0.015, above one page) stops the run before the keyword, uncharged; organic-only checks need the same floor, though they usually cost less.
  - **Organic only** (`sponsored: false`): about USD 0.002 a page instead of 0.008, since the ad read is the dear part. Offer it when the user only cares where they rank, not who buys the top slot: 10 keywords ≈ USD 0.03, up to USD 0.07.
- **Read the `rank` rows:**
  - `organicRank`, `organicPage` and `sponsoredRank`;
  - `outrankedBy` (the listings above theirs);
  - `badges`, `boughtPastMonth`, `rating` and `reviewCount`;
  - `adsShown` (whether ads were read at all).
- **Rows with `source: "provider"`** were read through the marketplace data service, not from Amazon's pages: they have organic places only, with no sponsored data. Say so instead of "no ad place", and don't compare them with Amazon readings. `sourceChanged: true` means the first reading from a new source, a baseline rather than a move.
- **Keywords Amazon refuses** (on every proxy; common on amazon.fr): the provider fallback reads them through CleanPull's marketplace data service instead. It is **on by default** (leave `providerFallback` out), and only keywords Amazon refused use it; the others are read from Amazon's pages as usual.
  - Cost: never dearer than a direct read. Each is billed one search page per page delivered, with the home-network add-on only where a direct read pays it, plus its rank rows; the data service itself is on CleanPull, never a provider charge. So the quotes above hold, with nothing to add or confirm.
  - When it reads the service's search records (1 to 5 minutes), those keywords come back as `source: "provider"` rows (above). A reading that isn't complete fails, uncharged, and `RUN_SUMMARY` lists it.
  - Keep `stopWhenFound: true` (the default) on every read, the `maxResults: 144` deep read above all; never turn it off.
- **Several readings for a noisy keyword:** organic places move 1 to 3 spots between two reads of the same page. When the user doubts a reading, compares with another tool, or a product sits near a page or top-10 edge on a keyword, offer `samples: 3` for those keywords only: each search is read 3 times on fresh sessions and the row gives the median rank with `rankRange`. Each reading is billed as its pages, so it costs up to 3× that keyword: say it with the figure ("3 readings of 'cordless eye mask' for a steadier rank: about USD 0.03, up to USD 0.075"), and cap at 3× the single-reading cap. Report the median and the range ("#7, read between #6 and #9"). Run those keywords as their own call so the other keywords stay at one reading.
- **Where Amazon is read:** as a signed-out shopper in the marketplace's own country, at Amazon's default delivery location (no postcode). Say it in one line with the first ranks: places can differ by a few spots from what the user sees signed in at their own address.
- **Answer:**
  - a table of keyword, ASIN, organic place, sponsored place, page;
  - the top 3 listings that outrank them, with price and reviews;
  - one line on what to do: improve the title for a keyword where they're on page 2, bid on keywords where they rank organically but rivals buy the top slot.

## 3. Ongoing (a watchlist)

- **The task:** `cleanpull/watch-digest`, named `cw-rank-<name>`, with:
  - `rankKeywords`, `rankAsins` and `rankMarketplace`;
  - `rankSponsored: false` for an **organic-only** watch (see below), when the user doesn't need ad places;
  - `alertRankMilestonesOnly: true` if the user wants the message to carry only milestones (`references/watchlists.md`, "Alerts");
  - `monitorName: "<name>"`;
  - `title`;
  - `maxRunCostUsd`: 1.5× the **top** of the per-run range (3 pages a keyword: 10 keywords × 2 ASINs ≈ 1.5 × 0.25 ≈ USD 0.38), never under one keyword's worst case (about USD 0.025 + USD 0.001 per extra ASIN, as in step 2), at least USD 0.03, so no keyword is skipped for its worst case (step 2).
- **Cost per run:**
  - digest USD 0.005;
  - keyword × ASIN pairs × USD 0.00025;
  - each keyword's search pages, USD 0.008 a page in the US, 1 to 3 pages a keyword (the tracker's default 48 results; 3 when Amazon shows 16 a page);
  - USD 0.001 per rank that changed.
  - **Example:** 10 keywords × 2 ASINs daily ≈ 0.005 + 20 × 0.00025 + 10 × 0.008 + a few changes ≈ **USD 0.09 a run, about USD 2.70 a month**, and up to about USD 0.25 a run (USD 7.50 a month) when Amazon shows 16 results a page. Weekly is about USD 0.40 to 1.10 a month. Quote the range, and set `maxRunCostUsd` from its top.
  - **Organic only (`rankSponsored: false`):** the ad read is about USD 0.006 of each USD 0.008 page, so the same 10 keywords × 2 ASINs daily cost about 0.005 + 20 × 0.00025 + 10 × 0.002 ≈ **USD 0.03 a run, about USD 0.90 a month** (up to about USD 0.07 a run, USD 2.10 a month, at 3 pages a keyword), a saving of about USD 1.80 to 5.40 a month. Offer it whenever the user hasn't said they care who buys the top slot; for ad places as well, a second weekly watch with ads on adds about USD 0.40 to 1.10 a month.
- **One watcher per set.** A watch's `rankAsins` are tracked on **every** keyword in its `rankKeywords`, so a catalogue in one flat list pays for pairs nobody wants (40 ASINs × 120 keywords = 4,800 pairs). When the user's ASINs come with their own keywords, work out both totals with the formula above first: each set is its own task with its own USD 0.005 digest fee a run, so for a few ASINs and keywords one flat list can be cheaper. Offer one watch per set (`cw-rank-<name>-<set>`, each with its own `monitorName`), staggered 10 to 15 minutes apart (`references/watchlists.md`, step 1; 8 sets spread over about 2 hours), only when it costs less, and show the saving in one line: "One flat list: about USD <x> a month; one watch per product group: about USD <y>, the same ranks you asked for." The search pages are per keyword, so the saving is in the pairs and in keywords read for ASINs that don't need them; a keyword shared by two sets is read in each.
- **Steps:** follow `references/watchlists.md`: create the task, do a baseline run with a cap, schedule it, and say where the results go: "your briefing in Claude, on request or on a Monday schedule"; the Console link for a channel only when the user asks for Slack, Discord, Teams, a webhook or email (step 7).
- **What the digests report:** rank moves of at least 3 places and 25%, with milestones and ads starting or stopping.
  - When you explain one, lead with milestones (reached page 1, left the top 10).
  - Remind the user that 1 to 3 place moves are normal reshuffling.
  - A watch reads each keyword once a run (Watch Digest has no readings setting); its 3-place and 25% rule keeps the reshuffle out. When a reported move looks like noise, offer a one-off check of that keyword with 3 readings (step 2), with its cost.
