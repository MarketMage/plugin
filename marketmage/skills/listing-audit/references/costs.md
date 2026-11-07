# Costs

From the actors' Store pricing (regenerate with `scripts/sync-references.py`; CI fails when it is out of date).
Estimate with the Bronze column: the paid-plan price (Silver and Gold pay less), so no paid-plan user pays more than you said.
Where the Free column differs, free-plan users pay that price: at the approval estimate, quote it too, in the same line ("up to about USD 0.09 (USD 0.17 on Apify's free plan), capped"), so they never pay more than you said either. These prices are for that one estimate before a yes (`running.md`, "Before any run"), never for cost lines elsewhere.
Every run also has a start event of $0.00005 per GB of memory.

### `cleanpull/listing-quality-checker`: Listing Quality Checker: Product Page Audit & Score

Default memory 256 MB. Prices per 1,000 events, by Apify plan:

| Event | What it is | Free | Bronze | Silver | Gold+ |
| --- | --- | --- | --- | --- | --- |
| `audit` (main) | Page audit | $5.00 | $5.00 | $4.50 | $4.00 |
| `page-checked` | Page checked, unchanged | $0.60 | $0.60 | $0.55 | $0.50 |
| `residential-page` | Page through residential addresses | $7.00 | $7.00 | $7.00 | $7.00 |
| `apify-actor-start` | Actor Start | $0.050 | $0.050 | $0.050 | $0.050 |
