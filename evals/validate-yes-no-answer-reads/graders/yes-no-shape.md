---
type: llm
focus: last_message
---

The user asked whether to sell red-light LED face masks on Amazon and said "just tell me yes or no dont need an essay". The check ran; its market data favours the idea (the top 10 sell at least 14,000 units a month, searches are rising).

PASS if all of these hold:
- the reply opens with a plain yes or no ("Yes", "No", "Yes, if …" or the same in other words) as its first word or first clause, before any verdict label line, heading or table;
- a verdict sentence with a market label follows (for example "For the market: Strong" or "Promising, with one fix"); its confidence and the reason for it in a few words are fine, but not a list of signal counts or a row-by-row breakdown;
- there is no signal table (no markdown table, no row-per-signal list of the data) and no headings;
- it is short: about 150 words or fewer in all, ending on a "Next step" line, with at most one line offering the table or more detail before it.

FAIL if the reply gives a table or a row-per-signal breakdown, opens with something other than the yes or no (a heading, a verdict line, "Here's what I found"), or runs well past about 150 words.
