# Launch plan: on-demand steps

The parts of the `launch-plan` skill read only when they apply: hours a week for a side income, Etsy, eBay or a maker, an exact amount the user gave, reading the test against the agreed stop rule, and the launch-week watch. Everything else is in `SKILL.md`.

## Hours a week

- **Hours a week, for a side income** (optional, one line): when the goal is a side income (the profile, or they say so) and they haven't said how much time they have, ask in the same message as the plan, skippable, nothing waiting on it: "Roughly how many hours a week can you give it (under 5, 5 to 15, 15 to 30, more)?" It is the profile's `timePerWeek` (`references/judgement-profile.md`), asked here once because a launch is where time decides: under 5 hours, the plan says which steps take weekly time (content for TikTok or own-store ads, restocking, answering buyers) and favours the lighter route (Amazon FBA or a marketplace listing over daily content), as one line of information, never a gate. Not asked again when it was answered or skipped in this chat.

## Etsy, eBay or a maker

- **Etsy or eBay:** that marketplace's fees (`marketplaceFees`), a listing draft for it (title and the description's opening lines, with Etsy tags as short phrases buyers type, from the rising searches and the matching listings' titles), and the test is a listing's first weeks (the listing fee, plus any ads they choose), read against the same stop-rule thresholds as Amazon ads when they run Etsy or eBay ads.
- **A maker** (`references/judgement-lens-maker.md`): no supplier step (step 1 is left out, said once: "you make it, so there's no factory to contact"); the "first order" is their first batch, at their own making cost; the plan's per-unit maths uses their marketplace's fees and that cost.

## An exact amount

**An exact amount given in this chat** (kept privately: `references/judgement-profile.md`, "Privacy, unchanged"): the goods are about half of it (a rule of thumb, said as such), rounded down to USD 100, 200, 300, 400 and so on, instead of the band's figure, and the stop rule's test spend is capped at about a quarter of it (below, "The test spend and length"): goods plus test spend leave about a quarter for freight, samples and fees. This is the same room the fit check leaves for freight, samples, fees and launch ads (`references/judgement-lens-own-stock.md`, "Against the amount you gave me"), so the plan and the fit check agree. Say the goods as the planning figure, never the amount or how it was worked out from it ("about USD 300 of goods, leaving room in the amount you gave me for freight, samples, fees and launch ads"). When half of it is under USD 100, or even the lowest-MOQ offer's cash is over half of it, say so in those words and plan from the smallest real offer (a lower-MOQ offer row, or AliExpress at MOQ 1).

## An exact amount: the test spend

**With an exact amount given in this chat,** the test spend is the lower of the band row and about a quarter of the amount (a rule of thumb, said as such), rounded down to USD 25; the length stays the band row's. Say it as the planning figure, never the amount or how it was worked out from it ("about USD 75 of ads, or 7 days, leaving room in the amount you gave me for freight and samples"); the note's test spend band word comes from that figure. The fit check's ad line uses the same figure.

## Reading the test against the rule

**Reading the test against the rule.** When the user pastes their ad numbers ("spent 160, 2,400 visitors, 31 add-to-carts, 4 sales"; an Ads Manager or Amazon ads export), read them against the stop rule agreed in this chat or saved in their notebook (the `test` decision entry's note), with no run and no cost:
- **One line per rule line, their number beside its threshold:** spend and days against the test spend and length; add-to-cart against 2% and 5% (own store or TikTok Shop), or orders against 5% of clicks with at least 100 clicks (Amazon); click-through against 1.5% (own store) or 0.5% and 0.3% (Amazon); cost per sale against what a sale leaves after the unit cost and fees (from the first-order maths). Work each rate out from their counts, with the sum shown ("31 add-to-carts ÷ 2,400 visitors = 1.3%, under 2%").
- **Then the rule's own call, in one word and the line that decides it:** **keep going** (add-to-cart 5% or more and sales cover their ad cost), **change** (curiosity, not intent: the one change the rule names, the offer or the page, or for Amazon the price or the listing), or **stop** (the rule's stop line met: on Amazon, no reorder, sell through the first order). Before the spend or the days are reached, say how far in they are and that the rule reads at the end, with the numbers so far as information only.
- **Between the lines** (own store or TikTok Shop: add-to-cart from 2% up to 5%, with click-through at 1.5% or less): the rule doesn't call it; say so, with their numbers, and that running the same spend again is their call.
- **Missing numbers:** read what they gave, and name the one number the rule still needs ("add-to-carts" from Shopify's analytics, "orders" from the Amazon ads report). Never fill a number in, and never forecast what the next days would show.
- **No rule agreed yet:** set it first from the band (above, no cost), ask them to agree it, then read the numbers against it. Their numbers never change the agreed thresholds after the fact; a threshold they change now is said as changed.
- With the notebook on, a call they then state (`park`, `drop`, or carrying on) is noted as `references/notebook-use.md` sets out, only when they say it; the reading itself is not a decision.

## The launch-week watch

One Watch Digest task that watches the market they're entering, daily, through launch (`references/watchlists.md`):
- **Input:** `cleanpull/watch-digest` with
  - `amazonAsins`: the 5 leaders, `amazonMarketplace` (price, Buy Box and stock moves);
  - `rankKeywords`: 3 keywords (the scan's keyword and the two rising searches closest to the difference), `rankAsins`: the 5 leaders (add the user's own ASIN once it's live: `watchlists`, "Change"), `rankMarketplace`, `rankSponsored: false` unless they want ad places;
  - `reviewAsins`: the 5 leaders, `reviewMarketplace` (new reviews and rating moves);
  - `monitorName: "launch-<idea>"`, `title`, `maxRunCostUsd`.
- **Cost per run, daily** (`references/costs.md`): digest USD 0.005 + 25 items (5 ASINs, 15 keyword × ASIN pairs, 5 review ASINs) × USD 0.00025 + 5 unchanged ASINs × USD 0.0005 + 3 keywords × USD 0.002 organic (USD 0.008 with ad places) + 5 review checks × USD 0.0005 + a few changes ≈ **USD 0.03 a run, about USD 0.95 a month daily** (with ad places about USD 0.05 a run, USD 1.40 a month). The first run reads everything (5 ASINs at USD 0.003, 15 ranks at USD 0.001, 5 reviews summaries with their top reviews at about USD 0.01 each) ≈ **USD 0.10**. Launch weeks are when daily matters; suggest weekly after (about USD 0.13 a month).
- **`maxRunCostUsd`:** 1.5× a typical run + USD 0.04 (room for one reviews item), about USD 0.09; the baseline run uses about USD 0.19.
- **Steps:** show the first-run and monthly figures and get a yes, then create the task, run the baseline, schedule it, and say where the results go: "your briefing in Claude, on request or on a Monday schedule"; a channel only when the user asks for one (`references/watchlists.md`, step 7). Never create it without the yes.
