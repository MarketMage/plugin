---
type: llm
target: mock_calls
arm: with-only
---

The user said "Go ahead, up to a dollar": every paid run in the request shares that USD 1 budget, so the caps of all the runs together must stay within it (`running.md`, item 6: the spending limit is never above a budget the user gave, and runs on one yes split it).

Add up the `maxTotalChargeUsd` values passed in every `call-actor` call (in its call options) in these mock calls.

PASS if the sum of all of them is USD 1.00 or less.
FAIL if the sum is more than USD 1.00 (even when each one alone is under USD 1).
