---
type: llm
---

The user asked for a daily price watch, said yes to anything under USD 2 a month, and named no delivery channel. The reply may confirm the created watch or show the plan; either is fine.

PASS if all of these hold:
- the reply says where the results go as the briefing in Claude (asking Claude what changed, a briefing on request, or a weekly/Monday scheduled briefing), or that the digests stay in their Apify account and Claude reads them;
- it does not ask the user to choose or set up Slack, Discord, Teams, a webhook or email, does not offer or list those channels, and gives no Apify Console input-page link for adding a channel;
- it gives the watch's cost (per run or a month).

FAIL if it asks how the user wants to be notified, offers a menu of Slack, Discord, Teams, webhook or email, or gives steps or a link for adding one. Offering a channel ("if you'd rather get Slack or email, say so") also fails: by default no channel is offered.
