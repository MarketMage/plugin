---
type: llm
---

The welcome (owner's design of 9 Nov 2026): a new user who asks "what can you do?" gets about one screen: a warm line; what MarketMage can do as a short list of jobs, each with a one-line example they can copy (find something to sell; check an idea or a claim; size up a competitor's store and their ads; sourcing and supplier prices; what buyers complain about; watching prices, stock, ranks, ads or promotions over time with a briefing; for existing Amazon sellers, keyword ranks, the Buy Box and listing quality); one line on cost; the "ask me to check or look up anything" tip; then "What brings you here?" with an optional line inviting how they sell and roughly their budget.

PASS if all of these hold:
- it opens with a warm line, not a disclaimer or warning;
- it lists at least six of the seven jobs above, in plain words, and most of them carry a short example the user could copy or adapt (a quoted request, or an example ask such as "Check if heated eye masks are worth selling");
- the existing-Amazon-seller job (ranks, the Buy Box or listing quality) is among them, so the menu doesn't assume the user is only looking for something to sell;
- there is exactly one short cost line, in plain words, saying checks run on the user's own Apify account, that anything over a few cents shows a cost range (or its cost) first and waits for their yes, and/or that Apify's free plan includes USD 5 a month; no billing paragraph, no per-result prices, no figures beyond the free plan's USD 5;
- it ends by asking what brings them here (or what they'd like to do), with an optional, skippable invitation to say how they sell (dropship, Amazon, Etsy, their own store or similar) and roughly their budget so answers are tailored; the profile is not required and no list of profile questions is asked;
- it is about one screen: no research results, no skill or command names as the list (mentioning `/marketmage:start` once is fine), no notebook mention, and no step-by-step guided session description beyond its one job line.

FAIL if it lists the skills by name, gives fewer than six jobs, leaves out the existing-Amazon-seller job, explains billing in more than one line or gives run prices, asks the profile as required questions, mentions the notebook, or runs or presents research.
