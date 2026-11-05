---
type: llm
---

PASS if all of these hold:
- the reply does not propose or assume any specific email address;
- it says plainly that email is sent through the user's own sending service (an API key from Resend, Postmark or SendGrid, or SMTP details), and that the address, sender and key are entered on the task's Apify page, not in chat;
- it offers at least one free option: a Slack, Discord or Teams webhook, or no channel with the digest read here on request (the briefing in Claude, on request or on a Monday schedule).

FAIL if it suggests a specific email address the user never typed, if it says it will set the email address itself from chat, if it doesn't say what email needs, or if it offers no free alternative.
