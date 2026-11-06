---
type: llm
---

The data read for heated eye masks on Amazon US favours the idea on every signal (demand rising about 96% over 5 years, a page-1 review median of about 310, a top-3 seller share of about 0.22, 4 ads in 48, a factory median of about USD 4.80 against the USD 29.99 price), so the verdict is Strong.

PASS if all of these hold:
- the reply's first line is the verdict line ("For the market: Strong…" or a direct plain answer to "is it worth selling" followed by that line), with its confidence and counts;
- the signals are shown in a Markdown table (rows of cells separated by "|") with their numbers, including a margin row;
- it ends on a next step with its cost, and says what the research cost;
- it says nothing about charts, visuals, diagrams or drawing: no apology, no "I can't draw the margin here", no offer to draw one, no placeholder where a chart would go.

FAIL if the signal table is missing, if the reply mentions a chart or visual in any way (including saying one can't be shown), or if it contains Mermaid, HTML, SVG, chart code or a chart drawn with text characters.
