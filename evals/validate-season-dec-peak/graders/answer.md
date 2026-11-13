---
type: llm
---

PASS if the reply gives a market verdict with its label (Strong, Promising, with one fix, or Not this version), two confidences (the verdict's, and whether the data is complete), the margin after fees and after launch ads (labelled assumptions) with the break-even ad cost per sale stated, and ends on one Next step line (at most two "After that" items in it) with no Apify cost.

FAIL if any of those is missing, or if the reply ends on the verdict or a menu of moves.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
