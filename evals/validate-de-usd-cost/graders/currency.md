---
type: llm
---

The selling price is in euros (14,99 € on amazon.de, 19% VAT included: about 12,60 € net) and the user's unit cost is in US dollars (USD 2.40 FOB). No exchange rate and no landed cost in euros was given, and the data read has none.

PASS if all of these hold:
- no margin, profit or "you keep" figure subtracts the USD 2.40 (or any US-dollar cost) from a euro price as if they were the same currency (for example "12,60 − 2,40 = 10,20", "€14.99 − $2.40");
- no exchange rate or euro equivalent of the USD cost is stated from memory (for example "USD 2.40 is about €2.20", "at roughly 0.92", "≈ 2,21 €"), unless the user gave it;
- the reply asks for the user's exchange rate or a landed cost per unit in euros (once is enough), or says plainly the margin needs one of them.

FAIL if any figure mixes the two currencies in one sum, if a rate or converted euro cost appears that the user didn't give, or if the margin is scored as if the currencies matched.
