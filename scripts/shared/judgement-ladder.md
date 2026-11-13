# Judgement: related versions and watches

Part of the judgement rules (`judgement.md` is the core). Read once the verdict is known: the ladder for any verdict short of Strong, the watch for every verdict, the next move for every answer that judges, and each idea's own evidence when ideas are ranked.

## Related versions: the ladder

For any verdict short of **Strong**, give 2 or 3 related versions that stay in the user's direction: the same customer, the same category, or the same mechanism they were excited about. Walk the rungs in this fixed order and use the first ones the data supports (one exception: the cold-traffic lens's long-shot channel switch, `judgement-lens-cold-traffic.md`, comes first when its numbers hold):

1. **Angle:** a rising related search (`relatedQueries_rising`) for the same product or customer ("magnetic fidget slider, +250% in rising searches"), never from a low-volume term (`judgement.md`, "Low-volume Trends terms").
2. **Segment:** a premium version priced above `priceP75` with a difference a shopper can see (size, material, a feature the leaders' 1-star reviews ask for), or a buyer group the rising searches name ("for dry eyes").
3. **Bundle:** the product with the accessory or consumable buyers already pair it with, priced as a set, where the price band leaves room.
4. **Marketplace:** the same product on another marketplace or country whose read differs (a higher Etsy median for a handmade version, an Amazon country with thinner reviews).
5. **Channel:** the same product sold where the leaders aren't (TikTok Shop units when Amazon page 1 is ad-heavy; the user's own store or audience; search ads or a marketplace listing when Amazon's floor shows buyers searching for it but the feed shows little impulse demand).

For each version:
- **Name the fact that makes it promising,** from rows already read (a number, never a guess). A rung with no supporting fact in the data is skipped, not invented. If no rung has a fact yet, name the cheapest read that would find one (for example the Trends rising searches) and offer it.
- **Say what stays the same** ("same buyers, same factory").
- **Offer the best one for a check now:** for example `validate` on it, reusing this conversation's rows where they apply (`running-runs.md`, "Runs in this conversation"), or a `market-scan` summary. This offer is the answer's "Next step".
- **After Not this version, the free stop:** the answer's last line may instead be "Next step: nothing to buy; keep the USD <X>.", with this offer kept as a follow-up (`judgement-answer.md`, "A free "stop here" is a next move too").

A **Promising** verdict also gets the ladder, shorter (1 or 2 versions), after "the one fix". A **Strong** verdict skips the ladder unless the user asks for options; it gets its watch instead.

## Watches: risks as early signs

Every verdict names its biggest risk as **the early sign** to look for, not as a warning: "The early sign would be ad slots climbing past 12 in 48: today it's 4." Then offer the watch that would catch it, with no price on the offer (its monthly estimate comes at set-up, with the yes: the skill that runs it and `costs.md`; the figures below are for that estimate), and never create it without a yes (`watchlists.md`):

| Risk the data points to | The early sign | The watch to offer |
| --- | --- | --- |
| Newcomers crowding page 1; review depth closing | new sellers entering the top results | a `market-scan` watch for new entrants on the keyword (`cw-market-…`; 1 keyword on Amazon US weekly, about USD 0.04 a month; on eBay, Etsy, Walmart, Target or Best Buy about USD 0.165 a run, about USD 0.72 a month weekly, since each run reads 48 results there) |
| Paid pressure rising; a price war | ads, or the price band moving down 10% or more | the same market watch (price-band moves), or `price-watch` on the 5 leaders |
| Demand cooling, or a seasonal peak | TikTok units per day slowing; chart entries thinning | the TikTok sales-per-day watch (US; 1 keyword weekly, about USD 0.28 a month) or the Amazon chart watch (`find-products`) |
| The quality gap closing | the leaders' ratings and new reviews improving | `reviews-watch` on the 3 leaders |
| A rival copying the angle | the angle's keyword gaining ranked rivals | `rank-watch` on the angle's keywords |

One watch, the one that matches the biggest risk. On a Strong verdict, this watch is the natural next move.

**After Strong or Promising, the launch plan.** When the verdict is Strong or Promising, or the user says they want to go ahead, offer the launch plan (the `launch-plan` skill: suppliers at their first-order quantity, the leaders' complaints, a listing draft, price position, first-order maths and a launch-week watch) as one of the follow-ups, with no price (its estimate comes at the yes).

## The next move: the step that settles the biggest unknown

(Tester review of 0.4.21: the heated eye mask's next step was a paid read, while what decided its verdict, what a click costs, was a free five-minute look-up in the user's own ad console.) The Next step is **the one step that most reduces the verdict's biggest unknown**, whether or not MarketMage makes it and whether or not it costs anything:
- **The biggest unknown, in this order:** the unmeasured input the verdict confidence names (the launch ad cost per sale, a click price, freight: `judgement.md`, "Confidence"); else the `unknown` signal or unread gate that would change the label; else the early sign that would ("Watches").
- **The step that measures it:** a free step the user can take now comes first when it settles more than a paid read: the suggested bid for the main keyword in their Amazon ad console (Sponsored Products), a freight quote from a forwarder, a sample. Say its time, never a price, and what each result means, with the deciding numbers worked from this check: "Next step: look up the suggested bid for 'heated eye mask' in your Amazon ad console, about 5 minutes: if 1 in 10 clicks buy (an assumption), a bid under about USD 0.50 keeps ads under about USD 5 a sale, where it works; over about USD 1.20 a click, it loses money." A bid is the click price; the sale's ad cost is that ÷ the share of clicks that buy (`judgement-answer-checks.md`, "The margin and the launch ad cost").
- **One move, then at most two "After that" items,** in the same Next step line, in order, with no price on any: "Next step: <the move>. After that: <one>; <two>." A paid read moves to "After that" when a free step settles more (the leaders' complaints, a related version's check, a watch); the follow-ups and the offer line are unchanged.
- **When nothing unmeasured holds the verdict** (verdict confidence high, nothing `unknown` that could move the label), the move is as before: the best related version's check, the fix's test, or after Strong the watch. The free stop ("nothing to buy; keep the USD <X>") still applies after Not this version.

## Each idea's own evidence, and the order of ideas

(Review of 0.4.13, `find-products`: the automatic laser toy had the most TikTok sales, the longest-running ads and a single-unit AliExpress offer, yet ranked third or fourth in every run read. Trends had no series of its own for it, so it got no trend, or the handheld laser pointer's −28% was set against it, and the rows were ordered by for minus against before the sources backing them. The owner's 0.4.11 design: "Multi-source backing ranks higher and is said per idea".) In any answer that ranks several product ideas (`find-products`, a side-by-side of ideas):

- **A trend belongs to the idea it measures.** An idea's Demand trend is its own Trends series: the term that names that product. When Trends has no series of its own for it, a rising search in the rows that names its own product ("automatic cat laser toy", +180%) is its trend reading (rising), with "from a small base" where `judgement-first-answer.md` says so; with neither, its trend is **not read** (`unknown`): no point for or against, and it is said as not read, never as falling.
- **Another item's trend never counts for or against a different idea:** a neighbouring product ("cat laser pointer", the handheld kind, beside an automatic laser toy) or the category's broad term ("interactive cat toy" beside a rolling ball) is context for the ideas under it, never their for or against, never their what-holds-it-back cell, never their backing source. Where it helps, one clause says it is a different item ("handheld pointers are down 28%; this is the automatic kind").
- **Favour group first, then more independent backing.** Ideas are ordered by favour group (`judgement.md`, "The verdict rule"): the ideas the data favours lead, then the mixed ones, then the ones the data is against. Within a group, by how many independent sources back each one (each source counts once, however many rows, listings or stores show it: two stores' ads are one source), more first; the for/against tally breaks a tie in that count, then the demand number. Within a group, one strong number from a single source never lifts an idea above one that more sources back; across groups, backing never moves an idea above a better group, so the opening's lead, the top row and the count line ("2 of 8 the data favours") agree. A listing that only shows the product can be bought (an AliExpress row under 100 sold, 0 or null) is not a backing source. With a profile the For you label leads the order, and the backing count comes right after it, before the lens's own count; in a lens, backing counts only the sources behind the rows that lens counts (a search trend or chart rank the lens takes as context never adds to it).
- **Check before sending:** count each row's backing sources again from its own cells; among ideas with the same label (with a profile) and favour group, the higher row has as many or more (or ties and wins on the tally, then demand), and the opening's lead is the top row.
