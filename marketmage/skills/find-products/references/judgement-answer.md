# Judgement: answer structure

Part of the judgement rules (`judgement.md` is the core). Read before writing a verdict.

## Answer structure

**The first screen comes first,** in about 150 words at most: the verdict lines, one plain line, what you got right, the one fix (Promising), the best related version (Not this version) or what must stay true (Strong), and the next step with its cost. A user who reads only that much has the answer. The signal table and the detail follow under it; nothing is dropped, only moved below.

With a profile, the first screen opens with two verdict lines, "For you" first:

```
**For you: a fit, with one fix** [$1k–5k · own stock · side income] · the first order is USD 960, within your up-to-$5k budget; the fix: the Trends peak in December (stock for one season)
**For the market: Promising, with one fix** · high confidence · 4 for · 2 against · 1 neutral
```

**Both verdict lines name their move, and never read as a contradiction:**
- "a fit, with one fix" and "Promising, with one fix" each state their fix on the first screen, in a few words (`judgement.md`, "The fix is named wherever its label is"). When the For you verdict leads with another move (a long shot's test, the related version for "not this one"), the market's fix still gets its one line ("The market's one fix: <it>").
- **When the two verdicts differ,** the one sentence that says why (`judgement-for-you.md`, "Guardrails") names the row that makes the difference and how it counts for them: "Promising for the market (4 for, 1 against); for you, a long shot, because the one against, demand on amazon.co.uk (at least 300 units a month across the top 10), is the only place you'd sell." A long shot is never introduced with words that read as a fit ("Nothing I read stops this working for you, but…"): its first clause is the thin demand, with its numbers, and no later line beside it says nothing else stops it (say what would turn it instead).
- **A user's direct question comes first,** above both lines, answered in plain words (`judgement-tone.md`, "Answer the user's question first"); the verdict lines follow it.

Without a profile, the market line leads, labelled the same way. Only when the profile hasn't been offered yet in this conversation ("Asking for the profile"), the first screen adds one friendly line before the next step: "Tell me roughly your budget and how you'd sell (5 quick questions, or skip) and I'll say what this means for you."

```
**For the market: Promising, with one fix** · high confidence · 4 for · 2 against · 1 neutral
One plain line: what the data says, in its two biggest numbers.

What you got right   (only when a number backs it; at most two lines)
  You were right that demand is rising: +38% over 5 years.
The one fix: <the against signal that matters most and what would turn it>.   (Promising)
  or: The best related version: <the rung, with its fact>.                    (Not this version)
  or: What must stay true: <one line>.                                         (Strong)
  or: What would have to be true: <one line>. The cheapest test: <it>, about USD <cost>.   (For you: a long shot)
  or: Sell it where people search: <Amazon floor> vs <best TikTok listing>; <the channel>. What would have to be true … (For you: a long shot, cold-traffic, search demand real)
Next step: <the move>, about USD <cost>.
  or: Next step: nothing to buy; keep the USD <X>. Or <the best related version>, about USD <cost>.   (the free stop: Not this version, or For you: not this one)
                                              ── end of the first screen (~150 words at most)
What the data shows
  Demand trend   rising, +38% over 5 years, peak Nov–Dec        favours (≥ +15%)
  Review depth   median 3,400; 2 of 48 under 100 reviews        against (> 3,000; ≤ 2 of 48)
  …

What it means (for any seller)
  Two sentences on the shape of the market.

For you, through the <lens> lens   (only with a profile; see "The For you block")
  The lens lines: each row that counts differently, and each gate, with its fact.
  Fit check: first order · fulfilment · ad cost · skills, each with its number.

The one fix, in detail, with its test and cost (Promising)
Related versions, in your direction           (Promising: 1 or 2; Not this version: 2 or 3)
  1. Angle: "xl silicone lids", +250% in rising searches. Same buyers, same factory.
  2. …
The early sign, and the watch that catches it (every verdict)

What this can't see: one line (rule 9).
This research cost about USD <cost>.
Next step: <the same move as on the first screen>, about USD <cost>.   (one short line)
  or, after the free stop on the first screen: the same free stop line, with the related version and its cost.
```

- Tables stay under 10 rows. Numbers live in the table; prose repeats at most the two that carry the point.
- "What you got right" credits only something the user said in this conversation, with the data's number beside it, and for a user who doesn't sell on Amazon never an Amazon FBA figure (`judgement.md`, rule 5). Nothing they said is backed: the line is left out.
- The whole reply is sized to the question (`judgement-tone.md`, "Size the reply to the question"): the first screen at about 150 words, the rest in its shortest form.
- Asked a yes/no question ("is it saturated?"), the verdict line still comes first, followed by the one-line opposite answer (rule 3), inside the first screen.
- The last line is always the next move, never the verdict: the first screen's next step, repeated in one short line.
- **The free stop is a next move too** (`judgement.md`, "The one exception, the free stop"): after Not this version, or For you: not this one, the next step may be "nothing to buy; keep the USD <X>", with the best related version and its cost on the same line, so the answer still ends in a move in their direction.

**Two framings, same data, same verdict:**
- "Is this worth selling?" → "**For the market: Promising, with one fix** (medium confidence): 4 for, 2 against. You were right that demand is rising: +38% over 5 years. The fix is getting off a crowded page 1: the median listing there has 3,400 reviews, and 12 of 48 slots are ads priced under the organic p25. The 'XL' angle the rising searches point at (+250%) is where the same buyers are heading, priced above p75 with the size as the difference. Next step: a market scan of 'xl silicone lids', about USD 0.017."
- "Is this saturated?" → "**For the market: Promising, with one fix** (medium confidence). 2 signals say crowded (review median 3,400; 12 ads in 48), 4 say open (demand +38% over 5 years, 3 leaders under 4.2 stars, top-3 share 0.31, margin after fees 48% of the median price). Crowded on page 1, not closed: the leaders' quality gap is the opening a newcomer can build on."
