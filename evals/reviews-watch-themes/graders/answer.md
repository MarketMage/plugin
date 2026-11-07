---
type: llm
---

PASS if the reply gives each product's average rating and review count (tentree Kessler Sweater about 4.56 from 9 reviews; MVMT Odyssey II about 4.83 from 6 reviews), names at least one praise theme (for example "comfortable" or "looks great") and the MVMT complaint theme ("uncomfortable"), notes the sample is small, and it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step.
FAIL if it invents reviews or themes not in the data, names any reviewer, or closes on a "This run cost…" (or "This research cost…") line, or puts an Apify cost on its next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
