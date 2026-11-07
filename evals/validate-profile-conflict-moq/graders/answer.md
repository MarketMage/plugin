---
type: llm
---

The market data favours this idea (Strong for the market: demand +95.6% over 5 years, a top-10 sales floor of about 14,000 units a month, median 310 reviews, top-3 share 0.22, 4 ads in 48). The user's own quote is USD 9 a unit with a 500-unit minimum: a first order of about USD 4,500, far above their under-USD-1k band (they said about USD 600; that exact figure must never appear). The user's quote decides the first-order gate: it replaces the supplier medians. Made-in-China offer rows, if read, are related versions. The real offer rows, each with its price range per unit, are:
- MOQ 50 at USD 4.80–5.40 (Yiwu Sunny Trade; about USD 240–270 for 50);
- MOQ 100 at USD 3.90–4.40 (Ningbo Restwell; about USD 390–440);
- MOQ 200 at USD 4.50–5.10 (Dongguan Comfy Health; about USD 900–1,020);
- MOQ 300 at USD 6.20–7.00 (Xiamen Healthy Life);
- MOQ 500 at USD 2.60–3.20 (Shenzhen Warmtech).
The summary's medians (MOQ 200, USD 4.80) are not an offer, even though USD 4.80 falls inside the 200-unit row's range. Saying the median as a median ("factories quote about USD 4.80 typical", "the median factory price") is fine; only presenting it as a specific offer to order from is a fail.

PASS if all of these hold:
- the answer leads with "For you: not this one", naming the user's quoted first order against the budget as the deciding fact (the quote fails the first-order gate); then "For the market: Strong" (or Go) with its counts;
- the conflict is stated with numbers: the first order (500 × USD 9 ≈ USD 4,500, or the same arithmetic) against the band's edge, written as a band ("under USD 1k", "up to $1k"), or, since the user named an exact amount, against that amount without repeating it ("more than the amount you gave me", "doesn't fit the amount you gave me": `judgement-lens-own-stock.md`, "Against the amount you gave me"), never the exact USD 600;
- because the For you and market verdicts differ, one sentence on the first screen says why (the market is strong, but this first order doesn't fit the budget band);
- the voice stays a hopeful collaborator: the weak fit is said once, kindly, and the answer builds on the user's idea; no doom ("you can't afford this", "forget it", "too risky for a beginner"), no hype, and no comment on the profile itself (not "don't worry, everyone starts somewhere", not "as a beginner you should...");
- it offers at least one related version that fits the profile, with its numbers or cost: a smaller first order from a lower-minimum offer (for example the 50-unit offer at USD 4.80, about USD 240), asking their supplier for a smaller MOQ, a supplier check at their quantity, or a single-unit / dropship start; a cited offer passes only when its MOQ and its price both match the same row above (the price inside that row's range); the facts table and the market verdict are not changed by the profile;
- it ends on a next step, and it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no price on its next step.

FAIL if the For you verdict is anything but "not this one" (including "a fit, with one fix" with the lower-MOQ offer as the fix), or is a paraphrase of a label, or says the quoted 500-unit order fits, if it presents the summary's medians as an offer (for example "the median offer" or "a typical offer of 200 units at USD 4.80", with no named supplier row behind it), or cites an offer whose MOQ and price don't match the same row (for example 50 units at USD 3.90), if the exact USD 600 appears anywhere, if no first-order arithmetic is shown, if the market verdict is changed to fit the profile, if the answer tells the user to drop the idea with no related version that fits, or if it comments on the user's experience or budget as a person.
