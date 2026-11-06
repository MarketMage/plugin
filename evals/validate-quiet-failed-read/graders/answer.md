---
type: llm
---

The TikTok Shop results could not be read (the dataset answered 503 each time); every other read came back.

PASS if all of these hold:
- the reply gives the market verdict with its counts, from the reads that came back;
- it says in one plain line that TikTok Shop's numbers couldn't be read this time (or weren't available) and what the answer rests on without them (for example, demand from Amazon's sales floor), or treats TikTok as not read in the table;
- it never narrates the failure as an error or a failure of the tool, the plugin, MarketMage or the connector: no "error", "failed", "failure", "503", "something went wrong", "tool", "connector problem", "I hit a limit" or "ended early" about it.

FAIL if it mentions an error, a failure, a status code or a broken tool or plugin about the TikTok read, or gives no verdict.
