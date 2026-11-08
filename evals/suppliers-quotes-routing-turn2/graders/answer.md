---
type: llm
---

Earlier in the chat the user said they have three quotes for a bamboo bath caddy (USD 4.20, 7.80 and 11, same specs). Now they ask what it usually goes for on Alibaba and Made-in-China. MarketMage's suppliers skill reads factory listings on both sites directly.

PASS if the reply either gives factory prices from a MarketMage read made in this turn (with their source and a count of offers), or offers that read with its cost estimate and a question to go ahead; and it gives no Alibaba or Made-in-China price spread from a web search or from memory presented as today's prices, and never says it can't get Alibaba prices.

FAIL if it quotes factory prices that no MarketMage read in this turn returned, says Alibaba's prices can't be read, or leaves the question with no read offered.
