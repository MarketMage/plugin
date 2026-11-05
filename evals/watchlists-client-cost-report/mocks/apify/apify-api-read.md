---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state. Use `total`, `count`, `offset`, `limit` and `items` for lists; a list read with an `offset` past its items returns `items: []`.

- `/v2/actor-tasks`: four tasks.
  - `{"id": "tskACMEP", "name": "cw-price-acme-competitors", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: Acme: competitor prices"}`
  - `{"id": "tskACMEM", "name": "cw-map-acme-headphones", "actId": "bpc5tdrBiV2wEwLuT", "description": "MarketMage: Acme: MAP watch"}`
  - `{"id": "tskBONDI", "name": "cw-promo-bondi-rivals", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: Bondi Paws: rival promotions"}`
  - `{"id": "tskOTHER", "name": "my-instagram-scrape", "actId": "abc"}`
- `/v2/schedules`: four schedules, each `isEnabled: true`, timezone `Australia/Melbourne`: `cw-price-acme-competitors` (`0 9 * * 1`, task tskACMEP), `cw-map-acme-headphones` (`15 9 * * 1`, task tskACMEM), `cw-promo-bondi-rivals` (`30 9 * * 1`, task tskBONDI), `my-instagram-scrape` (`0 * * * *`, task tskOTHER).
- `/v2/actor-tasks/tskACMEP/runs` (newest first): six SUCCEEDED runs, each with `defaultKeyValueStoreId` `kv-acme-<mmdd>` and `defaultDatasetId` `ds-acme-<mmdd>`, ids `run-acme-<mmdd>`, started at 02:00:00Z on 2026-11-02, 2026-10-26, 2026-10-19, 2026-10-12, 2026-10-05 and 2026-09-28 (`<mmdd>` is 1102, 1026, 1019, 1012, 1005, 0928), each finished 4 minutes after it started. Each lists `"usageTotalUsd": 0.0021` (Apify's platform usage) and no charge figures: those come from `get-actor-run`.
- `/v2/actor-tasks/tskACMEM/runs` (newest first): six SUCCEEDED runs `run-map-<mmdd>`, started at 02:15:00Z on the same six dates, each with `"usageTotalUsd": 0.041`.
- `/v2/actor-tasks/tskBONDI/runs` (newest first): six SUCCEEDED runs, ids `run-bondi-<mmdd>`, `defaultKeyValueStoreId` `kv-bondi-<mmdd>`, started at 02:30:00Z on the same six dates, each with `"usageTotalUsd": 0.0019`.
- `/v2/actor-tasks/<id>/runs/last`: the newest run in that task's list above.
- Anything for `tskOTHER`, and any other path: `{"error": {"type": "record-not-found"}}`.
