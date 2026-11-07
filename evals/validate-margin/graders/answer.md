---
type: llm
---

PASS if all of these hold:
- the reply gives a verdict (Strong, Promising with one fix, or Not this version; or Go, Maybe or No) with a confidence and its for/against counts (the data here reads mixed: Promising, the Maybe outcome);
- it shows the signals with their numbers apart from the judgement;
- it gives a margin estimate that uses a supplier unit cost (the data shows a Made-in-China median of about 1.13 US dollars) against the 19.99 price, and says what the margin leaves out (freight, duties, fees or ads);
- for a Promising/Maybe it names the fix or test that would settle it; and it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step.
FAIL if there is no margin estimate, the supplier cost is invented, or there is no verdict with counts.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
