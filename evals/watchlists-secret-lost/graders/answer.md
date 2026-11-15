---
type: llm
---

PASS if the reply says the product was added but the Slack setting (webhook) is no longer saved on the watchlist, and gives a link to the task's input page in the Apify Console (console.apify.com/actors/tasks/...) to paste it again.
FAIL if it reports success without mentioning the lost Slack webhook, or asks the user to paste the webhook into the chat.
