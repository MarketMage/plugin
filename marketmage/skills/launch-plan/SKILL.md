---
name: launch-plan
description: Turn a product idea the data favours into a first launch plan, in one guided flow - supplier prices at the user's first-order quantity, what buyers complain about in the Amazon leaders' 1-star reviews, a listing draft (title, 5 bullets and the difference that answers those complaints), the price position against the market's band, first-order maths after Amazon's fees against their budget band, a stop rule with numbers agreed before launch, and one launch-week watch on the leaders' prices, ranks and reviews - asking first, with one estimate, before the paid steps run. Use after a Strong or Promising verdict, when someone says they want to go ahead with, launch or start sourcing an idea, or when they paste their ad test results to read against the stop rule. Not for judging whether an idea is worth it (use validate first).
---

# Launch plan

The user has an idea the data favours and wants to go ahead. Build the first launch plan with them from today's data, reusing what this conversation already read. Read these first:
- `references/judgement.md`: the core: "Margin after fees", "The sales floor is a floor"; `references/judgement-answer.md`: the tone and the answer structure; `references/judgement-ladder.md` when a verdict or a watch is written; `references/judgement-profile.md`: the seller profile; with a profile, once the lens is chosen, `references/judgement-for-you.md` and the chosen lens's file only (`references/judgement-lens-cold-traffic.md` with `references/judgement-lens-cold-traffic-count.md`, `references/judgement-lens-marketplace.md`, `references/judgement-lens-own-stock.md`, `references/judgement-lens-maker.md` or `references/judgement-lens-general.md`; plus `references/judgement-lens-goals.md` when the goal is side income or brand); `references/judgement-abroad.md` (margins outside the US or across currencies, EU risk notes) before working such a margin;
- `references/judgement-rates.md`: the start-up costs with their sources (and the EU VAT rates, on an EU marketplace other than the UK and Germany), read when the first-order maths is written;
- `references/running.md`: costs, caps, tools, and "Runs in this conversation";
- `references/running.md` is the core; its parts are read only at their step (its first lines say when): `references/running-results.md` once results are in, before using them; `references/running-runs.md` before a data-provider read, when a run doesn't succeed, or when this chat already holds a run; `references/running-abroad.md` outside the US; `references/running-asks.md` when the user asks who runs this, offers an allowance, pastes a secret or asks for something MarketMage won't do.
- `references/known-limits.md`: routes established not to work, each with what to use instead: read in the same batch as `references/running.md`, before choosing any source (a store, a marketplace, a country, a keyword); never try a route it lists. `references/plain-words.md` (the words the user sees, for every answer) is read in that same batch.
- `references/watchlists.md`: the watch steps;
- `references/notebook.md`: if the user keeps a notebook (then `references/notebook-use.md` before any notebook call);
- `references/costs.md`: the prices.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. What it starts from

- **The idea and marketplace,** and the price the user plans (else the market's median, said as such).
- **Rows already read** in this conversation (`references/running-runs.md`, "Runs in this conversation"): the Amazon leaders (ASINs, prices, ratings, `starBreakdown`, `fees`), the keyword summary (`priceP25`…`priceP75`, `singleNewPrice`, `salesFloor`), the supplier summary (`unitPriceMedian`, `moqMedian`, `lowestMoqOffer`), the Trends rising searches, and the leaders' reviews if the "Leaders' complaints" add-on ran. Reuse them; never buy them again.
- **No verdict yet in this chat:** the plan needs the market rows. Offer `validate` first, or, if they only want the plan, the three reads it needs, with one estimate for the three together, with exactly these inputs (the same as `validate`'s):
  - the leaders: `cleanpull/amazon-product-scraper` with `searches: ["<idea>"]`, `maxResultsPerSearch: 10`, `marketplace`, `includeSearchSummary: true` (about USD 0.03);
  - the keyword summary: `cleanpull/marketplace-search-scanner` with `keywords: ["<idea>"]`, `sources: ["amazon"]`, `amazonMarketplaces: ["<marketplace>"]`, `listingRows: false` (about USD 0.017);
  - the supplier read below.
- **The budget band** (`references/judgement-profile.md`, "The seller profile and lenses"): from the profile in the chat or the notebook. Without one, ask only the budget question, in one line, as bands (under USD 250, under USD 1k, USD 1k to USD 5k, USD 5k to USD 25k, more), **unless a budget or profile question was already asked in this conversation**: then never ask again. If it was skipped or not answered, plan for a typical new seller's first order, the USD 1k to USD 5k band (USD 1,200 of goods in the table below), and say so in one line ("Planned for a typical first order, about USD 1,200 of goods; tell me your band to change it"). Never ask for an exact amount; an amount given is turned into its band, and is also kept privately for this chat's first order (below), never said back.

- **Hours a week, for a side income** (the goal is a side income and they haven't said how much time they have): one optional line, as `references/launch-plan-more.md`, "Hours a week" sets out.

### Their channel frames the plan

The plan is written for **where they'll sell**, from the question or the profile's channels (`references/judgement.md`, "The margin follows the user's channel"), never Amazon by default when they named another channel:
- **Amazon:** as written below (Amazon's fees, an Amazon listing, the Amazon ads column of the stop rule).
- **Their own store (Shopify or similar) with ads, or TikTok Shop:** the per-unit maths uses their channel's fee (TikTok Shop's `marketplaceFees` from the TikTok read, or the card fee assumption of 2.9% + USD 0.30 for their own store), never Amazon's FBA fee; the listing draft becomes **a product page** (a title, a short opening line on the difference, 5 benefit bullets) **and 3 ad hooks** (the first seconds of a video or the first line of an ad, each answering a complaint); the stop rule's "own store or TikTok Shop" column applies; the market's Amazon rows stay as the market, labelled as Amazon's.
- **Etsy or eBay, or a maker:** `references/launch-plan-more.md`, "Etsy, eBay or a maker", read before the plan for those channels.

Say the channel once, at the top ("Planned for selling on TikTok Shop and your own store").

## 2. The plan, asked once

Show the seven steps in one short numbered list, with no per-step prices, and ask one question with the one estimate for the paid steps (`references/running.md`, "Before any run"): "Shall I run steps 1 and 2 (up to about USD <total>, with a spending limit)?" Nothing paid runs before the yes. The per-step figures below are what that estimate is worked out from. The watch (step 7) always gets its own yes later, since it recurs.

1. **Suppliers at your first-order quantity** (`cleanpull/supplier-price-finder`, `products: ["<idea>"]`, `sources: ["made-in-china"]`, `maxOffersPerSource: 10`, `quantity: <units>`): about USD 0.025. With dropship or print on demand, add the AliExpress single-unit check as its own run beside it (`products: ["<idea>"]`, `singleUnitCheck: true`, `sources: ["aliexpress"]` (always say it: without `sources` the actor's default adds a paid Made-in-China read), and `marginCheck` for a cold-traffic seller with their own store, as in `suppliers`: AliExpress's top 3, MOQ 1 and the price for one unit before shipping; about USD 0.04 more), unless `validate` already read it in this conversation. It usually takes under a minute, 5 to 20 minutes when AliExpress is slow: say so with the estimate ("the AliExpress price usually takes under a minute"), start it first with `waitSecs: 0`, and when the other steps are in, wait for it (`get-actor-run` at `waitSecs: 45`, then once more at 15 if still RUNNING: `references/running-runs.md`, "Timing"). Finished by then (the normal case): give the plan with its numbers in place, with no provisional mark and no follow-up. Only if it is still RUNNING after that wait, say "AliExpress is slow on this one (it can take 5 to 20 minutes); I'll answer now and add it when it lands" and give the plan with the parts that read from it marked "AliExpress is slow on this one (it can take 5 to 20 minutes)": the MOQ-1 offer and its price, the check's `margin` (the break-even price, the profit at USD 8 and 12 of ads) and everything worked out from them (the first-order maths for dropship, the stop rule's ad spend, the price advice), and complete them in a short follow-up when it lands (the first answer is not the end of the turn: keep following the run in the same turn and write the follow-up when it lands). Follow it as `references/running-runs.md`, "Timing" sets out; a check already running for this idea in this conversation (from `validate`) is followed, not started again.
2. **The leaders' complaints** (`cleanpull/reviews-monitor`, `asins`: the 3 leaders with the highest 1-star share in `starBreakdown`, `amazonMarketplace`, `maxReviewsPerProduct: 20`): about USD 0.01 an ASIN, USD 0.03 for 3. Skipped when this chat already read them. **For US leaders, it isn't run on amazon.com:** there it gives no review text, only the star breakdown already in the leaders' rows (`references/known-limits.md`, "Amazon reviews in the US"). Use their 1-star share, and offer the same ASINs on amazon.co.uk or .de instead. Other marketplaces run it as written.
3. **A listing draft:** no run.
4. **Price position:** no run.
5. **First-order maths:** no run.
6. **The stop rule, agreed before launch:** no run (below).
7. **A launch-week watch:** recurring, its own yes (below).

**The first-order quantity** comes from the budget band, so that the goods leave room in the band for freight, samples and launch ads:

| Budget band | Goods in the first order, about | Units |
| --- | --- | --- |
| under USD 250 | USD 100 | goods ÷ the supplier's `unitPriceMedian`, rounded down to 10, 20, 50, 100 or 200, never under the MOQ |
| under USD 1k | USD 400 | goods ÷ the supplier's `unitPriceMedian`, rounded down to 50, 100, 200, 300, 500, 1,000 or 2,000, never under the MOQ |
| USD 1k to USD 5k | USD 1,200 | the same |
| USD 5k to USD 25k | USD 4,000 | the same |
| USD 25k and more | USD 10,000 | the same |

Say the rule in one line ("about USD 1,200 of goods for a USD 1k–5k band: 250 units at USD 4.80, rounded to 200"). When the median MOQ's cash (`moqMedian` × `unitPriceMedian`) is above the band's goods figure, plan from `lowestMoqOffer` or AliExpress (MOQ 1) instead, and say so. This is planning arithmetic from the band, never the user's own figure.

**An exact amount given in this chat** (never repeated back): the goods and the test spend follow `references/launch-plan-more.md`, "An exact amount", read when the user gives one.

## 3. Run and read

Follow `references/running.md` (caps, `waitSecs: 45`, polling). Read:
- **Suppliers:** the summary row in full (`quantity`, `unitPriceMin`, `unitPriceMedian`, `unitPriceP25`, `moqMedian`, `cheapestOffer`, `lowestMoqOffer`, `landedUnitCostMedian`), and the offers with `fields: "recordType,title,url,unitPriceMin,unitPriceAtQuantity,moq,priceTiers,supplierName,supplierYears,supplierVerified,supplierLevel,supplierRating,specs"`. From the single-unit check, its summary's `singleUnit` (`moq1OfferFound`, `unitPriceMin` before shipping, `sampleUrl`), its `margin` when present (read as `references/judgement-lens-cold-traffic.md` says), and the offers' `sellsSingleUnit`; with `offersRead: 0`, say "AliExpress showed no matching listing under this name; try another name" and offer one rerun under a synonym; when AliExpress didn't answer in any form (`aliexpress: "no answer"` or `"not checked"`, a free `unavailable` row ("AliExpress didn't answer within 20 minutes") or `stopped` row, or no summary row), say "single units: not confirmed yet (AliExpress didn't answer in time; most consumer goods sell single units there)" and offer one rerun. Rank the top 3 to contact by this trust score (the same rule as the `suppliers` skill), and show the rule so the user can disagree with it:
  - `supplierYears`: 1 point for 3+ years, 2 for 8+;
  - `supplierVerified` (audited or verified): 2 points;
  - `supplierLevel` Diamond or Gold: 1 point;
  - `supplierRating` 4.5 or more: 1 point (AliExpress store ratings count the same way).

  Put unit price at the quantity and MOQ next to each, and name the trade-off plainly when the cheapest offer scores low ("the cheapest offer (USD 0.48) is from a 1-year supplier with no audit, score 0; the median offer (USD 0.61) from a 12-year audited one, score 5"). The score is a first filter from public listing data, not a check of the business.
- **Complaints:** each `rating-summary` row's `histogram` (`percent` on Amazon), `topComplaints` and `themes` (complaint themes with `reviews` and `share`), and the 1- and 2-star `review` rows (`fields: "recordType,asin,rating,title,text"`). Amazon shows only its 8 to 13 top reviews per product: say the complaints are a sample, and quote short phrases, never names. The actor's named themes match English phrases only: on non-English reviews (amazon.de, .fr, .es) they come mostly as recurring phrases in that language, or none, so read the 1- and 2-star texts themselves for the complaints, and say so.

## 4. The plan, in this order

1. **One line on where they stand:** the verdict and its two biggest numbers, from this conversation (or the notebook, with its date).
2. **Suppliers to contact first:** the top 3 by trust score, unit price at their quantity, MOQ, and the three questions to send each (the price at their quantity with a sample, lead time, and the one spec that answers the main complaint: "can you make the strap adjustable?"). List prices are a first look, not a quote.
3. **What buyers complain about:** the top 3 complaint themes across the leaders, each with how many reviews mention it and one short quoted phrase.
4. **The difference:** the one change that answers the biggest complaint, in a sentence a shopper would understand, and whether the suppliers' `specs` or titles show they can make it.
5. **Listing draft,** in the marketplace's language (German for amazon.de, French for amazon.fr; English for the US and the UK), with an English line under it only if they ask:
   - a title (under 150 characters): the keyword shoppers use (the scan's keyword, and a rising search where it fits), the difference, size or count;
   - 5 bullets, the first one on the difference, each answering a complaint or a question the reviews raise;
   - only claims their product will meet; nothing about health, safety or certifications they haven't confirmed.
6. **Price position:** their price against `priceP25`…`priceP75` (or `singleNewPrice` when it excluded listings): inside the band, or above `priceP75` with the difference as the reason a shopper pays more. Under `priceP25` is named once as a race to the bottom, with the price the difference would earn instead.
7. **First-order maths** (a small table, numbers from the rows, arithmetic shown):
   - units × unit cost at that quantity = the goods' cash, against the band ("about USD 960, inside USD 1k–5k, leaving room for freight and launch ads"; with an exact amount, "fits the amount you gave me" or "doesn't fit the amount you gave me", never the figure); landed cost only where a page quoted shipping, else "freight and duty to add from the supplier's quote";
   - per unit: the price, Amazon's fees (`references/judgement.md`, "Margin after fees": referral at the leaders' rate plus the comparable leaders' median FBA fee; a range when only ranges exist), paid out after fees, less the unit cost: what each sale leaves before freight, duty and ads, and that as a share of the price;
   - units to sell to get the goods' cash back (cash ÷ paid out after fees per unit);
   - **start-up costs to add,** one short line, no figures unless the user or a read gives them (never from memory): the marketplace's seller plan (Amazon's Professional plan is monthly), samples and their shipping, freight and duty to them or into Amazon, barcodes and labels, and product photos. Figures they give go into the cash line, labelled as theirs;
   - **and, from `references/judgement-rates.md` ("Start-up costs before the first sale"), with each source named:** a US sales-tax permit for a seller in the US (their state's tax agency; in Texas, the Comptroller's permit, which the page says takes 2 to 3 weeks), barcodes (GS1 US: USD 30 for one GTIN, or USD 250 plus USD 50 a year for a prefix of 10, when their marketplace asks for them), and Etsy's listing fee (USD 0.20 a listing, renewed every four months or after each sale) for an Etsy seller; for a seller in Canada, Etsy's Canadian fees and the CAD note from that file. Only the lines that fit their channel and country, in a few words each;
   - **the worst case, one line:** "If nothing sells, you're out about USD <goods> of goods plus the USD <test spend> test: about USD <total>." The goods are the first order's cash above (for a dropshipper, the sample order); the test spend is the stop rule's (below); the start-up figures they gave are added, labelled. With an exact amount of theirs, the line gives these planning figures, never the amount ("about USD 300 of goods plus a USD 75 test, about USD 375, within the amount you gave me"). Said plainly, as a planning figure, never as a warning; the stop rule is what keeps it to that;
   - the order against the market: their units against the top 10's sales floor ("200 units; the top 10 sell at least 12,000 a month between them"), said as a floor, never as a forecast of their sales.
   Fees are modelled on amazon.com and on amazon.co.uk, .de, .fr, .it and .es (there, what a sale pays out is the leaders' `afterFeesExVat`, VAT out first: `references/judgement-abroad.md`, "Amazon's fees in the UK and the EU"); on other marketplaces outside the US the maths is before fees, and says so.
   A unit cost in another currency than the price (USD factory prices against a euro or pound price) is never subtracted across currencies: ask once for their rate or a landed cost in their currency, and use it labelled as theirs (`references/running-abroad.md`, "Country"). Freight and duty come from them or a page that quotes them, never from memory.
   **The visual moment, just before this table** (`references/running-results.md`, "Explaining results": "One visual, where it helps"; only where you can draw one, and otherwise nothing about it is said): the per-unit line as **a waterfall**: the price, then Amazon's referral and FBA fees (VAT first where it came off; the channel's own fee for TikTok Shop or an own store), then the unit cost, ending on what each sale leaves and its share of the price, each bar labelled with its amount, the same figures as the table (a fee range drawn at its lower end, labelled "from"). One visual per answer, so the steps stay a list. Caption: the sources and the date read ("Amazon US fees and Made-in-China list prices, read 6 Nov").
8. **For you, through the lens:** only with a profile: the lens's gates and fit lines that bear on the launch (the first order against the band, fulfilment against the product, ad cost against the band), each naming its fact (`references/judgement-for-you.md`, "The For you block").
9. **The stop rule** (below): the rule with its numbers, in three short lines, and one question: "Agree this stop rule before you spend, or change a number?"
10. **The notebook:** if the user keeps one, note their decision only when they state it (`pursue`, with its note starting `stage: sourcing`), the agreed stop rule (below), and the watch link once it's created (`references/notebook.md`).
11. **The launch-week watch, as a follow-up line** that says what it watches, with no price (its monthly estimate comes with the yes it needs): "Also on offer: a launch-week watch on the 5 leaders' prices and Buy Box, their ranks on 3 keywords, and their new reviews." Created only after a yes (below).
    **The plan as a document, offered in one line once the stop rule is agreed (so in the next answer, not beside the stop-rule question)** (`references/running-results.md`, "Explaining results": "Things people keep, offered"): "Want this plan as a document you can share with a partner?" On a yes, a document in this chat (an artifact, or a Word or PDF file where this Claude makes files; from Claude Code, an artifact's claude.ai link) with the plan's sections as headings, the stop rule as agreed and no MarketMage internal names. Never made unasked.
12. **Next step, last, and only one:** send the three questions to the first supplier and ask for a sample. The watch is never the closing line.

**Voice:** hopeful and practical (`references/judgement-answer.md`, "Tone"): this is the user's plan, built on numbers they can check. Credit what the data backs; one step line at most for outside knowledge ("Before listing: check whether heated products need extra approval in your category").

## 5. The stop rule

Before any money goes on ads, agree **when to stop**, with numbers, so the call is made by a rule set in calm rather than by hope during the test. Set it from the budget band and how they'll sell; the figures are rules of thumb, said as such, and every number is theirs to change.

**The test spend and length, from the band** (planning figures from the band, never their own amount):

| Budget band | Ads to their own store or TikTok Shop | Amazon ads (sponsored products) |
| --- | --- | --- |
| under USD 250 | USD 75 or 7 days | USD 50 or 14 days |
| under USD 1k | USD 150 or 7 days | USD 100 or 14 days |
| USD 1k to USD 5k | USD 300 or 7 days | USD 250 or 14 days |
| USD 5k to USD 25k | USD 600 or 10 days | USD 500 or 14 days |
| USD 25k and more | USD 1,000 or 14 days | USD 1,000 or 21 days |

**With an exact amount given in this chat:** the test spend as `references/launch-plan-more.md`, "An exact amount" sets out.

Whichever comes first. Then the rule, in three lines:

- **Ads to their own store or TikTok Shop (cold traffic):** after the spend or the days, **add-to-cart under 2% of visitors → stop**; **link click-through above 1.5% with add-to-cart under 2% = curiosity, not intent**: change the offer or the page once (price, proof, the difference), not the creative, and stop if the same spend again doesn't lift it; **no sale at all, or a cost per sale above what a sale leaves after the unit cost and fees** (from the first-order maths) → stop or reprice. Keep going when add-to-cart is 5% or more and sales cover their ad cost.
- **Amazon:** after the spend or the days, **orders under 5% of ad clicks (with at least 100 clicks) → stop the ads and fix the listing**, then stop reordering if a second round doesn't lift it; **ad click-through above 0.5% with orders under 5% of clicks = curiosity, not intent**: fix the price or the listing, not the ads; **click-through under 0.3%** → the main image or title isn't stopping anyone. "Stop" here means no reorder: sell through the first order.
- **The check date:** the day they start ads plus the days above. It comes from the start date they give: ask "When will you start ads?" in the same line, and say the date ("check on 8 Nov"). Without a start date, the check is "7 days after you start ads", never counted from today.

Say it in three lines with the numbers filled in, then the one question. Agreeing the rule is planning: it moves no stage and records no decision to buy or launch. On their yes (or their changed numbers), and only then: with the notebook on, `addEntry` one `decision` entry linked to the idea, `decision: "test"`, with the note in the fixed form, at most 300 characters (`references/notebook-use.md`, "What to write"), the test spend as its **band word** (`under-100`, `100-250`, `250-500`, `500-plus`), never the amount: `stop rule · check 2026-11-08 (start + 7 days) · test spend band 100-250 · add-to-cart under 2% → stop; click-through over 1.5% with add-to-cart under 2% = curiosity, not intent; no sale → stop` (without a start date: `check after start+7 days`, filled in with `updateEntry` when they give it). No first-person or budget words in it, and no `stage:` prefix. This is the idea's only `test` entry: never add another (the actor would overwrite this one); later news ("I've ordered stock", "ads are running") moves the stage on the idea entry with `updateEntry` (`references/notebook-use.md`, "Journey stages"), and only that news moves it to `launching`. Say "Noted your stop rule; once 8 Nov has come, I'll bring it up when you ask what's new." The `briefing` skill raises it only once the check date has come (today or past). Without the notebook, give them the rule as one line to keep.

**Reading the test against the rule** (when the user pastes their ad numbers, or asks how the test went): `references/launch-plan-more.md`, "Reading the test against the rule", read then.

## 6. The launch-week watch: `cw-launch-<idea>`

One Watch Digest task that watches the market they're entering, daily, through launch: its input, cost per run, cap and steps are in `references/launch-plan-more.md`, "The launch-week watch", read on the user's yes to it (or when they ask what it would cost), before quoting or creating it. The follow-up line in step 4 (item 11) carries no price: the monthly estimate is given once, with the yes it needs.
