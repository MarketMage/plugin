# Find products: the ongoing watches

Step 5 of the `find-products` skill, read when the user wants to keep an eye on the niche or asks what a watch would cost: the weekly opportunity digest, TikTok Shop sales per day and chart moves, as watchlists (`references/watchlists.md`). Reading their digests later is step 6 of `SKILL.md`.

Offer these with the answer when the user wants to keep an eye on the niche ("once or ongoing", `references/running.md`). All are Watch Digest watchlists (`references/watchlists.md`), so their results go to "your briefing in Claude, on request or on a Monday schedule" (sent to Slack, Discord, Teams or email only when the user asks), and the `watchlists` skill reads them.

**The weekly opportunity digest** (the one to offer first: new rising products in the niche, every week), task `cw-opps-<niche>`:
- **Input:** `cleanpull/watch-digest` with, in one task:
  - `trendsTerms`: the niche's product types and the rising searches this run found (at most 100; 5 to start), `trendsGeo` (the marketplace country, `US` by default), `trendsTimeRange: "past-90-days"` (suits a weekly digest), `trendsMinInterestChangePercent` (50 by default: a term's latest quarter of the period against its earliest);
  - `chartCategories` (the department read in step 2), `chartTypes: ["new-releases"]` (add `movers-and-shakers` if the user wants climbers too), `chartMarketplaces`, `chartMaxItemsPerChart: 50`;
  - `tiktokKeywords` (US only; the niche term), `tiktokMaxProductsPerKeyword: 20`;
  - `monitorName: "<niche>"`, `title`, `maxRunCostUsd`.
- **What it reports:** the digest opens with an **Opportunities this week** section: new rising searches and breakouts first, then new entries on the chart, then TikTok Shop products selling faster. Every other change follows by watcher. The first run is the baseline (rising searches remembered, chart and TikTok recorded): rising searches and chart entries start with the second run, TikTok products speeding up with the third (the second gives the first units per day). Interest moves are Google's relative interest (0 to 100), not search counts.
- **Cost per run, weekly** (`references/costs.md`): digest USD 0.005 + USD 0.00025 per item (term, chart, keyword); each Trends term USD 0.0015 every run; the chart and TikTok parts as below. **Example:** 5 terms, the New Releases chart of one department at 50 ranks, and 1 TikTok keyword: first run ≈ 0.005 + 7 × 0.00025 + 5 × 0.0015 + 50 × 0.0015 + 0.002 + 0.06 ≈ **USD 0.15**; later runs ≈ 0.005 + 0.002 + 0.0075 + about 0.04 for the chart's moves + up to 0.06 for TikTok ≈ **USD 0.115 a run, about USD 0.50 a month**. Without TikTok (outside the US, or to keep it light) about USD 0.25 a month. Daily isn't needed: the section is built for a week.
- **`maxRunCostUsd`:** about 1.5× a typical run (USD 0.17 for the example); the baseline run uses the first-run cap (about USD 0.23).
- **Steps:** follow `references/watchlists.md` (cost, yes, task, baseline, schedule weekly, where the results go). If the user keeps a notebook, link the watch to the niche's idea entry (`references/notebook.md`).

**TikTok Shop sales per day** (US only), task `cw-tiktok-<name>`:
- **Input:** `cleanpull/watch-digest` with `tiktokKeywords` (at most 100), `tiktokMaxProductsPerKeyword` (20 by default), `monitorName: "<name>"`, `title`, `maxRunCostUsd`.
- **What the digests report:** the top products' units per day from the second run; from the third, products speeding up or slowing down; products new to the keyword; price moves.
- **Cost per run:** digest USD 0.005 + USD 0.00025 per keyword; the first run delivers each keyword's top products in full (20 × USD 0.003 = USD 0.06 a keyword); later runs the ones that sold or changed (USD 0.003 each) and USD 0.0005 per unchanged one, so up to about USD 0.06 a keyword. **Example:** 1 keyword weekly ≈ USD 0.065 a run at most, about USD 0.28 a month; daily up to about USD 1.95 a month. Weekly or every few days is enough to see a trend.

**Amazon chart watch** (new entries, re-entries, climbers), task `cw-charts-<name>`:
- **Input:** `cleanpull/watch-digest` with `chartCategories` (department slugs, names or `department/node`, as in step 2), `chartTypes` (`best-sellers` and `new-releases` by default; also `movers-and-shakers`, `most-wished-for`, `gift-ideas`), `chartMarketplaces` (US by default), `chartMaxItemsPerChart` (100 by default), `chartMinRankChange` (10 places by default), `monitorName: "<name>"`, `title`, `maxRunCostUsd`. At most 200 charts (categories × chart types × marketplaces).
- **Brands entering** need product pages: `chartProductDetailsTopN` (0, off, by default) reads that many top products per chart at USD 0.004 each. Offer it only when the user asks which brands are coming in.
- **Cost per run:** digest USD 0.005 + USD 0.00025 per chart; the first run reads every rank (USD 0.0015 each: USD 0.15 for 100) + USD 0.002 a chart summary; later runs USD 0.002 per move and USD 0.0001 per unchanged rank, about USD 0.03 a chart a day. **Example:** `kitchen`, Best Sellers and New Releases, 100 ranks, daily: first run ≈ USD 0.31, then about USD 0.065 a run, about USD 1.95 a month. With `chartMaxItemsPerChart: 50` and Best Sellers only: first run ≈ USD 0.08, then about USD 0.02 a run, about USD 0.65 a month.

**Both:**
- **`maxRunCostUsd`:** about 1.5× a typical run, at least USD 0.02; the baseline run uses the first-run cap (`references/watchlists.md`, step 4). These watchers stop cleanly at their share of the cap and keep what they didn't deliver for the next run; a digest that says one stopped early needs a higher figure.
- **One digest:** both can go in one task with other watches (`watchlists` skill, "Change"), named for its main kind.
- **Steps:** follow `references/watchlists.md` (cost, yes, task, baseline, schedule, where the results go).
