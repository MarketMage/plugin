---
type: llm
---

Real-user test round 2 (R2-12): a deeper answer quoted a median price that appeared nowhere in the data. The search summaries' `priceMedian` per direction in this data: deshedding brush USD 17.99, dog nail grinder USD 22.99, dog grooming glove USD 9.99, waterless dog shampoo USD 12.99, cordless dog clippers USD 44.99, dog hair dryer USD 74.99, dog paw cleaner USD 15.99.

PASS if every median, typical or middle price the reply quotes for a direction (including as "the median", "typical", "most sell at", or the middle figure of a band) equals that direction's priceMedian above. A reply that quotes no median passes this check.

FAIL if any figure called the median or typical price of a direction differs from its priceMedian above.
