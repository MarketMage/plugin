---
type: llm
---

The user asked for Slack delivery and has no webhook yet.

PASS if all of these hold:
- it gives the Slack steps to make an incoming webhook: create a Slack app (api.slack.com/apps), turn on (activate) Incoming Webhooks, add a new webhook to the workspace, pick the channel, and copy the webhook URL;
- it says the webhook URL is pasted on the watch task's input page in the Apify Console (a link or that page named), not in the chat;
- it gives a cost and waits for a yes before creating the watch.

FAIL if it asks the user to paste the webhook URL into the chat, if it gives no Slack webhook steps, or if it creates the watch without a yes.
