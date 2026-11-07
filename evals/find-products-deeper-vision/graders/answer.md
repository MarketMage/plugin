---
type: llm
---

The user wants to sell dog grooming products on TikTok Shop US, asked to go deeper rather than get a plain list, and set two rules: things they'd use on their own dog, and nothing they'd have to buy thousands of.

PASS if all of these hold:
- it restates the user's own rules (things they'd use on their own dog; a first order well short of thousands) in a line, in words close to theirs;
- it asks at most two questions, about the buyer or their taste (for example their dog's breed, size or coat, what they already buy or use, anything they'd rule out); one of them may be roughly what a first order could be, as a band (no profile is known); it does not ask again how or where they'd sell (TikTok Shop US is known) and does not send a list of five profile questions;
- in the same message it says what it will read in plain words (for example what sells on TikTok Shop and rising searches, then buyers' complaints in the leading listings and factory prices or minimum orders) and gives ONE cost figure for all of it with a spending limit ("up to about USD … (with a spending limit)" or the same in other words; a second figure only for Apify's free plan), asking the user to answer and say go;
- it runs no research and shows no ideas, cards or ranking in this turn;
- it is short: about 170 words at most.

FAIL if it runs research or presents ideas or directions now, asks more than two questions, asks again how they'd sell, gives no estimate, gives separate cost figures per read, or runs long.
