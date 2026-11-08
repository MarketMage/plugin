---
type: llm
---

Weighting map P4 and the 0.4.5 offer tidy: a new user's first answer ends with at most one offer line and then the Next step line. When the seller profile hasn't been offered yet, its offer ("tell me how you'd sell it and roughly your budget") is part of that one offer line, not a separate line beside it. A new user's first answer carries no notebook offer ("keep this for next time", "keep a notebook"), and no note that such reads can take up to about 12 minutes.

PASS if all of these hold:
- after the table (and any exclusion or caveat line), the reply has at most one line or sentence group offering more (the full detail and, if present, the profile's two questions, together), then the Next step line last;
- it has no notebook offer and no "keep this for next time" line;
- it has no line about reads taking up to about 12 minutes.

FAIL if two or more separate offer lines are stacked before the Next step (for example a full-detail offer and, on its own line, a profile offer or a notebook offer), if a notebook offer appears, or if a wait-time note appears in the answer.
