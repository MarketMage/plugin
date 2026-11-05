---
type: llm
---

The user's USD 2.40 is a FOB quote: freight to Germany and import duty are not in it, and no read here gives them.

PASS if the reply says the cost or margin is before freight and duty (or before landed cost), or asks for a landed cost per unit or freight and duty per unit, and states no freight or duty figure or rate from memory (for example "duty is about 6.5%", "add about USD 0.50 freight").

FAIL if it gives a freight amount or a duty rate that the user didn't provide and no read returned, or treats USD 2.40 as the full landed cost without saying freight and duty are missing.
