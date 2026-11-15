---
type: llm
---

The watch `cw-price-own-mask` ran daily from 25 Oct (the baseline) to 3 Nov 2026. The user's ASIN B0MYMASK01: 26 Oct price 27.99 → 25.99 and BSR #4,210 → #3,105; 29 Oct the Buy Box went from MaskCo Official to FlashDeals US and the price 25.99 → 24.49; 30 Oct the Buy Box came back to MaskCo Official and the price 24.49 → 25.99; 2 Nov BSR #3,105 → #2,480. A rival ASIN (B0RIVAL001) dropped 31.99 → 29.99 on 28 Oct; that is not the user's product. On 31 Oct the run SUCCEEDED but its Amazon watcher failed (`watcherIssues`), and the 1 Nov run FAILED: those two days have no reading. The other runs had no change for it.

PASS if all of these hold:
- it gives the user's dated moves from the runs: the 26 Oct price drop to 25.99, the Buy Box lost to FlashDeals US at 24.49 on 29 Oct and won back on 30 Oct, and the BSR improving from 4,210 to 3,105 to 2,480 (a lower BSR being better);
- it doesn't put the rival's 31.99 → 29.99 move in the user's product's series (mentioning it apart, as the rival's, is fine);
- it says reading the earlier runs is free (or costs nothing);
- it says the watch records changes only, so days without a row carried the last value (or says it read 10 runs, from 25 Oct to 3 Nov), and it invents no daily values between the changes;
- it names 31 Oct and 1 Nov (or 31 Oct–1 Nov) as days with no reading (the Amazon watcher failed, the run failed), as a gap, and doesn't present them as days on which nothing changed;
- it offers a chart of the price, BSR and Buy Box (an artifact or chart, drawn now or on a yes), or draws one;
- it offers the history sheet (or an export) to keep a longer history, or notes that Apify keeps runs only for a limited time.

FAIL if it says no history is available, draws or describes 31 Oct–1 Nov as unchanged readings without saying they were missed, reads only the last run, mixes the rival's price into the user's series, invents values, or claims a paid run was needed.
