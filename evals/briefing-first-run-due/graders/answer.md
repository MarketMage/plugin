---
type: llm
---

A live briefing (no notebook) on 4 Nov 2026. The account has three MarketMage watches:
- `cw-map-xm5`, a MAP watch created on 3 Nov with a weekly schedule (Mondays 08:00 Chicago) that has never fired: no `lastRunAt`, `nextRunAt` 9 Nov, and no run yet;
- `cw-reviews-eyemask`, a reviews task whose schedule was deleted (no schedule points at it); its last run was on 20 Oct;
- `cw-launch-eyemask`, a daily watch that ran on 4 Nov as scheduled; its digest has a rival's price drop (Lunara 32.99 → 27.99) and a rank gain (#14 → #9 on "heated eye mask").

PASS if all of these hold:
- it gives `cw-map-xm5` (or the MAP watch) a status saying it hasn't run yet and its first run is due on 9 Nov (or Monday 9 Nov), or that it is new and waiting for its first scheduled run;
- it does NOT say `cw-map-xm5` missed a run, failed, or "didn't run as scheduled" (on 2 Nov or any other date), and doesn't tell the user to check their usage limit, plan or memory because of it;
- it says `cw-reviews-eyemask` (or the reviews watch) has no schedule (not scheduled, runs only when started by hand, or its schedule was removed), and does not call it missed or failed;
- it reports the launch watch's changes from the 4 Nov digest.

FAIL if it reports `cw-map-xm5` as a missed, failed or late run, or gives either of the first two watches no status at all.
