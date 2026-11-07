---
name: notebook
description: The user's MarketMage notebook, kept opt-in in their own Apify account - the product ideas they checked with their verdicts and key numbers, the versions they tried, their decisions, the watches linked to an idea, and their seller profile as bands - to start one, show it, find an idea in it, or delete an entry or all of it. Use when someone asks MarketMage to remember them or an idea across chats, asks what they checked or decided before, says "my notebook", or wants their saved data shown or deleted. Not for running a new check (use validate or find-products).
---

# Notebook

Memory across chats, only with the user's yes. Read `references/notebook.md` and `references/notebook-use.md` first and **follow them exactly**: when to ask, when to read, what to write, and what never goes in. Also `references/running.md` (tools, caps) and `references/notebook-use.md`, "What to write" (the profile bands).

`references/running.md` is the core; its parts are read only at their step (its first lines say when): `references/running-results.md` once results are in, before using them; `references/running-runs.md` before a data-provider read, when a run doesn't succeed, or when this chat already holds a run; `references/running-abroad.md` outside the US; `references/running-asks.md` when the user asks who runs this, offers an allowance, pastes a secret or asks for something MarketMage won't do.
- `references/known-limits.md`: routes established not to work, each with what to use instead: read in the same batch as `references/running.md`, before choosing any source (a store, a marketplace, a country, a keyword); never try a route it lists.

Every call is `cleanpull/marketmage-notebook` through `call-actor`, one operation at a time, with `callOptions.maxTotalChargeUsd: 0.01`. Use the input shapes in `references/notebook-use.md` exactly: entry fields go inside an `entry` object (`{"operation": "addEntry", "entry": {"kind": "idea", "idea": "…", "verdict": "maybe", …}}`), profile fields inside a `profile` object, and `startNotebook`, `entryId` and `confirmDeleteAll` at the top level.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## Start one

If they haven't said yes in this chat, ask once in the one line from `references/notebook.md`. After the yes: `{"operation": "read"}` (it brings back anything saved before; on a new account it finds nothing), then the first write with `"startNotebook": true` at the top level: `{"operation": "upsertProfile", "startNotebook": true, "profile": {"budgetBand": "1k-5k", …}}` with any profile they gave, as bands, or `{"operation": "addEntry", "startNotebook": true, "entry": {"kind": "idea", …}}` for the first idea. Later writes leave `startNotebook` out. Give them the line `MarketMage notebook: on` to paste into a new chat or a Claude project's instructions, so later chats read it from the start, and `store.consoleUrl` to see it in Apify.

## Show it, or find something

`{"operation": "read"}`, or add `"search": "<word>"` for one idea (its variations, decisions and watches come with it), or `"kinds": ["decision"]`, `"since": "<YYYY-MM-DD>"`. Answer with a short table: date, idea, verdict, confidence, the decision if any, a watch if linked. If the row names `skipped` records, say how many couldn't be read. The numbers are as they were on that date: offer a fresh check (`validate`, cheaper when it reuses this chat's rows) when the user wants to act on one.

## Change or delete

- **A decision or a correction:** `{"operation": "addEntry", "entry": {"kind": "decision", "parentId": "i-3k9x2a", "decision": "test"}}` (no idea text), or `{"operation": "updateEntry", "entryId": "i-3k9x2a", "entry": {<only the fields to change; null clears one>}}`. An entry's date can't change: delete it and add it again.
- **One idea:** confirm which, then `{"operation": "deleteEntry", "entryId": "<its id>"}` (its linked entries go with it). A watch keeps running until it's paused (`watchlists`).
- **Everything:** only after they confirm in words, `{"operation": "deleteAll", "confirmDeleteAll": true}`. It deletes the store; nothing is kept.

End with the next move in one line: the idea worth a fresh look, or "Ask me to check a new idea any time".
