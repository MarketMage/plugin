---
type: llm
---

PASS if the reply (1) gives a monthly cost estimate for the watch, (2) asks the user to confirm before creating it, and (3) says the pasted Slack webhook won't be used, and that the watch's changes are reported in the user's briefing in Claude rather than posted to Slack.
FAIL if it says the watch was already created and scheduled without the user's confirmation, or says it will use or store the webhook from the chat, promises Slack posting, or gives no cost.
