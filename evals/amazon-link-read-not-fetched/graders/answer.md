---
type: llm
---

The user pasted their amazon.it listing (ASIN B082N24VWQ). MarketMage's read of it returns: "Lumea Siero Viso Acido Ialuronico Puro 30 ml" (a hyaluronic acid face serum) by Lumea Cosmetici, EUR 24.90, 4.4 stars from 2,310 reviews, in Bellezza (beauty). If a market read was made, amazon.de ("Hyaluron Serum Gesicht") shows a median EUR 14.99 and a 2,900-review median, and amazon.com ("hyaluronic acid serum") a median USD 13.99 and a 6,400-review median.

PASS if all of these hold:
- the reply knows the product is their hyaluronic acid face serum (from the listing read) and does not ask the user what the product is;
- it either compares the competition on amazon.de and amazon.com from a read, or offers that read with its cost, using search terms for the serum (in German for amazon.de);
- it gives no example of an unrelated product (such as a water bottle) as a search term.

FAIL if it asks what the product is or what shoppers would type, uses an unrelated product as an example, or says it couldn't open the listing.
