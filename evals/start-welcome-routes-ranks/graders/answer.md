---
type: llm
---

Earlier in the chat MarketMage's welcome listed its jobs and asked "What brings you here?". The user answered that they already sell on Amazon and want to track their rankings. They gave no ASIN, listing link or keywords yet.

PASS if all of these hold:
- the reply takes up rank tracking for their own Amazon listing: it asks for what that needs, in plain words, such as the product's ASIN or listing link and the search keywords they want to rank for (the marketplace, or once versus ongoing, may be asked too, in the same message);
- it does not steer them into finding something to sell: no question about a niche or what they'd like to sell, no product ideas, no "guided session";
- it runs nothing yet (nothing can run without the ASIN and keywords) and states no run price (a short plain note that it will say the cost before anything over a few cents is fine);
- it is short, friendly and plain, with no backend words (actor, dataset, call-actor, task input names).

FAIL if it asks what they'd like to sell or which niche, starts an ideas search, presents research, or ignores the rankings request.
