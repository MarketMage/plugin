# Watchlists: delivery channels

The part of `watchlists.md` read only once the user names a channel (email, Slack, Discord, Teams or a webhook): step 7's channel steps, and where the user pastes a setting. Everything else about watches is in `watchlists.md`.

## The channel they name

- **Slack, step by step** (when they ask for Slack and have no webhook yet): 1. go to `https://api.slack.com/apps`, select **Create New App** (or "Create an app"), choose **From scratch**, name it (for example "MarketMage digests"), pick the workspace and select **Create App**; 2. in the app's settings, open **Incoming Webhooks** and switch **Activate Incoming Webhooks** on; 3. select **Add New Webhook to Workspace**, pick the channel the digests should go to (for a private channel, they must already be in it) and select **Allow** (or **Authorize**); 4. copy the new URL under **Webhook URLs for Your Workspace** (it starts `https://hooks.slack.com/services/`) and paste it on the task's input page ("Where the user pastes a setting" below), never in chat: anyone with the URL can post to that channel. One webhook posts to one channel. On a Workspace where apps need approval, an admin approves the app first.
- **Never set email fields from chat** (`emailTo`, `emailFrom`, `emailProvider`): Watch Digest refuses a run whose `emailTo` is set without `emailFrom` and the provider's API key (or the SMTP host, user and password), so a task saved with only an address fails on every scheduled run. The user adds the address, the sender and the key together on the task's input page (`https://console.apify.com/actors/tasks/<taskId>/input`, "Where to send it (optional)"), then saves.
- **The email address comes only from the user.** Never take one from account details, the client's or system context, memory, git settings, the notebook or anything else they didn't type, and never suggest one ("Should it go to …?"). Ask which address they'll use only to fill in the steps; they enter it themselves on that page.
- **When they ask for email, say plainly what it needs, before the plan:** the watch sends email through the user's own sending service: an API key from Resend, Postmark or SendGrid, or SMTP details from an email account (the key or password goes on the task's Apify page, never in chat). Many sellers have none of these, so **offer the free options first**, in one line each:
  - **Slack, Discord or Teams:** a webhook from a channel they already use, free to create, pasted on the task's page the same way;
  - **no channel at all:** the digests stay in their Apify account, and they ask here ("what changed in my price watch?") to read the latest one, free.
Then set up the one they pick; email only when they already have one of those services or want to set one up, and then only through that page: the address, the sender and the key together.

## Where the user pastes a setting

Give these steps with the link, exactly:
1. Open `https://console.apify.com/actors/tasks/<taskId>/input`. It opens the task's **Input** tab.
2. Expand the section that holds the field, if it's collapsed:

   | Task for | Setting | Section | Field |
   | --- | --- | --- | --- |
   | `cleanpull/watch-digest` | Email API key, SMTP password, Slack, Discord, Teams or other webhook | **Where to send it (optional)** | Email API key, SMTP password, Slack webhook… |
   | `cleanpull/watch-digest` | Email (all together) | **Where to send it (optional)** | Email to (their address), Email from (a sender their service allows), Email provider, and that provider's API key (or SMTP host, user and password) |
3. Paste the key or webhook address into its field; for email, fill every email field in that row before saving (a saved address without the sender and key makes every scheduled run fail).
4. Select **Save**.

The run options on that page show **Maximum cost per run: Unlimited**. That's Apify's platform setting, and it's expected: the task's own limit is the **Max cost per run (USD)** field in the input (`maxRunCostUsd`). Tell the user not to worry about it.
