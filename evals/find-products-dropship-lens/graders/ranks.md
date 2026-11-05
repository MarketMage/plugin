---
type: llm
---

Finding 16 (ranks and counts come from the table shown). Check every rank or count stated in the prose ("#3", "the 2nd", "3 of the top 5", "the only two in the top 4", "N of M ideas the data favours") against the table the answer shows, counting its rows in order.

A "#N for you" in a For you cell is the idea's rank for this user (by For you label, then TikTok units), not its row position: check it against that ranking, not against the row order. Any other rank is the row position unless the answer says which ranking it is.

PASS if every such rank or count matches the table shown (or says plainly what else it counts, such as the actor's own rank among more rows read), or if the answer states no such rank or count beyond the table itself.

FAIL if any stated rank or count disagrees with the rows of the table shown (for example "3 of the top 5" where the table shows 2, or an idea called #2 that is third in the table).
