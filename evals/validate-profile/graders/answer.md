---
type: llm
focus: last_message
---

The market data favours this idea (Strong, the Go outcome, for the market: demand +95.6% over 5 years, a top-10 sales floor of about 14,000 units a month, median 310 reviews, top-3 share 0.22, 4 ads in 48). The user is a first-time dropshipper with under USD 1k selling through their own store with TikTok and Facebook ads, so the cold-traffic dropship lens applies. Through it: TikTok felt want is strong (the top 5 sold 1,200 to 3,400 units each); the high Amazon sales floor is search-led demand, a caution for cold traffic; Amazon itself sells none of the top 10; the leaders' quality gap favours. AliExpress sells single units: the USB rechargeable mask at USD 8.49 with USD 2.19 shipping to the US (`landedPrice` USD 10.68), the cordless steam mask at USD 6.20 with `shippingCost` 0 (shipping not established: plus shipping still to add, never free; its USD 1.09 is a one-time new-shopper deal, never the cost) and a graphene mask at USD 7.35 whose page wasn't read (`detailsRead: false`: shipping not read). The rechargeable kind leads the page, so its USD 10.68 delivered is the matching cost; the cheaper USD 6.20 one may be a steam version; using the matching version's price (and saying the cheaper one is a different version) is the plugin's rule (running-results.md, "A cheaper sibling version is not a match") and is correct. The leaders ship at about 0.62 lb. Several titles say "rechargeable"/"cordless" (a lithium battery) and "for dry eyes" (a health claim): no named ad platform prohibits these, so they are risk notes, not a policy fail.

PASS if all of these hold:
- the answer leads with a "For you" verdict, then gives "For the market" as Strong (or Go) with its counts;
- the "For you" verdict is NOT "not this one" because of the battery or a health claim; the battery (lithium) and/or health-claim wording appears as a neutral risk note (what the risk is, e.g. carrier shipping limits or stricter ad review), not as a failed gate or a reason to avoid;
- the "For you" reasoning ties the lens to facts: Amazon search demand (the 14,000-unit floor) named as a caution for cold traffic (it reads neutral in the count and is never against on its own, since TikTok felt want favours), and TikTok units as felt want;
- the AliExpress price is given with its shipping (landed where the page charged it, else shipping still to add), never "free shipping", and no shipping or freight figure is invented; if the verdict is a fit with one fix, the fix is named;
- a fit check with numbers is present (the MOQ-1 offer or first order against the under-USD-1k band, and an ad-cost assumption stated as an assumption, ideally as a range such as USD 8 to 12 per sale);
- the profile is repeated as bands (under USD 1k, dropship, first time, side income), not the exact USD 400;
- it makes no comment on the profile itself (no "great that…", no "don't worry", no praise of the person or their situation); credit for the user's own pick that the data backs ("What you got right: your USD 29.99 sits in the middle of what shoppers pay") is the plugin's rule (judgement.md, rule 5) and is fine;
- the facts table is labelled for any seller / the market (the short default's "What the data shows" heading counts), separate from the For you block, and the profile does not change any number in it;
- it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step.

FAIL if "For you" is "not this one" because of the lithium battery or the health-claim wording, if the market verdict changes because of the profile, if there is no "For you" verdict, if a landed cost or shipping figure is invented, if the exact USD 400 is repeated, if it flatters the user, or if it closes on a "This run cost…" (or "This research cost…") line, or puts an Apify cost on its next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
