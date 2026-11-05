# Judgement: the Maker lens

Part of the judgement rules (`judgement.md` is the core). Read with `judgement-for-you.md` when the lens is Maker: the user makes what they sell ("I make it myself": handmade, small-batch, made to order in their own workshop, kitchen or studio). They are the supplier, so no factory or supplier read applies to them, and there is no first order to buy.

**Maker** (they make it themselves and sell it, usually on Etsy, their own store or both; the buyers search for handmade):

### Which marketplace is read

The marketplace **they sell on**: the one named in the question, else `channels` (`etsy`, `ebay`, `store`, `amazon` for Amazon Handmade). With no channel named, **Etsy**, said once ("read on Etsy, where buyers search for handmade; tell me if you sell somewhere else"). The read is the Marketplace lens's own (`judgement-lens-marketplace.md`, "Which marketplace is read": `cleanpull/marketplace-search-scanner`, `sources: ["etsy"]`, `maxResults: 24`, `listingRows: true`, about USD 0.10; USD 0.19 on Apify's free plan from 2026-11-07; cap about USD 0.29; up to about 12 minutes), started first. Use the words that describe their making in the keyword ("wheel thrown stoneware mug", "hand poured soy candle"), not the bare product, so the page holds more listings like theirs. Amazon's scan still runs for the market table, the same for everyone; for them Amazon's floor is one labelled context line, never their demand.

**Which country the other reads use.** Amazon's scan and Trends follow **the country they sell from**: the one they named in this chat ("a potter in Vancouver" is Canada), else the profile's `marketCountry`, else the US. Canada reads amazon.ca with Trends `geo` CA; the UK amazon.co.uk with GB; and so on for every marketplace Amazon's scan covers (a country it doesn't cover: amazon.com with US, said once). Etsy is still read on the US site ("Fees outside the US" below). The choice is made once and kept for the whole chat, so the market table never moves from one marketplace to another between answers.

**TikTok Shop, for a maker: context only, and only in the US.** The TikTok Shop read covers the US shop. It runs for a maker only when the country they sell from is the US, and then as one labelled context line, never a counted row. Outside the US it doesn't run, and the answer says so once, plainly: "TikTok Shop's read covers the US shop only, so it isn't one of your reads; it doesn't count either way." Nothing in their verdict waits on it, and its cost is left out of their cost line.

**They sell only through their own store or social pages** (`channels` `store` or `social`, with no marketplace named): no read covers their own store, so **Etsy is read as the handmade reference**, labelled as such once ("read on Etsy as the handmade reference: buyers there search for pieces like yours; your own store's buyers aren't on this page"), never as their marketplace and never silently. From it:
- **Price band:** the matching band (below), labelled "the handmade reference on Etsy", with their own price against it;
- **Margin:** after their store's payment fee, not Etsy's: the fee they gave, else a card-payment fee of 2.9% + USD 0.30, an assumption (a common Shopify Payments rate), said once; with their own unit cost (below);
- **Demand level:** `unknown` (their store's buyers aren't read); their own sales, when they mention them, are their evidence, as in the rows below;
- **Concentration:** one line of information about the Etsy page, **not counted** (they don't compete on that page);
- every other row as in the rows below. The count is the Marketplace lens's own count with these rows, and the verdict is labelled with the reference ("For you, through the maker lens, with Etsy as the handmade reference [makes it · own store · side income]").

When they sell in their own store **and** on a marketplace, the marketplace is theirs and is read as above; the store's fee is said once as a note when they mention selling there too.

### Their unit cost: materials plus time, asked once

The unit cost is **theirs**, never a factory's. Ask once, in one skippable line, in the message with the cost line (or, when the run went ahead without one, in the answer beside the margin): "What does one cost you to make: materials and packaging, and about how long it takes you? If you'd like your time counted, what would you pay yourself an hour?"
- **Materials and their hourly rate given:** unit cost = materials + hours × their rate, both shown and labelled as theirs ("USD 6.50 materials + 0.75 h × your USD 20 = USD 21.50 to make").
- **Materials only:** the margin is worked on materials, labelled "before your time", and the time they gave is said in hours beside it ("USD 14.10 left after fees and materials, for about 45 minutes of your time"), so they can see what an hour earns them: that figure ÷ the hours, labelled as such.
- **Nothing given:** the margin is `unknown` ("needs your making cost"), never scored on a factory price, a guess or a typical figure for the craft. Never an hourly rate, a material cost or a wage from memory.
- Like an exact budget, their making cost is used in this chat only: never stored, never put in a run's input, never saved to the notebook.

### Their price band: listings that match what they make

The marketplace summary's percentiles cover every organic result, and a handmade search mixes in printed, print-on-demand and factory-made versions, sets and other products. For a maker, **the band comes only from the listing rows that match their product**, checked against each title (and the shop name where it says so):
- **kept:** the same product made the same way and of a similar size (for a wheel-thrown stoneware mug: "handmade", "wheel thrown", "stoneware", "pottery", "ceramic" with a handmade word);
- **set aside, and named with a count:** printed, personalised-print or print-on-demand versions ("custom photo mug", "sublimation", "printed"), factory or mass-made ones, a different material, sets and multi-packs (unless they sell sets), supplies or kits, and other products;
- **recomputed** from the kept rows: the cheapest quarter, the median and the top quarter of their prices, said as recomputed ("from the 14 of 24 listings that are handmade stoneware mugs; 8 printed mugs and 2 sets were left out").

With **6 or more** matching rows, the band is scored on the usual Price band thresholds. Under 6, the Price band is `unknown` ("too few listings like yours to set a band"), with one rerun offered at `maxResults: 48` with `listingRows: true` and a more exact keyword (about USD 0.19; USD 0.35 on Apify's free plan from 2026-11-07; cap about USD 0.52). The summary's own band may be said once, labelled as covering every result, never as theirs.

### The rows, for you

| Row | For you | Reads from |
| --- | --- | --- |
| Every market row | **same** as in the table, except as below | the table |
| Demand level | **replaced** by their marketplace's, which is `unknown` on Etsy and eBay (neither publishes sales). Amazon's floor is one context line, labelled, not counted. **Their own sales, when they mention them** ("it outsells everything", their Etsy stats), are their best demand evidence: one line of information, labelled as theirs, never scored as a market figure | their marketplace; Amazon `salesFloor` as context; the user |
| Concentration | **replaced** by the top 3 shops' share of the **matching** listing rows (10 or more, else `unknown`, "sample too thin to score"), on the top-3 share thresholds only | matching listing rows |
| Price band | **replaced** by the matching band (above); their own price, when given, against it | matching listing rows |
| Margin | **replaced**: after their marketplace's fees (`marketplaceFees`), with their own unit cost (above); `unknown` until they give it | their cost, the read's fees |
| The market table's Margin row | **their own unit cost stands in for the supplier cost**: no supplier read runs for them, so the market's Margin row is worked out on the market's fees (as for everyone) with their making cost in the supplier cost's place, labelled ("Margin if sold on Amazon, after its fees, on your making cost"); `unknown (no supplier read: you make it; needs your making cost)` until they give it, never a factory price, a guess or a typical figure. It is scored and counted in the market verdict like any Margin row ("Settled early" included) | their cost, the market's fees |
| TikTok Shop | **context only, not counted**: read only when they sell from the US, as one labelled line; outside the US not read, and said once ("Which country the other reads use") | the TikTok read, US only |
| Quality gap, Review depth, Paid pressure | **not counted**, as in the Marketplace lens on Etsy or eBay (Amazon's ratings and ads aren't their buyers'; Etsy's reviews are the shop's) | the table |
| Demand trend | **same**, and its peak month is one line of information for making ahead ("searches peak in November: start making in September") | Trends |
| Supplier rows, first order, MOQ, single units | **not read, not counted**: they are the supplier. No factory or supplier read runs for them, and there is no first-order gate or MOQ-1 gate | none |

**This lens uses the Marketplace lens's own count** (`judgement-lens-marketplace.md`, "On Etsy or eBay, this lens uses its own count"), with the rows above, and maps it the same way (Strong → "a strong fit"; Promising → "a fit, with one fix"; Not this version → "not this one", naming its rows). The one cap carries over (Amazon's floor under 1,000 a month: at most "a fit, with one fix", the fix a small demand test on their marketplace), **except when they already sell this product**: their own sales are that test, so the cap doesn't apply, and the line says so ("you already sell it, so your own sales are the demand test"). A failed gate still makes "not this one" as in every lens; the counterfeit gate is the only gate that applies to a maker (`judgement-for-you.md`, "Counterfeits").

**Making time, when they gave hours a week** (`timePerWeek`): one line of information, never a gate: the units a week their hours allow at the time per piece they gave ("about 20 mugs a week at 45 minutes each in 15 hours").

### Fees outside the US

Etsy's `marketplaceFees` are US sellers' rates in US dollars, and Etsy is read on the US site, in US dollars. For a seller whose bank account is in Canada, the payout uses Etsy's Canadian rates from `judgement-rates.md` ("Etsy fees for sellers in Canada"), and the answer says the listing prices read are US-dollar prices: their own CAD price and costs are compared only in CAD, with their rate for any conversion (`judgement.md`, "Mixed currencies"). Other countries: say the fees are US sellers' rates, and that Etsy's fee page for their country gives theirs.

### The fairness line

Every maker's first For you block in a conversation carries one plain line on fairness to other makers, and any time they ask ("is this fair to other makers?", "am I stealing?"), it is the answer, first:
> "Is it fair to other makers? Reading shops' public search pages is what any shopper browsing sees, and pricing your own work at a price that sustains it is fair, not a price war. Copying another maker's design, photos or listing words isn't fair, and MarketMage never copies designs or photos and never downloads or analyses them: it reads prices, counts and titles, and a result may carry a link to the listing's image."

Said once, plainly, with no lecture and no comment on the user. It never moves a verdict.

### Worked example

- **Etsy, a wheel-thrown speckled stoneware mug** (illustrative figures): the Etsy read gives 24 listings; 14 are handmade stoneware mugs from 12 shops, and 8 printed mugs and 2 sets were left out. Their band: USD 32.00 to 48.00, median USD 38.00 (the summary's band over every result, USD 18.00 to 42.00, isn't theirs). The top 3 shops hold 4 of the 14 (0.29, favours). Demand: `unknown` on Etsy; "on Amazon, at least 900 a month" as context; "you said it outsells everything in your shop" as their evidence, so no cap. Margin at their USD 40.00: 40.00 − (9.5% + USD 0.45) fees = 35.75; − USD 7.00 materials = USD 28.75 before their time, about USD 38 an hour at 45 minutes a mug. No supplier read, no first-order gate. "For you, through the maker lens, on Etsy [makes it · Etsy · side income]: a strong fit." Then the fairness line.
