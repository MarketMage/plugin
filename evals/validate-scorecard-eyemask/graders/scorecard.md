---
type: llm
---

The data (heated eye masks at $28.99 on Amazon US): searches up about 96% over 5 years; the top 10 sell at least 14,000 units a month; review median about 310; top-3 seller share about 0.22; 4 ads in 48. A sale pays out $20.28 after Amazon's fees; minus the $6.10 factory median and freight (15 to 30% of the unit cost, an assumption) it leaves about $12.35 to 13.26 before ads (the break-even ad cost per sale); the healthy ad cost is about $5.10. Against $8 to 12 of launch ads a sale (an assumption) the ad cost decides it, so the verdict is **Promising, with one fix**, verdict confidence medium (it hangs on the ad cost), data complete.

Since 0.4.23 the first answer is a scorecard readable in 10 seconds, in this order: (1) a headline with a badge emoji (🟡 for Promising), the product and the label "Promising, with one fix" with what it turns on; (2) one bold sentence of why in plain words; (3) signal chips, at most five, each a badge emoji (✅, ⚠️, ❌ or ❔) and a few words, covering areas such as Demand, Market size, Competition, Profit, Product fit; (4) the deciding number: the break-even ad cost per sale (about $12) and/or the healthy ad cost (about $5), in plain words; (5) both confidences on one short line (data complete, verdict confidence medium with its reason); (6) one "Check first" line naming a risk in plain words; then at most a few required lines and one short offer line for the full detail; (7) the Next step line last.

PASS if all of these hold:
- the reply opens with the headline (badge emoji, product, "Promising, with one fix"), with nothing before it but at most one short sentence;
- there is one bold sentence of why near the top;
- there are between 3 and 5 signal chips, each starting with a badge emoji, and no more than 5;
- the deciding number (break-even about $12 to 13.5 a sale, and/or healthy about $4 to 6 a sale) is stated;
- both confidences are given: data complete and verdict confidence medium (with a reason about the ad cost);
- exactly one line starts with or is labelled "Check first";
- the reply ends on one "Next step:" line, whose move measures the ad cost (for example looking up the suggested bid for "heated eye mask" in the Amazon ad console), which says it is free; at most two "After that" items in that line; no second menu competing with it (one short offer line for the full detail before it is fine);
- money is written with "$" (e.g. "$28.99", "about $5"), not "USD";
- there is no signal table (no Markdown table) in the reply: the table waits for the full detail.

FAIL if the verdict is not Promising, with one fix; if chips are missing or more than five; if the deciding number or either confidence is missing; if the reply contains a Markdown table, analyst notation (HHI, p25/p75, MOQ, "favours (≥ …)", "4 for · 0 against"); or if it ends on anything other than the Next step line.
