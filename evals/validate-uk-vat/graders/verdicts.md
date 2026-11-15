---
type: llm
---

Findings 8 and 12 (the two verdict lines). The reply should open with a "For you" line and a "For the market" line.

PASS if all of these hold:
- each verdict label that says "with one fix" ("a fit, with one fix", "Promising, with one fix") has its fix stated in a few words on the first screen (before the signal table), not only later or never;
- when the For you label and the market label differ (for example "For you: a long shot" with "For the market: Promising, with one fix"), the first screen has a sentence saying why, naming the row or number that makes the difference (for example thin demand on amazon.co.uk, at least 300 units a month across the top 10, which is the only place this seller sells);
- a "long shot" is not introduced with words that read as a fit, such as "Nothing I read stops this working for you".

FAIL if a "with one fix" label never names its fix, if two different labels sit side by side with no reason given that names a row or number, or if "a long shot" is paired with "nothing stops this working" wording.
