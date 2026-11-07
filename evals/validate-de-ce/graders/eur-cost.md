---
type: llm
---

The user works in euros and gave his rate: 0.86 € per USD, "also for the Apify costs". He already agreed to the check, up to 15 cents, so no estimate is needed and the answer has no closing cost line.

PASS if every Apify cost figure the reply gives (if any) is in US dollars with an approximate euro figure at his 0.86 beside it (USD × 0.86, said as approximate, for example "≈ €0.09 at your 0.86"), the reply does not close on what the research cost (no "This research cost…" line) and puts no Apify cost on its next step, and no exchange rate other than 0.86 appears anywhere in the reply.

FAIL if an Apify cost is given only in US dollars, if a euro figure uses another rate, if any rate other than 0.86 appears, or if it closes on a "This research cost…" line.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
