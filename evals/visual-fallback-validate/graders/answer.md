---
type: llm
---

The data read for heated eye masks on Amazon US favours the idea on every signal (demand rising about 96% over 5 years, a page-1 review median of about 310, a top-3 seller share of about 0.22, 4 ads in 48, a factory median of about USD 4.80 against the USD 29.99 price). Since 0.4.22 the Margin row is scored after freight and launch ads: at USD 29.99 a sale pays out USD 20.87 after Amazon's fees; minus the USD 4.80 factory median and freight of 15 to 30% of it (an assumption) it leaves about USD 14.63 to 15.35 before ads (the break-even ad cost per sale, about USD 14 to 15), and after USD 8 of launch ads about USD 6.63 (about 22%), under 25%: the margin reads against after ads, so the market verdict is **Promising, with one fix**, the fix being the ad cost per sale (under about USD 7 a sale it keeps a healthy margin), with a medium verdict confidence (it hangs on the ad cost).

PASS if all of these hold:
- the reply's first line is the verdict line ("For the market: Promising, with one fix…" or a direct plain answer to "is it worth selling" followed by that line), with its confidence and counts;
- the signals are shown in a Markdown table (rows of cells separated by "|") with their numbers, including a margin row;
- it ends on a next step, and it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step;
- it says nothing about charts, visuals, diagrams or drawing: no apology, no "I can't draw the margin here", no offer to draw one, no placeholder where a chart would go.

FAIL if the signal table is missing, if the reply mentions a chart or visual in any way (including saying one can't be shown), or if it contains Mermaid, HTML, SVG, chart code or a chart drawn with text characters.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
