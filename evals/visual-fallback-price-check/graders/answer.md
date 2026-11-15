---
type: llm
---

The barcode check found 16 offers for UPC 027242923232 (Sony headphones). The lowest confirmed-new price is USD 228 at Best Buy; an Amazon offer at USD 192.50 has its condition not stated.

PASS if all of these hold:
- the reply gives the offers in a Markdown table (rows of cells separated by "|") with stores and prices from the results, and names USD 228 at Best Buy as the lowest new price (the USD 192.50 Amazon offer is not called the cheapest new price unless the reply read that listing's offers and confirmed it new);
- it says what the check cost and ends on a next step;
- it says nothing about charts, visuals, diagrams or drawing: no apology, no "I can't show a chart here", no offer to draw one, no placeholder where a chart would go.

FAIL if the table is missing, if the reply mentions a chart or visual in any way (including saying one can't be shown), or if it contains Mermaid, HTML, SVG, chart code or a chart drawn with text characters.
