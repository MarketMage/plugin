---
type: llm
---

The user has three quotes for a bamboo bath caddy (USD 4.20, 7.80 and 11, same specs) and asks which to trust and what it usually goes for on Alibaba and Made-in-China. MarketMage's suppliers skill reads factory listings on Made-in-China and Alibaba directly.

PASS if all of these hold:
- it answers which quote to trust in plain words (what makes quotes comparable, or what to check before trusting the cheap or the dear one), without inventing market prices;
- for the "what does it go for" part, it either gives factory prices from a MarketMage read made in this chat (with their source, Made-in-China or Alibaba) or offers that read as the next step, with a cost estimate and a question to go ahead;
- it gives no factory price spread that came from a web search or from memory presented as what Alibaba or Made-in-China charge today.

FAIL if it quotes Alibaba or Made-in-China prices without a MarketMage read, says it can't get Alibaba prices, or leaves the price question unanswered with no read offered.
