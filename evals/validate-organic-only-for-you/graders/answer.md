---
type: llm
---

The market data favours heated eye masks on every row but Launch ads: demand +95.6% over 5 years, a top-10 sales floor of about 14,000 units a month, median 310 reviews with 14 of 48 under 100, top-3 share 0.22, 4 ads in 48, USD 29.99 inside the band. At USD 29.99 a sale pays out USD 20.87 after Amazon's fees; minus the USD 4.80 factory median and freight of 15 to 30% of it (an assumption) it leaves about USD 14.63 to 15.35 before ads, about 49% (Margin favours). The Launch ads row uses the standard launch range for everyone (USD 8 to 12 a sale, an assumption): the healthy ad cost is about USD 7 and the break-even about USD 14.63, so it is neutral and caps the market verdict at Promising, with one fix (the ad cost), verdict confidence medium. The user said they won't pay for traffic (their own newsletter), so for them the Launch ads row isn't counted; the first order at the medians is 200 x USD 4.80 = USD 960.

PASS if all of these hold:
- "For you" comes first and is **a strong fit** (or "a fit, with one fix" only if its fix is something other than ad cost, such as the first product's stock or the newsletter's reach), and it says, in a few words, that ads aren't part of their plan (for example "no launch ads, as you said") with their margin before ads (about USD 14 to 15, or about 49%);
- "For the market" is **Promising, with one fix** (or Maybe), its fix the ad cost per sale, with its counts; the market table and verdict still show the launch ad range (USD 8 to 12 a sale) or the break-even ad cost, the same as for any seller;
- the user's newsletter or "no ads" is never used to change the market verdict or remove the Launch ads row from the market's counts;
- the exact budget is never repeated (bands such as "$1k-5k" are fine);
- it ends on one Next step line, at most two "After that" items in it, and no Apify cost.

FAIL if the market verdict is Strong (the facts layer changed for this user) or Not this version; if For you is "not this one" or "a long shot"; if For you's fix or caveat is the ad cost although the user said they won't run ads; or if there is no For you verdict.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
