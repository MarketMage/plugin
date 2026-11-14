---
type: llm
---

The user said they use a screen reader. Since 0.4.23 validate's first answer is a scorecard; in the screen-reader shape it keeps the scorecard's order in plain sentences or a plain numbered list, with each badge said as a word (good sign, watch, warning sign, not read) instead of an emoji, no table, and no report artifact. The data: heated eye masks at $28.99 on Amazon US, **Promising, with one fix** (works under about $5 of ads a sale; loses money over about $12), verdict confidence medium, data complete.

PASS if all of these hold:
- it opens with the verdict ("Promising, with one fix") for heated eye masks and a plain sentence of why;
- the signal areas (such as demand, market size, competition, profit, product fit) are given in words, each with a word for its reading, at most five;
- the deciding number (about $12 break-even and/or about $5 healthy ad cost a sale) and both confidences are stated;
- it ends on one "Next step:" line;
- it says nothing about a report, artifact or chart.

FAIL if it uses emoji or a table, mentions a report or chart, or leaves out the verdict or the next step.
