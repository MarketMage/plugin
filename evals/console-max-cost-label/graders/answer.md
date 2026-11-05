---
type: llm
---

PASS if all of these hold:
- it points to the task's Input tab or input page (a link to https://console.apify.com/actors/tasks/Xq7pRtWatch01/input, or the task page and its Input tab);
- it names the field "Max cost per run" (or maxRunCostUsd);
- it names controls by their label only, with no screen positions such as "top right", "top left", "on the left", "in the sidebar", "the third tab" or "the icon next to".

FAIL if it gives no way to find the field, names a different field, or describes any control by its position on the screen.
