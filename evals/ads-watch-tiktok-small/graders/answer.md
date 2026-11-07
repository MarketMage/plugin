---
type: llm
---

The data: TikTok's library (UK market), checked by name for the five brands, one row per advertiser with each account's ad count. GlowNest UK (widest reach 1M-10M, 23 ads in TikTok's library, ads running at least 119 days), Heatwell Official (1M-10M, 4,812 ads, 201 days), SnoozeHaven (100K-1M, 9 ads, 77 days), EyeEase Shop (10K-100K, 41 ads, 21 days), Calmora (10K-100K, account size null, 47 days). None has a landing page.

PASS if all of these hold:
- it says TikTok's library can't be searched for long-running ads by keyword (results come newest first, or there is no date filter), so it checked the named brands instead;
- it stays within the user's 40 cents and it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step (the user already agreed to up to 40 cents, so no estimate is needed either);
- it names GlowNest and SnoozeHaven as proven small advertisers, with the rules of thumb stated (ads running 35 days or more; about 50 or fewer ads in TikTok's library, read as approximate or an order of magnitude);
- it does not count EyeEase as proven (only 21 days) and does not call Heatwell (4,812) small;
- it says Calmora's account size wasn't read (unknown), not small or large;
- the brands are listed widest reach first: the two 1M-10M brands (GlowNest, Heatwell, in either order) before SnoozeHaven (100K-1M), before the two 10K-100K brands (EyeEase, Calmora, in either order);
- it does not size or read stores (TikTok rows have none), invents no spend, sales or revenue, and ends with a next move with no Apify cost.

FAIL if it claims to have searched TikTok by keyword for long-running ads, closes on a "This run cost…" (or "This research cost…") line, or puts an Apify cost on its next step, counts EyeEase as proven, calls Heatwell small, counts Calmora as small, lists them in an order other than by reach without saying why, or invents spend or sales.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
