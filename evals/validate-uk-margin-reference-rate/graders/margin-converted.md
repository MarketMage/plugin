---
type: llm
---

UK seller, Amazon UK, FBA. The supplier prices are in US dollars (median about USD 4.80 a unit) and the selling prices in pounds (median about £27.49, VAT included). The plugin's reference rate is about USD 1.34 to £1 (0.747 £ per USD), the ECB's reference rate of 6 Nov 2026.

PASS if all of these hold:
- the reply works out a margin (or what a sale leaves) in pounds, converting the US-dollar unit cost at an approximate rate it states;
- that rate is labelled as approximate with its date or source (for example "about USD 1.34 to £1, 6 Nov 2026" or "the ECB's rate"), not presented as the user's own rate;
- it does not leave the margin unknown for want of a rate, and does not ask the user what exchange rate they use (inviting their landed cost in pounds, or their own rate, as an optional refinement is fine).

FAIL if the margin is left unknown or "needs your rate", if the user is asked for their exchange rate before a margin is given, or if a conversion appears with no rate or date stated.
