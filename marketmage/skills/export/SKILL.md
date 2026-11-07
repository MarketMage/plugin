---
name: export
description: Send the results of a MarketMage run or watchlist (prices, products, ranks, digests from this plugin) to a Google Sheet - append, replace, or keep a sheet in sync by a key such as SKU or URL. Use when someone asks to put those results in a spreadsheet, export them to Google Sheets, or keep a sheet updated from one of their CleanPull watchlists. Not for other spreadsheets or data.
---

# Export to Google Sheets

Write a dataset into a Google Sheet with `cleanpull/google-sheets-sync`. Read `references/running.md` first (costs, caps, tools, secrets). Prices are in `references/costs.md`.

`references/running.md` is the core; its parts are read only at their step (its first lines say when): `references/running-results.md` once results are in, before using them; `references/running-runs.md` before a data-provider read, when a run doesn't succeed, or when this chat already holds a run; `references/running-abroad.md` outside the US; `references/running-asks.md` when the user asks who runs this, offers an allowance, pastes a secret or asks for something MarketMage won't do.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. Ask only for

- **What to export:** a run from this chat (you know its `defaultDatasetId`), a watchlist task (its `taskId`, which writes the last successful run), or a dataset ID.
- **The spreadsheet URL** and, optionally, a tab name. Use `{date}` in it for one tab per day.
- **How:**

  | Mode | What it does |
  | --- | --- |
  | `append` (default) | adds rows |
  | `replace` | clears the tab, then writes |
  | `upsert` | updates rows by a key and adds new ones |
  | `sync` | `upsert` plus removing rows no longer present |

  For `upsert` and `sync`, ask which field identifies a row (`keyFields`: `url`, `asin`, `barcode`, `sku`).
  `replace` clears the tab and `sync` deletes rows that are no longer in the data: before either, say so plainly and get a yes.

## 2. Access

- The user shares the sheet with `cleanpull-sheets-1@cleanpull-sheets.iam.gserviceaccount.com` as **Editor**, with "Notify people" unticked. Say this before the run, with whose account it is and what it does, in these words or close to them: "Share the sheet with CleanPull's Google service account, cleanpull-sheets-1@cleanpull-sheets.iam.gserviceaccount.com, as Editor (untick Notify people). That lets CleanPull's Sheets Sync actor edit this one sheet. The first export adds a small hidden tab, `_cleanpull`, holding only your Apify user ID, so no other Apify account can write to it. The share stays until you remove it (Share → that address → Remove access): remove it when you're done, unless the sheet is kept in sync. To share nothing with CleanPull, your own Google credentials can go in the actor's secret fields in the Apify Console instead."
- The address isn't a secret, and nothing else is needed.
- **Which Apify account the sheet is linked to:** the one connected to Claude here, the account whose runs these are (its username shows in the Apify Console under **Settings**). When the user mentions a team or a colleague, add one line: a colleague signed in to Claude with a **different** Apify account can read the sheet but can't write to it (the export says "linked to another Apify account"). So either the team exports from one shared Apify account, or each person exports to a spreadsheet of their own (a new file, not a new tab: the link covers the whole spreadsheet). Deleting the hidden `_cleanpull` tab moves the link to whoever exports next, and then the first account is refused: say so before anyone does it.
- If they'd rather use their own Google credentials (a service account key, or an OAuth client and refresh token), those are secret fields. Point them to the actor's Console input instead of asking in chat.

## 3. Run

- **Run** `cleanpull/google-sheets-sync` with:
  - `spreadsheet`, `tab` and `mode`;
  - `keyFields` when needed;
  - one of `datasetId`, `runId` or `taskId`;
  - `columns`, to pick and order the columns that matter (the default writes every field).
  - Flattened nested fields like `price.amount` become their own columns.
- **A choice of fields:** offer it in one line, before the run (with the estimate, when it needs a yes): a readable set for the data's kind, or every field. When the user already said to go ahead, don't stop to ask: write every field, as they asked, and offer the readable set for the next export in the answer. The readable sets:

  | Data | Readable columns |
  | --- | --- |
  | Watch Digest changes | `at`, `source`, `what`, `changeType`, `title`, `from`, `to`, `detail`, `url` |
  | Prices and products | `title`, `price`, `currency`, `availability` or `inStock`, `url` |
  | Anything else | the 5 to 8 fields a reader needs, named as in the dataset |

  A sheet a person reads (a colleague, a client) suits the readable set; a sheet that feeds another tool (Looker Studio, a script) usually wants every field. A history sheet (appended changes, kept for charts) keeps at least `from` and `to`, the numbers a price or BSR line is drawn from (`watchlists`, "A history chart"). Use the field names the dataset really has (read one item first when unsure).
- **Cost:** USD 0.0001 per row written, so 500 rows ≈ **USD 0.05**. Up to USD 0.05, just run it, with no cost said; above it, give the one estimate (`references/running.md`, "Before any run") and get a yes first. Pass a cap as usual.
- **If nothing was written,** the run still ends SUCCEEDED and the target's row says why (`error`, `errorKind`), uncharged:

  | What the row says | Why | What to tell the user |
  | --- | --- | --- |
  | No access to the spreadsheet (403) | the sheet isn't shared with the address above, or not as Editor | share it as Editor, then run again |
  | No access, and the user says the Share dialog refused the address or warned it is outside the organisation | their Google Workspace blocks sharing with outside accounts | ask the Workspace admin to allow that address, or use their own Google credentials (above) |
  | Linked to another Apify account | the hidden `_cleanpull` tab holds a different Apify user ID | if the sheet is theirs, delete that hidden tab (View → Hidden sheets) and run again |

## 4. Answer

- Give the link to the sheet and tab, how many rows were written, and the columns.
- **An email when the sheet changes,** in one line when the sheet is kept updated or the user asks for alerts: Google Sheets can send it itself: in the sheet, **Tools → Notification settings → Edit notifications**, choose **Any changes are made** and **Email - right away** (or **Email - daily digest**), then **Save**. Google sends it to their own Google account's address; MarketMage and CleanPull never see it.
- **For a watchlist,** offer to keep the sheet updated after every run:
  - It must run after the digest has finished: Sheets Sync with `taskId` writes the task's *last successful* run, so an action in the same schedule would write the previous one.
  - Apify schedules can't wait for another run to finish, so create a second schedule after the watchlist's (for example `30 8 * * *` after `0 8 * * *`, same time zone), with `create-schedule`:
    - name: `cw-export-` plus the watchlist's task name without `cw-` (for `cw-price-competitors`, `cw-export-price-competitors`), so the `watchlists` skill can list, pause and resume it with its watchlist (deleting it is done in the Console, at its own link `https://console.apify.com/schedules/<scheduleId>`, with the ID filled in, after pausing it: never only the schedules list);
    - **For a Watch Digest watchlist** (change rows have no single stable key), use `mode: "append"` with `incremental: true` (Sheets Sync remembers what it wrote to that tab and skips it), or `mode: "upsert"` with `keyFields: ["url", "what", "at"]`. Either way the same change is never written twice.
    - **Timing:** 30 minutes after the watchlist; **60 minutes after** when the digest has eBay, Etsy, Walmart, Target, Best Buy, AliExpress, Alibaba or Trustpilot items, which take longer.
    - **A digest that stopped early (ABORTED at its cap) isn't a successful run,** so that day's export writes the previous run again; with `incremental` or the key fields above, nothing is duplicated. Say so when you set it up.
    - one Actor action: `cleanpull/google-sheets-sync`, with input `spreadsheet`, `tab`, `mode` and `incremental` or `keyFields` as above (for other watchlists, `mode: "upsert"` with `keyFields` such as `url` or `barcode`), `taskId` of the watchlist, and **`limit`**: about 1.5× the rows a run writes (at least 50). Scheduled runs have no spending cap of their own, and Sheets Sync has no cost cap input, so `limit` is what bounds each export: at most `limit` × USD 0.0001.
  - Never edit the watchlist's own schedule for this. If you ever must change a schedule's actions, read it with `get-schedule` first and pass the whole actions list back with the change, since an update replaces the list.
  - Before creating it, show the monthly cost (rows per run × USD 0.0001 × runs a month) and the per-run limit it implies, and get a yes.
