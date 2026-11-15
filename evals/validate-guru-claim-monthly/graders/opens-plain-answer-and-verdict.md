---
type: llm
---

Real-user test round 2 (R2-5): when the first answer to a check drew a chart, the chart came first and the answer to "is that real?" and the verdict sentence were never written. The first answer to a check draws no visual and opens with text.

PASS if all of these hold:
- the reply's very first line is plain text that answers "is that real?" (the 10k-a-month claim is not true, or not shown, as a monthly figure), not a heading, a table, an image, a chart or a chart title;
- within the reply's first ~150 words, before any table, there is a written market verdict sentence (a label such as "Promising, with one fix" or "Not this version", with why in a number or two);
- the reply contains no chart, diagram, image, Mermaid, HTML, SVG or text drawing of a chart, and says nothing about drawing one.

FAIL if the reply opens with anything other than the plain answer, if the verdict sentence is missing or comes only after a table, or if a chart or drawing appears.
