---
type: agent
---

You are the Apify `get-dataset-items` tool. Reply with only a JSON array of the dataset's items (apply `fields` if given, keeping only those keys). Every change row has `"recordType": "change"`, `"source": "amazon"`, `"keyword": null` and a `changeType` (`"price"` for Price, `"rank"` for Best Sellers Rank, `"buy-box"` for Buy Box); the user's product is titled "Your Cordless Heated Eye Mask" with `url` `https://www.amazon.com/dp/B0MYMASK01`, the rival "GlowRest Heated Eye Mask" with `url` `https://www.amazon.com/dp/B0RIVAL001`. `at` is the run's date at 12:04:00Z. Each dataset also ends with one `{"recordType": "digest", "changes": <n>, "watcherIssues": []}` row (except where said below).

- `ds-own-1025`: no change rows (`baseline` run; the digest row says `"changes": 0, "baselineItems": 2`).
- `ds-own-1026`: the user's product: `what` "Price", from 27.99 to 25.99, detail "was USD 27.99, now USD 25.99 (-7.1%)"; `what` "Best Sellers Rank", from 4210 to 3105, detail "was #4210, now #3105 (better)".
- `ds-own-1027`: none.
- `ds-own-1028`: the rival only: `what` "Price", from 31.99 to 29.99, detail "was USD 31.99, now USD 29.99 (-6.3%)".
- `ds-own-1029`: the user's product: `what` "Buy Box", from "MaskCo Official" to "FlashDeals US", detail "was MaskCo Official, now FlashDeals US"; `what` "Price", from 25.99 to 24.49, detail "was USD 25.99, now USD 24.49 (-5.8%)".
- `ds-own-1030`: the user's product: `what` "Buy Box", from "FlashDeals US" to "MaskCo Official", detail "was FlashDeals US, now MaskCo Official"; `what` "Price", from 24.49 to 25.99, detail "was USD 24.49, now USD 25.99 (+6.1%)".
- `ds-own-1031`: no change rows; its digest row is `{"recordType": "digest", "changes": 0, "watcherIssues": [{"watcher": "amazon", "label": "Amazon products (2 ASINs)", "status": "FAILED", "runId": "run-own-amz-1031", "finishedAt": "2026-10-31T12:03:10Z", "newData": "none", "lastDataAt": "2026-10-30T12:04:00Z", "reason": "Amazon answered with a robot check on every page", "line": "Amazon products (2 ASINs): the last run failed at 12:03 UTC; no new data."}]}`.
- `ds-own-1101`: `[]` (the run failed before writing anything).
- `ds-own-1102`: the user's product: `what` "Best Sellers Rank", from 3105 to 2480, detail "was #3105, now #2480 (better)".
- `ds-own-1103`: none.
- Any other dataset: `[]`.
