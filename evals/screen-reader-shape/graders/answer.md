---
type: llm
---

PASS if all of these hold:
- the reply has no table (no rows of cells separated by "|" characters);
- it contains none of these symbols: "·", "→", "←", "×", "≈", "✓", "✗";
- it still names the cheapest offers with their stores and prices from the results, and says what the check cost.

FAIL if it uses a table or any of those symbols anywhere (including follow-up suggestions and the last lines), or drops the prices or the cost.
