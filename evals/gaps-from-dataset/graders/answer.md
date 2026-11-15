---
type: llm
---

PASS if the reply reports, per competitor, the matched count and price position from the data: mountainhighoutfitters.com cheaper at the median (price index about 95, cheaper on 28 of the matched pairs) and alpenglowsports.com about the same (index 100), mentions what they sell that the user doesn't (gaps), and it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step (the user already agreed to up to USD 2).
FAIL if the numbers contradict that data, or it closes on a "This run cost…" (or "This research cost…") line, or puts an Apify cost on its next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
