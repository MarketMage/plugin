---
type: llm
---

The user asks their margin on Amazon at USD 34.99 for a bamboo bath caddy with a USD 4.20 factory quote. Amazon's fees depend on the item's size tier and weight, which MarketMage reads from the Amazon leaders (their `fees`).

PASS if all of these hold:
- it either works the margin from Amazon fees read by MarketMage in this chat (the leaders' referral and FBA fees, with their size tier or weight from that read) or offers that read as the next step with its cost estimate and a question to go ahead;
- it does not present an FBA fee worked from an assumed size or weight (such as "if it's 75 cm and 5 lb, it's oversize, so about USD 18") or from fee tables found on the web as the answer;
- a rough before-fees figure, if given, is labelled as before Amazon's fees (for example 34.99 − 4.20).

FAIL if it gives an FBA fee or a margin after fees from an assumed size or a web search, or says it can't read Amazon's fees.

What MarketMage's Amazon read returns for this product, if the reply made it: the top 10 bamboo bath trays on Amazon US, priced USD 16.99 to 34.99 (median 22.49), each with Amazon's own fees: a 15% referral fee (Sports and Outdoors), an FBA fee of USD 4.48, size tier Large standard, 0.62 lb. Fees, size and weight quoted from that read are read, not assumed.

A reply that gives no margin yet and offers the read (with its cost and a question to go ahead) passes the first point; it needs no rough figure.
