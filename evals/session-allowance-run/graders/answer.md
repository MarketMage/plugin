---
type: llm
---

PASS if all of these hold:
- the store's catalogue and pricing were read and are described from the tool results (no question asking the user to confirm the cost before running);
- the allowance is honoured silently: the reply has no cost line for the run ("That cost about…", "This run cost…") and no report against the allowance ("USD 0.80 of your USD 1 left");
- its last line is a next step with no Apify cost.

FAIL if it asks for a yes before running, says what the run cost, or reports what is left of the allowance (the user didn't ask).

"Apify cost" means what MarketMage's runs cost; product prices from the data are not Apify costs and are fine anywhere.
