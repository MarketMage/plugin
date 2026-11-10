---
name: ads-watch
description: See or monitor the ads competitors run, from the platforms' public ad libraries - Google Ads Transparency Center (search, YouTube and display, any country), Meta Ad Library (Facebook and Instagram, running ads in any country) and TikTok's ads library (EU, UK and Switzerland) - with first and last shown dates, active status, text where the library gives it, and links, once or on a schedule that reports new and stopped ads; and find proven small advertisers for a product keyword (small stores whose Meta ads have run 35+ days, their store size and the angle they use). Use when someone asks what ads a competitor is running, when they launched new creatives, wants to be told when a rival starts or stops ads, or asks who is successfully advertising a product, which small stores keep running ads for it, or for proof an idea sells with ads. Not for writing or running the user's own ads.
---

# Ads watch

A competitor's ads and how they change. Read these first:
- `references/running.md`: costs, caps, tools, timing;
- `references/running.md` is the core; its parts are read only at their step (its first lines say when): `references/running-results.md` once results are in, before using them; `references/running-runs.md` also before a status message stands in for rows; `references/running-runs.md` before a data-provider read, when a run doesn't succeed, or when this chat already holds a run; `references/running-abroad.md` outside the US; `references/running-asks.md` when the user asks who runs this, offers an allowance, pastes a secret or asks for something MarketMage won't do.
- `references/known-limits.md`: routes established not to work, each with what to use instead: read in the same batch as `references/running.md`, before choosing any source (a store, a marketplace, a country, a keyword); never try a route it lists. `references/plain-words.md` (the words the user sees, for every answer) is read in that same batch.
- `references/watchlists.md`: scheduling;
- `references/costs.md`: the prices.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. Ask only for

- **The competitors:** brand names or domains (`advertisers`); optionally a Google advertiser ID (`AR…`) or a Meta page ID for an exact match, or `keywords` for ads on a topic (Meta and TikTok).
- **Where:** Google, Meta, TikTok (all three by default), and countries (up to 5 two-letter codes; empty means anywhere). **TikTok's library covers ads shown in the EU, the UK and Switzerland only:** when the user's market is outside them (the US, Canada, Australia…), leave TikTok out of `platforms` (a one-off run) or Watch Digest's `adPlatforms` (a watch: always pass it, since it includes TikTok by default) and say why in one line; include it when they sell into Europe or ask for it.
- **Once or ongoing.**

Nothing else is needed: no tokens or developer apps. What each platform shows:

| Platform | How it's read | Covers |
| --- | --- | --- |
| Google Ads Transparency Center | directly | verified advertisers' search, YouTube, display and Shopping ads, any country; format and a creative link, no ad text for image and video ads, no landing page |
| Meta Ad Library | CleanPull's ad library service (a third-party API that reads the public library) | Facebook, Instagram, Messenger and Audience Network ads **running in any country** (pass the user's country; without one, results mix countries and often start with European ads); text, title, call to action, landing page and creative links. Stopped ads (with `activeOnly: false`) only for ads that reached the EU |
| TikTok ads library | the same service | ads shown in the EU, the UK and Switzerland (countries don't narrow it); a caption, dates, reach and the video link |

## 2. Run

- **Run** `cleanpull/ad-library-monitor` with `advertisers` (and `keywords`, `googleAdvertiserIds`, `metaPageIds` if given), `platforms` (always pass it), `countries`, `activeOnly: true`, and **`maxAdsPerTarget: 30` for a one-off look** (about USD 0.05 a brand and platform). Use 100 when the user wants every active ad, and for a watch's baseline, since a stop is only reported after a full read.
- **Cost (paid plans):** a watch item is one brand on one platform.
  - USD 0.001 per watch item checked (per 100 ads read) + USD 0.0015 per ad delivered;
  - Meta and TikTok: + USD 0.0035 per library request (a page of 30 Meta ads, or 12 TikTok ads; on Meta, per country chosen). Google ads data comes from the ad data provider only on a run where Google's library returns none, and then charges library requests the same way;
  - a brand with many active ads at the default `maxAdsPerTarget: 100`: Google ≈ **USD 0.15**, Meta ≈ USD 0.165, TikTok ≈ USD 0.18. For a quick look, `maxAdsPerTarget: 30`: about USD 0.05 a brand on Google, USD 0.05 on Meta, USD 0.06 on TikTok.
  - **Example:** 2 brands on Google, Meta and TikTok at 30 ads ≈ USD 0.32: one approval line ("Usually USD 0.20–0.32; it can't go over USD 1.") and a yes.
- **Timing:** Google takes seconds to a minute a brand (requests are spaced out); Meta and TikTok pages come through the service and can take a minute or two. Start with `waitSecs: 45` and follow the run.
- **The spending limit:** the ceiling from the approval line (`references/running.md`, item 6): the run's `maxTotalChargeUsd`.

## 3. Read the results

- **`ad` rows:** `fields: "recordType,platform,advertiser,adId,status,active,firstShown,lastShown,text,title,mediaType,mediaUrl,cta,landingUrl,countries,reach,adUrl,watch"`, `limit` about 60.
  - `firstShown` and `lastShown` are the platform's dates; `adUrl` opens the ad in the platform's own library; `mediaUrl` is a link to the creative (nothing is downloaded or stored; the links expire after a while).
- **`RUN_SUMMARY`:** per watch item, the advertisers matched (Google matches a brand to its advertiser accounts, for example several country entities; on Meta, a brand name keeps the pages named for it), ads read, active, and whether every active ad was read. A service outage or refusal names the items not read, uncharged.

## 4. Explain it like an expert

- **Volume and recency:** how many ads are active per brand and platform, and how many started in the last 7 and 30 days. A burst of new ads usually means a launch, a sale or creative testing.
- **Formats:** the mix of text, image and video; a shift to video is a budget signal.
- **The visual moment, after the volume line** (`references/running-results.md`, "Explaining results": "One visual, where it helps"; only where you can draw one, and otherwise nothing about it is said; never in the first answer to this skill's new reads, only in a follow-up turn: the full detail or list, a chart the user asks for, a deeper turn): **how long the ads have run**, one horizontal bar per advertiser or brand in the answer (at most 10), its days running (`daysRunning` on `advertiser` rows; for a brand read, the longest-running active ad's days since its `firstShown`, the same figure the answer gives), labelled with the name and the days, and a marked line at 35 days labelled "proven (35+ days)". Coloured as a second cue: 35 days or more green, the rest grey, with "new" beside those at 14 days or fewer. Caption: the library, the market country and the date read ("Meta ads, US, read 6 Nov").
- **Longest-running ads** (earliest `firstShown` still active) are usually the winners: those are the ones worth studying.
- **Meta text:** recurring offers, hooks and landing pages in `text`, `title`, `cta` and `landingUrl`.
- **Limits in one line, where they matter:** Google gives no text for image and video ads; TikTok covers the EU, UK and Switzerland only; Meta lists stopped ads only for ads that reached the EU.
- **Always pass the user's country to Meta** (from their words or the market), so the ads are the ones their buyers see. Say once, only when stopped ads matter, that Meta keeps stopped ads only for ads that reached the EU.
- Offer the watch: "I can tell you each day when they launch or stop ads."

## 5. Ongoing (a watchlist)

- **The task:** `cleanpull/watch-digest`, named `cw-ads-<name>`, with `adAdvertisers` (and `adKeywords`, `adGoogleAdvertiserIds`, `adMetaPageIds`), `adPlatforms`, `adCountries`, `monitorName: "<name>"`, `title` and `maxRunCostUsd` (at most 200 watch items). One digest a run, read in "your briefing in Claude, on request or on a Monday schedule"; sent to Slack, Discord, Teams, a webhook or email only when the user asks for that channel (`references/watchlists.md`, step 7).
- **What the digests report:** new ads (started since the last run) and stopped ads (confirmed when a second full read agrees; on TikTok only after an ad has gone a week unshown). Brands with more than 100 active ads get no stops reported (a stop needs a full read).
- **Cost:**
  - **the first run** delivers every active ad as the baseline: up to about USD 0.15 per watch item (100 ads), plus Meta and TikTok library requests;
  - **later runs:** digest USD 0.005 + USD 0.00025 per watch item; USD 0.001 per watch item checked; USD 0.0015 per new ad; Meta and TikTok about 1 and 3 library requests per brand a day at 30 ads (USD 0.0035 each), more for brands with many ads.
  - **Example:** 5 brands on Google daily, about 3 new ads a day: 0.005 + 5 × 0.00025 + 5 × 0.001 + 3 × 0.0015 ≈ **USD 0.016 a run, about USD 0.48 a month**; the first run up to about USD 0.76. The same 5 on Meta and TikTok add about 20 library requests a day ≈ USD 2.10 a month.
- **`maxRunCostUsd`:** 1.5× the typical run + **USD 0.05 of room** for the ads watcher (Watch Digest gives an ad item it has already read whole its steady-state share). For the Google example: about USD 0.075, so USD 0.08. The baseline run uses the first-run cap (`references/watchlists.md`, step 4), with **USD 0.18 of room** for the ads watcher on top of its first-run estimate.
- **Steps:** follow `references/watchlists.md`.

## 6. Proven small advertisers

The best evidence an idea sells with paid ads is a **small store that keeps paying for them**: an ad still running after 35 days is paying its way (a test that doesn't pay usually stops within one to three weeks), and a store with about 20 products or fewer is one the user could match. This search finds them for a product keyword, then offers to read 1 to 3 of their stores and the angle their ads use. Offer it to dropshippers selling through ads (the cold-traffic lens), or whenever someone asks who is successfully advertising a product.

**Plan it in one message,** the steps with no price on each, and one approval line for steps 1 and 3 together, a range and a ceiling (`references/costs.md`, the Bronze column and "Range and ceiling"; add the Free high end where it differs), with one yes up to that ceiling; never more than it without another yes. Step 5 always gets its own yes, with its own estimate.

| Step | What | Run | Cost |
| --- | --- | --- | --- |
| 1 | Meta ads for the keyword in the user's country, one row per advertiser, only ads running 35+ days | `cleanpull/ad-library-monitor` with `keywords: ["<product>"]`, `platforms: ["meta"]`, `countries: ["<market country>"]`, `activeOnly: true`, `oneRowPerAdvertiser: true`, `minDaysRunning: 35`, `maxAdsPerTarget: 30` | 1 watch item check USD 0.001 (one per 100 ads read) + up to 6 library pages × USD 0.0035 (with `minDaysRunning` the actor's cap is 3× the 2 pages 30 ads need, to find ads old enough) + up to 30 advertiser rows × USD 0.0015 ≈ **USD 0.07 at most**; on the Free plan from 2026-11-07, library pages are USD 0.007: ≈ **USD 0.09 at most**; younger ads are left out and not charged |
| 2 | Their landing domains | no run | nothing to run |
| 3 | Each domain's store size | `cleanpull/shopify-store-scraper` with `stores`: up to 15 domains, `summaryOnly: true` | USD 0.003 per Shopify store (one store summary each); a domain that isn't Shopify gets a free row; 15 ≈ **USD 0.045 at most** |
| 4 | The proven small advertisers | no run | nothing to run |
| 5 | Read 1 to 3 of those stores and their ads' angle (its own yes) | per store: `cleanpull/shopify-store-scraper` with `stores: ["<domain>"]`, `maxProductsPerStore: 50`, `storeSummary: true`, `bestSellerRank: true`; and `cleanpull/ad-library-monitor` with `metaPageIds: ["<advertiserId>"]`, `platforms: ["meta"]`, `countries`, `activeOnly: true`, `maxAdsPerTarget: 10` | store: up to 20 products × USD 0.0008 + USD 0.003 summary ≈ USD 0.02; ads: USD 0.001 + up to 2 library pages × USD 0.0035 + 10 × USD 0.0015 ≈ USD 0.023; **about USD 0.04 a store**, 3 ≈ USD 0.13 (Free plan from 2026-11-07: about USD 0.05 a store, 3 ≈ USD 0.15) |

Steps 1 and 3 together: **about USD 0.11 at most** on paid plans, and on the Free plan from 2026-11-07 about USD 0.13 (say "Usually USD 0.06–0.11; it can't go over USD 0.50.", adding the Free high end, "(up to USD 0.13 on Apify's free plan)", for a Free-plan user once that date has come or the run may cross it; the two runs share the ceiling in proportion to their high ends, `references/running.md`, item 6: about USD 0.33 for step 1 and USD 0.17 for step 3). Start step 1 with `waitSecs: 45`: Meta pages come through CleanPull's ad library service and can take a minute or two.

**Reading it:**
- **Step 1** (`fields: "recordType,advertiser,advertiserId,landingDomain,landingUrl,adsKept,earliestFirstShown,daysRunning,sampleAdUrl"`): every row is an advertiser whose earliest kept ad has run 35 days or more. Leave out advertisers whose name and landing page plainly sell something else (the keyword in an unrelated ad), and say how many.
- **Step 2, the domains:** keep one domain per advertiser from `landingDomain`. Set aside, and say how many: marketplaces and platforms (amazon., ebay., etsy., walmart., aliexpress., temu., tiktok.com, facebook.com, instagram.com, linktr.ee and other link pages), and big brands the user plainly couldn't match. Keep at most 15, the longest-running first. None left: say so, with the advertisers' count, and stop (no further run starts).
- **Step 3** (`fields: "recordType,storeDomain,storeName,publishedProductsCount,country,currency,url,reason"`): on each `store` row, `publishedProductsCount` is the store's size. **Count the rows against the domains sent:** in a mixed run (some stores read), a domain that isn't Shopify or didn't answer gets **no row at all**; the domains sent minus the rows returned are the ones not read. Read the run's `RUN_SUMMARY` (`get-key-value-store-record` on its default store): its `failures` give each one's `store` and `reason`. Name them, never drop them silently: "3 domains aren't Shopify stores, size not read: a.com, b.com, c.com". Only when no store at all was read does the run return a free `recordType: "unreadable"` row per domain with its `reason`; name those the same way. Either can still be read with `spy-store`'s sample (its estimate comes with its yes, when it needs one).
- **Step 4, the reading:** a **proven small advertiser** is an advertiser with ads running **35 days or more** and a store of **about 20 products or fewer** (up to 25 when the rest are much bigger, said as such). Rules of thumb: print them next to the numbers. Show a short table (at most 10 rows): advertiser, domain, days running, products, and the sample ad link. Then one line on what it means: "3 stores of under 20 products have kept Meta ads running 35 to 140 days on this: small sellers are making the ads pay." None found: say so plainly with what was found (for example "6 proven advertisers, all with 80+ products"), as information, not a verdict, and offer the angle read on the smallest one instead.
- **Step 5:** from the store, the catalogue (`productCount`, the best sellers, the price of the product that matches the keyword, `onSaleShare`, the apps in the summary); from the ads (`fields: "recordType,advertiser,text,title,cta,landingUrl,firstShown,mediaType,adUrl"`), **the angle**: the hook their copy leads with (a problem, a buyer group, a feature, a bundle or an offer), the call to action, and the page it sends to, quoted in short phrases. End with what the user could take from it: the angle they share, and one no current advertiser uses, only from what the ads and the store show. For a fuller read of one store, `spy-store` follows (its estimate comes with its yes).

**Close** with the one next move, with no price on it (its estimate comes with its yes): reading the strongest store (step 5), or, when the user hasn't checked the idea yet, `validate` on it. Say the libraries show advertisers, not their spend.

**No cost talk after the runs** (`references/running.md`, "No cost talk anywhere else"): the answer never reports against the amount the user gave ("everything fit within your 15 cents", "well under your budget"), never calls a link, a step or a read free or cheap, and puts no price on an offer or the next move. Their amount is honoured through the caps, silently.

### Proven advertisers checked on TikTok (EU, UK, Switzerland)

For a market in the EU, the UK or Switzerland (TikTok's library covers only those), the advertisers found above, or brands the user names, can be checked on TikTok too: how long their TikTok ads have run, their widest reach and how big their TikTok account is. **TikTok's library can't be searched for long-running ads by keyword:** a keyword search returns the newest ads first, with no date filter or sort, and carries no account ids to size from. Say so plainly, in one line of the answer itself (not only before the run), whenever this check runs or someone asks for proven TikTok advertisers on a product, so they know why it works from names; and offer this check by name instead of a keyword search. Offer it after step 4 ("check these proven Meta advertisers on TikTok too?"), or straight away for named brands. Where a skill already offers the US TikTok Shop feed as a labelled proxy, that offer stays as it is.

- **The run:** `cleanpull/ad-library-monitor` with `advertisers: ["<name>", …]` (the advertisers' names as the Meta read gave them, or the brands the user named; at most 10), `platforms: ["tiktok"]`, `activeOnly: true`, `oneRowPerAdvertiser: true`, `maxAdsPerTarget: 12` (up to two pages; no `tiktokAccountSize`: a named advertiser's own read fills `accountAdsInLibrary` when TikTok gives it, at no extra cost; no `minDaysRunning`, which would skip the newest-first page; countries don't narrow TikTok). Start with `waitSecs: 45`.
- **Cost, worst case, said before the yes:** per name, 1 watch item check USD 0.001 + up to 4 library requests × USD 0.0035 (up to two pages of ads plus two name-suggestion asks) + up to 12 advertiser rows × USD 0.0015 (a name can match several accounts) ≈ **USD 0.033 at most a name** (about USD 0.006 when the name matches one account and one request carries its ads); on the Free plan from 2026-11-07, library requests are USD 0.007: ≈ USD 0.047 at most a name. Say the total for the names once, as a range and a ceiling, "Usually USD <low>–<x>; it can't go over USD <ceiling>." (low: about USD 0.006 a name; the ceiling as `references/costs.md`, "Range and ceiling" sets out), and set the run's cap to that ceiling.
- **Reading it** (`fields: "recordType,platform,advertiser,advertiserId,adsKept,maxReach,accountAdsInLibrary,earliestFirstShown,daysRunning,sampleAdUrl,watch"`): leave out rows whose advertiser plainly isn't the brand asked for (a name search can match others), and say how many. `daysRunning` is the oldest of the ads read (the newest page), so it is "at least" that many days.
  - **Proven** on TikTok: an ad running **35 days or more**, as on Meta. **Small** means about **50 or fewer ads** in TikTok's library (`accountAdsInLibrary`), read as an order of magnitude: TikTok's own count varies between reads, so 41 and 60 are both "a few dozen", and thousands is plainly not small. Print both rules of thumb next to the numbers.
  - **`accountAdsInLibrary` missing or null** means TikTok gave no count for that account in this read: "size not read", never small or large. Read it whenever it is present.
  - **Sort by `maxReach`**, the widest reach band among the kept ads (TikTok's estimated audience, "1M-10M" above "100K-1M"), then by days running.
  - Show a short table (at most 10 rows): advertiser, days running (at least), widest reach, ads in TikTok's library, the sample ad link. Then one line on what it means: "2 of these, each with a few dozen TikTok ads or fewer, have kept an ad running 77 to 119 days, one reaching 1M-10M: small sellers are making TikTok ads pay in the UK." None small or proven: say what was found, as information, never a verdict.
- **Next move, with no price on it:** the sample ad links open in the library; step 5's angle read works on TikTok by name (`advertisers: ["<advertiser>"]`, `platforms: ["tiktok"]`, `maxAdsPerTarget: 12`; its estimate, when it runs: about USD 0.006, ≈ USD 0.033 at most, ≈ USD 0.047 at most on the Free plan from 2026-11-07). Say the library shows advertisers and reach bands, not their spend or sales.

## 7. Reading an ads digest later

Lead with new ads per brand (first shown, format, the library link), then stops, and what the pattern suggests (a new campaign, a promotion ending).
