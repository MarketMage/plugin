---
type: llm
---

PASS if the reply names the cheapest offers found, with their stores and prices taken from the results (Best Buy at 228 among the lowest), and gives no cost at all: a check under USD 0.05 just runs, with no estimate before it and no cost line after it.
FAIL if it gives a cost line (before or after the check) or a price on its next step, or names stores or prices that do not appear in the tool results.
