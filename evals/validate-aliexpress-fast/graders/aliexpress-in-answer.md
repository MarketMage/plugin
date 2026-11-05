---
type: llm
focus: trace
---

The AliExpress single-unit check (`cleanpull/supplier-price-finder` with `singleUnitCheck: true`) usually returns in under a minute, and the plugin waits for it briefly before answering. In this run it had already finished when the plugin waited on it: its `get-actor-run` (or its `call-actor`) returned SUCCEEDED the first time, with 3 AliExpress offers read, all selling single units (`moq1OfferFound: true`), the cheapest MOQ-1 offer at USD 6.20 before shipping. The user is a first-time seller under USD 1k dropshipping on Amazon US, so the Marketplace lens applies: gate 2 (single units) and the margin row (at USD 29.99 after Amazon's referral fee, with USD 6.20 as the unit cost) read from that check.

You see the whole run: the assistant's messages and its tool calls in order.

PASS if all of these hold:
1. **One answer with the result in it:** the answer that gives the verdict already reads gate 2 from the check (MOQ-1 offers exist, at about USD 6.20 before shipping) and the margin with USD 6.20 as the unit cost (or says plainly which unit cost it used).
2. **Nothing marked as pending:** no message says AliExpress is still being read, is slow on this one, or will be added later; gate 2, the margin and the For you verdict are not marked "(provisional)" because of AliExpress.
3. **No follow-up:** the turn does not end with a promise to post the AliExpress result later, and there is no separate later message that adds the AliExpress price or changes the label ("now: …") after an answer already given.

FAIL if any message labels gate 2, the margin, the AliExpress price or the For you verdict as provisional, still reading or pending AliExpress (for example "still reading AliExpress", "AliExpress is slow on this one", "(provisional)" on those parts), if any message promises a follow-up for the AliExpress result ("I'll add it when it lands", "I'll post a follow-up"), if a second message re-reads gate 2 or gives a "now: …" label after the answer, or if the answer gives no AliExpress MOQ-1 price although the check returned one. A line saying the AliExpress price usually takes under a minute, said before the run, is fine.
