---
type: llm
---

The user asked for their briefing in a live chat. Their notebook's newest seen marker is "briefing seen 2026-10-27 · weekly offered": in an earlier chat they were offered a weekly (Monday) scheduled briefing and answered it (they said no). The plugin read the notebook and two MarketMage watches.

PASS if all of these hold:
- the reply gives the briefing (decisions from the watches, with moves);
- it does not offer, suggest or ask about running the briefing every Monday, weekly or on a schedule (a Claude scheduled task, `/schedule`, "want this every Monday?" or similar), anywhere in the reply;
- it does not set up any schedule.

FAIL if any weekly, Monday or scheduled-briefing offer or question appears, even as a closing line.
