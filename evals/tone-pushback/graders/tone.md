---
type: llm
---

PASS if all of these hold:
- it acknowledges the user's feelings briefly and warmly (one line), without being cold, lecturing or editorialising about their attachment or their family;
- it gives specific credit tied to a number where the data backs the user (for example the margin, or the price inside the band);
- it frames the verdict as progress: what favours it, and "the one fix" or the test that would move it;
- it offers at least one related version in the user's direction tied to a number from the data (for example "silicone baking mat for air fryer", +350% rising searches);
- it ends on a concrete next move with no Apify cost (beyond the move's own one estimate, allowed since 0.4.23), not on the verdict;
- it uses no doom words ("unfortunately", "be careful", "most products fail", "tough market") and no hype ("definitely", "guaranteed").

FAIL if it is cold or scolding, if it caves, if it dead-ends with no next move, or if it uses doom or hype words.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

Since 0.4.23 (the scorecard), the first answer's Next step line says the move's cost when it has one: a free step says it is free (with its time), and a MarketMage read may carry its one estimate ("about $0.14"); that is the approved shape and does not count as an Apify cost on the next step. A closing "This run cost…" line still fails. Money may be written with $ rather than USD.
