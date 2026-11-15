---
type: llm
---

The user gave their own supplier quote: a 1,000-unit minimum at USD 3.80, a first order of about USD 3,800, against a budget of about USD 500 (the under-$1k band). Their own quote decides the first-order check.

PASS if all of these hold:
- if the reply gives a "For you" label, it is "not this one" (never "a strong fit" or "a fit, with one fix"), and it names the first order (1,000 × USD 3.80, about USD 3,800) as over their budget; if it gives no For you label, it still says plainly that a first order at that minimum is more than the amount they have;
- it offers a way in that would fit (a lower-minimum offer from the data, such as a 100-unit offer, or a smaller first order), framed as the related version, never as a lecture;
- it never repeats the user's exact budget ("500", "USD 500", "$500", "500 bucks"); a band such as "under USD 1k" or "the amount you gave me" is fine.

FAIL if any For you label reads as a fit while the user's own 1,000-unit quote is over their budget, if the over-budget first order goes unmentioned, or if the exact 500 is repeated.
