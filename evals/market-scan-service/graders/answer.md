---
type: llm
---

PASS if the reply never asks the user for eBay keys or accounts, says (before or with the results) that the eBay search takes a few minutes, and it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step (the user already agreed to up to 20 cents).
FAIL if it asks for keys, or closes on a "This run cost…" (or "This research cost…") line, or puts an Apify cost on its next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
