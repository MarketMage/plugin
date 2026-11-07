---
type: llm
---

The data (Amazon pet-supplies Best Sellers, TikTok "cat toy", Trends over 12 months): cat window perch (new to the chart, 182 reviews, 3,800 TikTok units, +62%) and the interactive rolling ball (420 reviews, 5,200 units, +38%) and the automatic laser toy (390 reviews, 6,400 units; rising search "automatic cat laser toy" +180%) look favoured; the handheld laser pointer (22,300 reviews, 60 TikTok units, interest −28%) is against; tunnels, catnip toys and scratchers are mixed. Non-cat rows (dog toys, litter, treats, a dog grooming glove) are not cat toys.

PASS if all of these hold:
- a table of ideas with for/against counts, ordered so the ideas the data favours come first;
- the handheld laser pointer is reported as not favoured, with a number, briefly (a short "what to avoid and why", not a lecture);
- it builds on the user's laser-pointer hunch with the related version the data supports (an automatic or motion-activated laser toy, with a number such as 6,400 TikTok units or the +180% rising search), or credits the hunch only as far as the data backs it;
- non-cat rows are left out of the cat-toy ideas;
- it ends on a next step naming two ideas for `validate`, with no Apify cost;
- it uses no hype words ("hot", "winning", "goldmine", "definitely") and no doom words ("unfortunately", "saturated to death", "be careful");
- it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step.

FAIL if the laser pointer is recommended as a top idea against the data, if the against ideas dominate the answer, if dog or litter products are presented as cat-toy ideas, or if there is no next step, or it closes on a "This run cost…" (or "This research cost…") line, or puts an Apify cost on its next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
