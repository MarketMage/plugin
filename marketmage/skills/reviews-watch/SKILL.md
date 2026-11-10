---
name: reviews-watch
description: Read or monitor product reviews - average rating, review count, share per star, the newest reviews and the complaint and praise themes in them - for product pages on shops using Judge.me, Yotpo, Okendo, Loox or Stamped, for Amazon ASINs, and for businesses on Trustpilot, once or on a schedule that reports new reviews and rating moves. Use when someone asks what customers say about a product (theirs or a competitor's), what shoppers complain about, whether a rating is slipping, or wants to be told about new or bad reviews. Not for writing replies to reviews.
---

# Reviews watch

Ratings, new reviews and what shoppers praise or complain about, now or over time. Read these first:
- `references/running.md`: costs, caps, tools, secrets;
- `references/running.md` is the core; its parts are read only at their step (its first lines say when): `references/running-results.md` once results are in, before using them; `references/running-runs.md` also before a status message stands in for rows; `references/running-runs.md` before a data-provider read, when a run doesn't succeed, or when this chat already holds a run; `references/running-abroad.md` outside the US; `references/running-asks.md` when the user asks who runs this, offers an allowance, pastes a secret or asks for something MarketMage won't do.
- `references/known-limits.md`: routes established not to work, each with what to use instead: read in the same batch as `references/running.md`, before choosing any source (a store, a marketplace, a country, a keyword); never try a route it lists. `references/plain-words.md` (the words the user sees, for every answer) is read in that same batch.
- `references/watchlists.md`: scheduling;
- `references/costs.md`: the prices.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. Ask only for

- **The products:** product page URLs from the user's or competitors' shops, and Amazon ASINs or URLs with the marketplace (US by default).
- **A brand's best seller, not its ASIN** ("watch TruSkin's best seller"): find it with `cleanpull/amazon-product-scraper` (`searches: ["<brand> <product>"]`, `marketplace`, about USD 0.03 for 10 results), keeping the brand's rows (the most "bought in past month" leads), never with a web search (`references/known-limits.md`).
- **Companies on Trustpilot:** a domain (`allbirds.com`) or its `trustpilot.com/review/…` page, as `trustpilotDomains`.
- **A store whose own reviews can't be read** (listed in `references/known-limits.md`, such as allbirds.com): never pass its product pages; read its Trustpilot page (`trustpilotDomains`) instead, even when the user pasted a product link, and say so once in the plain words given there.
- **Once or ongoing.** If ongoing, how often: daily or weekly.
- **Optional:** how far back (`sinceDays`, 30 by default) and how many reviews per product (`maxReviewsPerProduct`, 20 by default; 0 for the rating summary only).

Never ask for reviewer names, and leave `includeReviewerNames` off (its default). Names are personal data, and themes, alerts and comparisons don't need them. If the user asks for names, say they're off by design; they can turn the field on in the actor's input in the Console only if they have a lawful reason to process them.

## 2. One-off read

- **Run** `cleanpull/reviews-monitor` with `productUrls`, `asins`, `trustpilotDomains`, `amazonMarketplace`, `sinceDays`, `maxReviewsPerProduct`.
- **A one-off read of what buyers say or complain about** passes `sinceDays: 3650`, never the 30-day default: Amazon's featured reviews are mostly older than a month (`references/known-limits.md`). A short window is for watches.
- **Cost (paid plans):**
  - each product read: a rating summary USD 0.003 + USD 0.0005 per review delivered;
  - a shop product with 20 reviews ≈ **USD 0.013**; an Amazon ASIN outside the US (its 8 to 13 top reviews) ≈ **USD 0.01**; an amazon.com (US) ASIN: its rating summary only, USD 0.003 (below); outside the US, add up to USD 0.012 for the local-address reads;
  - **a Trustpilot business:** summary USD 0.003 + USD 0.003 for its read (provider search) + USD 0.0035 per review delivered (review USD 0.0005 + provider record USD 0.003): with 20 reviews ≈ **USD 0.076**. It's read through CleanPull's marketplace data service (a third-party provider; nothing to set up) and takes about 30 to 60 seconds a business;
  - a product whose shop uses another review app, or that can't be read, is not charged.
  - **When the estimate is USD 0.05 or less,** run it straight away, with no cost mention; above that, give the one approval line, a range and a ceiling, and ask first (`references/running.md`, "Before any run"). **Example above it:** 4 product pages and 2 ASINs, 20 reviews each: "Usually USD 0.05–0.07; it can't go over USD 0.25. Go ahead?", with the run's cap at that ceiling.
- **Read** with `get-dataset-items`:
  - the `rating-summary` rows in full: `average`, `count`, `histogram` (`histogramUnit` is `count` for the review apps and `percent` for Amazon), `themes`, `topComplaints`, `topPraise`, `newestReviewDate`;
  - the `review` rows with `fields: "recordType,productTitle,rating,title,text,date,verified,variant,reviewId"` and a `limit` of about 100.
- **Not read:** `RUN_SUMMARY.failures` names each product that wasn't, with the reason. Say which:
  - shops using Bazaarvoice, Junip, REVIEWS.io, PowerReviews or another app, and review apps loaded only by a theme's scripts;
  - Amazon's full review list (it needs a sign-in): outside the US Amazon gives the rating, the share per star and the top reviews only; amazon.com gives the rating and the share per star only (next point).
- **amazon.com (US) shows no review text to signed-out shoppers:** follow `references/known-limits.md`, "Amazon reviews in the US" (say it before the run, price US ASINs as the summary only in any estimate, offer amazon.co.uk or .de or shop pages, never "no complaints").

## 3. Explain it like an expert

- **Lead with the verdict per product:** rating, count, and whether the recent reviews are better or worse than the average.
- **The visual moment, after the verdict lines and before the detail** (`references/running-results.md`, "Explaining results": "One visual, where it helps"; only where you can draw one, and otherwise nothing about it is said; never in the first answer to this skill's new reads, only in a follow-up turn: the full detail or list, a chart the user asks for, a deeper turn): for one product (the user's own when it was read, else the one the answer leads with), **the star breakdown**: five horizontal bars, 5 stars down to 1, from the `rating-summary` row's `histogram` as shares of all ratings (a `count` histogram turned into shares, with the counts in the labels), each labelled with its share; beside it, **the top complaint themes** (at most 3, from `themes` or `topComplaints`) as labelled bars of how many reviews mention each (`reviews`, with `share`), in the words the answer uses. No themes read (amazon.com, a non-English page with none): the stars alone. Stamped and Loox publish no counts per star: no visual for them. Under about 20 reviews, the caption says the themes are a hint. Caption: the source, the `count` of ratings, and the date read ("Amazon UK, 1,204 ratings, read 6 Nov"). The same figures are given in one line of the answer as well.
- **The shape of the stars:** a healthy product is heavy at 5 with a thin middle. A bump at 1 star usually means a defect, a shipping problem or a listing that promises too much; read those reviews first.
- **Themes:** name the top complaint and praise themes with how many reviews mention each (`reviews`, `share`), and quote one short example review per theme (text only, never a name).
  - **On a competitor:** their complaints are the user's selling angle ("doesn't run small", "arrives in a padded box"); their praise is the bar to meet.
  - **On the user's own product:** turn each complaint into a fix: a size chart, packaging, a clearer photo or description.
- **Going deeper** (the elevation layer), offered once, in one line before the watch offer (the watch offer stays last): "Want the full list, or shall we go deeper and turn this into what you'd build or fix?" On a yes: **on a rival's products,** the complaint brief (`complaint-brief`: the complaint you'd fix with its count across the products read, the praise to match, the fix as a spec line, how to show it, and its honesty rules: a complaint needs 3 or more mentions across 2 or more products to be worth building on, below that a hint); **on the user's own product,** the complaints ranked by their share of the low reviews read, each turned into one concrete fix (a size chart, packaging, a clearer photo, a spec change at the factory) with the reviews that would show it worked. From the review text already read; no cost said. **When only stars were read** (US ASINs: `references/known-limits.md`), the yes offers the same products on Amazon UK and Germany with its one estimate (`complaint-brief`, step 2), and no complaint or theme is named until that text is read: the star shares are the only facts until then, and the usual causes of a 1-star bump ("a defect, a shipping problem…") aren't offered as the reason for these products either.
- **Small samples:** under about 20 reviews, say the themes are a hint, not a trend. Themes come from keyword and phrase matching, not AI, so a theme is a pointer to reviews to read, not a measured sentiment score. **Named themes are English only:** the known complaint and praise phrases ("runs small", "arrived damaged") are English, so reviews in another language (amazon.de, .fr, .es, a German Trustpilot page) give mostly recurring phrases in that language, or no themes: say so, and read the review texts themselves for what buyers complain about.
- **Loox** shows no dates in some layouts, and **Stamped** and **Loox** publish no counts per star: say so when it matters.
- When the answer quotes only some of the reviews, one plain line with the link to all of them ("Full list of the reviews: <link>") (`references/plain-words.md`); then offer the watch, with no price on the offer (its monthly estimate comes at set-up): "I can tell you each morning when these get new or low reviews."

## 4. Ongoing (a watchlist)

- **The task:** `cleanpull/watch-digest`, named `cw-reviews-<name>`, with:
  - `reviewProductUrls`, `reviewAsins`, `reviewTrustpilotDomains` (domains or `trustpilot.com/review/…` pages) and `reviewMarketplace` (at most 1,000 products and businesses together);
  - `monitorName: "<name>"` and `title`;
  - `maxRunCostUsd` (see below);
  - `alertBelowRating` (for example 3) when the user only wants to hear about bad reviews: the message then lists only new reviews under that many stars, and ratings that fell under it (`references/watchlists.md`, "Alerts").

  The digest reports new reviews (with the lowest rating among them and their top themes), the rating moving by 0.1 stars or more, the count jumping or dropping by 10% or more, and a product page removed (confirmed on a second run). A Trustpilot business is checked through its newest 5 reviews each run: more new reviews than that between runs aren't all listed, so suggest daily for busy businesses.
- **Cost per run:**
  - digest USD 0.005;
  - products × USD 0.00025;
  - each product with nothing new USD 0.0005; each with something new USD 0.003 + USD 0.0005 per new review;
  - **each Trustpilot business:** its read (provider search) USD 0.003 + its newest 5 reviews re-checked at USD 0.003 each, so USD 0.0185 with nothing new (with the USD 0.0005 check); a new review is USD 0.0035 instead of a re-check, plus the USD 0.003 summary. About **USD 0.56 a month per business daily**, USD 0.08 weekly. **Suggest weekly for Trustpilot** unless the business gets more than about 5 reviews a day (then daily, so the newest 5 cover them). It adds about 30 to 60 seconds to the digest (up to 4 businesses at a time);
  - USD 0.001 per message once a channel is added.
  - **The first run** reads each product's summary and up to 20 reviews as the baseline: about USD 0.013 per product; a Trustpilot business's summary, read and newest 5 reviews: about USD 0.024.
  - **Example:** 20 products daily, 4 of them with a couple of new reviews: 0.005 + 20 × 0.00025 + 16 × 0.0005 + 4 × 0.004 ≈ **USD 0.034 a run, about USD 1.00 a month**; the first run ≈ USD 0.27. Weekly is about USD 0.15 a month.
- **`maxRunCostUsd`:** 1.5× the typical run + USD 0.04 (room for one product's worst case, USD 0.037; with Trustpilot businesses only, + USD 0.03, for a business's USD 0.0235; `references/watchlists.md`). For the example, about USD 0.09; for 3 Trustpilot businesses daily, 1.5 × 0.06 + 0.03 ≈ USD 0.12.
- **Steps:** follow `references/watchlists.md`: show the monthly and first-run cost and get a yes, create the task, run the baseline (with `maxRunCostUsd` raised to the first-run cap in that run's input), schedule it, and say where the results go: "your briefing in Claude, on request or on a Monday schedule"; the Console link for email or Slack delivery only when the user asks for a channel (step 7).
- **The watch can share a digest** with an existing price watchlist: add the review items to its task (`watchlists` skill, "Change") instead of creating a second one, if the user prefers one message.

## 5. Reading a reviews digest later

When you explain one (the `watchlists` skill reads it):
- lead with new low ratings (1 to 2 stars) and what they're about;
- then rating moves and count jumps; a count that drops usually means the shop or Amazon removed reviews;
- a product reported removed was gone on two runs in a row: the page was taken down or moved.
