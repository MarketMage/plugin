# Judgement: the checks before an answer is written

Part of the judgement rules (`judgement.md` is the core). Read in the same batch as `judgement-answer.md` and `judgement-first-answer.md`, before writing any answer that gives a verdict or a label. From the real-user test on claude.ai of 8 Nov 2026 (round 3b); where an older line elsewhere says otherwise, this file wins.

## The answer-time reads are required

(R3-18: "shud i sell those led face mask thingys on amazon? … just tell me yes or no" read only `judgement.md` and `known-limits.md`, skipped the answer files, and so gave a full table to someone who asked for a yes or no, and left out the regulated-product line an LED therapy mask needs.)
- **Before the first word of an answer that gives a verdict or a label,** the answer-time parts the skill names must have been read in this conversation: for `validate`, `find-products` and `market-scan`, `judgement-answer.md`, `judgement-first-answer.md`, `judgement-ladder.md` and this file (with `judgement-timing.md` on a timing question); for `suppliers` and `gaps`, `judgement-answer.md`, this file and `running-results.md`. Other skills that read `judgement.md` (`briefing`, `launch-plan`, `start`, `complaint-brief`) read only the parts their own steps name.
- **Any not yet read are read then,** in one batch of parallel reads, before writing. The answer's shape, its required lines and its labels are in them: an answer written without them is wrong, however right its numbers. A part already read in this chat is not read again.

## Where these parts sit in the answer

**Where these parts sit in the answer** (`judgement-answer.md`, "The short default, and the full detail on request"): the short default carries the table (rule 1), the scores (rule 2), the credit (rule 5), the next move (rule 6), the verdict lines (rule 7), the best related version or the one fix (rule 10) and, for a yes/no question, the one-line opposite answer (rule 3). "What it means" (rule 1), the early sign and its watch (rule 3), the full ladder (rule 10) and what the data can't see (rule 9) are in the full detail, except that for a yes/no question the one-line opposite answer (for "is it worth selling?", the early sign with today's number) stays on the first screen (`judgement-answer.md`, "Answer structure"); its watch offer waits. The rest is offered in one line, unless a caveat changes the verdict or its confidence: that one line stays in the default. **No notes block under the table in the default:** caveats that don't change the verdict (list prices, not quotes; an assumed fee or rate; a comparison term that came back different; rows kept as close cousins) and a one-sentence policy step ("Before listing: …") are full detail too; only an exclusion or mismatch line, suspicious text and a verdict-changing caveat sit under the table by default.

Also under the table by default: a cross-check that fires and a regulated product's one line (`judgement-first-answer.md`).

## The margin after freight and launch ads

(Tester review of 0.4.21: heated eye masks at USD 28.99 on Amazon US scored "helps" at 49% after fees and read **Strong**, high confidence; after USD 1–2 of freight and USD 8–12 of ads a sale they leave USD 0–5. Approved 13 Nov 2026: score the margin a launching seller keeps.) The Margin row (`judgement.md`) is scored after three things come off what a sale pays out after fees:
- **The unit cost,** as before (the user's quote or landed cost, else the factory offers that are the idea).
- **Freight and duty,** only on a factory price (Made-in-China, Alibaba) with no landed cost given: **15 to 30% of the unit cost**, an assumption (a planning range for sea freight and duty on a small item from China), said once with "a freight quote replaces it". None on a cost that is already landed (the user's landed cost, an AliExpress `landedPrice`, a DHgate estimate) or for a maker; an AliExpress price before shipping stays "plus shipping, still to add". An own-store seller's shipping estimate per order (`judgement-rates.md`) is separate, and stays.
- **Launch ads: USD 8 and USD 12 of ads per sale,** the cold-traffic lens's range, the same assumption on every channel (on Amazon, the sponsored-ads cost of a sale while a new listing has no organic rank). Ad cost per sale = price per click ÷ share of clicks that buy: USD 0.80 a click with 1 in 10 clicks buying (both assumptions) is USD 8 a sale. In another currency, the same numbers in it (€8 and €12, £8 and £12).

**Framed fairly to Amazon.** Not every Amazon sale comes from an ad: as reviews and organic rank build, ads buy a smaller share of sales and the ad cost averaged over every sale falls. So the allowance is said as **the launch ad cost per sale**, a planning range for the months when most sales are bought with ads, never as what every sale costs for good; the before-ads margin is what the margin rises toward as organic sales take over. The launch is what the first order has to survive, so the launch is scored.

**Scored and said:**
- **Scored:** the margin at **USD 8 of ads**, with freight at the top of its allowance (30%), on the same thresholds (40% or more favours, under 25% against).
- **In the Margin row's cell:** the before-ads margin as context, then the margin at both ad costs, in one line: "USD 28.99 − 8.71 fees = 20.28; − 6.10 unit cost − 1.83 freight (30%, an assumption) = 12.35 before ads (43%); − USD 8 to 12 of launch ads = 4.35 to 0.35 a sale (15% to 1%)".
- **The user's own figures replace the assumptions,** labelled as theirs: an ad cost per sale, a click price with a conversion rate, an ACoS, a share of sales from ads, a freight quote. **A seller who won't pay for traffic** (organic only, or an audience of their own that buys, said in this chat) gets the row scored before ads, with "no launch ads, as you said" in its cell.
- **Dropship and cold traffic** keep their own sums (`judgement-lens-cold-traffic.md`), which already carry USD 8 and 12 of ads; no freight allowance on a landed cost.

**The break-even ad cost per sale: the deciding number.** Whenever ads are part of the launch (every channel, unless the user says they won't advertise), the answer reports **the break-even ad cost per sale**: the profit per unit after fees and freight, before ads (USD 12.35 above). It needs no ad assumption: it comes from measured fees and costs (the freight allowance labelled when used). Beside it, **the ad cost that keeps a healthy margin**: the break-even less 25% of the price (12.35 − 7.25 = 5.10), the point where the Margin row stops reading against. Spoken rounded down to the dollar ("about USD 5", "about USD 12"); the cents stay in the row. Where they sit: in the Margin row's cell, and in the verdict sentence only when ad cost decides it; never a note of their own under the table (the short default's limits: "Where these parts sit in the answer").
- **When the ad cost decides the verdict** (the margin is `against` at USD 8 of ads but not before ads, and that row keeps the label from the next one up; or the label is Strong at USD 8 and the margin is `against` at USD 12): the break-even is **the deciding number**, on the first screen with the fix: "**For the market: Promising, with one fix**: it works if ads cost under about USD 5 a sale, and loses money over about USD 12." The fix is that ad cost; the verdict confidence drops one step (`judgement.md`, "Confidence").
- **The arithmetic, when asked,** one step a line: the payout, the unit cost, the freight, the break-even, then "ad cost per sale = price per click ÷ share of clicks that buy: USD 0.80 a click with 1 in 10 buying is USD 8 a sale (both assumptions)". Every click price and conversion rate is labelled an assumption or the user's, never presented as measured.

## A yes or no asked for

"Just tell me yes or no", "yes or no?", "no essay", "short answer please": the shape the user asked for wins (`judgement-answer.md`, "Size the reply to the question"), in about 80 words and never past 120 (live runs of 0.4.7's first draft gave 190: three sentences of reasons, a "what must stay true", the profile offer):

**A verdict asked for is not this shape.** "Tell me it's a yes", "I need this to be a yes", "say yes": that is a verdict asked for, and it gets "When the user wants a verdict, or pushes back" below: the acknowledgement, the verdict with its counts, the table, the thresholds between it and Strong, and the best related version. The yes/no shape is only for a user who asks for brevity, never for one who asks for a particular answer.
1. **The plain answer, one sentence,** its first word set by the label (with a profile, the For you label): **Strong** or **a strong fit** → "Yes:"; **Promising, with one fix** or **a fit, with one fix** → "Yes, if <the fix>:"; **Not this version**, **a long shot** or **not this one** → "No, but <the best related version>:" (the search never dead-ends: `judgement.md`, rule 10). Then the one or two numbers that decide it.
2. **The verdict, one sentence:** its label, word for word (with a profile, the For you label first, then the market's), with its verdict confidence in a few words; when ad cost decides it, the deciding number once, in the plain answer ("Yes, if ads cost under about USD 5 a sale; it loses money over about USD 12:"), and the Next step's thresholds in a few words, all within the 120 words (and "some data missing" when the data is partial); the one fix or the best related version only when the label carries one, in a few words. No counts list (the counts wait for the table), no "what must stay true".
3. **Only the lines that always reach the user, one short sentence each, two at most:** a regulated product's line (`judgement-first-answer.md`, "A regulated product gets one line before ordering") first, then the one that matters most of an exclusion or mismatch, a caveat that changes the verdict and a cross-check that fires (the rest wait for the table). The regulated line is never dropped for brevity: it is part of the yes.
4. **One short offer line,** "Want the table and the details?", then the Next step line, last, in a few words. The profile's offer waits for the next answer here (it is still the one offer for the chat).

No table, no For you block beyond its verdict line, no "What you got right" (unless it is the reason itself), no headings, no bullets. The same data gets the same label as in the full answer; only the shape is shorter. For example (73 words):

> **Yes:** the LED masks in Amazon's top 10 sell at least 6,500 a month, and searches are up 51% over 5 years.
> **For the market: Strong** (low confidence: only 4 of the top 10 were LED masks).
> Before ordering, check the supplier model's FDA status, Amazon's approval for the category, and the skin claims a listing can't make.
> Want the table and the details?
> Next step: more factory prices for LED masks only.

## One peak, said the same way everywhere

(R3-19: the table said searches "peaked April 2026", and the text under it said "Searches peaked last December, and that's under 90 days away".) One demand statement per idea (`judgement-first-answer.md`) covers its peak too. An answer names **at most one peak per idea**, read from the Trends `interestOverTime` points, and every place that mentions it (the table's trend cell, the 90-day line, the timing line, the prose, a later turn) names the same month:
- **Read the peak from the series, year by year** (tester review of 0.4.21: a heated eye mask answer said searches peak in April, while the 5-year data peaks every December; a one-off spring 2026 surge made April 2026 the single highest week). The series is the row's `interestOverTime_timelineData` (5 years of weekly points, each with `date` and `value`); read it from the row, never from the status message; when the row is too long to come back whole (cut short, or saved to a file), read that term's series with `apify-api-read`: `https://api.apify.com/v2/datasets/<id>/items?offset=<the term's position, from 0>&limit=1&fields=interestOverTime_timelineData&unwind=interestOverTime_timelineData&omit=time,formattedTime,formattedAxisTime,formattedValue,hasData,isPartial`. Unread, no peak month is named. For each **complete calendar year** in it, note the month holding that year's highest week; the month that tops the most years (at least 2) is the yearly peak. `summary.peakDate`, and the status message's "peak N on <date>", are only the single highest week; the latest 12 months alone are one year, never the pattern. The part-year at the end can give a one-off high, never the yearly peak.
- **A yearly peak** (the same month or season is the highest of its year in at least 2 of the years read) is "the peak", said as "peaks every <month>". It is the one the seasonality cross-check and the timing line use ("the yearly peak, December, is under 90 days away").
- **No yearly peak:** the single highest point (`summary.peakDate`) is said as "highest in <month year>", and no 90-day line is written: a one-off high doesn't come round again.
- **Both, in different months** (a one-off high in April 2026, a yearly peak every December): the yearly peak is "the peak"; the one-off high, only when it matters, is a separate plain fact ("a one-off high in April 2026"), never called "the peak" or "peaked".
- **Check before sending:** the table and the text each name the same peak month, or one of them names none. Two different months each called the peak is a mistake to fix, not two facts. And the month named is the one that topped most complete years in the series ("peaks every December: the highest month in each of 2021 to 2025"); a month taken from `peakDate` or the last 12 months alone is the R3-19 mistake again.

## Labels in the user's language

(R3-17: a Spanish conversation got "For you: not this one · For the market: Not this version: here's one that could be (en claro: …)".) The labels are fixed strings (`judgement.md`, rule 7) in every language. **In an answer written in another language, the labels are the fixed translations below, word for word, every time,** never the English label, a mix, or the English with a gloss in brackets; the label-exactness rule (never a paraphrase, the explanation after the label, never inside it) applies to the translated set in the same way. Their meaning is said once in the user's language, in plain words, the first time they appear (`judgement-answer.md`, "Plain words for a newcomer").

| English | Spanish (ES) | German (DE) | French (FR) | Italian (IT) | Portuguese (PT) |
| --- | --- | --- | --- | --- | --- |
| For you: | Para ti: | Für dich: | Pour vous : | Per te: | Para você: (Portugal: Para si:) |
| a strong fit | encaja muy bien | passt sehr gut | très adapté | molto adatto | encaixa muito bem |
| a fit, with one fix | encaja, con un ajuste | passt, mit einer Anpassung | adapté, avec un ajustement | adatto, con una modifica | encaixa, com um ajuste |
| a long shot | una apuesta arriesgada | ein Wagnis | un pari risqué | una scommessa rischiosa | uma aposta arriscada |
| not this one | este no | nicht das Richtige | pas celui-ci | non questo | este não |
| For the market: | Para el mercado: | Für den Markt: | Pour le marché : | Per il mercato: | Para o mercado: |
| Strong | Sólido | Stark | Solide | Solido | Sólido |
| Promising, with one fix | Prometedor, con un ajuste | Vielversprechend, mit einer Anpassung | Prometteur, avec un ajustement | Promettente, con una modifica | Promissor, com um ajuste |
| Not this version: here's one that could be | Esta versión no: esta otra podría funcionar | Nicht diese Version: diese hier könnte funktionieren | Pas cette version : en voici une qui pourrait marcher | Non questa versione: eccone una che potrebbe funzionare | Esta versão não: aqui está uma que poderia funcionar |
| Not this version (in running text) | esta versión no | nicht diese Version | pas cette version | non questa versione | esta versão não |

- **Another language:** translate each of the seven labels once, plainly and close to the English, and use exactly that wording every time in the conversation.
- **The answer's language** is the user's: the language of their messages. A user who writes in English gets the English labels, whatever their marketplace.
- **The internal readings** (favours, against, neutral) are said in the user's language too, in the plain table's words (helps, hurts, neutral).

## The margin row, for a seller who won't sell on Amazon

(R3-21: a dropshipper's table showed "Margin if sold on Amazon", and a line under it said that row didn't apply to them; graders and users read it as their margin.) For a user who has said they'll sell somewhere other than Amazon (TikTok Shop, their own store, Etsy, eBay: in the question, the chat or the profile), **the Amazon-fee margin row is left out of the printed table,** and their own margin is said where their figures live:
- **Their per-sale line:** with a profile, in the For you block, where it already is (the fit check's money per sale: the price, their channel's fee from this run's data or its stated assumption, the unit cost, and for an own store or cold traffic the ad cost per sale as an assumption), worked as `judgement.md`, "The margin follows the user's channel" says. Without a profile (the channel said in the question), it is one plain line right under the table, labelled with their channel ("On TikTok Shop, a sale at USD 24.99 leaves about USD 9 after its 6% fee, the USD 6.10 cost and USD 8 of ads (an assumption)").
- **The market's Margin signal is unchanged:** it is still worked on Amazon's fees and scored, and the market verdict's counts include it, as for everyone. One clause, once, where the market's counts are given, says so, without the Amazon figure and as Amazon's, not theirs: "(these counts include the margin Amazon sellers would make; yours is below)". Amazon's margin is never one of the reasons the verdict sentence names for them ("searches are up and Amazon sellers keep a healthy margin" reads as their margin praised): the reasons named are the other rows.
- **No line saying an Amazon figure doesn't apply:** none is on screen. The Amazon figure comes only if they ask for it, labelled as Amazon's.
- **On Amazon, or not said:** the Margin row is printed as before. Outside the US, or with no Amazon fees read, the same rule holds for that marketplace's row.

**Off Amazon, the Amazon margin row isn't printed** (8 Nov 2026; this replaces the row above for them): it is still scored on Amazon's fees (`judgement-answer-checks.md`, "The margin row").

**Why this choice, against the facts layer** (`judgement.md`: the same data gets the same table and the same market verdict, whoever asks). The facts layer's promise is that the facts are the same for everyone and no profile moves a number: the signals, thresholds, counts and market verdict are unchanged, and every row that is printed is the same row anyone would see. Leaving out one row that doesn't apply to this reader changes no number; the row stays in the scoring, and the clause above says it counts. The alternative, printing a row and then telling the reader to ignore it, presents a figure as theirs that isn't. Their own margin is not put into the facts table (that would make the table depend on who asks); it stays in the For you block, the fit layer, or its one labelled line.

## The phrase that reads live, taught once

(R3-20: on claude.ai an information question, "what does X go for on alibaba", goes to Claude's web search whatever the skill descriptions say, while "can you check …" loads MarketMage.) Once per conversation, one plain line teaches it: **"Ask me to check or look up anything and I'll read it live."**
- It goes in the welcome when there is one (the "What can you do?" menu, the guided session's opening: `first-use.md`). Otherwise it goes only where it reads naturally: as the last clause of the one offer line in a `suppliers` or `gaps` answer ("Want the offers side by side? And anytime, ask me to check or look up something and I'll read it live."), never as a line of its own and never after the Next step.
- **Not in a full check's answer** (`validate`, `find-products`, `market-scan`, and any yes or no): their end is the one offer line and the Next step, nothing more (`judgement-first-answer.md`, "The end of a first answer").
- Said once in the chat: never repeated, never in a later answer, never in a reply to a bare greeting (its one offer line stays as `first-use.md` sets it).

## When the user wants a verdict, or pushes back

**A verdict asked for, or pushback:** `judgement-answer-checks.md`, "When the user wants a verdict, or pushes back". Never change a verdict because the user is upset.

**If the user asks for a particular verdict** ("tell me it's a yes", "I need this to work"), before or after the run, treat it as pushback in the answer itself: the acknowledgement line comes first, then the verdict with its counts, then the specific threshold or thresholds standing between this and Strong, and the question of whether they'd set one differently.

**If the user pushes back,** stay warm and stay exact. Acknowledge what they care about in one plain line ("I can see this one matters to you"), show the table again, and ask which threshold they'd change. Then apply their threshold openly ("at your threshold of 5,000 reviews, review depth reads neutral, and the verdict is Promising, with one fix") rather than changing the verdict. Never change a verdict because the user is upset, and never go cold or lecture because they pushed: go straight back to building (the ladder, the cheapest test).

## Wording that doesn't contradict itself

A credit and a fix about the same number are said as one fact: "priced like the leader, above most of the page" (never "What you got right: your USD 19.99 is where the top listing sells" beside "the one fix: USD 19.99 sits above the market's band").
