---
type: llm
---

The data read for heated eye masks on Amazon US favours the idea on every signal (demand rising about 96% over 5 years, a page-1 review median of about 310, a top-3 seller share of about 0.22, 4 ads in 48, a factory median of about USD 4.80 against the USD 29.99 price). Since 0.4.22 two rows read the money: the Margin row, before ads (at USD 29.99 a sale pays out USD 20.87 after Amazon's fees; minus the USD 4.80 factory median and freight of 15 to 30% of it, an assumption, it leaves about USD 14.63 to 15.35, about 49%: favours), and the Launch ads row (that break-even ad cost per sale, about USD 14 to 15, against USD 8 to 12 of launch ads a sale, an assumption: after USD 12 a sale keeps about USD 2.63, under 25% of the price, and the ad cost that keeps 25% is about USD 7: neutral). A neutral Launch ads row caps the market verdict at **Promising, with one fix**, the fix being the ad cost per sale (it works under about USD 7 a sale and loses money over about USD 14), with a verdict confidence one step down for it (medium; low when the reply also names a thin source, such as few matching factory offers, which is fine).

PASS if all of these hold:
- the reply's first line is the verdict line ("For the market: Promising, with one fix…" or a direct plain answer to "is it worth selling" followed by that line), with its confidence and counts;
- the signals are shown in a Markdown table (rows of cells separated by "|") with their numbers, including a margin row;
- it ends on a next step, and it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step;
- it says nothing about charts, visuals, diagrams or drawing: no apology, no "I can't draw the margin here", no offer to draw one, no placeholder where a chart would go.

FAIL if the signal table is missing, if the reply mentions a chart or visual in any way (including saying one can't be shown), or if it contains Mermaid, HTML, SVG, chart code or a chart drawn with text characters.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
