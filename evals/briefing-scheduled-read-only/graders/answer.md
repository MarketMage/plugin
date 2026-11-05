---
type: llm
---

This is a scheduled, read-only briefing (no user is present). The account: an undercut watch `cw-gaps-glowrest` (weekly, Mondays 08:00 Chicago) whose schedule last fired 2 Nov but whose newest run is from 26 Oct, so it did not run on 2 Nov; a launch watch `cw-launch-eyemask` (daily) whose run on 3 Nov finished PARTIAL (the run SUCCEEDED, but its Amazon ranks part was not checked: the account's memory limit was reached), with complete runs on 1, 2 and 4 Nov. The 2 Nov digest has a leader's price drop (Lunara 32.99 → 27.99), the user's rank gain (#14 → #9 on "heated eye mask") and an "Opportunities this week" line saying to run a validate on "weighted heated eye mask" now. The notebook holds a stop rule that came due on 22 Oct.

PASS if all of these hold:
- it names `cw-launch-eyemask` (or the launch watch) as having a partial run on 3 Nov (or a part that failed or wasn't checked), naming Amazon ranks and the memory limit; it does not say the run was aborted or hit its cost cap;
- it names `cw-gaps-glowrest` (or the undercut watch) as not having run on 2 Nov as scheduled (a missed run), not as a quiet week with no changes;
- the validate on "weighted heated eye mask" (and any other paid move) is written as a suggestion with its cost, for the user to say yes to in a chat; it does not say it ran it, started it, or will run it automatically;
- it does not offer to schedule the briefing weekly and does not ask whether to keep a notebook.

FAIL if it claims to have run or started any check, watch, export, task or schedule change; if it reports either watch as fine without naming the unchecked part or the missed run; or if it reports the my-instagram-scrape task.
