---
type: llm
---

PASS if all of these hold:
- the reply gives a verdict (Strong, Promising with one fix, or Not this version; or Go, Maybe or No) with a confidence and its for/against counts (the data here reads mixed: Promising, the Maybe outcome; since 0.4.22 the margin is scored before ads and a Launch ads row judges what a sale leaves before ads against USD 8 to 12 of launch ads; a Not this version that follows the reply's own counts passes too);
- it shows the signals with their numbers apart from the judgement;
- it gives a margin estimate that uses a supplier unit cost (the data shows a Made-in-China median of about 1.13 US dollars) against the 19.99 price, and says what the margin leaves out or assumes (freight, duties, fees or ads; since 0.4.22 a freight allowance comes off, and USD 8 to 12 of launch ads a sale are set against the break-even, labelled as assumptions; either way passes);
- for a Promising/Maybe it names the fix or test that would settle it; and it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step (beyond the move's own one estimate, allowed since 0.4.23).
FAIL if there is no margin estimate, the supplier cost is invented, or there is no verdict with counts.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

Since 0.4.23 (the scorecard), the first answer's Next step line says the move's cost when it has one: a free step says it is free (with its time), and a MarketMage read may carry its one estimate ("about $0.14"); that is the approved shape and does not count as an Apify cost on the next step. A closing "This run cost…" line still fails. Money may be written with $ rather than USD.
