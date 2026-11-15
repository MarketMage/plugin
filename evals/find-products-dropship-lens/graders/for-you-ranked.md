---
type: llm
---

Findings 8 and 12, with real-user round 2 (R2-3): the For you reading is a short note in each idea's cell, and the row order is the rank. Look at the table's rows and their For you notes (or the per-idea For you readings).

PASS if all of these hold:
- the rows are in the For you order (the strongest lead for the user first), each idea's note tells it apart (its own fix or fact; ideas with the same label are separated by what differs), and no cell carries a "#N for you" prefix;
- every "a fit, with one fix" names a specific fix or a specific check in a few words; when what holds an idea back is only data not read yet (the single-unit price, the ad crowd), it is written as a check still to make ("to check: …", or said once above the table for all ideas), not presented as the fix itself ("a fit, with one fix: MOQ-1 unread" alone fails this point);
- no label stands alone with nothing after it.

When every idea has the same label, the plugin's rule is one line above the table saying so, why, and what orders the rows (`judgement-for-you.md`, "If every idea has the same label…"). That satisfies the first point as long as each idea's note still carries its own fact (its sales, its feature, its catch), so no two notes are the same. Plain row numbers ("1.", "2.") are the row order and are fine; only a "#N for you" prefix fails.

FAIL if a cell carries "#N for you"; if the rows are not in the order the answer gives for them; if two or more ideas' notes are identical or empty, so the notes tell the user nothing; if a shared label is repeated on every row with no line saying why; or if "data not read" is the only thing given as the fix on most rows.
