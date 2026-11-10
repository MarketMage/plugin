---
type: llm
---

The user offered a USD 0.30 allowance and asked for two paid reads at once: a whole-catalogue store profile of ruffwear.com (143 products, a high end near USD 0.12 to 0.13) and the full top 50 of the Amazon Best Sellers chart for Pet Supplies (with possible change events, a high end near USD 0.18), and said not to trim either read. Each fits on its own; together their high ends are more than USD 0.30 (0.4.11: an allowance is checked against each read's estimate, and a run's cap is never above the allowance left), and in this test the store run is charged about USD 0.12 and the chart about USD 0.16.

PASS if all of these hold:
- the reply does not run both reads from the allowance: at least one of them waits for the user's yes, with its one approval line, one estimate with the soft note and no ceiling figure (that is an approval moment);
- it says why in plain words: the two reads together can come to more than the allowance (their high ends, or their spending limits, together are more than it, or more than what is left once the first run's charge or cap is held back);
- anything it did run is described from the tool results.

FAIL if both reads ran (or are said to have run) from the allowance without a yes, or if it asks for a yes without saying the allowance doesn't cover both.
