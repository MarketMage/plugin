---
type: llm
---

PASS if all of these hold:
- it is kind and hopeful: it says the weak version is weak once, with numbers, and does not imply the user is doomed, naive or too new;
- it makes no comment on the profile itself (no "don't worry, everyone starts somewhere", no "great that you saved", no praise of the person);
- it offers at least one related version in the user's direction (for example "magnetic fidget slider", +250% rising searches) with the number that makes it promising;
- it points to a cheap, reversible next step, with no Apify cost on it (beyond the move's own one estimate, allowed since 0.4.23) (for example checking the related version, or a small first order or sample), and ends on that move, not on the verdict;
- it uses no doom words ("unfortunately", "most products fail", "be careful", "risky", "doomed").

FAIL if it is discouraging or patronising, comments on the profile, dead-ends, or ends on the verdict.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

Since 0.4.23 (the scorecard), the first answer's Next step line says the move's cost when it has one: a free step says it is free (with its time), and a MarketMage read may carry its one estimate ("about $0.14"); that is the approved shape and does not count as an Apify cost on the next step. A closing "This run cost…" line still fails. Money may be written with $ rather than USD.
