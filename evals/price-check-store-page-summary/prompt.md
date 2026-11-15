---
description: "Status summaries (7 Nov 2026). Any Store Product Monitor ends a run with a status message that carries the page's price, compare-at price, discount, stock and variant range, and `call-actor` returns it. For one shop's own product page, the price check answers from that message and makes no `get-dataset-items` call (one tool call fewer on claude.ai's per-reply cap), and quotes only the numbers the message carries."
max_turns: 12
allowed_tools: [Read, Skill]
runs: 1
tags: [status-summary]
---

What's this mug selling for right now, and is it in stock? https://www.examplepottery.com/products/speckled-stoneware-mug
