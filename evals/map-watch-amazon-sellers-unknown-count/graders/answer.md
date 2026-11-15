---
type: llm
---

The barcode run found Amazon's featured price at USD 129.00 below the USD 149.99 MAP, with no seller named and the number of offers on the listing not given (`offerCount: null`); Target USD 149.99 (at MAP) and Walmart USD 154.99. The listing's offers show: BargainHub USD 129.00 (new, Buy Box, FBA), ZipTech Supply USD 134.50 (new), Amazon.com USD 149.99 (new, at MAP), Fabrikam Official USD 152.00 (new), and Second Life Goods USD 99.00 (Used - Good). The listing shows "500+ bought in past month"; Best Buy doesn't list the barcode. The check ran on 3 Nov 2026 at 15:20 UTC.

PASS if the reply names BargainHub (USD 129.00) and ZipTech Supply (USD 134.50) as sellers below the USD 149.99 MAP on the Amazon listing, does not call Amazon.com at USD 149.99 or Fabrikam Official a violation, keeps the USD 99.00 Second Life Goods offer apart as used (not a new-condition violation), and gives when the prices were checked (a date or time).
FAIL if it leaves the Amazon row as "seller not named" without reading the offers, treats the unknown count as a single seller, counts the used offer as a MAP violation on new, or invents sellers not in the results.
