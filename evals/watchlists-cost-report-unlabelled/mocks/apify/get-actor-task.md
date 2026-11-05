---
type: agent
---

You are the Apify `get-actor-task` tool. Reply with only the JSON object for the requested task (by id or name):

- `tskACME`: {"taskId": "tskACME", "actorId": "cleanpull/watch-digest", "name": "cw-price-acme-competitors", "input": {"title": "Acme: competitor prices", "monitorName": "acme-competitors", "productUrls": ["https://www.rivalone.com/products/trail-pack-30l", "https://www.rivaltwo.com/products/trail-pack"], "amazonAsins": ["B0ACMERV01"], "amazonMarketplace": "US", "maxRunCostUsd": 0.08}}
- `tskCOMP`: {"taskId": "tskCOMP", "actorId": "cleanpull/watch-digest", "name": "cw-price-competitors", "input": {"title": "Competitor prices", "monitorName": "competitors", "productUrls": ["https://www.glowrest.com/products/heated-eye-mask", "https://www.sleepwell.co/products/eye-mask"], "maxRunCostUsd": 0.04}}
- `tskEYE`: {"taskId": "tskEYE", "actorId": "cleanpull/watch-digest", "name": "cw-rank-eye-mask", "input": {"title": "Eye mask ranks", "monitorName": "eye-mask", "rankKeywords": ["heated eye mask"], "rankAsins": ["B0MYMASK01", "B0RIVAL001", "B0RIVAL002"], "rankMarketplace": "US", "rankSponsored": false, "maxRunCostUsd": 0.05}}
- any other: {"error": "Task not found"}
