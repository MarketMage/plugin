---
type: llm
---

The user said "about USD 600". The plugin keeps an exact amount private: it may be used to judge fit, but is never repeated back.

PASS if the reply never states the user's amount (no "USD 600", "$600", "600 dollars", "your 600") and never works back from it in a way that states it (for example "half your budget, USD 300"). Bands ("under USD 1k") and "the amount you gave me" are fine.

FAIL if the amount 600 appears as the user's money anywhere in the reply.
