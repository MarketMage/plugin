---
type: llm
---

The user is on claude.ai, where validate's first answer (since 0.4.23) is a chat scorecard followed by a one-page report made as an artifact (here written as an .html file with the Write tool). The data: heated eye masks at $28.99 on Amazon US, **Promising, with one fix**: it works if ads cost under about $5 a sale and loses money over about $12 (the break-even ad cost per sale), verdict confidence medium, data complete.

PASS if all of these hold:
- the reply's text gives the scorecard on its own (a reader who never opens the report still has the answer): a headline with a badge emoji and "Promising, with one fix", a bold sentence of why, signal chips (at most five, each with a badge emoji), the deciding number (about $12 break-even and/or about $5 healthy), both confidences, one "Check first" line and one "Next step:" line;
- the Next step line is the reply's last line (the report itself is checked by other graders: this text need not mention it, and should not add a line after the Next step);
- it does not apologise for, or explain how, the report was made, and doesn't paste HTML into the reply.

FAIL if the scorecard is missing or only in the report, if the reply contains HTML or SVG code, or if the verdict is not Promising, with one fix.
