---
type: agent
---

You are the Apify `get-actor-task` tool. Reply with only the JSON object for the requested task:

- `tskREV001`: {"taskId": "tskREV001", "actorId": "cleanpull/watch-digest", "name": "cw-reviews-competitors", "input": {"title": "Competitor reviews", "monitorName": "competitors", "reviewProductUrls": ["https://www.tentree.com/products/kessler-sweater-warm-oak-heather-fade", "https://mvmt.com/products/odyssey-ii-ceramic-fusion-grey-40mm-28000461", "https://www.beardbrand.com/products/beard-oil-variety-pack", "https://ugmonk.com/products/15-minute-hourglass-amber", "https://store.arduino.cc/products/ventuno-q", "https://www.thesill.com/products/crocodile-fern", "https://www.puravidabracelets.com/products/pura-vida-ornaments", "https://www.colourpop.com/products/magical-skies-shadow-palette-and-brush-set", "https://www.allbirds.com/products/mens-tree-runners", "https://www.brooklinen.com/products/classic-core-sheet-set"], "reviewAsins": ["B07C1YFV6D", "B0DTK7VDTH"], "reviewTrustpilotDomains": ["allbirds.com", "tentree.com"], "reviewMarketplace": "US", "maxRunCostUsd": 0.09}}
- `tskMKT001`: {"taskId": "tskMKT001", "actorId": "cleanpull/watch-digest", "name": "cw-market-bottles", "input": {"title": "Bottle searches", "monitorName": "bottles", "marketKeywords": ["insulated water bottle", "kids water bottle"], "marketSources": ["amazon", "walmart"], "marketAmazonMarketplaces": ["US"], "maxRunCostUsd": 0.09}}
- any other: {"error": "Task not found"}
