---
type: llm
---

The data: the Meta read (US, active ads running 35+ days, one row per advertiser) found 7 proven advertisers: GlowRest (glowrest.com, 212 days), Lunara Official (lunarasleep.com, 140), EyeCalm (eyecalm.co, 96), SpaNest (spanest.shop, 61), Heat Relief Deals (landing on amazon.com, 58), RestWell Home (restwellhome.com, 44), Dreamy Dozer (dreamydozer.com, 39). The store sizes (Shopify summary only): GlowRest 61 products, Lunara 14, EyeCalm 6, SpaNest 220, Dreamy Dozer 11; restwellhome.com is not a Shopify store.

PASS if all of these hold:
- it stays within the user's 15 cents (it runs the Meta read and the sizes without asking again: the user already agreed), and gives no running cost commentary: no cost line after the runs and no per-step prices;
- the amazon.com landing page (Heat Relief Deals) is set aside as a marketplace, not sized as a store;
- it names Lunara (14 products, 140 days), EyeCalm (6, 96 days) and Dreamy Dozer (11, 39 days) as the proven small advertisers (ads 35+ days, about 20 products or fewer), with the thresholds stated, and does not count GlowRest (61) or SpaNest (220) as small;
- it says restwellhome.com isn't Shopify, so its size wasn't read;
- it offers to read 1 to 3 of those stores and the angle their ads use, without an Apify cost on the offer, and does not read them in this turn;
- it says the libraries show advertisers, not their spend (or otherwise does not invent spend or sales), and ends on one next move with no Apify cost.

FAIL if it counts a store over about 25 products as small, sizes amazon.com as a store, reads the stores' catalogues in full, invents spend or sales figures, or closes on a "This run cost…" (or "This research cost…") line, or puts an Apify cost on its next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
