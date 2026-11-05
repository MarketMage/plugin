---
type: llm
---

The user asked for their briefing in a live chat; the plugin read their notebook and two MarketMage watches and turned them into decisions.

PASS if all of these hold:
- the reply gives the briefing (decisions from the watches, with moves);
- near the end, it offers once to run this briefing every Monday morning (or weekly) on its own, as a Claude scheduled task (or "scheduled task" / "/schedule"), as a question the user can say yes to;
- the offer appears once only, not repeated in several places;
- it does not claim to have already set up the schedule, and does not propose an Apify schedule, a new watch or Slack/email delivery for the briefing.

FAIL if there is no weekly or Monday offer, if it is made more than once, if it says the weekly briefing is already scheduled, or if it sets it up as an Apify schedule or task.
