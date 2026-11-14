---
type: llm
---

In Claude Code, validate's first answer (since 0.4.23) is a scorecard: a headline with a badge emoji and the label, a bold sentence of why, at most five signal chips each with a badge emoji, the deciding number, both confidences on one line, one "Check first" line, then the Next step line last. The data: heated eye masks at $28.99 on Amazon US, **Promising, with one fix** (works under about $5 of ads a sale; loses money over about $12), verdict confidence medium, data complete.

PASS if the reply follows that scorecard shape (headline with 🟡 and "Promising, with one fix"; 3 to 5 chips; the deciding number; both confidences; one Check first line; ends on one Next step line) and says nothing about a report, artifact or chart.

FAIL if the scorecard parts are missing, if there is a Markdown signal table, or if the reply mentions a report, artifact or chart in any way.
