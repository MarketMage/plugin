---
name: gaps
description: Compare the user's product catalogue with one or more competitors' - which products both sell (matched by barcode, part number, SKU, model or title, with a confidence), the price gap on each, what competitors sell that the user doesn't (and the reverse), and an overall price index. Reads the catalogues from Shopify stores, any online store's product pages or Amazon first. Use when someone asks which of their products a rival also sells and at what price, what ranges a competitor carries that they don't, or whether they are cheaper or dearer overall.
---

# Catalogue gaps

Match catalogues and say where the user is cheaper, dearer, alone or missing. Read `references/running.md` first (costs, caps, tools, secrets, and the runs already made in this conversation) and `references/judgement.md` (the core: facts apart from judgement), with its parts only as each step needs them: `references/judgement-tone.md` (the tone) and `references/judgement-answer.md` before the answer, `references/judgement-ladder.md` (the watches) when offering one, `references/judgement-profile.md` (the seller profile) when there is one or it is to be offered, and with a profile, once the lens is chosen, `references/judgement-for-you.md` and the chosen lens's file only (`references/judgement-lens-cold-traffic.md`, `references/judgement-lens-marketplace.md`, `references/judgement-lens-own-stock.md`, `references/judgement-lens-maker.md` or `references/judgement-lens-general.md`; plus `references/judgement-lens-goals.md` when the goal is side income or brand). Prices are in `references/costs.md`. If the user asks to be remembered or keeps a notebook, follow `references/notebook.md`.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. Ask only for

- **The user's catalogue,** in the form they have it:
  - their store's domain (a Shopify store is read whole; another platform is read from its sitemap);
  - a dataset from an earlier CleanPull run in this chat (its `defaultDatasetId`);
  - or a short list they paste: title, brand, price, and a barcode or SKU where they have one (`yourItems`).
- **The competitors:** store domains, or Amazon ASINs or a search for the range.
- **Optional:** whether they want gaps both ways (default), only what competitors sell (`gaps: "they-sell"`), or none; and whether gaps should stay within brands the user already carries (`gapsInYourBrandsOnly`, on by default: the ranges they could add first).

## 2. Read the catalogues first

Catalog Matcher only matches datasets; it reads nothing from the web. So read each catalogue with the actor that fits, and **show the cost of these reads and the match together** before anything runs.

| Catalogue | Actor | Input | Cost on paid plans |
| --- | --- | --- | --- |
| Shopify stores (the user's and rivals' in one run) | `cleanpull/shopify-store-scraper` | `stores: ["mystore.com", "rival1.com", "rival2.com"]`, `maxProductsPerStore: 250`, `storeSummary: false` | USD 0.0008 per product: 250 a store ≈ **USD 0.20 a store** |
| Another platform | `cleanpull/any-store-product-monitor` | `sitemaps: ["brand.com"]`, `maxProductsPerSitemap: 100`, `includeVariants: true` | USD 0.0015 a product page: 100 ≈ **USD 0.15** |
| Amazon | `cleanpull/amazon-product-scraper` | `asins: [...]` or `searches: ["<range>"]` with `maxResultsPerSearch`, `marketplace` | USD 0.003 a product |

- **One Shopify run can hold every Shopify store,** the user's included: the matcher splits it by store and `yourStore` says which one is theirs.
- **Barcodes matter.** Shopify's public catalogue has no barcodes, so two Shopify stores match by part number, SKU, model or title only. Product pages read with Any Store usually carry barcodes (GTIN) from their structured data, and match exactly. Say this when it affects the result.
- **Large stores:** `maxProductsPerStore` up to 1,000 (about USD 0.80 a store) only if the user wants the whole catalogue.

## 3. Match

When the user gives a dataset from an earlier read, match it directly: Catalog Matcher reads it and says in `RUN_SUMMARY` if it isn't usable. Don't read the whole dataset into the chat first.

- **Run** `cleanpull/catalog-matcher` with:
  - `competitorDatasetIds`: the dataset IDs of the competitor reads (one ID can hold several stores);
  - `yourDatasetId` (the user's own read, if separate), or `yourStore: "mystore.com"` when their store is inside a competitor dataset, or `yourItems` for a pasted list;
  - `gaps` and `gapsInYourBrandsOnly` as agreed.
- **Cost:** USD 0.05 per competitor catalogue compared + USD 0.002 per matched pair + USD 0.0001 per gap row.
  - Pairs: estimate 10% of the smaller catalogue (rival stores usually overlap less: 2 to 4% in CleanPull's tests on outdoor stores; a reseller of the same brands can overlap much more). Gaps: up to the size of the other catalogue, fewer with `gapsInYourBrandsOnly`.
  - **Example:** the user's 250 products against two rivals' 250 each, all on Shopify: reads 750 × 0.0008 = USD 0.60; match 2 × 0.05 + about 80 pairs × 0.002 + about 300 gaps × 0.0001 ≈ USD 0.29. **About USD 0.90 in all:** say so and get a yes.
- **The cap** on the match run: 1.5× its estimate plus USD 0.05 (in a live check, a cap only a little above the estimate stopped the pairs while the summary still came out). If it stops at the cap, `RUN_SUMMARY` says so (`stoppedAtSpendingLimit`): say how many pairs the summary counted but weren't delivered, and offer a rerun with a higher cap.

## 4. Read the results

- **The `summary` row per competitor** (read in full): `matched`, `overlapPercent` (of the user's products), `medianPriceIndex` (their price as % of the user's: 95 means they are 5% cheaper at the median), `youAreCheaper`, `theyAreCheaper`, `samePrice`, `currencyMismatches`, `gapsTheySell`, `gapsYouSell`, `topGapBrands`.
- **Matches:** `get-dataset-items` with `fields: "recordType,catalogue,yourTitle,theirTitle,matchMethod,confidence,matchedOn,yourPrice,theirPrice,priceGapPercent,cheaper,priceNote,theirUrl"`.
  - `priceGapPercent` is theirs against the user's: −10 means they are 10% cheaper.
  - `confidence`: barcode matches are 1; title matches go up to 0.9. In CleanPull's test on 146 hand-checked title pairs, none at 0.85 or above was wrong. Treat pairs below 0.85 as "check by eye", and say why when `matchedOn` notes a doubt (gender or a number on one side only).
  - `priceNote` explains a gap that wasn't computed: different currencies are never compared.
  - **Check each pair you report like an analyst** (`references/running.md`, "Read the data like an analyst"): a title match can pair a 2-pack with a single, a different size or colour, a kit with the bare product, or a different model generation. Read both titles; a pair that isn't the same item is left out of the price comparison (and of the answer's counts), and the answer says how many. Barcode matches are the same item; title matches below 0.85 are checked first.
- **Gaps:** rows with `recordType: "gap"`, `direction` `they-sell` or `you-sell`, `title`, `brand`, `price`, `url`, `youCarryBrand`.
- **`RUN_SUMMARY`:** `droppedCatalogues` (a competitor whose read failed part-way is left out, with no charge) and `gapsSkipped` (the user's catalogue was read only in part, so gaps weren't made: say so, rather than reporting no gaps).

## 5. Answer

Facts first, then what they mean (`references/judgement.md`, rules 1, 5 and 6).
- **Price position first:** "On the 80 products you both sell, rival1 is 6% cheaper at the median; they undercut you on 31, you're cheaper on 22."
- **Confidence, from how the pairs matched:** the summary's `byMethod` (pairs matched by barcode against title, part number, SKU or model) and the share at `confidence` 0.85 or above. Mostly barcode or 0.85+: `high`; under half: `medium`, and say the price index rests on title matches to check by eye; very few pairs (under 10): `low`.
- **The counterweight, both ways:**
  - where the user is cheaper on most pairs, say what it wins (price position) **and** what it costs: the margin given up on those pairs (their price gap × the user's price), and whether matching the rival instead would still leave them cheapest;
  - where the user is dearer, say where the dearer items are ones only they sell (`gapsYouSell`), so the price is less constrained, and which shared items carry the gap.
- **The visual moment, after the price position** (`references/running.md`, "Explaining results": "One visual, where it helps"; only where you can draw one, and otherwise nothing about it is said): **where the matched pairs stand**, one stacked horizontal bar per competitor, split into the pairs they are cheaper on (`theyAreCheaper`, red), the same price (`samePrice`, grey) and the user is cheaper on (`youAreCheaper`, green), each part labelled with its count after any pair left out as not the same item, and the competitor's `medianPriceIndex` written at the bar's end ("94: 6% cheaper at the median"). Caption: the catalogues, the date read and the confidence ("high: 72 of 80 pairs by barcode").
- **The biggest gaps on shared products:** the top 10 by `priceGapPercent`, with both prices and confidence.
- **What they sell that you don't,** grouped by brand (`topGapBrands`): ranges to consider adding. **What only you sell:** where you have no direct price competition.
- **For you:** only with a profile (`references/judgement-profile.md`, "The seller profile and lenses"), in its own block, each line naming its fact, never the budget as a reason: for example "because the first order of gap items is 200 units at USD 3.10, start with the 2 cheapest gap items", or "because 14 of the gap items are in brands you already carry, add those first (no new supplier account)".
- **Caveats in one line:** prices as listed, no shipping or tax; title matches below 0.85 need a look; a competitor showing compare-at prices on most products may be listing sale prices as its usual price.
- **Where the user stands strong,** in one line with its number: the products only they sell, or the shared ones where they are cheapest. Credit tied to the data, never about the person.
- **Next steps,** the most useful last: `export` to put the matches in a sheet; `price-watch` on the matched products where a rival already undercuts the user; the undercut watch (step 6) to hear when a rival newly sells one of the user's products for less (the early sign of a price move), with its cost.

## 6. Ongoing: watch for undercuts

When both the user's store and the rivals are Shopify stores, offer "watch for undercuts": one weekly task that reads the stores, matches them and reports what changed. (For other platforms, a scheduled comparison isn't offered: a pasted list or an old dataset wouldn't refresh.)

- **The task:** `create-actor-task` for `cleanpull/catalog-matcher`, named `cw-gaps-<name>` (`references/watchlists.md`, "Naming"), with:
  - `yourStore: "mystore.com"` (read in the same run, since nothing else holds the user's products);
  - `competitorStores`: up to 10 Shopify stores, each read in the run by a Shopify Store Scraper run in the user's account, at its own prices;
  - `alertUndercutPercent`: the gap that counts, for example 5 (0 for any amount);
  - `monitorName: "<name>"`, `changesOnly: true`, and `gaps` and `gapsInYourBrandsOnly` as agreed in step 1;
  - `maxRunCostUsd` (below).
- **What later runs report:** `undercut` changes (a pair where the rival is now at least that much cheaper and wasn't on the last run, with `gapPercent`), and the other changes: `new-match`, `your-price`, `their-price`, `new-gap`, and `match-lost` or `gap-closed` (after two runs). Each summary row gives `undercuts` and `newUndercuts`.
- **Cost, at 250 products a store** (store reads included: USD 0.0008 a product, the user's store too):

  | Rivals | First run (the baseline: every pair, at most) | A typical run | A month, weekly |
  | --- | --- | --- | --- |
  | 1 | USD 0.95 | USD 0.48 | about USD 2.10 |
  | 2 | USD 1.70 | USD 0.76 | about USD 3.30 |
  | 3 | USD 2.45 | USD 1.05 | about USD 4.50 |

  Larger stores cost more in proportion (USD 0.20 per 250 products a store a run). Show the first-run and typical figures and the monthly cost, and get a clear yes.
- **`maxRunCostUsd`:** about **USD 2 for one rival, 3 for two, 4 for three** at 250 products each, and USD 1 more for each further rival up to 10 (more for larger stores), on the task and in the baseline run. Unlike other watches, it stays at the first-run figure: the matcher divides it among the store reads, and a rival whose share is too small is skipped (unread, unpaid, with a reason giving the limit to set). Later runs charge only what they use.
- **Weekly** is the default cadence: each run reads every store in full.
- **Steps:** follow `references/watchlists.md` (cost, yes, task, baseline run now with a cap of the same `maxRunCostUsd`, then `create-schedule`).
- **Delivery:** results stay in the user's Apify account and go to "your briefing in Claude, on request or on a Monday schedule"; the `watchlists` skill also reads them on request ("what changed in my undercut watch?"). Don't bring up channels. Only if the user asks for email or chat alerts, say plainly that this watch can't send them: Catalog Matcher sends no messages.

## 7. Reading an undercut watch later

Lead with the new undercuts (product, their price against the user's, `gapPercent`, the link), then the user's price moves and the rivals', then new matches and new gaps. From the summary rows, say how `undercuts` and the `medianPriceIndex` moved. If `RUN_SUMMARY` says a rival was skipped for its share, give the `maxRunCostUsd` it names.
