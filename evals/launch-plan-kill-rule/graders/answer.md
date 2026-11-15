---
type: llm
focus: trace
---

The user dropships heated eye masks through their own store with Facebook ads, budget band under USD 1k, starting ads on 1 November 2026. The plan's data: Amazon leaders USD 18.99 to 39.99 (band 22.99 to 34.99), AliExpress one-unit offers from about USD 6.20 plus shipping still to add, and the leaders' complaints (masks that stop heating, cool quickly, tight straps, short cables).

In this run the AliExpress single-unit check was slow (its product pages) (still running after its wait, several minutes in all), so the reply comes in two parts: the first answer, with what reads from that check marked as still reading AliExpress, and a short follow-up that adds it when it lands. You see the whole run (messages and tool calls); judge the assistant's messages. Judge the whole plan, both parts together: a figure or plan part given in either counts.

PASS if all of these hold:
- the plan includes a stop rule agreed before launch, with numbers: a test spend and length from the under-USD-1k band (about USD 150 of ads or 7 days, whichever comes first, or close figures stated as rules of thumb), an add-to-cart threshold that means stop (about 2% of visitors), and the curiosity case (click-through high, about 1.5% or more, with add-to-cart under the threshold = curiosity, not intent, so change the offer or page, not the creative);
- the stop rule has a check date worked out from 1 November (about 8 November);
- it asks the user to agree the rule or change a number, and does not claim to have saved it anywhere;
- the rest of the plan is present in short form: suppliers (single units for dropship), the complaints, a listing or page draft with a difference that answers them, and the price position;
- it offers the launch-week watch only as an offer (not created), and it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step.

FAIL if there is no stop rule, if the stop rule has no numbers, if the rule's spend is not tied to the budget band (for example a figure above the under-USD-1k band's typical test), if it says the rule was saved to a notebook, if it creates a watch, or if it closes on a "This run cost…" (or "This research cost…") line, or puts an Apify cost on its next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
