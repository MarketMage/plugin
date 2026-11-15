---
description: "0.4.13 (owner's rules of 11 Nov 2026): a dropshipper asks what a heated eye mask really costs delivered to US buyers. The AliExpress read is AliExpress Scraper with product pages (`includeDetails: true`), top 3, ship to US. Mocked rows: USD 8.49 with USD 2.19 shipping on its page (landed USD 10.68); USD 6.20 with no shipping charge on its page (`shippingCost` 0, `freeShipping` true) and a one-time new-shopper deal of USD 1.09; USD 7.35 whose page could not be read (`detailsRead: false`, shipping not read). The answer gives the landed cost as price + shipping where the page charged it, says shipping is still to add where it didn't (never \"free shipping\"), calls the unit price what a repeat buyer pays, and mentions the USD 1.09 only as a one-time first-order deal."
max_turns: 25
allowed_tools: [Read, Skill]
runs: 2
tags: [aliexpress, dropship, landed-cost]
---

I'm dropshipping heated eye masks to customers in the US. What would one actually cost me per order from AliExpress, delivered to my customer? Go ahead and check.
