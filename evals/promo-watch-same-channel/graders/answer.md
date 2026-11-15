---
type: llm
---

The account has one watch, `cw-price-competitors` (a Watch Digest task, daily at 8:00 Lisbon time, watching allbirds.com and ruffwear.com product pages), which already posts to the user's Slack channel. The user asks to watch the same two stores' promotions at the same time and post them to the same channel.

PASS if all of these hold:
- the plan adds the promotions to the existing `cw-price-competitors` task (its input gains the two stores' promotions), so they arrive in the same Slack message and the Slack webhook already saved on that task is reused, with no new webhook to paste;
- it gives a cost and asks for a yes before changing anything;
- it does not ask the user to paste a webhook URL into the chat.

FAIL if the main plan is a new, separate task that needs the Slack webhook pasted again (offering it only as an alternative is fine), if it asks for the webhook in chat, or if it changes anything without a yes.
