---
description: 'Fix round for PR #29 (adversarial review 2026-11-03, items 2, 7 and 8). A live briefing without a notebook. A MAP watch created yesterday (3 Nov) on a Monday-only schedule has never fired: its `lastRunAt` is empty and `nextRunAt` is 9 Nov, and it has no run (MAP watches skip the baseline run). It is "first run due 9 Nov", never "didn''t run on 2 Nov as scheduled". A reviews task whose schedule the user deleted is "not scheduled". The daily launch watch ran on time.'
max_turns: 25
allowed_tools: [Read, Skill]
runs: 1
tags: [companion, adv-2026-11-03]
---

What's new with my MarketMage watches?
