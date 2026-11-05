---
type: llm
---

PASS if the reply (1) gives a monthly cost estimate for the watch, (2) asks the user to confirm before creating it, and (3) says the Slack webhook will not be taken from the chat and is added in the Apify Console instead (a link or the task's input page).
FAIL if it says the watch was already created and scheduled without the user's confirmation, or says it will use or store the webhook from the chat, or gives no cost.
