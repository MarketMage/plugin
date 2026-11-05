---
type: llm
---

The data: the Meta read (US, active ads running 35+ days, one row per advertiser) found 7 proven advertisers: GlowRest (glowrest.com, 212 days), Lunara Official (lunarasleep.com, 140), EyeCalm (eyecalm.co, 96), SpaNest (spanest.shop, 61), Heat Relief Deals (landing on amazon.com, 58), RestWell Home (restwellhome.com, 44), Dreamy Dozer (dreamydozer.com, 39). The store sizes (Shopify summary only): GlowRest 61 products, Lunara 14, EyeCalm 6, SpaNest 220, Dreamy Dozer 11; restwellhome.com is not a Shopify store.

PASS if all of these hold:
- it states the cost of the search steps before or as they run (about USD 0.07 for the Meta read and about USD 0.003 a store for the sizes, or a total near USD 0.11 at most; figures from USD 0.06 to 0.09 for the Meta read and up to about USD 0.13 in total are fine) and stays within the user's 15 cents;
- the amazon.com landing page (Heat Relief Deals) is set aside as a marketplace, not sized as a store;
- it names Lunara (14 products, 140 days), EyeCalm (6, 96 days) and Dreamy Dozer (11, 39 days) as the proven small advertisers (ads 35+ days, about 20 products or fewer), with the thresholds stated, and does not count GlowRest (61) or SpaNest (220) as small;
- it says restwellhome.com isn't Shopify, so its size wasn't read;
- it offers to read 1 to 3 of those stores and the angle their ads use, with a cost per store, and does not read them in this turn;
- it says the libraries show advertisers, not their spend (or otherwise does not invent spend or sales), and ends on one costed next move.

FAIL if it counts a store over about 25 products as small, sizes amazon.com as a store, reads the stores' catalogues in full, invents spend or sales figures, or gives no cost.
