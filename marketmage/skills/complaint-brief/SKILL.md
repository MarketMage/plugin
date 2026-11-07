---
name: complaint-brief
description: Turn what buyers complain about in the leading listings for a product idea into a product brief - the complaint you'd fix (how many low reviews name it, across how many leaders, with a quote), why it matters (the leaders' sales floor), the praise to match, the fix as a factory spec line, whether factories already list it, how to show it in the main photo, and the sample test. Reads the Amazon top 10's best sellers and their reviews (for US leaders, the same products on Amazon UK and Germany, the brand's own shop or Trustpilot), plus factory offers. Use when someone asks what buyers complain about in a product or niche, what they would improve, how to beat the top listing, or what version to build. Not for the reviews of one specific product page, ASIN or store the user links, or for watching reviews over time (use reviews-watch).
---

# The complaint brief

Find the complaint the user could fix in the leading listings, and turn it into a brief a factory can quote on.

**Up front, in one batch, only these:** `references/judgement-complaints.md` (picking the leaders, the sources, reading the low reviews, the brief's shape and the honesty rules: **follow it exactly**), `references/judgement.md` (the core: the facts layer, the sales floor as a floor), `references/running.md` (costs, caps, tools, secrets, the runs already made in this chat), `references/known-limits.md` (routes established not to work, read before choosing any source; never try a route it lists) and `references/plain-words.md` (the words the user sees). The run prices this skill needs are in its table below.
- **Later, only at their step:** `references/running-results.md` in the same batch as the first result read; `references/running-runs.md` only for a Trustpilot read (a data-provider read), a run that doesn't succeed, or when this chat already holds a run; `references/costs.md` only when an estimate needs a price the table below doesn't give; `references/running-abroad.md` outside the US; `references/running-asks.md` when the user asks who runs this, offers an allowance, pastes a secret or asks for something MarketMage won't do; `references/judgement-answer.md` ("Tone") and the other judgement parts only when the brief turns into a verdict; no lens file.
- **The tool calls:** about 14 when the brief is a chat's first job (5 reference reads, 3 runs, 3 result reads, 1 reference read with them); a `RUN_SUMMARY` read only when the user needs to know why a page wasn't read (a leader with no rows in the results simply wasn't read: say so).

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. Ask only for

- **The product,** in shoppers' words ("women's hiking hip pack"), and the marketplace (`references/running.md`, "Country"; US by default).
- **Optional:** the version they have in mind (their price, a feature), and any leaders they already know (links, brands). Reviews they paste (Walmart, a rival's own site) are read as given.

## 2. Runs

Check this conversation first (`references/running-runs.md`, "Runs in this conversation"): the Amazon leaders' rows from `validate` or a directions read, and factory offers for the same product, are reused, not bought again.

| Round | What | Actor | Input | Cost on paid plans |
| --- | --- | --- | --- | --- |
| 1 | The Amazon top 10, to pick the leaders (skipped when this chat holds them) | `cleanpull/amazon-product-scraper` | `searches: ["<product>"]`, `maxResultsPerSearch: 10`, `marketplace`, `includeSearchSummary: true` | 10 × USD 0.003 ≈ **USD 0.03**; outside the US + 10 × USD 0.003 local-market |
| 1 | Factory offers, for "can a factory make it?" (skipped when this chat holds them) | `cleanpull/supplier-price-finder` | `products: ["<product>"]`, `sources: ["made-in-china"]`, `maxOffersPerSource: 10` | USD 0.005 + 10 × USD 0.002 ≈ **USD 0.025** |
| 2 | The leaders' reviews, from the sources `references/judgement-complaints.md` step 2 chooses | `cleanpull/reviews-monitor` | `asins`: the picked leaders as product links (for US leaders, `https://www.amazon.co.uk/dp/<ASIN>` and `https://www.amazon.de/dp/<ASIN>` for each; never amazon.com links for the text), `maxReviewsPerProduct: 20`, `includeThemes: true`; `productUrls` for a brand shop page, `trustpilotDomains` for a brand on Trustpilot | each product page USD 0.003 + up to 13 reviews × USD 0.0005 + up to USD 0.012 for the local-address reads outside the US ≈ **USD 0.022**; 5 leaders on UK and Germany ≈ **USD 0.22**, 3 ≈ **USD 0.13**; a Trustpilot business ≈ USD 0.076 with 20 reviews |

- **One estimate for both rounds,** at the yes (`references/running.md`, "Before any run"), with the known-limits line in it for US leaders and how long it takes (about 2 to 4 minutes): "Amazon US shows review text only to signed-in shoppers, so I'll read the same best sellers on Amazon UK and Germany (a brand sold only in the US comes back empty there), plus factory offers. Up to about USD 0.28 (with a spending limit), about 3 minutes. Go ahead?" Round 1 runs together; round 2 starts when round 1 is back, on the leaders picked from it (`references/judgement-complaints.md`, step 1).
- **Leaders already in this chat:** only round 2 runs (and the factory offers when not read), with its own estimate when it needs a yes.

## 3. Read the results

- **Amazon leaders** (`fields: "recordType,asin,title,brand,price,rating,reviewCount,starBreakdown,boughtPastMonthMin,dateFirstAvailable"`): check each row is the product, then pick the leaders (`references/judgement-complaints.md`, step 1).
- **Reviews:** the `rating-summary` rows in full (`average`, `count`, `histogram`, `themes`, `topComplaints`, `topPraise`, `reviewsNotShownKind`); the `review` rows with `fields: "recordType,productUrl,productTitle,rating,title,text,date"` and a `limit` of about 150. A run that ends PARTIAL names the pages not read in `RUN_SUMMARY.failures`: a leader's UK or German page that isn't there means the brand isn't sold in that country ("not read", never "no complaints").
- **Factory offers:** each offer's `title` and attributes, for the fix ("adjustable strap 20–48 in"); offers that aren't the product are left out.

## 4. Answer

The brief, exactly as `references/judgement-complaints.md` steps 4 and 5 set it out, on one screen, in plain words (`references/plain-words.md`). Voice: a hopeful, grounded collaborator: the complaint is the user's opening, said as one, with the numbers exact.

**The visual moment, after the opening line** (`references/running-results.md`, "Explaining results": "One visual, where it helps"; only where you can draw one, and otherwise nothing about it is said): the complaints found, one horizontal bar per complaint (at most 4), its length the number of low reviews read that name it, labelled with the complaint and "N of M low reviews · K leaders", a hint under the threshold drawn in grey and labelled "a hint". Caption: the sources and the date read ("Amazon UK and Germany, read 7 Nov").

End on the Next step, last, with no price: factory quotes with the fix as the spec (`suppliers`), the launch plan with the listing leading on the fix (`launch-plan`), or a `validate` check at their price. Before it, at most two follow-ups as the user would say them ("write me the spec sheet" · "what if they copy me?").
