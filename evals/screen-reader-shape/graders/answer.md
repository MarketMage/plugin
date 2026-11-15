---
type: llm
---

PASS if all of these hold:
- the reply has no table (no rows of cells separated by "|" characters);
- it contains none of these symbols: "·", "→", "←", "×", "≈", "✓", "✗";
- it still names the cheapest offers with their stores and prices from the results, gives no cost line (a check under USD 0.05 just runs, with no cost before or after it), and ends on a next step with no Apify cost.

FAIL if it uses a table or any of those symbols anywhere (including follow-up suggestions and the last lines), or drops the prices, or closes on what the check cost.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.
