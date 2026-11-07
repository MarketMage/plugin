---
type: llm
---

The user works in euros and gave his rate: 0.86 € per USD, "also for the Apify costs". He agreed no budget, and the check costs more than USD 0.05, so this is an approval moment.

PASS if all of these hold:
- the reply gives one estimate for the check in US dollars (for example "up to about USD 0.12 (with a spending limit)") with an approximate euro figure beside it at his 0.86 (USD × 0.86, said as approximate and as at his rate, for example "≈ €0.10 at your 0.86");
- it asks him to confirm before running, and presents no research results;
- no exchange rate other than 0.86 appears anywhere in the reply.

FAIL if the estimate is only in US dollars, if a euro figure uses another rate or isn't marked approximate, if any other rate appears, if there is no estimate, or if it presents results as if the check had run.
