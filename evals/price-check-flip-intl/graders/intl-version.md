---
type: llm
---

The only Amazon listing the barcode matched is "Sony WH-CH520 Wireless On-Ear Headphones, Blue (International Version, No Warranty)", with barcodeVerified true and matchConfidence 1. Its Buy Box is USD 44.95 and it pays out USD 36.60 after fees.

PASS if all of these hold:
- the reply says the match is an International Version (or international / no-warranty listing) and that this may not be the same as the user's unit (region, warranty or model);
- it gives the match confidence as medium (or explicitly "not high", or "unconfirmed match"), never "high", "confirmed" or "exact match";
- it does not present the profit or ROI on this listing as a settled flip: either it holds the profit until the user confirms their unit is the International Version, or it labels any profit figure as depending on that, and it offers a way to settle it (asking which version they hold, or reading the US/domestic listing).

FAIL if it calls the match high-confidence or exact, if it never mentions the International Version, or if it gives a plain flip verdict (profit and ROI) on this listing with no caveat about the version.
