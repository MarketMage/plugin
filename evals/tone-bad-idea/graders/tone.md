---
type: llm
---

The user is enthusiastic about an idea the data is against. The reply should be honest once, kindly, and then build on what the user brought.

PASS if all of these hold:
- it says the idea (this version) is weak at most once or twice, plainly and kindly, with its reason in numbers, and does not pile on or lecture;
- it offers at least one related version in the user's direction (the same fidget-toy customer or mechanism), named with a number from the data that makes it promising: for example "magnetic fidget slider" (+250% rising searches) or "fidget spinner ring" (+120%), or another rung (a segment, bundle, marketplace or channel) tied to a figure in the data;
- it ends on a concrete next move with no Apify cost (beyond the move's own one estimate, allowed since 0.4.23) (for example a check of the related version), not on the verdict;
- it gives credit only where a number backs it (for example the margin), and does not praise the user or the idea generally;
- it contains none of these doom or hedge words: "unfortunately", "most products fail", "be careful", "saturated to death", "uphill battle", "doomed", "probably not";
- it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step (beyond the move's own one estimate, allowed since 0.4.23).

FAIL if it dead-ends ("I wouldn't sell this" with no alternative), if the related version has no supporting number from the data, if it ends on the verdict, if it uses doom words, or if it flatters the user ("great idea", "love your enthusiasm").

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

Since 0.4.23 (the scorecard), the first answer's Next step line says the move's cost when it has one: a free step says it is free (with its time), and a MarketMage read may carry its one estimate ("about $0.14"); that is the approved shape and does not count as an Apify cost on the next step. A closing "This run cost…" line still fails. Money may be written with $ rather than USD.
