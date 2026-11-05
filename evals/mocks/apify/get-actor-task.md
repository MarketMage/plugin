---
type: agent
---

You are the Apify `get-actor-task` tool. Look at the earlier calls in your history: count how many times `get-actor-task` was already answered before this call.

- If this is the first call (none before), reply with exactly this JSON and nothing else:

{"taskId": "tskPRICE1", "actorId": "cleanpull/watch-digest", "name": "cw-price-competitors", "title": "Competitor watch", "description": "MarketMage: competitor prices", "input": {"title": "Competitor watch", "monitorName": "competitors", "productUrls": ["https://www.allbirds.com/products/mens-tree-runners", "https://ruffwear.com/products/climate-changer-coverall"], "amazonAsins": ["B0BZYCJK89"], "minPriceChangePercent": 2, "maxRunCostUsd": 0.05, "slackWebhookUrl": "ENCRYPTED_VALUE:SmnldJ2CObNIR9EX7BnvWxNe"}}

- Otherwise (any later call, after the user's change was saved), reply with exactly this JSON and nothing else:

{"taskId": "tskPRICE1", "actorId": "cleanpull/watch-digest", "name": "cw-price-competitors", "title": "Competitor watch", "description": "MarketMage: competitor prices", "input": {"title": "Competitor watch", "monitorName": "competitors", "productUrls": ["https://www.allbirds.com/products/mens-tree-runners", "https://ruffwear.com/products/climate-changer-coverall", "https://www.allbirds.com/products/womens-tree-runners"], "amazonAsins": ["B0BZYCJK89"], "minPriceChangePercent": 2, "maxRunCostUsd": 0.05, "slackWebhookUrl": "ENCRYPTED_VALUE:SmnldJ2CObNIR9EX7BnvWxNe"}}
