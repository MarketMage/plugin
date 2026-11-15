---
type: llm
focus: trace
---

The AliExpress single-unit check (`cleanpull/aliexpress-scraper`, top 3 with their product pages) can take several minutes; the plugin waits for it once (45 seconds) before answering. In this run it had already finished when the plugin waited on it: its `get-actor-run` (or its `call-actor`) returned SUCCEEDED the first time, with its three rows: the USB rechargeable mask at USD 8.49 with USD 2.19 shipping to the US (`landedPrice` USD 10.68), the cordless steam mask at USD 6.20 with `shippingCost` 0 (shipping not established: plus shipping still to add, never free; its USD 1.09 is a one-time new-shopper deal, never the cost) and a graphene mask at USD 7.35 whose page wasn't read (`detailsRead: false`: shipping not read). All three sell single units. The user is a first-time seller under USD 1k dropshipping on Amazon US, so the Marketplace lens applies: gate 2 (single units) and the margin row (at USD 29.99 after Amazon's fees) read from that check, with the unit cost the answer names from those rows (the USD 10.68 delivered cost of the rechargeable one that leads the page, or USD 6.20 with shipping still to add as a best case).

You see the whole run: the assistant's messages and its tool calls in order.

PASS if all of these hold:
1. **One answer with the result in it:** the answer that gives the verdict already reads gate 2 from the check (one-unit offers exist, with a price from the actor's rows and its shipping as the rows give it, never "free shipping") and the margin with the unit cost it used said plainly.
2. **Nothing marked as pending:** no message says AliExpress is still being read, is slow on this one, or will be added later; gate 2, the margin and the For you verdict are not marked "(provisional)" because of AliExpress.
3. **No follow-up:** the turn does not end with a promise to post the AliExpress result later, and there is no separate later message that adds the AliExpress price or changes the label ("now: …") after an answer already given.

FAIL if any message labels gate 2, the margin, the AliExpress price or the For you verdict as provisional, still reading or pending AliExpress (for example "still reading AliExpress", "AliExpress is slow on this one", "(provisional)" on those parts), if any message promises a follow-up for the AliExpress result ("I'll add it when it lands", "I'll post a follow-up"), if a second message re-reads gate 2 or gives a "now: …" label after the answer, or if the answer gives no AliExpress single-unit price although the check returned one. A line saying the AliExpress price usually takes under a minute, said before the run, is fine.
