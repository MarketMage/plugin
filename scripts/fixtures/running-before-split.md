# Running CleanPull actors through the Apify connector

These rules apply to every MarketMage skill.

## Tools

The plugin's Apify connector exposes these tools:
- `call-actor`, the one tool that starts a run: it takes any CleanPull actor by its full name (`cleanpull/<name>`), checks the input against that actor's own input schema (and returns the schema when the input is missing or wrong), and carries the spending cap (`callOptions.maxTotalChargeUsd`). The connector has no tool per actor, on purpose: those tools take no cap;
- the run and storage readers (`get-actor-run`, `get-actor-run-list`, `get-dataset-items`, `get-key-value-store-record`, `abort-actor-run`);
- the task tools (`create-actor-task`, `get-actor-task`, `update-actor-task`);
- the schedule tools (`create-schedule`, `get-schedule`, `update-schedule`); no delete tool for tasks or schedules (`watchlists.md`, "Stop" and "Deleting");
- `apify-api-read` (read-only GET requests), **only** for these paths: `/v2/actor-tasks`, `/v2/actor-tasks/<id>` and `/v2/actor-tasks/<id>/runs…` for tasks whose name starts with `cw-`, `/v2/schedules` and `/v2/schedules/<id>`, and the two store paths below. Never read any other path (account, billing, other storages, other actors' runs).

Use only these tools, and only with `cleanpull/...` actors. **Create, change or pause only tasks and schedules whose names start with `cw-`.** Never touch any other task, schedule or run in the account: those belong to the user's other work.

**Not connected yet.** Before anything else, check that these tools exist: they may be listed by name only (deferred, loaded with ToolSearch), with names that contain `apify` and `call-actor`. Seeing the names is enough: never call a tool just to test the connection, and never read `/v2/users/me`, the user's tasks, schedules or notebook to check the setup. If they are missing, or a call answers with a sign-in or authorization error (401, "Unauthorized", "authentication required"), the Apify connector isn't connected: say so kindly in one line ("One quick setup step first: MarketMage needs its Apify connection, about 2 minutes."), give the steps, then stop (don't run anything another way, and don't answer a research question from memory):

- **claude.ai, the desktop app or Cowork:**
  1. **Customize → Plugins → MarketMage → Connectors → Connect.**
  2. An **"Add custom connector"** notice opens with the details already filled in. That's expected: it is Apify's official server, set up with the tools MarketMage uses. Signing in gives the connector access to your Apify account; MarketMage's skills only run CleanPull's actors and only create, change or pause their own `cw-` watches (that's how the skills are written, not a technical lock). Check the connector address starts with `https://mcp.apify.com/`, keep the details as they are and click **Add**. If it shows any other address, don't add it, and tell me what it says.
  3. Sign in to Apify, or **create a free Apify account** (it includes USD 5 of credit every month).
  4. Approve the access, come back to this chat and say "done".
- **Claude Code:** run `/mcp`, choose the Apify server and sign in (or create a free account) there.
- Screenshots of each step: https://marketmage.io/start/

Give only the steps for the surface you can tell you're on; if you can't tell, give both. Keep what the user asked: once they say it's connected, carry on with it.

**Actors not public yet.** A table in `costs.md` that starts with **Pending** is for an actor CleanPull hasn't published yet. If its run fails because the actor isn't found, say plainly that this part of the job is coming soon, give what the other steps found, and don't retry.

## Before any run

1. **Collect only what the job needs:** URLs, ASINs, barcodes, keywords, store domains, brand names, a marketplace. Never ask for anything else, and never look in memory or earlier chats for it. (The one optional extra is the seller profile in `judgement-profile.md`, for the judgement skills only: bands, sent to Apify only through the user's opt-in notebook, `notebook.md`. **Quick reads, the one exception to `judgement-profile.md`'s "Asking for the profile":** when the user asks for one read under about USD 0.10 (a TikTok list, a trends check, a price), the five profile questions don't come before it, not even in its estimate. Run it (or, when the request comes to more than USD 0.05, give its estimate and wait for the yes alone), and offer the profile in one line after the answer, if it hasn't been offered in this chat; that line is the conversation's one offer. The notebook itself is read only on a cue from the user: `notebook.md`, "When to read".)
2. **Check this conversation first** ("Runs in this conversation" below): if an earlier run already holds the data and is fresh enough, reuse it instead of paying again.
3. **Once or ongoing?** Before a first read that could be a watch's baseline, find out ("Once or ongoing" below).
4. **Cost is said once, at the approval, and only there.** Apify usage is the one cost MarketMage talks about, and only where it needs the user's yes (item 5): a request whose runs together come to more than USD 0.05 (all the runs started for one request, counted together: one estimate for all of them), and anything recurring. **Below that, just run it:** no estimate before, no cost during, no cost line after. Managing the user's Claude usage is not MarketMage's job: never comment on it.
   - **The approval line: one estimate with a soft note.** From `costs.md`, each event at its published per-result price (the **Bronze** price, the paid-plan price; Silver and Gold pay less), plus the start event ($0.00005 per GB of the run's memory: the `apify-actor-start` row; $0.0002 for a 4 GB actor). The **estimate** is the counted worst case of what is planned: each event × the count the input can return, no padding. Say it once, in one line, as one figure with the soft note, and the question: "This reads 48 listings and 10 product pages on Amazon US. This costs about USD 0.12, occasionally a little more if I need to dig deeper to answer you. Go ahead?" Several runs for one request get one estimate for all of them, never a figure per run. No range, no upper bound, no spending-limit figure: that limit (item 6) is internal.
   - **The free-plan price only when it differs.** Where the run's events cost more in the **Free** column (provider records and searches, ad library requests), add the free-plan figure in the same line: "This costs about USD 0.09 (about USD 0.17 on Apify's free plan), occasionally a little more if I need to dig deeper to answer you", with the spending limit from the higher figure. A price `costs.md` lists "from <date>" counts only from that date. Where the columns agree, give one figure. Every figure the skills quote is a paid-plan figure: check `costs.md` for the free-plan one.
   - **Change events on repeat reads.** Actors that remember what they read before, under a tracking name (`monitorName`, or `watchlistName` for the marketplace scan; "default" when the input doesn't set one), bill change events on any later run of the same thing on this account, on a one-off read too. Count them in the estimate whenever this account may have read the same thing before (assume it may, unless this is the account's first MarketMage run): **Amazon Best Sellers** (`cleanpull/amazon-bestsellers-tracker`) bills each product that has dropped out of the ranks read since the last read of that chart as `item-change` (USD 0.002 each), up to the ranks read (`maxItemsPerChart`): up to USD 0.10 a chart at 50; **the marketplace scan** (`cleanpull/marketplace-search-scanner`) bills up to 4 `market-change` rows a search (USD 0.004). The estimate counts them ("This costs about USD 0.18, counting products that left the chart since this account last read it, occasionally a little more if I need to dig deeper to answer you"), and the spending limit is set from that estimate. Other change events in `costs.md` (`product-change`, `item-change` on watches) are counted the same way when the read repeats one this account made.
   - **The notebook** (`notebook.md`) runs with no yes and no cost mention once the user has opted in (its reads and writes are a fraction of a cent each).
5. **Wait for the user's go-ahead** when the request's runs together come to more than $0.05, or before anything recurring, with the one estimate above. **A go-ahead already in their message** ("go ahead and check", "run it") is that yes for a one-off read (never a watch) over USD 0.05 whose **estimate** (the free-plan figure when higher) is up to USD 0.25; the bound compares the estimate, never the spending limit: start at once, with the estimate and its soft note in a "Reading … now" line before the first `call-actor` ("Reading TikTok Shop now: about USD 0.14, occasionally a little more if I need to dig deeper to answer you."). **An answer that changes the plan:** `running-asks.md`, "A changed plan", first.

## Remembering between chats

If the user asks Claude to remember anything for next time (their profile, an idea, a decision), or mentions a notebook or earlier work, follow this file: the opt-in notebook is MarketMage's way to remember. Offer it in its one line (where it lives, what it costs, that they can view or delete it): it is an opt-in to ongoing writes, so its cost is said there, at the approval. Claude's own memory, if the user has it on, is fine too: never steer them away from it. Keep the two apart in answers: a question about earlier MarketMage work ("what did I check last month?") is answered from the notebook when they keep one, and an answer that comes from Claude's own memory or this chat says so, so it is never taken for the notebook's record.

## Country

Take the marketplace from the user's first message: a `.co.uk`, `.de` or `.co.jp` domain, "for the UK", "in Germany", a price in GBP or EUR, without asking again. Outside the US (TikTok Shop skipped, Amazon's marketplace, Trends `geo`, the `local-market` event, own currencies): `running-abroad.md`, "Country, outside the US".
- Amazon actors get that `marketplace` (or `amazonMarketplace`, `amazonMarketplaces`, `rankMarketplace`);
- Google Trends gets the same country as `geo`;
- TikTok Shop is skipped (it covers the US shop): say so once;
- every Amazon product read outside the US adds the `local-market` event (USD 0.003 a product, also on watch checks): put it in the estimate and in `maxRunCostUsd`;
- prices are compared in their own currencies, never converted.

US when nothing says otherwise. Say which marketplace you used: in the estimate line when a yes is needed, otherwise in the answer.

## First use

**When it applies:** this conversation has no earlier MarketMage run (no CleanPull tool result above) and no mention of an existing `cw-` watch, and the user is new or asks broadly ("what can this do?", "I'm new to this", "help me find something to sell", "I want to start selling", `/marketmage:start`). Every skill reads this file before its first run, so this check fires whichever skill the user's first message reached; a broad first message that names no product or niche goes to the `start` skill, which runs this section. Skip all of it when the user goes straight to a specific job (a price check, a named idea to validate): do that job, and keep the first-session offer for the end, in one line.

**The opening, in this order** (real-user test, 7 Nov 2026: warmth first, no billing paragraph, at most two questions, no notebook talk to someone new):

1. **The connection.** If the Apify tools are missing, give the setup steps ("Not connected yet" above) and stop there; the rest follows once they're connected.
2. **A returning user** (the conversation holds `MarketMage notebook: on`, or they say they've used MarketMage before, "I'm back", "last time"): read the notebook (`notebook.md`, "When to read": past-work words, "back again" or "where were we" included, get the store list at once, and a notebook found there is read with no ask and no cost line), then welcome them back instead of starting over, naming their stage and offering its next step (`notebook-use.md`, "Journey stages"): "Welcome back. You're at sourcing for heated eye masks (Strong for the market; for you, a fit, with one fix; 12 Oct): next is sending the three supplier questions." When the notebook holds watch entries, or the chat opens with a greeting or "what's new", the `briefing` skill gives this welcome as the top of its briefing (their watches' latest digests are free to read). Offer to pick up there, or start something new. Use the saved profile (re-check it if stale: `judgement-profile.md`, "The profile"). Skip steps 3 to 5.
3. **No billing paragraph: the welcome's one cost line instead.** How billing works is not explained in the opening (it adds worry before anything costs money); the welcome's cost line (item 3 of "The welcome") is said once, after the guided session sentence. A new user's first approval in this chat, whichever skill asks it, carries its one estimate with the soft note, and adds the billing clause only when that cost line wasn't said in this chat: "The three steps cost about USD 0.55, occasionally a little more if I need to dig deeper to answer you, billed to your own Apify account (its free plan includes USD 5 a month). Go ahead?" Asked how it's paid, or who runs it, answer in full (`running-asks.md`, "Who runs this").
4. **At most two questions, the most decisive first,** in one message: what they'd like to sell or are into (the niche: nothing can run without it), then, only when they haven't said, how they'd sell it, as one question (`judgement-answer.md`, "Asking for the profile"). The budget band, when they haven't given one, waits for the estimate message, as its one skippable line. When the welcome's profile line was said in this chat, ask the niche alone: no how-they-sell question and no budget line; never a third question here, and never two questions folded into one bullet. Everything else they've already said (a budget, "never sold", "Shopify probably", "side income") is used, repeated back once as bands, never asked again. For someone new, the second question is asked in plain words with no trade terms to define: "Would you rather keep stock and post orders yourself, have a supplier ship each order for you, or something else (Amazon's warehouses, made to order, or you make it)?" (the names dropship, own stock and FBA come later, each explained the first time it appears, or when they ask); never a glossary of options. Their budget is repeated only as its band, never the figure they gave. Nothing waits on the answers: skipped, the profile is never asked again in this chat, and the market verdict leads every answer.
5. **The guided first session,** aimed at a "found something" moment and said as their goal, not the tool's process, in one or two sentences ("we'll look at what's selling in something you like, check the two best for you, try one better version of the stronger one, and you can keep a watch on it"), with no costs on it (the one estimate comes when they pick a niche and it is about to run, below). Its steps, for Claude:
   1. **Ideas in their interest,** searched through their lens: `find-products` on the niche they name.
   2. **The 2 best, checked:** `validate` on the two ideas the counts favour (for them, with a profile), reusing the TikTok and Trends rows already read (the AliExpress single-unit check is added for a dropship lens, and the cold-traffic lens also reads where they'd compete on Meta ads).
   3. **One related version:** the best rung of the ladder (`judgement.md`, "Related versions") for the stronger of the two, checked with a market scan summary or `validate`.
   4. **One watch on the chosen niche:** the watch that catches its early sign (`judgement.md`, "Watches"), for example TikTok sales per day or new entrants on page 1 (offered at the end, with its own yes and its monthly estimate).

   - **without dropship, off Amazon** (no profile, own stock off Amazon, print on demand off the marketplaces, General): 0.15 + 2 × 0.08 + 0.14 ≈ **USD 0.45**, **USD 0.55** with up to USD 0.10 of chart changes (the default: `running.md`, "Change events on repeat reads", unless this is the account's first MarketMage run): "about USD 0.55" (spending limit USD 0.83; the account's first run: "about USD 0.45", limit USD 0.68);
   - **dropship through ads** (cold-traffic lens: the Where you'd compete read in each check; AliExpress already read in step 1): 0.20 + 2 × 0.12 + 0.19 ≈ **USD 0.64** (**USD 0.72 on Apify's free plan**): "about USD 0.64 (about USD 0.72 on Apify's free plan)" (limit USD 1.08, shared by the runs in proportion to their high ends; the AliExpress read has no floor). find-products' own offer of the Where you'd compete read is skipped here: the checks read it. The wave read (whether the advertisers' stores added it in the last 30 days) isn't offered in the guided session; it can follow after it.

   Say it once, when they've picked a niche and the first step is about to run, as the approval for steps 1 to 3: "The three steps cost about USD 0.55, occasionally a little more if I need to dig deeper to answer you. Go ahead?" (with "billed to your own Apify account (its free plan includes USD 5 a month)" only when the welcome's cost line wasn't said in this chat), the figures for their lens; when the profile isn't known yet, the higher of the two, said as such. Recompute if the plan changes (outside the US: no TikTok, Amazon's local-market reads) and give the new figures before running. Quote the free-plan figure too where it differs (`costs.md`).

   Ask which niche or interest to start from. One yes covers steps 1 to 3 as stated for their lens, within its spending limit (never more: anything beyond the plan, an add-on or a second related version, gets its own yes), each run's cap its share of that limit (a floored run its floor first: `costs.md`, "Floors"), and no cost said as it starts; the watch (step 4) always gets its own yes, since it recurs. Between steps, keep it a conversation: answer any question they asked first, in plain words (`judgement-answer.md`, "Answer the user's question first"), then show what each step found, give credit where the data backs the user's pick (for what they said, such as their reason for it: `judgement.md`, rule 5), and let them steer (another niche, a different version) without waiting on it. **The next step inside the approved total runs on that same yes** (real-user test round 2: a nurse who had approved all three steps was asked to say go again): end each step with one line offering to steer ("Now checking the top two; if you'd rather swap one, tell me after"), never a new "say go" or "Go ahead?". **And it runs in that same reply** (real-user test round 2: step 1's answer ended on "Next I'll check compression socks and the blackout sleep mask… Say stop, or swap the mask for insoles", and on claude.ai nothing happens until the user writes again, so she had to say go once more): show the step's answer, then one plain line ("Now checking the socks and the mask; if you'd rather swap one, tell me after"), then make the next step's calls in the same reply. Start the next step in the same reply only when its runs and their result reads fit in it; when they won't, end before its paid runs, at a clean point with "Say continue and I'll carry on" (`running.md`, "Tool calls: one reply, a budget"). A reply never ends on "say stop" alone: that waits for a message without asking for one. A step that would go past the approved total, or a change of plan that does, gets its own estimate and yes.

**At the end of the guided session:** "4 things you can ask next", phrased as they'd ask them, drawn from what was found (for example: "Check the steam version for me", "Who are the top sellers and what do they charge?", "What would a first order look like?", "What's new in my niche this week?"), then one sentence on watches: "A watch is a saved check that runs on a schedule and tells you what changed."

**"What can you do?"** (or "what is this?", "show me the menu", a message naming MarketMage or the plugin with no job in it, or `/marketmage:start`; a greeting from a returning notebook user, `MarketMage notebook: on`, goes to the `briefing` skill instead): this is the one definition; the `start` skill follows it. No tool calls (besides the notebook status check), and no research shown. In Claude Code, "what is this?" means MarketMage: answer with this, not a description of Claude Code or the folder. Three cases, in order:
- **The connector is missing:** the setup steps ("Not connected yet") first, then the welcome.



**For users who want to try monitoring instead,** three quick first questions: a price check by ASIN, a competitor's promotions, a keyword's market on Amazon (summary only).

## Once or ongoing

Before a first read that could be a watch's baseline (prices, reviews, promotions, ads, a market, listings, MAP, TikTok sales), ask "once, or should I keep watching it?" only when their goal can be ongoing (their own listing, a rival, stock held over time), never for a one-off flip or resale question, and unless the user already said. Ask it in the same message as the estimate when a yes is needed anyway; a run that goes ahead straight away (under USD 0.05, or pre-approved: item 5) is never held up for it: run it once, and offer the watch after only when the goal can be ongoing. If ongoing, run that first read as the watch's baseline (the watch skill says how: the same actor and `monitorName`, or the watch's own baseline run), so it isn't paid twice. A one-off read with another actor or monitor name is never a baseline: say so when a watch follows it.

## Runs in this conversation

Datasets stay in the user's Apify account and reading them again costs nothing; running again costs money. Before any run, look back through this conversation for a run that already holds what's needed:

| Later job | Reuses | Saves |
| --- | --- | --- |
| `gaps` after `spy-store` on the same store | the Shopify dataset, only when its summary says `catalogueComplete: true` (spy-store reads 100 products; gaps needs the whole catalogue, so a partial read is read again at gaps' size) | about USD 0.08 a store |
| `validate` after `find-products` | TikTok rows and the Trends record for the same keyword | USD 0.06 to 0.09 |
| `validate` after `market-scan` | the keyword summary | USD 0.017 |
| `reviews-watch` after `spy-store` | the best sellers' URLs | a question |
| `listing-audit` after `rank-watch` | `outrankedBy` URLs as `competitorUrls` | a question |
| `price-watch` after `price-check` | the same URLs and ASINs as items (not a baseline: a different actor and monitor); Walmart, Target, Best Buy, eBay and Etsy pages read the same day skip the baseline run, and the first scheduled run records them (`price-watch`, "Same-day marketplace pages") | a second confirm; about USD 0.0045 a page and USD 0.015 a marketplace |
| `launch-plan` after `validate` | the Amazon leaders (ASINs, fees, ratings), the keyword summary, the supplier summary, and the leaders' complaints if read | about USD 0.08 |
| `export` after anything | the dataset ID | a question |

**Fresh enough:** prices, stock, Buy Box, ranks and promotions the same day; catalogues, review summaries and ads 7 days; Trends, supplier prices, listing audits and tech stacks 30 days. Say "from your check at 09:12 today" when you reuse one, and offer a fresh read if the user wants it.

## Running

- **Start the run:** use `call-actor` with `actor: "cleanpull/<name>"` (always the full name with the `cleanpull/` prefix, for example `cleanpull/barcode-price-checker`; a bare name looks for an actor in the user's own account and fails), the input, `waitSecs: 45`, and the cap in `callOptions.maxTotalChargeUsd`.
- **If it isn't finished,** call `get-actor-run` every 30 to 45 seconds until its status is SUCCEEDED, FAILED, ABORTED or TIMED-OUT (the AliExpress single-unit check is followed as "Timing" says, "The single-unit check, in that pattern"). Tell the user it's still running, and roughly how long it may take.
- **Never call `call-actor` again for the same job** after a timeout, a dropped connection or a tool error: the first run may well be running and charging. First look for it with `get-actor-run-list` (`{"limit": 10, "desc": true}`): a run of the same actor started in the last few minutes is yours; follow it with `get-actor-run`. Only when there is none, and the user agrees, start again.
- **Read the results** with `get-dataset-items` on the run's `defaultDatasetId`, asking only for the fields you need (`fields`) and a sensible `limit`.
  - A run's own summary is in its key-value store under `RUN_SUMMARY` (`get-key-value-store-record`).
  - Watch Digest's report is under `DIGEST.md`.
- **Always start `cleanpull/google-trends-scraper` with `callOptions.memory: 512`:** it needs no more, and it leaves room under the account's memory limit.

## When a run goes wrong

| What happened | What to do |
| --- | --- |
| **ABORTED with results** (usually the cap) | Show what was read and what it cost. Work out from `RUN_SUMMARY` which items weren't read, estimate a rerun of **only those** (pass just those items, or `maxItems` for the rest), and get a new yes. |
| **FAILED, "Actor not found"** | The actor isn't public yet (see "Actors not public yet"): say this part is coming soon, give the other steps' results, don't retry. |
| **Memory limit** (Apify refuses the start for the account's memory) | Nothing ran or was charged. Apify limits the total memory of the actors running in an account at once (8 GB on the free plan at the time of writing; the user's plan may differ). Start the runs one after another instead of together, or wait a few minutes for the running ones (often a scheduled digest), and say so. |
| **A data provider was unavailable** (`RUN_SUMMARY` names the items not read, uncharged) | Say which items. For a watch, they are read on the next run; for a one-off, offer a rerun of only those items later. |
| **A site couldn't be read** (a page with no product data, a store that didn't answer, a site the actor doesn't cover) | Name it and the reason from `RUN_SUMMARY`, uncharged. Suggest another way in: the barcode instead of the page, the product's page on another store, or the brand's own site. |
| **A slow provider search** | Poll every 30 to 45 seconds and say how many minutes it has run. After 13 minutes, offer to stop it with `abort-actor-run`: what was read so far stays, and only that is charged. **Except the AliExpress read:** followed as "Timing" says; the stop is offered only after 15 minutes. |
| **FAILED or TIMED-OUT, other reasons** | Read `RUN_SUMMARY` or the status message; say plainly what went wrong and what would fix it (a wrong URL, a marketplace not supported). Rerun only with a yes. |
| **A tool error or dropped connection** | Never start the same job again straight away: find the run first (see "Running"). |

## Secrets: never in chat

- **The plugin needs no keys from the user** beyond their Apify sign-in: every marketplace, supplier, review and ad source is read by the actors themselves. Never ask for a marketplace, supplier or ad platform key, token or account.
- **Never ask for, accept or pass** an API key, access token, SMTP password, or Slack, Discord, Teams or webhook URL in chat. Webhook URLs are secrets: anyone who has one can post to the channel.
- **If the user pastes one anyway,** don't use it, and don't repeat it back. Say why, point them to the Console link below, and suggest they rotate it (create a new key or webhook and delete the pasted one), since it is now in the chat history.
- **To add a delivery channel to a saved watchlist:** create or update the task without the secret, then give the user `https://console.apify.com/actors/tasks/<taskId>/input`. They paste the key or webhook into its secret field there and save. Apify stores it encrypted. Give the steps in `watchlists.md`, "Where the user pastes a setting".
- **When you update a task's input,** pass the whole input you read with `get-actor-task`. That includes every `ENCRYPTED_VALUE:` field, unchanged, because the update replaces the stored input and would otherwise drop the user's saved secrets. Then check it:
  1. Before the update, note which fields hold an `ENCRYPTED_VALUE:` value.
  2. After it, read the task again with `get-actor-task`.
  3. If any of those fields is now missing or no longer `ENCRYPTED_VALUE:`, tell the user plainly which channel lost its setting and give them `https://console.apify.com/actors/tasks/<taskId>/input` to paste it again.

## Timing: sources from data providers

Some sources come from licensed third-party data providers that CleanPull holds the accounts for, under the providers' terms; CleanPull's actors don't read those sites themselves:
- **CleanPull's marketplace data service** (Bright Data, a web-data provider) is the source for eBay, Etsy, Walmart, Target, Best Buy, Home Depot and Lowe's searches and product pages, Target and Best Buy records by barcode, Alibaba searches, and Trustpilot reviews;
- **CleanPull's ad library service** (ScrapeCreators, an ad data provider) is the source for the Meta and TikTok ad libraries, and for Google's Ads Transparency Center items on a run where Google's own library returns none.

These reads are slower:
- **marketplace and supplier searches:** usually 1 to 4 minutes a run for Walmart, eBay, Home Depot and Lowe's, and Alibaba (its search pages are read directly: about 35 to 80 seconds a product idea); usually 4–5 minutes, sometimes up to about 9 for Etsy; up to about 12 minutes for Target and Best Buy, and for the others when a page can't be read and the service reads the search the slow way; whatever the number of keywords; with Amazon in the same job, answer with Amazon first while the others run;
- **Target and Best Buy by barcode:** 3 to 5 minutes a run;
- **product pages on those marketplaces:** a few seconds to a few minutes;
- **Trustpilot:** about 2 to 3 minutes for a business; never quote it as under a minute.

Say so before the run ("this takes a few minutes"), even when the user has already said yes, start it with `waitSecs: 45`, and follow it with `get-actor-run` as above. Each such run also has a provider search fee per source (see `costs.md`), so group the user's items into one run rather than several.

**Never hold the whole answer for a slow read.** When a job mixes fast reads (Trends, Amazon, TikTok Shop, the ad libraries, Made-in-China) with a slower provider read (a marketplace or supplier search: an Etsy, Target or Best Buy search, and a Walmart, eBay, Home Depot, Lowe's or Alibaba search, which usually takes 1 to 4 minutes but can fall back to the slow way; and the AliExpress read, whose product pages can take several minutes, so the answer comes first: below), start the slow one **first**, as its own run with `waitSecs: 0`, then the fast ones; answer as soon as the fast ones are in, naming the slow part as still reading ("still reading Walmart (usually 1 to 4 minutes, up to about 12)"; for AliExpress, "AliExpress is slow on this one (its product pages can take a few minutes)") and marking what depends on it as provisional; then follow the slow run with `get-actor-run` every 30 to 45 seconds (the single-unit check less often: below) and, when it lands, complete the answer in a **short follow-up message**: only what changed (the gate it settles, the verdict now final), never the whole answer again.

## Read the data like an analyst

The actors return what a search or a page gave them; a keyword match is not proof that a row is the product. Before using any row (for an answer, a table, a price or a verdict), read it the way a human analyst would:

- **Relevance:** is this really the product or market asked about? Judge by the title, brand, category and description, never by the search term having matched. A "lip gloss" search can return the same brand's deodorant; an "XM5" barcode can find its case.
- **Comparability, before any price comparison.** Two prices are compared only when the offers are the same thing:
  - **condition:** new, renewed or refurbished, used, open box. Read the `condition` field where the actor gives one, and always the title ("Renewed", "Refurbished", "Open Box", "Used", "Pre-owned"). Google Shopping labels a condition only when an item isn't new, so a missing condition means new unless the title says otherwise. Never set an offer aside on price alone: a much cheaper offer with no stated condition is reported as "condition not stated; check before relying on it";
  - **pack size or quantity:** a 2-pack, a lot of 10, a case; compare per unit, or set it aside;
  - **bundle or kit:** with accessories or extras;
  - **variant:** size, colour, capacity, model or generation (an XM4 is not an XM5);
  - **region and currency:** never compare across currencies; a store outside the user's market is flagged;
  - **who sells it:** the brand or a third-party marketplace seller, when that matters (MAP, the Buy Box, authenticity);
  - **outliers:** a price far from the rest (under half the median, or over twice it) is checked for one of the reasons above. Set a row aside only for a real mismatch (product, condition, pack or variant), never for its price alone: an unusually low or high price with no mismatch is reported as it is, with a note.
- **Exclude or flag every mismatch, and say so** (in the short default only when it changed a price or cost shown or left out half or more of a read: `judgement-answer.md`), in one plain line: "3 of 10 results weren't lip gloss and were left out", "the USD 184.99 offer is a renewed unit; the lowest new price is USD 279.99", "one listing is a 2-pack (USD 28.50 a block), counted per block". Recompute any figure the actor summed over all rows (a median, a total, a lowest price) from the rows that remain, and say it was recomputed.
- **Don't over-filter.** Keep borderline rows (a slightly different size, a close variant) and say how they were treated. Remove only what is clearly a different product or a different condition.
- **Coverage.** If too little relevant data is left (under about half the rows, or fewer than 6 comparable rows), lower the confidence (`judgement.md`, "Confidence"), and offer a better read: a refined keyword, more results, or listing rows, run on a yes. Never build a verdict or a "lowest price" on one or two relevant rows.
- **Summaries the actor computed over every result** (a market scan's percentiles, TikTok keyword totals, a barcode's `lowestPrice`) carry the same risk. When the rows behind them were read, check them; when only the summary was read, say it covers every result as the site ranked them.

## Explaining results

Lead with what matters, then the evidence:
- **what changed or what the data says;**
- **why it matters** for a seller (margin, demand, a competitor's move);
- **what to do next.**

Judgement skills follow the answer structure in `judgement.md`. Every answer follows these format rules:
- **Tables:** at most 10 rows (5 where a short answer will do), one idea per row, numbers in the table rather than in the prose.
- **Plain words:** explain a trade term the first time it appears, from `glossary.md`, in a few words ("MOQ, the minimum order").
- **At most two follow-ups, with no prices,** drawn from this data and phrased as the user would ask them, for example: "Who outranks you on 'yoga mat'?" · "Watch these 5 prices daily?". Each gets its estimate only when the user takes it up and it needs a yes (`running.md`, "Before any run"). They come just before the Next step line and don't repeat the next step. The user doesn't need to know skill names.
- **Export:** when a run returned 20 rows or more, offer in one line, in plain words ("Want all 48 in a Google Sheet, or as a spreadsheet file to download?"), to put them in a Google Sheet (`export`, with the dataset ID already known), or to download a CSV from the dataset's page in the Console (`https://console.apify.com/storage/datasets/<datasetId>`, Export).
- **A wait:** whenever the results include a read from a data provider (eBay, Etsy, Walmart, Target, Best Buy, Home Depot, Lowe's, Alibaba, Trustpilot, Meta, TikTok ads) or AliExpress, say, as the read starts or in the full detail, that such reads can take up to about 12 minutes (Target and Best Buy searches, and Walmart, eBay or Alibaba searches when a page can't be read; usually a few minutes for those and for Home Depot and Lowe's; Etsy searches usually 4–5 minutes, sometimes up to about 9; AliExpress product pages several minutes, with the answer first and AliExpress added when it lands), however long this one took, so the user knows what to expect next time. This line goes in the estimate or the "Reading … now" line as the read starts, and in the full detail; a judgement's short default leaves it out (`judgement.md`, "Where these parts sit in the answer").
- **The last line,** always: "Next step: <the one action>." (for a judgement, the check of the best related version, the test that settles it, or the watch: `judgement.md`, rule 6). No closing cost line ("This run cost…") and no Apify cost on the next step or a follow-up, in figures or in words ("a few cents", "it's free"), nor what a part did or didn't charge ("nothing was charged for it"): a paid move gets its one estimate when the user takes it up and it needs a yes (`running.md`, "Before any run"). An answer ends on a move, never on a verdict. When the user asks what a run cost, answer from its charged events, with the dataset link for the full list.
