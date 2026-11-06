---
name: map-watch
description: Check sellers against a minimum advertised price (MAP) by barcode across Amazon, Best Buy, Walmart, Target and other Google Shopping stores, once or on a schedule that reports new violations, price drops and new sellers. Use when a brand or distributor asks who is selling below MAP, or wants ongoing MAP monitoring for their UPCs/EANs.
---

# MAP watch

Find sellers below MAP, now and over time. Read these first:
- `references/running.md`: costs, caps, tools, secrets;
- `references/watchlists.md`: scheduling;
- `references/costs.md`: the prices.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. Ask only for

- **The barcodes** (UPC or EAN) with each one's **MAP**, for example `{"027242923232": 329.99}`.
- **Their UPC and MAP sheet, as it is:** offer it in one line ("Paste your UPC and MAP sheet, upload the file, or share the CSV: I'll read the columns"). Take a pasted table or CSV, an uploaded spreadsheet, or the rows of a Google Sheet the user pastes or a connected Google Drive opens. Then:
  - find the barcode column (UPC, EAN, GTIN, barcode) and the MAP column (MAP, min price, minimum advertised), and a dealer column if there is one (below);
  - read barcodes as text: a spreadsheet that dropped a leading zero leaves an 11-digit UPC or a 12-digit EAN; name those rows and ask, never pad them on a guess;
  - before the quote, one line: how many barcodes, and any row left out with its reason (no MAP, not a barcode, a duplicate with two different MAPs).
  - The whole sheet goes in one run (`products` and `mapPrices`): the actor reads 5 barcodes at a time, so a long list takes longer; follow the run until it ends.
- **Optional:**
  - **their authorised dealers:** a list of store or seller names, or a column in the sheet. With it, each violation is tagged as on the list or not (step 2, "Dealer tags"). Never ask for it as a gate; offer it once when the user mentions dealers, resellers or authorised sellers;
  - which stores matter (`googleStores`, default Walmart and Target);
  - whether to include used or refurbished offers (`conditions`, default new only).
  - Target and Best Buy matched by exact barcode (`serviceStores: ["target", "bestbuy"]`): USD 0.02 per store per run + USD 0.003 per barcode it sells, and 3 to 5 minutes a run; best for scheduled checks.

## 2. First check

If the user already wants it scheduled, make this first check the watchlist's baseline (`monitorMode: true` and the `monitorName`, as in step 3), so it isn't paid twice.

- **Run** `cleanpull/barcode-price-checker` with:
  - `products: [barcodes]`;
  - `mapPrices: {...}`;
  - `sources: ["amazon", "bestbuy", "google"]`.
- **Cost per barcode:** USD 0.003 + 3 Google searches × USD 0.004 ≈ **USD 0.015**. With extra `googleStores`, add USD 0.004 for each. 20 barcodes ≈ USD 0.30, so say this and get a yes over USD 0.05.
- **Read all three lists** in each record, never only the first:
  - `mapViolations`: confirmed-new offers below MAP, each with `store`, `seller`, `price`, `belowBy`, `title`, `condition`, `conditionBasis`, `url` with `urlSource` and `googleUrl`, and `isInternationalVersion`;
  - `mapUnconfirmed`: offers below MAP whose condition is `unknown`. **These are breaks too:** a new or unstated-condition offer under MAP is a violation unless its title shows another condition. Put them in the violations table, each marked "condition not stated"; never drop them;
  - `mapOtherCondition`: renewed, used and open-box offers below MAP: listed separately, as "below MAP, not new"; not violations.
  - Also `lowestNewPrice`, `lowestPrice` with `lowestPriceCondition`, `storeCount`, `conditionCounts`, and any set-aside listing's `flag` (the actor's reason, such as "store outside the US"): mention it when you say what was left out.
- **Amazon's other sellers:** the Amazon offer (`store: "Amazon"`, in `offers`, with the ASIN in `storeId`) has no seller named. With `offerType: "listing"` it is the listing's featured price, the one Amazon shows in search (its Buy Box price); with `offerType: "lowest-offer"` the listing has no featured offer and it is the lowest of its offers (say which). Its `offerCount` is the number of offers on the listing when Amazon showed it, and is often `null` with `listing`: that means **not known**, never one seller. Its place in the record still decides: in `mapViolations` it is a violation (a row in the table, whatever its `offerType`), in `mapUnconfirmed` a break marked "condition not stated", in `mapOtherCondition` not new; other sellers on the same listing may be below MAP. When that Amazon price is below MAP or within about 10% above it and `offerCount` is above 1 **or `null`** (only a count of exactly 1 rules other sellers out), **read the listing's offers**: `cleanpull/amazon-product-scraper` with `asins: [<storeId>]`, `marketplace: "US"`, `includeOffers: true` and `maxOffers` set to that offer's `offerCount` (at most 100), or `maxOffers: 30` when the count is `null` (the offers read is charged once per product, so more offers cost nothing more), about **USD 0.004** an ASIN. Run it straight away, without asking, while the MAP check and it stay under USD 0.05 together (up to about 8 such ASINs); for more, give the cost and ask. Then each new offer below MAP goes in the violations table **by seller name** (`seller`, its price, `buyBox` and whether it's FBA), with the Amazon listing link; used and refurbished offers go with `mapOtherCondition`. Not read (a no, or too many): name the Amazon price as "Amazon's featured (Buy Box) price, seller not named" for `listing` (or "Amazon's lowest offer" for `lowest-offer`) and add one line with the read's cost: "Name the <offerCount> sellers on this listing? (about USD 0.004)", or "Name the sellers on this listing? (about USD 0.004)" when the count is `null`.
- **Verify the clues against the titles** (`references/running.md`, "Read the data like an analyst"): an offer in `mapViolations` whose title shows a bundle, an accessory or another model is left out, and the answer says so. A confirmed-new offer far below MAP is a violation all the same: never dismiss a real violator for being cheap. Runs from before these fields (only `mapViolations`, with no condition): match each violation to its offer and read its `condition` and title.
- **Answer:**
  - **the check time** above the table, from the record's `scrapedAt`, in the user's time zone ("Checked 3 Nov, 14:05 ET"): a price is evidence for the moment it was read;
  - **the visual moment, just above the violations table** (`references/running.md`, "Explaining results": "One visual, where it helps"; only where you can draw one, and otherwise nothing about it is said): **sellers' prices against MAP**, one dot per seller in the answer (the `mapViolations` and `mapUnconfirmed` rows, and the sellers at or above MAP in the context line) on one price line, with the `mapPrice` as a marked line labelled "MAP USD <x>"; each break below it red and labelled with the seller and how far below (`belowBy`), a "condition not stated" one hollow and labelled so, the sellers at or above MAP grey; `mapOtherCondition` offers are left out (they are not breaks). With 2 to 5 barcodes, one row per barcode in the same visual; over 5, the barcode with the most breaks, said in the caption. Caption: the sources and the check time from `scrapedAt` ("Amazon, Best Buy and Google Shopping, checked 3 Nov, 14:05 ET");
  - a table of violations, worst first: seller, price, how far below, the link: every `mapViolations` row, and every `mapUnconfirmed` row marked "condition not stated" (unless its title shows another condition). Name each link by its `urlSource`: `"store"` is the store page; `"google"` (or no `urlSource`, on runs from before it) is Google's listing of the offer, not the store's page, since Google gave no store link: say so once. A Google Shopping row also has `googleUrl` (Google's listing), a second link where the main one is the store page. A row with `isInternationalVersion: true` (the title says International, Global Version or Intl) is a unit made for another country: mark it "international version" beside the row; it stays in the table, and what it means for the policy is the user's call. **More than 10 violations:** show the 10 worst, say how many more, and offer the full list in chat on request or in a Google Sheet (`export`, USD 0.0001 a row), with the dataset link (`https://console.apify.com/storage/datasets/<datasetId>`) for a CSV;
  - then, apart, `mapOtherCondition` (renewed, used or open box, with their condition): below MAP, not breaks;
  - **sellers at or above MAP, for context:** the record has no list of them, so take them from `offers`: each offer whose `price` is at or above `mapPrice`, new or with the condition not stated, after the same title checks. One line per barcode: "At or above MAP: Target USD 329.99, Crutchfield USD 329.99 and 3 more (5 sellers)", at most 5 named, the rest counted. None: "No seller found at or above MAP";
  - one plain line on what was set aside and why;
  - a count per store;
  - the barcodes with none.
  - Name the matching rule: Google listings are matched by model number and name (`minConfidence` 0.7). Say which matches are weaker.
- **Dealer tags** (when the user gave their authorised dealers): add a column to the violations table. A row is **"authorised"** when its seller, or, when no seller is named, its store (unless the row is a marketplace row, below), matches a name on the list: the same name ignoring case, punctuation and endings such as Inc., LLC or Ltd. Every other row is **"not on your list"**: never "unauthorised" or "illegitimate", since a list can be out of date and the brand decides. A close but different name ("Daily Spirit" against "Daily Spirit Deals") is "not on your list (close to: Daily Spirit)", for the user to decide. Amazon's featured price with no seller named is "seller not named" until the listing's sellers are read. The same goes for a marketplace store's row from Google Shopping (`source: "google"`; Walmart, eBay, Target Plus, Newegg and the like) with `seller: null`: Google Shopping often leaves marketplace sellers unnamed, so the row may be the store's own stock or a third-party seller's. Tag it "seller not named", never "authorised" on the store's name, and point the user to the link to see who sells it. Then one line each: how many violations are from dealers on the list, and how many from sellers not on it. The two usually take different routes (a dealer conversation, or a marketplace or reseller route), and that choice is the user's.
- **A draft MAP notice, on request** ("draft a notice to that seller", "write to the violators"): one draft per violation the user picks, for them to edit and send themselves. Ask once for what only they know: the brand and policy name (and its date or version, if they have one), and who signs it. Never invent a policy clause, a deadline or a consequence. Each draft, in neutral, factual wording:
  - who it is to: the seller and store as read. **A row with no seller named** (Amazon's featured price, or a marketplace store's `seller: null`) is never addressed to the store itself: for Amazon, read the listing's sellers first (above, about USD 0.004) and address the seller at that price; otherwise ask the user who the notice is for;
  - the product: its title as listed, and the barcode;
  - the facts: the MAP, the advertised price seen, how far below, when it was checked (from `scrapedAt`, with the time zone) and the link. With `urlSource: "store"` call it the store page; with `"google"` (or none) say it is Google's listing of the offer, so the reader knows where to look. `googleUrl` can go as a second link ("also listed on Google Shopping");
  - the condition as read ("listed as new", or "condition not stated on the listing");
  - one request: to review the advertised price under the brand's MAP policy for its products, with a line inviting a reply if the reading is wrong. The notice never says the seller is bound by the policy, has received it or agreed to it: that isn't a fact we have.
  - **A seller not on the user's dealer list:** before the draft, one neutral line to the user: "A MAP policy usually applies to the dealers it was issued to; whether and how it reaches this seller is your call." Then the draft as above, worded as the brand's policy for its products, not the seller's obligation.
  - It is about the advertised price and the brand's own policy only. It never asks the seller to agree a price, never mentions other sellers or their prices, and never makes legal claims or threats. It says "not on our authorised dealer list" only when the user gave a list and asks for that line.
  - After the drafts, one line: "Drafts to edit: check them against your policy before sending."

## 3. Scheduled (if wanted)

- **The task:** `cleanpull/barcode-price-checker`, named `cw-map-<name>`, with the same input plus:
  - `monitorMode: true`;
  - `monitorName: "<name>"`;
  - `minPriceChangePercent: 1`.
  - **The dealer list,** when the user gave one: in the task's description after "MarketMage:" ("MarketMage: MAP watch. Authorised dealers: Best Buy; Crutchfield; B&H Photo"), so later reads tag violations the same way. It's a list of names, not a secret.
- **What later runs return:** only products whose offers changed (new offer, removed, price up or down, stock). A changed product costs USD 0.003 + USD 0.002; an unchanged one costs only its searches.
- **Cost:** every run still pays the searches, about USD 0.012 per barcode. Daily, 20 barcodes with a few changes ≈ USD 0.26 a run, or **about USD 8 a month**; weekly is about USD 1.10. Show both.
- **The cheaper split, about USD 1.40 a month for 20 barcodes:** a daily check of the exact-barcode stores only (`sources: ["amazon", "bestbuy"]`: no Google searches, and unchanged products cost nothing, about USD 0.30 a month) plus a weekly full run with Google Shopping for Walmart, Target and the rest (about USD 1.10 a month). That's two tasks, `cw-map-<name>` (daily, exact) and `cw-map-<name>-all` (weekly, full), each with its own `monitorName`, so each records its own baseline. Offer it alongside the daily full run: the trade-off is that a Walmart or Target violation shows up within a week, not a day.
- **Baseline:** if the first check ran with `monitorMode` and this `monitorName`, it is the baseline: skip `references/watchlists.md` step 4 ("Run it once now"). If it ran without, the first scheduled run records the baseline (its products show `firstCheck: true`, no changes); say so instead of paying for another run now.
- **Bound each run:** add `maxRunCostUsd` to the task input, about 1.5× the per-run cost, at least USD 0.02.
- **Steps:** follow `references/watchlists.md`. Barcode Price Checker has no delivery channels: results stay in Apify, and the `briefing` and `watchlists` skills read them. Where the results go: "your briefing in Claude, on request or on a Monday schedule".
- **A violation log:** offer to keep one in a Google Sheet: the `export` skill's export schedule 30 minutes after each run (`mode: "append"`, `incremental: true`), so each run's changed products and their violations add dated rows (with `scrapedAt`) and the sheet shows when a seller was first and last seen below MAP, week by week. About USD 0.0001 a row: a few cents a month for 20 barcodes. One line, with its cost.
- **Amazon sellers on a scheduled run:** the watch reads Amazon's Buy Box price only. When the `watchlists` skill reads a run where that price is below or near MAP, it offers the listing's sellers as in step 2 (about USD 0.004 an ASIN).
