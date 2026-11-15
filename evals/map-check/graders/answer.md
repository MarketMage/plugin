---
type: llm
---

The results (Sony WH-1000XM5, UPC 027242923232, MAP USD 329.99): 9 offers confirmed new below MAP in `mapViolations` (Best Buy 228, three Walmart offers 239.95 to 249.99, Lowe's 281.99 whose title bundles JBL T110 earbuds, Dressinn.com 282.99, BuyDig.com 319.99, RELYmedia 319.99, Macy's 324.98), and Amazon's lowest offer at 192.50 in `mapUnconfirmed` (condition not stated). If the Amazon listing's sellers were read (ASIN B0CFSD4TSQ), that 192.50 offer is GlobalTech Imports, new, with Electronic Experts new at 214.00, Second Spin Audio used at 178.00 and Crutchfield at 334.99.

PASS if the reply lists sellers below the 329.99 MAP with their prices, includes Best Buy at 228 (about 102 below MAP), keeps Amazon's 192.50 offer as a break (marked condition not stated, or named as GlobalTech Imports, new, after reading the listing's sellers), and gives a count that fits the results (setting the Lowe's bundle aside and counting one fewer is fine).
FAIL if it lists no violations, drops Amazon's 192.50 offer, calls it confirmed new without having read the listing's sellers, counts the used 178.00 offer as a violation, or invents sellers not in the results.
