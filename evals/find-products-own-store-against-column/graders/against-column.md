---
type: llm
---

The data includes Amazon Best Sellers review counts (a cardboard scratcher's chart leader at 31,200 reviews, a handheld laser pointer's at 22,300) and TikTok Shop units and 12-month search trends for each idea. The user sells on TikTok Shop and their own store, not on Amazon.

Find the ideas table (rows of cells separated by "|"). PASS if all of these hold:
- in the table, the column for what goes against an idea or holds it back (whatever its header: "against", "what holds it back", "the number against it") never names an Amazon review count, Amazon reviews or Amazon page-1 crowding for any row; its cells hold what counts against on the user's channels (falling interest, a low price or thin margin, a regulation, a dominant brand on their channel, thin TikTok sales) or are empty or "nothing yet";
- no row's for/against count reads Amazon review depth as an against;
- the table has at most five columns.

FAIL if any against or holds-back cell cites Amazon reviews or Amazon review counts (for example "31,200 reviews on Amazon"), or the table has six or more columns.
