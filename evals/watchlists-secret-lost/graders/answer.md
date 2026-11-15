---
type: llm
---

PASS if the reply says the product was added but a saved setting on the watchlist (the Slack webhook field) is no longer there, and gives a link to the task's input page in the Apify Console (console.apify.com/actors/tasks/...) where the user can add it back if they want.
FAIL if it reports success without mentioning the lost Slack webhook, or asks the user to paste the webhook into the chat.
