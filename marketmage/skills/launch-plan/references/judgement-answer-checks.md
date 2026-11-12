# Judgement: the checks before an answer is written

Part of the judgement rules (`judgement.md` is the core). Read in the same batch as `judgement-answer.md` and `judgement-first-answer.md`, before writing any answer that gives a verdict or a label. From the real-user test on claude.ai of 8 Nov 2026 (round 3b); where an older line elsewhere says otherwise, this file wins.

## The answer-time reads are required

(R3-18: "shud i sell those led face mask thingys on amazon? … just tell me yes or no" read only `judgement.md` and `known-limits.md`, skipped the answer files, and so gave a full table to someone who asked for a yes or no, and left out the regulated-product line an LED therapy mask needs.)
- **Before the first word of an answer that gives a verdict or a label,** the answer-time parts the skill names must have been read in this conversation: for `validate`, `find-products` and `market-scan`, `judgement-answer.md`, `judgement-first-answer.md`, `judgement-ladder.md` and this file (with `judgement-timing.md` on a timing question); for `suppliers` and `gaps`, `judgement-answer.md`, this file and `running-results.md`. Other skills that read `judgement.md` (`briefing`, `launch-plan`, `start`, `complaint-brief`) read only the parts their own steps name.
- **Any not yet read are read then,** in one batch of parallel reads, before writing. The answer's shape, its required lines and its labels are in them: an answer written without them is wrong, however right its numbers. A part already read in this chat is not read again.

## A yes or no asked for

"Just tell me yes or no", "yes or no?", "no essay", "short answer please": the shape the user asked for wins (`judgement-answer.md`, "Size the reply to the question"), in about 80 words and never past 120 (live runs of 0.4.7's first draft gave 190: three sentences of reasons, a "what must stay true", the profile offer):

**A verdict asked for is not this shape.** "Tell me it's a yes", "I need this to be a yes", "say yes": that is a verdict asked for, and it gets "When the user wants a verdict, or pushes back" below: the acknowledgement, the verdict with its counts, the table, the thresholds between it and Strong, and the best related version. The yes/no shape is only for a user who asks for brevity, never for one who asks for a particular answer.
1. **The plain answer, one sentence,** its first word set by the label (with a profile, the For you label): **Strong** or **a strong fit** → "Yes:"; **Promising, with one fix** or **a fit, with one fix** → "Yes, if <the fix>:"; **Not this version**, **a long shot** or **not this one** → "No, but <the best related version>:" (the search never dead-ends: `judgement.md`, rule 10). Then the one or two numbers that decide it.
2. **The verdict, one sentence:** its label, word for word (with a profile, the For you label first, then the market's), with its confidence in a few words; the one fix or the best related version only when the label carries one, in a few words. No counts list (the counts wait for the table), no "what must stay true".
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
- **A yearly peak** (the same month or season is the highest of its year in at least 2 of the years read) is "the peak", said as "peaks every <month>". It is the one the seasonality cross-check and the timing line use ("the yearly peak, December, is under 90 days away").
- **No yearly peak:** the single highest point (`summary.peakDate`) is said as "highest in <month year>", and no 90-day line is written: a one-off high doesn't come round again.
- **Both, in different months** (a one-off high in April 2026, a yearly peak every December): the yearly peak is "the peak"; the one-off high, only when it matters, is a separate plain fact ("a one-off high in April 2026"), never called "the peak" or "peaked".
- **Check before sending:** the table and the text each name the same peak month, or one of them names none. Two different months each called the peak is a mistake to fix, not two facts.

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

## Each idea's own evidence, and the order of ideas

(Review of 0.4.13, `find-products`: the automatic laser toy had the most TikTok sales, the longest-running ads and a single-unit AliExpress offer, yet ranked third or fourth in every run read. Trends had no series of its own for it, so it got no trend, or the handheld laser pointer's −28% was set against it, and the rows were ordered by for minus against before the sources backing them. The owner's 0.4.11 design: "Multi-source backing ranks higher and is said per idea".) In any answer that ranks several product ideas (`find-products`, a side-by-side of ideas):

- **A trend belongs to the idea it measures.** An idea's Demand trend is its own Trends series: the term that names that product. When Trends has no series of its own for it, a rising search in the rows that names its own product ("automatic cat laser toy", +180%) is its trend reading (rising), with "from a small base" where `judgement-first-answer.md` says so; with neither, its trend is **not read** (`unknown`): no point for or against, and it is said as not read, never as falling.
- **Another item's trend never counts for or against a different idea:** a neighbouring product ("cat laser pointer", the handheld kind, beside an automatic laser toy) or the category's broad term ("interactive cat toy" beside a rolling ball) is context for the ideas under it, never their for or against, never their what-holds-it-back cell, never their backing source. Where it helps, one clause says it is a different item ("handheld pointers are down 28%; this is the automatic kind").
- **Favour group first, then more independent backing.** Ideas are ordered by favour group (`judgement.md`, "The verdict rule"): the ideas the data favours lead, then the mixed ones, then the ones the data is against. Within a group, by how many independent sources back each one (each source counts once, however many rows, listings or stores show it: two stores' ads are one source), more first; the for/against tally breaks a tie in that count, then the demand number. Within a group, one strong number from a single source never lifts an idea above one that more sources back; across groups, backing never moves an idea above a better group, so the opening's lead, the top row and the count line ("2 of 8 the data favours") agree. A listing that only shows the product can be bought (an AliExpress row under 100 sold, 0 or null) is not a backing source. With a profile the For you label leads the order, and the backing count comes right after it, before the lens's own count; in a lens, backing counts only the sources behind the rows that lens counts (a search trend or chart rank the lens takes as context never adds to it).
- **Check before sending:** count each row's backing sources again from its own cells; among ideas with the same label (with a profile) and favour group, the higher row has as many or more (or ties and wins on the tally, then demand), and the opening's lead is the top row.

## The margin row, for a seller who won't sell on Amazon

(R3-21: a dropshipper's table showed "Margin if sold on Amazon", and a line under it said that row didn't apply to them; graders and users read it as their margin.) For a user who has said they'll sell somewhere other than Amazon (TikTok Shop, their own store, Etsy, eBay: in the question, the chat or the profile), **the Amazon-fee margin row is left out of the printed table,** and their own margin is said where their figures live:
- **Their per-sale line:** with a profile, in the For you block, where it already is (the fit check's money per sale: the price, their channel's fee from this run's data or its stated assumption, the unit cost, and for an own store or cold traffic the ad cost per sale as an assumption), worked as `judgement.md`, "The margin follows the user's channel" says. Without a profile (the channel said in the question), it is one plain line right under the table, labelled with their channel ("On TikTok Shop, a sale at USD 24.99 leaves about USD 9 after its 6% fee, the USD 6.10 cost and USD 8 of ads (an assumption)").
- **The market's Margin signal is unchanged:** it is still worked on Amazon's fees and scored, and the market verdict's counts include it, as for everyone. One clause, once, where the market's counts are given, says so, without the Amazon figure and as Amazon's, not theirs: "(these counts include the margin Amazon sellers would make; yours is below)". Amazon's margin is never one of the reasons the verdict sentence names for them ("searches are up and Amazon sellers keep a healthy margin" reads as their margin praised): the reasons named are the other rows.
- **No line saying an Amazon figure doesn't apply:** none is on screen. The Amazon figure comes only if they ask for it, labelled as Amazon's.
- **On Amazon, or not said:** the Margin row is printed as before. Outside the US, or with no Amazon fees read, the same rule holds for that marketplace's row.

**Why this choice, against the facts layer** (`judgement.md`: the same data gets the same table and the same market verdict, whoever asks). The facts layer's promise is that the facts are the same for everyone and no profile moves a number: the signals, thresholds, counts and market verdict are unchanged, and every row that is printed is the same row anyone would see. Leaving out one row that doesn't apply to this reader changes no number; the row stays in the scoring, and the clause above says it counts. The alternative, printing a row and then telling the reader to ignore it, presents a figure as theirs that isn't. Their own margin is not put into the facts table (that would make the table depend on who asks); it stays in the For you block, the fit layer, or its one labelled line.

## The phrase that reads live, taught once

(R3-20: on claude.ai an information question, "what does X go for on alibaba", goes to Claude's web search whatever the skill descriptions say, while "can you check …" loads MarketMage.) Once per conversation, one plain line teaches it: **"Ask me to check or look up anything and I'll read it live."**
- It goes in the welcome when there is one (the "What can you do?" menu, the guided session's opening: `first-use.md`). Otherwise it goes only where it reads naturally: as the last clause of the one offer line in a `suppliers` or `gaps` answer ("Want the offers side by side? And anytime, ask me to check or look up something and I'll read it live."), never as a line of its own and never after the Next step.
- **Not in a full check's answer** (`validate`, `find-products`, `market-scan`, and any yes or no): their end is the one offer line and the Next step, nothing more (`judgement-first-answer.md`, "The end of a first answer").
- Said once in the chat: never repeated, never in a later answer, never in a reply to a bare greeting (its one offer line stays as `first-use.md` sets it).

## When the user wants a verdict, or pushes back

**If the user asks for a particular verdict** ("tell me it's a yes", "I need this to work"), before or after the run, treat it as pushback in the answer itself: the acknowledgement line comes first, then the verdict with its counts, then the specific threshold or thresholds standing between this and Strong, and the question of whether they'd set one differently.

**If the user pushes back,** stay warm and stay exact. Acknowledge what they care about in one plain line ("I can see this one matters to you"), show the table again, and ask which threshold they'd change. Then apply their threshold openly ("at your threshold of 5,000 reviews, review depth reads neutral, and the verdict is Promising, with one fix") rather than changing the verdict. Never change a verdict because the user is upset, and never go cold or lecture because they pushed: go straight back to building (the ladder, the cheapest test).
