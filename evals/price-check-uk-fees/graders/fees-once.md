---
type: llm
---

The data: amazon.co.uk listing B0UKBTL001 with a £24.99 Buy Box. Its `fees` say supported: true, marketplace GB: referral £3.75, FBA £3.17 (£6.92 in all, excluding VAT), VAT 20%, afterFeesExVat £13.91 (the £24.99 less £4.16 VAT is £20.83, less £6.92 fees), confidence low. The user's landed cost is £7.

PASS if all of these hold:
- it gives Amazon UK's fees from the data (the £6.92 total, or the £3.75 referral and £3.17 FBA fees) and never says Amazon UK's fees are missing, not in the data or not modelled;
- what a sale pays out is about £13.91, and the profit about £6.91 (anything from £6.85 to £6.95), shown with the VAT step once (£24.99 including about £4.17 VAT at 20%, so about £20.83);
- it never takes VAT off a second time: no payout near £11.59, no profit near £4.59, and no division of £13.91 or of £20.83 by 1.2;
- it says it assumed they are VAT-registered, or asks whether they are;
- it notes the fees' low confidence or that the fee category should be checked, in a few words.

FAIL if it says UK fees aren't in the data, uses a fee figure not in the data, removes VAT twice, or gives a profit outside £6.85 to £6.95 as the VAT-registered figure.
