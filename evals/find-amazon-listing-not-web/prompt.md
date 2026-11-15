---
description: "Real-user test round 3 (R3-5/R3-7 extended; a live agency journey): \"find their best selling one yourself\" was answered by web-searching the brands' Amazon listings. When MarketMage needs a brand's or a product's Amazon listings, it uses its own Amazon search read (amazon-product-scraper searches, or the market scan), keeping the brand's rows: real ASINs, ranks and bought badges. Here the user wants TruSkin's best-selling vitamin C serum watched on Amazon US: an Apify read finds it (TruSkin Vitamin C Serum for Face, B0TRUSK000, 40K+ bought last month); no web search, no web fetch."
max_turns: 25
allowed_tools: [Read, Skill, WebSearch, WebFetch]
runs: 1
tags: [real-user-round3, routing]
---

I run an agency. One client is TruSkin. Find their best-selling vitamin C serum on Amazon US yourself and set up a price watch on it for me.
