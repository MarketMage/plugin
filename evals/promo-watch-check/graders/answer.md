---
type: llm
---

PASS if the reply reports the free-shipping thresholds (tentree over 100 US dollars, Zwilling above 79, ColourPop 35 in the US), the tentree code FREESHIP, and tentree's 30-50% off sale, says something about what these mean for a competing seller, and it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step (the user already agreed to up to 30 cents).
FAIL if it invents codes or thresholds, or closes on a "This run cost…" (or "This research cost…") line, or puts an Apify cost on its next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
