# The notebook: memory across chats, opt-in

The plugin remembers nothing between chats on its own. With the user's yes, it keeps a **notebook** in their own Apify account, written and read only by `cleanpull/marketmage-notebook`: their seller profile as bands, the ideas checked with their verdicts and key numbers, the related versions tried, their decisions and the watches linked to an idea. It lives in a key-value store named `marketmage-notebook` in their account (one record per entry, one for the profile); they can open, download or delete it in the Apify Console (Storage → Key-value stores) at any time.

## Ask once

Ask at most once per conversation, in one line, at the first natural moment: after the first verdict (before the Next step line), or straight away when the user asks Claude to remember something ("remember my budget", "save this idea"). For MarketMage, the notebook is its way to remember: offer it. Claude's own memory, if the user has it, is fine too: don't steer them away from it, and never present what it holds as the notebook's record. The line always says where it lives, what it costs and that they can view or delete it. Never ask if they already said yes or no in this chat, or if a notebook was read in this chat.

> Want me to keep a notebook of the ideas we check, their verdicts and your profile (as bands only)? It lives in your own Apify account, each save costs a fraction of a cent, and you can view or delete it any time.

When a paid run also needs a yes, ask both in the same message: one yes can cover both, and the user can say yes to one only. If they say no, don't ask again; when they wanted a profile remembered, give them the `Profile:` line to keep instead (`judgement.md`, "The seller profile and lenses").

## When to read

The plugin can't tell whether a user kept a notebook in an earlier chat without reading it, and a run in an account that never opted in can leave an empty `marketmage-notebook` store there that the user never asked for. So **read only on a cue from the user**, never by default at the start of a chat:

1. **They said yes in this chat:** read once straight away, to bring back anything saved in an earlier chat (on an account without a notebook, the read finds nothing and costs only the run start). A read never starts a notebook: the first write does (below).
2. **They point to it or to past work:** "my notebook", "use my profile", "last time", "back again", "where were we", "the ideas I checked", "what did I decide about the steel version", a greeting with them included. "My notebook" and "use my profile" name it: read. Past-work words (real-user test round 3: "good morning! back again, where were we with the sleep mask thing?" got a permission ask with a cost line, then "I don't carry anything over from earlier chats"): make the store list at once ("Is it on?" below), and when a store named `marketmage-notebook` is in it, read the notebook straight away, with no ask and no cost line (it is theirs; a read is a fraction of a cent), then pick up where they left off. Only when the list shows no such store, say in one line that you don't carry anything over from earlier chats and ask where they'd got to; a notebook they then say they keep is read, as "my notebook" is. Never "you have no notebook".
3. **The conversation holds the line `MarketMage notebook: on`** (in their message or a Claude project's instructions). Give them this line after they opt in, to paste in a new chat or a project's instructions so later chats read it from the start.

Read once per conversation (again only when they ask to see it). A read that returns entries or a profile means they opted in earlier: write as below without asking again: a profile they state in this chat that differs from the saved one, and each verdict, also one delivered when they say "continue" or "finish it" (`notebook-use.md`, "A profile said in this chat that differs from the saved one").

## How to call it

`call-actor` with `actor: "cleanpull/marketmage-notebook"`, `waitSecs: 45`, `callOptions.maxTotalChargeUsd: 0.01`, then read the one result row with `get-dataset-items`. Each call is one operation, one at a time: wait for each to finish before the next. No yes is needed per call once the user has opted in (a read is about USD 0.0002, plus USD 0.01 per 1,000 entries read beyond the first 20; a write about USD 0.0003), and no cost line.

**Saying so: one line, never a section.** Put it just before the closing lines, not at the top and never under a heading: "Noted in your notebook: your profile as bands ($1k–5k · FBA · first time) and this idea." The first time in a chat, the same line may add the Console link and the `MarketMage notebook: on` line for later chats; nothing more.

- **Read:** `{"operation": "read"}` (newest first, compact, up to 50 entries); add `"search": "<word>"` (at most 80 characters) for one idea and its linked entries, `"kinds": ["decision"]`, `"since": "YYYY-MM-DD"`, `"limit"` (1 to 500), or `"detail": "full"` with a high `limit` when they want an export. The row holds `profile`, `entries`, `counts` and `store.consoleUrl`. What the notebook holds is a record of past checks, not today's market: quote its numbers with their date, and offer a fresh check when they matter.
- **A profile from the notebook** is used like one given in the chat: repeat it once as bands ("Judging for: $1k–5k · own stock · first time · US") and don't ask the profile question. If its newest entry is 30 days old or more, re-check it once in this chat, in one line ("Still around $1k–5k and dropshipping?"; `judgement.md`, "The profile"), and save a change with `upsertProfile`.
- **Welcome back:** when the first read of a chat returns entries, open with them before anything new, in one or two lines: their stage (below) with the idea it belongs to, its verdict, date and any decision, and that stage's next step ("Welcome back. You're at launching for heated eye masks (Strong for the market, 12 Oct): want me to read the launch watch?"). In the selling stage, lead with their own listings' watches (below). A stop rule whose check date has come (today or past) goes first (`launch-plan`, "The stop rule"); one whose date is still ahead, or that has no date yet (`check after start+N days`), isn't raised. With watches in the notebook, the `briefing` skill turns this into the full briefing.
- **Starting it:** the **first write after the user's yes in this chat** carries `"startNotebook": true` at the top level of the input (next to `operation`, never inside `entry` or `profile`), so it starts the notebook if there is none. Later writes leave it out. Never send it without a yes in this chat: a write without it on an account with no notebook saves nothing and says so ("There is no notebook in this Apify account…"). If that happens (the notebook was deleted, or never started), tell the user nothing was saved and ask whether to start a new one; don't retry on your own.
- **A read may name `skipped` records** that couldn't be read: say how many were left out, and serve the rest.
- **Refusals** come back as `ok: false` with the reason in `error` (for example a field that looks like an email or a personal amount). Fix the call (drop or reword that field) and never repeat the refused value back to the user.

## What to write, and when

**The input shapes, exactly.** The input is strict: a key outside these is refused, and so is an entry field on the wrong kind. Entry fields always go **inside an `entry` object**, the profile inside a `profile` object; only `operation`, `startNotebook`, `entryId`, `deleteLinked`, `confirmDeleteAll` and the read options sit at the top level.

```json
{"operation": "upsertProfile", "startNotebook": true, "profile": {"budgetBand": "1k-5k", "fulfilment": "fba", "experience": "none"}}
{"operation": "addEntry", "startNotebook": true, "entry": {"kind": "idea", "idea": "Silicone garlic press", "marketplace": "amazon.com", "verdict": "maybe", "confidence": "high", "signals": {"favours": 3, "against": 2, "neutral": 1, "unknown": 0}, "keyNumbers": {"priceMedian": 14.99, "medianReviews": 1850}, "note": "Paid pressure is the main risk."}}
{"operation": "addEntry", "entry": {"kind": "variation", "parentId": "i-3k9x2a", "change": "Steel, not silicone", "verdict": "go", "confidence": "medium"}}
{"operation": "addEntry", "entry": {"kind": "decision", "parentId": "i-3k9x2a", "decision": "test"}}
{"operation": "addEntry", "entry": {"kind": "watch", "parentId": "i-3k9x2a", "watch": {"actor": "cleanpull/watch-digest", "taskId": "<17-character task id>", "scheduleId": "<17-character schedule id>", "label": "cw-launch-garlic-press"}}}
{"operation": "updateEntry", "entryId": "i-3k9x2a", "entry": {"verdict": "go", "note": null}}
{"operation": "deleteEntry", "entryId": "i-3k9x2a"}
{"operation": "deleteAll", "confirmDeleteAll": true}
```

(`startNotebook` only on the first write after a yes, as above.) `upsertProfile` merges: send only the fields that changed; `null` clears one. `updateEntry` takes the `entryId` and, in `entry`, only the fields to change (`null` clears one), never `kind` or `date`. `deleteEntry` also deletes the entry's linked entries (`deleteLinked` is `true` by default). Entry ids look like `i-3k9x2a` (`i` idea, `v` variation, `d` decision, `w` watch) and come back in each write's `entry.id` and in reads.

| When | Operation | What goes in `entry` (or `profile`) |
| --- | --- | --- |
| They give or change their profile | `upsertProfile` | `profile` as bands only: `budgetBand` (`under-1k`, `1k-5k`, `5k-25k`, `25k-plus`), `fulfilment` (`dropship`, `own-stock`, `fba`, `print-on-demand`), `experience` (`none`, `some`, `brand`), `channels` (`none`, `store`, `amazon`, `tiktok`, `etsy`, `ebay`, `email-list`, `social`), `goal` (`side-income`, `brand`), `marketCountry` (two letters, `US`), and `skills` (`ads`, `content`, `sourcing`, `design`), `timePerWeek` (`under-5h`, `5-15h`, `15-30h`, `30h-plus`) if they volunteered them |
| After each verdict (`validate`) | `addEntry`, `kind: "idea"` | `idea` (a short label, at most 80 characters), `marketplace` (for example `amazon.com`), `verdict` (`go` for Strong, `maybe` for Promising, `no` for Not this version), `confidence` (`high`, `medium`, `low`), `signals` (`favours`, `against`, `neutral`, `unknown`, whole numbers), up to 10 `keyNumbers` (below), and a `note` (at most 300 characters, starting `stage: validating · `, then the For you label and the one fix, or the early sign); no `parentId` |
| A related version checked | `addEntry`, `kind: "variation"` | `parentId` (the idea's id), `change` (what differs, at most 120 characters), and the same verdict fields; no `idea` (it takes its parent's) |
| They state a decision | `addEntry`, `kind: "decision"` | `parentId`, `decision` (`pursue`, `test`, `park` or `drop`): only what they said ("I'll test the XL version" is `test`), never a decision inferred for them; no `idea`. A `test` only when the idea has no `test` entry yet (an agreed stop rule is one): never a second |
| A watch is created for an idea | `addEntry`, `kind: "watch"` | `parentId`, `watch` (`actor`, `taskId`, `scheduleId`, `label`); no `idea` |
| They agree a stop rule before launch (`launch-plan`) | `addEntry`, `kind: "decision"`, once per idea | `parentId`, `decision: "test"`, and a `note` in the fixed form `stop rule · check YYYY-MM-DD (start + N days) · test spend band <band> · <the rule's percentages>`, or `stop rule · check after start+N days · …` while the start date isn't known (at most 300 characters; no `stage:` prefix: agreeing a rule moves no stage) |
| They give the start date later ("I started ads on the 3rd") | `updateEntry` on the stop rule's `entryId` | `note`: the same note with `check after start+N days` replaced by `check YYYY-MM-DD (start + N days)` |
| Their stage moves (below) | `updateEntry` on the **idea** entry's `entryId`, never a new decision entry | `note`: `stage: <stage> · <what they did, a few words, no first person: "ads started 2026-11-01">`, then the old note's text after its prefix, cut to 300 characters |

**`keyNumbers`: numbers only, names from the actor's fixed list.** Any other name, or a text value ("12 of 48", "+38%"), is refused. The names: `priceMedian`, `priceP25`, `priceP75`, `priceMin`, `priceMax`, `medianReviews`, `under100Reviews`, `top3SellerShare`, `sellerCount`, `listingCount`, `sponsored`, `boughtPastMonth`, `unitsPerMonthMin`, `unitsPerMonthMax`, `revenuePerMonthMin`, `revenuePerMonthMax`, `bestSellersRank`, `unitPrice`, `landedCost`, `moq`, `marginPercent`, `feePercent`, `trendChangePercent`, `trendIndex`, `rating`, `oneStarShare`, `tiktokSalesPerDay`, `adCount`. For a verdict, typically `priceMedian`, `medianReviews`, `under100Reviews` (a count: 14, not "14 of 48"), `top3SellerShare` (0.22), `unitsPerMonthMin` (the sales floor), `unitPrice`, `marginPercent` (after fees, 54), `trendChangePercent` (95.6) and `adCount`.

**Only the user's own profile.** The notebook's profile is the person you're talking to. When they describe someone else (a relative, a client, a friend), judge for that person in the chat, but never offer to save their profile or ideas to this notebook.

**Only market figures read from data.** `keyNumbers` hold what a run read: marketplace prices, reviews, shares, units, and suppliers' public list prices. `unitPrice`, `landedCost` and `moq` are the supplier listings' figures (`unitPriceMedian`, `landedUnitCostMedian`, `moqMedian` from the supplier run), **never the user's own**: no unit price or landed cost from a quote their supplier gave them, no planned order quantity, no budget. Leave a number out rather than store one of theirs.

**Entries are fixed to their date.** `updateEntry` can change an entry's other fields, never its date or kind: to move one, delete it and add it again.

**Never in the notebook:** amounts of the user's own money (budgets, savings, quotes, revenue, ad spend; the profile takes the band), supplier names, account details, names of people, or anything the user didn't share for this. Market figures (prices, medians, review counts) are fine. There are no exceptions: an agreed stop rule keeps its test spend as a **band word**, `test spend band under-100`, `100-250`, `250-500` or `500-plus` (USD, the band the plan's figure falls in: USD 150 is `100-250`), never the amount, plus its days and percentages ("stop rule · check 2026-11-08 (start + 7 days) · test spend band 100-250 · add-to-cart under 2% → stop"). No first-person or budget words in it.

**One stop rule per idea, never overwritten.** The actor treats an `addEntry` with the same kind, idea, date and parent (and the same `decision`) as the same entry and overwrites it, so a second `decision: "test"` for the idea on the same day would replace the stop rule. The stop rule is the only `decision: "test"` entry for its idea: what the user later says about the launch ("I've started ads", "ordered stock", "it's live") is an `updateEntry` on the idea entry's note (the stage, below), never a new decision entry. A changed rule (their new numbers) is an `updateEntry` on the stop rule's own note.

## Journey stages

Where the user is, from what they did and said, never guessed ahead of it. Six stages, in order:

| Stage | Set when | Next step to offer (no price: its estimate comes at the yes) |
| --- | --- | --- |
| `exploring` | nothing saved yet, or only ideas from a search | `find-products` in their niche |
| `validating` | an idea was checked (every idea entry from `validate` starts its note with `stage: validating`) | the one fix or the best related version (`validate`) |
| `sourcing` | they said they'll go ahead (a `pursue` decision), or the launch plan's supplier step ran | the launch plan's supplier questions and a sample; the launch plan if not run yet |
| `launching` | they said they ordered stock or started ads (agreeing a stop rule alone isn't launching) | the stop rule's check once its date has come, and the launch-week watch (created with its own yes) |
| `selling` | they said it's live and selling ("my listing is up", "first sales") | their own listings' watches first (below); a listing audit of their page |
| `expanding` | while selling, they check or ask for a next product | `gaps` against their rivals, or `find-products` next to what sells |

- **Where it's kept:** in the `note` of an entry, which starts with the fixed prefix `stage: <stage>` (lower case, one of the six names), followed by ` · ` and the rest of the note: `stage: sourcing · suppliers asked for a sample`. The notebook has no stage field, so the prefix is the record; never another spelling.
- **Writing it:** on the idea entry's own note: the idea's `addEntry` after `validate` starts it at `validating`; every later move is an `updateEntry` on that idea entry, its `note` rewritten as `stage: <new stage> · <what they said>`, keeping the old note's text after its prefix (cut to 300 characters). A decision they state ("I'll go ahead", "park it") is still its own `decision` entry, without a stage prefix, and the stage moves on the idea entry in the same turn. A stop rule moves no stage. A stage moves only on something they did or said in a chat, and only forward, except when they say they've stopped (`park` or `drop`: the idea leaves the stages).
- **Reading it:** each idea's stage is the furthest stage named by the prefix on any of its entries (the idea's own note, and, in notebooks written before this rule, its linked entries), so a re-check never moves it back; the user's stage is the furthest among their ideas that aren't parked or dropped (an idea whose newest decision is `park` or `drop`); `exploring` when none has one. Name it once, in plain words ("You're at sourcing for heated eye masks").
- **Selling mode:** in the `selling` and `expanding` stages, welcome-back and the briefing lead with the watches on their own listings: a `cw-rank-` task's `rankAsins`, a `cw-listing-` task's pages, a `cw-gaps-` task's `yourStore`, a launch watch with their own ASIN added, or any watch whose title says it's theirs. When it isn't clear which watch is theirs, ask once which one. Then their rivals and the market.

## Viewing and deleting

- **Show it:** read it and give a short table of ideas (date, label, verdict, the decision if any), and `store.consoleUrl` for the full record.
- **Delete one idea:** `deleteEntry` with its `entryId` (its variations, decisions and watch links go with it) after they confirm which. Deleting a watch link doesn't stop the watch: that is the `watchlists` skill.
- **Delete everything:** `deleteAll` with `confirmDeleteAll: true`, only after they confirm in words ("delete my whole notebook"). It removes the store; nothing is kept.

If a call fails with "Actor not found", the notebook isn't published yet: say it's coming soon, and give the `Profile:` line to keep in the meantime.
