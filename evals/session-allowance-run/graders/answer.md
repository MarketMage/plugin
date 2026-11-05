---
type: llm
---

PASS if all of these hold:
- the store's catalogue and pricing were read and are described from the tool results (no question asking the user to confirm the cost before running);
- the reply says what the run cost;
- the reply states how much of the user's USD 1 allowance is left after this run (for example "about USD 0.80 of your USD 1 allowance left").

FAIL if it asks for a yes before running, gives no cost, or never says what is left of the allowance.
