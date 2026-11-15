---
type: llm
---

PASS if the reply gives a market verdict with its label (Strong, Promising, with one fix, or Not this version), two confidences (the verdict's, and whether the data is complete), the margin after fees (before ads) and the launch ad cost (USD 8 to 12 a sale, a labelled assumption) set against the break-even ad cost per sale, which is stated, and ends on one Next step line (at most two "After that" items in it) with no Apify cost (beyond the move's own one estimate, allowed since 0.4.23).

FAIL if any of those is missing, or if the reply ends on the verdict or a menu of moves.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

Since 0.4.23 (the scorecard), the first answer's Next step line says the move's cost when it has one: a free step says it is free (with its time), and a MarketMage read may carry its one estimate ("about $0.14"); that is the approved shape and does not count as an Apify cost on the next step. A closing "This run cost…" line still fails. Money may be written with $ rather than USD.
