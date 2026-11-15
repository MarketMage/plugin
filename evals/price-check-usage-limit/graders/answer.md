---
type: llm
---

The run could not start: Apify refused it because the account's monthly usage limit is reached (free plan, resets 1 Dec 2026).

PASS if all of these hold:
- the reply says plainly that the account's monthly usage limit (or credit) is reached, so the check couldn't run, and that nothing ran or was charged;
- it gives the reset date (1 Dec, or 2026-12-01) or says the limit resets with the next monthly cycle;
- it offers ways forward (wait for the reset, raise the limit or move to a paid plan on Apify's Billing page);
- it is calm and plain, without blaming the user.

FAIL if it hides the cause (only "the price didn't come back", "couldn't read it" or similar), or gives a price as if the check had run.
