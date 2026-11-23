# Judgement: where you'd compete (cold-traffic dropship)

Part of the cold-traffic dropship lens (`judgement-lens-cold-traffic.md`). Read when the Where you'd compete read is made or offered.

**Where you'd compete** (read only through the cold-traffic dropship lens): a row of facts in the table, the same for everyone, with its counts (Meta advertisers active, proven, new; TikTok Shop shops and the top 3 shops' share of units) and no market reading. It is left out of the market verdict: whether a crowd of advertisers is a wall or proof that ads pay depends on the budget, so only the lens reads it ("Where you'd compete: saturation on paid social and TikTok Shop").

**Where you'd compete: saturation on paid social and TikTok Shop.** Amazon page 1 is not where this seller competes: the ad auction for the same buyers on Meta and the TikTok Shop feed are. The counts are the same for everyone (the facts table's "Where you'd compete" row); only their reading changes with the profile. A product can pay for a seller with budget and experience and still be closed to a newcomer testing on a small budget, and a crowd is proof that ads pay when the budget can outlast the tests.

The facts (from the ad library keyword read, one row per advertiser, active ads only, the market's country, one page of 30 ads; a read that filled the page is "at least"):
- **Active advertisers:** the advertiser rows.
- **Proven:** advertisers whose earliest active ad has run **35 days or more** (`daysRunning`): five weeks is past the one to three weeks a test that doesn't pay usually runs, so the ad is paying its way.
- **Newcomers:** advertisers whose earliest active ad started in the **last 14 days** (`daysRunning` 14 or fewer).
- **TikTok Shop** (from the TikTok read already made): distinct shops (`shopName`) among the relevant top 20, and the **top 3 shops' share** of their units.
- **Coverage, said once:** Meta's ad library lists running ads in every country, so a US read counts ads shown in the US; TikTok's ads library covers only the EU, the UK and Switzerland, so TikTok ads are read only for a market there, and a US seller's TikTok side is TikTok Shop (US data). The libraries list advertisers, not their spend.

Thresholds (rules of thumb; print each next to its number). They are **per library**: Meta's advertisers in its 30-ad page are read against them; when TikTok's ads library is read (EU, UK, Switzerland), its advertisers are counted and read separately, on their own 30 ads, against the same thresholds. Never sum the two libraries into one count.
- **Crowded:** **10 or more** active advertisers in one library's 30 ads read (a third of a page, each a separate store bidding for the same buyers), or the top 3 TikTok shops holding **60% or more** of the units (the feed's buyers already go to a few shops with working creatives).
- **Room:** **4 or fewer** active advertisers in each library read, and the top-3 TikTok share under 60% (or TikTok Shop not read): a handful a test budget can sit beside.
- **Several proven:** **3 or more** proven advertisers (more than one store has made the ads pay).
- **Late wave:** **5 or more** newcomers, making at least a third of the active advertisers (a burst, not the usual one or two tests).

Which reading applies, from the budget band and `experience`:

| Budget band | experience none | a bit | brand | not given |
| --- | --- | --- | --- | --- |
| under $1k | testing | testing | testing | testing |
| $1k–5k | testing | outlasting | outlasting | middle |
| $5k and over | middle | outlasting | outlasting | outlasting |
| not given | testing | outlasting | outlasting | middle |

The reading:

| Reading | Crowded | Room | Between |
| --- | --- | --- | --- |
| **testing** (a small budget or a first try: each test bids against the crowd) | **against**: "you'd be outbid while testing" | **favours** with 1+ proven (proven, and room beside them); neutral with none proven (nobody has shown the ads pay) | neutral |
| **middle** | neutral, with the fix as a line: an angle or audience no current advertiser targets | **favours** with 1+ proven; neutral with none | neutral |
| **outlasting** (budget or experience to run tests past the crowd) | **favours** with 3+ proven ("demand that pays"); neutral with fewer | **favours** with 1+ proven; neutral with none | neutral |

- **Any budget, a late wave:** one caution line ("a late wave: 6 of 15 advertisers started in the last 14 days"); it doesn't move the reading.
- **Saturation alone never makes "not this one".** It is a row, not a gate: against, it caps at "a fit, with one fix", and the fix is an **unserved angle**: an angle or audience no current advertiser targets, found on the ladder (the angle rung's rising searches; the segment rung's buyer group or a feature the leaders' complaints ask for) and checked against the advertisers' ads (their sample ad links, or the same read with one row per ad to read their copy). **Never call an angle unserved before their ads were read:** when the user's spending limit covers it, run that ad-copy read before the answer and say what it found ("none of the 14 advertisers' ads mention sound"); otherwise say what was seen ("none of their names point at sound") and that their ad copy would confirm it, and word the fix as unconfirmed ("an angle none of them appears to pitch"). The middle reading names the same fix as a line, without capping.

**The wave read: are the advertisers' stores adding it now** (optional follow-up, cold-traffic lens only). Offered once, after the ad library read is back, as one of the follow-ups; run on a yes, or straight away when the user already asked whether stores are adding it now. Only `validate` and `find-products` offer it (they run the ad library read through the cold-traffic lens); other skills don't. Never in the guided first session (`first-use.md`). It answers one question: how many of the stores advertising it added it to their catalogue in the last 30 days.
- **The stores:** the distinct `landingDomain` of the advertiser rows kept (unrelated advertisers already left out). Set aside marketplaces and platforms (amazon., ebay., etsy., walmart., aliexpress., temu., tiktok.com, facebook.com, instagram.com, linktr.ee and other link pages) and say how many. Keep at most 30, the longest-running first. None left: say so, and don't run it.
- **The run:** `cleanpull/shopify-store-scraper` with `stores`: those domains, `keywords`: the idea's core term ("eye mask", not "heated eye mask for dry eyes": it is matched inside product titles, so it may be broader than the idea), `createdWithinDays: 30`, `waveSummary: true`, `maxProductsPerStore: 1000` (each store's first 1,000 products are read), `maxItems: 150`.
- **The cost:** only the matching products delivered are charged, USD 0.0008 each (`product-result`), the same on every plan, Apify's free plan included; the products read but not matched, the wave summary row and the row for a store not on Shopify are free. At most 150 × USD 0.0008 ≈ **USD 0.12** (usually less: few stores add the same product in one month); the run's spending limit USD 0.27, never said (`running.md`, item 6). Say the 30-store cap in the offer; the figures above make its estimate at the yes.
- **Read** the `waveSummary` row (the dataset's last row: `get-dataset-items` with `desc: true`, `limit: 1`): `storesChecked`, `storesWithMatch`, `storesWithoutMatch`, `storesUnreadable`, `storesNotShopify`, `storesNotRead`, `partial`, `stopReason`, and per matching store `domain`, `matchingProducts`, `earliestCreatedAt`. Then **confirm the matches**: read the product rows (they are delivered and charged anyway; `fields: "recordType,storeDomain,title,price,createdAt"`, `limit` 200) and check each title against the idea, as TikTok rows are confirmed. A store counts only when at least one of its matched titles is the same product as the idea (the core term may be broader for the search; the confirmation is against the idea).
- **The fact:** "N of M stores advertising it added it in the last 30 days", N being the confirmed stores and M the Shopify stores read (`storesWithMatch` + `storesWithoutMatch`), with each confirmed store's date (the earliest `createdAt` among its confirmed products: republishing doesn't reset it) and the stores named: "6 of 14 stores advertising it added it in the last 30 days (warmnap.shop on 29 September … softdusk.shop on 16 October)". Matches that are a different product are said apart: "2 more matched the term but are a different product (a cooling gel mask)". A store without a match is "no match among the first 1,000 products read": never say it added nothing, and it may have sold it for longer. Unreadable and not-Shopify stores are stated with their count, never guessed ("2 not on Shopify, 1 unreadable: not counted"). With `partial: true`, say so and why (`stopReason`), and that N of M covers the stores read.
- **A store wave** (stores adding the product): **3 or more** confirmed stores, making **a third or more** of those read, in the last 30 days, from the Shopify read; print the threshold beside the number. It is not the **late wave** above (newcomer advertisers in the ad library, 5 or more in 14 days, a third of the active advertisers): each is stated with its own source and threshold; both can appear, never merged into one line or one count. Under the threshold: "no store wave: the advertisers mostly sell it already".
- **Its reading follows the Where you'd compete reading** (crowd and budget band together, the tables above):
  - **Room** (4 or fewer advertisers, whatever the band): "others are finding it now: move early, with an angle".
  - **Crowded, read against** (the testing reading): "a crowd arriving: you'd be outbid testing the same pitch"; an unserved angle matters more than before (the fix above, checked against their ads).
  - **Crowded, read neutral** (the middle reading) or **between:** neutral, with the unserved angle as a line.
  - **Crowded, read in favour** (the outlasting reading): demand being proven now: several stores think it's worth a launch this month; the ones still advertising in five weeks join the proven count.
- **Never counted, never a gate.** It is one line beside Where you'd compete: it doesn't change that row, the for/against count or the label, and never makes "not this one" or "a long shot". It goes in the For you block's ad-cost line, after the advertiser counts.

## Said exactly

**Two Meta reads, never blurred.** The lasting-ads read (`minDaysRunning: 35` on the niche's keyword: which stores have kept ads running 35+ days) shows that ads for the niche have paid for someone; Where you'd compete (one row per advertiser for each idea: how many stores advertise it, active, proven and new) is the crowd for each idea. When only the first was read, a line about the missing read names both exactly, in plain words: "I read which stores have kept ads running 35+ days for "cat toys"; I haven't yet counted how many stores advertise each idea (the Where you'd compete read)". Never "the ideas are missing the ads check", "how many stores already run Facebook and Instagram ads for them" as if nothing on Meta were read, or the lasting-ads advertisers counted as Where you'd compete's crowd.
