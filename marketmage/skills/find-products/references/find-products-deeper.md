# Find products: going deeper (the directions read)

Read on the user's yes to going deeper, in one batch with `judgement-deeper.md` (which sets out the conversation: the vision questions, the direction cards, "Where we are", the working brief and the end). This file holds what only `find-products` does: the directions read's runs, their cost and the tool calls they take.

## The turns

1. **The yes to going deeper:** read, in one batch, every reference the deeper path will need that this chat hasn't read yet: this file, `judgement-deeper.md`, `judgement-complaints.md`, `running-runs.md` and `running-results.md`. Then ask the vision questions with the estimate below, in one message; no runs. Reading them all here keeps the directions turn's tool calls for the runs.
2. **Their answer and "go":** pick the 3 directions from the rows already read (`judgement-deeper.md`, "The directions"), run the directions read, then write the cards in the shape `judgement-deeper.md` gives (about 300 words in all: each card line one fact, one number, copied from its row; check each number against its row and the word count before sending); no reference is read again.
3. **After that, press and narrow:** from the rows already read; a new read only as `judgement-deeper.md`, "A conversation that converges" says.

**No ideas read yet** (the user asked to go deeper before any table): the standard read (step 2 of the skill) runs first, under the same yes, and its figure is part of the one estimate.

## The directions read: one run per source for all three directions

Round 1 runs together; round 2 starts when the Amazon top 10 is back. TikTok Shop and Trends rows from the quick answer are reused, never bought again (`running-runs.md`, "Runs in this conversation").

| Round | What | Actor | Input | Cost on paid plans |
| --- | --- | --- | --- | --- |
| 1 | The Amazon market for each direction | `cleanpull/marketplace-search-scanner` | `keywords`: the 3 directions' search terms, `sources: ["amazon"]`, `amazonMarketplaces: ["<marketplace>"]`, `listingRows: false`, `includeAds: false` | 3 × USD 0.005 ≈ **USD 0.015** in the US (+ USD 0.012 a keyword elsewhere), up to 3 × USD 0.016 more for change rows when this account scanned them before |
| 1 | The Amazon top 10 for each | `cleanpull/amazon-product-scraper` | `searches`: the same 3 terms, `maxResultsPerSearch: 10`, `marketplace`, `includeSearchSummary: true` | 30 × USD 0.003 ≈ **USD 0.09**; outside the US + 30 × USD 0.003 local-market |
| 1 | Factory prices and minimum orders | `cleanpull/supplier-price-finder` | `products`: the 3 terms, `sources: ["made-in-china"]`, `maxOffersPerSource: 10` | 3 × (USD 0.005 + 10 × USD 0.002) ≈ **USD 0.075** |
| 2 | The leaders' complaints, 2 per direction | `cleanpull/reviews-monitor` | `asins`: per direction, the 2 leaders with a sales badge and the highest 1-star share, as product links: for US leaders on amazon.co.uk (`https://www.amazon.co.uk/dp/<ASIN>`; review text is never asked of amazon.com: `known-limits.md`), elsewhere their own marketplace; `maxReviewsPerProduct: 20`, `sinceDays: 3650` (no date window), `includeThemes: true` | 6 × about USD 0.022 ≈ **USD 0.13** |

- **The one approval line,** in the vision questions' message, one estimate with the soft note: "It costs about USD 0.40, occasionally a little more if I need to dig deeper to answer you" in the US (the runs above come to about USD 0.31, and the high end covers change rows), about 3 to 6 minutes, plus the standard read's figure in the same total when it runs first, with the known-limits line for US leaders ("Amazon US shows review text only to signed-in shoppers, so I'll read the same products on Amazon UK."). The spending limit, USD 0.60, is internal and never said, split across the runs (`running.md`, "Before any run", item 6).
- **Through the cold-traffic lens,** the read adds the Meta advertisers for the 3 terms and the AliExpress single-unit check on the 3 (their inputs: `references/find-products-lenses.md`, "Step 2, cold-traffic offers"), and leaves the factory prices out: about USD 0.55 to 0.65, with the free-plan figure in the same line where it differs (`running.md`, "The free-plan price only when it differs").
- **Outside the US:** no TikTok Shop (`known-limits.md`); the reviews are the marketplace's own pages.

## Reading it

- **Market** (`keyword-summary` rows): `salesFloor`, `priceP25`…`priceP75`, `medianReviews`, `under100Reviews`, `top3SellerShare`: the demand floor and the price band with few strong listings.
- **Top 10** (`fields: "recordType,asin,title,brand,price,rating,reviewCount,starBreakdown,boughtPastMonthMin,dateFirstAvailable,fees,salesFloor"`): which rows are the product, the leaders to read for complaints (round 2), and variants the rising searches name that the leaders' titles don't carry.
- **Factory offers:** the unit price and MOQ at the user's first-order size, and offers that list a fix.
- **Reviews:** read as `judgement-complaints.md`, step 3; a leader not sold in the UK is "not read".

## Tool calls

The directions turn stays within about 16 tool calls, for claude.ai's limit per reply: no reference reads (they were read at the yes), 3 runs and their 3 reads in round 1, 1 run and its read in round 2 (a `RUN_SUMMARY` read only when it ended PARTIAL): about 8. When the standard read runs first in the same turn (no ideas read yet), it adds its runs and reads, about 5 more. Through the cold-traffic lens, the AliExpress single-unit check is followed with `get-actor-run` (`running-runs.md`), 1 to 3 more calls: with both, the turn can pass 16, so stop at a clean point as `running.md` says rather than skip a read. Independent calls go in one message. If the reply might still run out, stop at a clean point as `running.md` says ("Tool calls: one reply, a budget").
