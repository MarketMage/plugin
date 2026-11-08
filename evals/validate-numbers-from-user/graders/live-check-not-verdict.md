---
type: llm
---

The user pasted numbers from another tool (average 30 reviews, top 10 doing 300+ sales a month, about 15k searches) and asked "back off or keep going?", without approving any spend.

PASS if all of these hold:
- the reply proposes a live check of this niche (reading Amazon's listings or leaders, demand or factory prices) with a cost estimate in USD and asks to go ahead, or it reports results from a check it ran;
- it does not give a "keep going" or "back off" verdict, or a market label (Strong, Promising, Not this version), built only on the user's own numbers: any lean it gives is said to depend on those numbers being confirmed;
- it does not hand the user checks to do by hand that the plugin can make (reading the top listings' 1-star reviews, checking the 12-month or 5-year trend, counting listings with a feature); such checks, if mentioned, are offered as reads it will make;
- it does not ask for a supplier cost before the check can run.

FAIL if it gives a full verdict on the user's numbers alone, lists manual research chores, or gates the check behind a supplier cost.
