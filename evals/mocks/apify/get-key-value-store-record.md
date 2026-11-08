---
type: agent
---

You are the Apify key-value store record reader. For key `RUN_SUMMARY` of store `kv-spf-halfsheet`, return exactly:

{"outcome": "COMPLETE", "products": 1, "summaries": 1, "offers": 4, "offersWithShipping": 0, "offerPagesRead": 0, "filteredOut": 16, "residentialRequests": 0, "providerRecords": 4, "providerSearches": 2, "sources": {"aliexpress": {"searched": 1, "withOffers": 1, "noResults": 0, "failed": 0}, "alibaba": {"searched": 1, "withOffers": 1, "noResults": 0, "failed": 0}}, "charged": {"product-summary": 1, "provider-search": 2, "offer": 4, "provider-record": 4}, "stoppedBySpendingLimit": false, "warnings": ["16 offers were left out because their title does not name every word of the product idea (not charged)."], "failures": []}

For key `RUN_SUMMARY` of store `kv-cb-rm-hippack`, return exactly:

{"outcome": "PARTIAL", "products": 4, "reviews": 26, "sources": {"amazon": {"read": 4, "failed": 4}}, "charged": {"rating-summary": 4, "review": 26, "residential-request": 12}, "stoppedBySpendingLimit": false, "warnings": [], "failures": [{"url": "https://www.amazon.co.uk/dp/B0HIPPK003", "reason": "No product page at this address on this marketplace (404): the product isn't sold there."}, {"url": "https://www.amazon.de/dp/B0HIPPK003", "reason": "No product page at this address on this marketplace (404): the product isn't sold there."}, {"url": "https://www.amazon.co.uk/dp/B0HIPPK010", "reason": "No product page at this address on this marketplace (404): the product isn't sold there."}, {"url": "https://www.amazon.de/dp/B0HIPPK010", "reason": "No product page at this address on this marketplace (404): the product isn't sold there."}]}

For key `RUN_SUMMARY` of store `kv-cb-aps-hippack`, return {"outcome": "COMPLETE", "products": 10, "failures": []}.

For key `RUN_SUMMARY` of store `kv-sl-aps-slides`, return {"outcome": "COMPLETE", "products": 10, "failures": []}.

For key `RUN_SUMMARY` of any other store, return a short JSON summary consistent with a successful run of the actor implied by the store ID (the store ID is `kv-<actor name>`), with `"outcome": "COMPLETE"` and `"failures": []`. For key `DIGEST.md` of store `kv-watch-digest-last`, return exactly:

**3 changes** across 3 watched items.

## Store products
- **Price**: [Men's Tree Runner](https://www.allbirds.com/products/mens-tree-runners) USD 98 → USD 89 (-9.2%)
- **Stock**: [Climate Changer Coverall](https://ruffwear.com/products/climate-changer-coverall) InStock → OutOfStock

## Amazon products
- **Buy Box**: [Owala FreeSip 24 oz](https://www.amazon.com/dp/B0BZYCJK89) Owala → Verona Sky

For key `DIGEST.md` of store `kv-watch-digest`, return exactly:

**First run: baseline recorded.** The current state of every watched item is recorded, so the next run reports what changed. No changes are reported on a first run.

For any other key, return {"error": "record not found"}.
