---
name: listing-audit
description: Audit product pages from any online store or Amazon listings and give each a 0-100 score with every check marked pass, warn or fail and a concrete fix - product structured data (Product and Offer markup, GTIN, availability, shipping and returns, review markup), title, images and alt text, attributes, meta tags, canonical and page weight; for Amazon, title rules, bullets, images, A+ content and description - with a side-by-side comparison against a competitor's page. Use when someone asks why Google doesn't show their product with price or stars, how to improve a product page or listing, or how their page compares with a competitor's. Not for profiling a competitor's whole store (use spy-store).
---

# Listing audit

A score and a fix list for product pages. Read `references/running.md` first (costs, caps, tools, secrets). Prices are in `references/costs.md`.

`references/running.md` is the core; its parts are read only at their step (its first lines say when): `references/running-results.md` once results are in, before using them; `references/running-runs.md` before a data-provider read, when a run doesn't succeed, or when this chat already holds a run; `references/running-abroad.md` outside the US; `references/running-asks.md` when the user asks who runs this, offers an allowance, pastes a secret or asks for something MarketMage won't do.

**Read once, together:** a reference already read in this conversation (by this skill or another MarketMage skill: their copies are the same text) is not read again. Read the references a step needs in one batch of parallel reads, never one after another.

**Reading a run's record** (`RUN_SUMMARY`, `DIGEST.md`): `get-key-value-store-record` with `keyValueStoreId` set to the run's `defaultKeyValueStoreId` (from `call-actor` or `get-actor-run`) and `recordKey` set to the key; never without `keyValueStoreId` (`references/running.md`, "Running").

## 1. Ask only for

- **The user's product pages:** any shop, or Amazon (`amazon.<marketplace>/dp/<ASIN>`), up to 200.
- **Optional:**
  - competitors' pages to compare with (`competitorUrls`);
  - the search terms the titles should carry (`keywords`).

## 2. Run

- **Run** `cleanpull/listing-quality-checker` with `productUrls`, `competitorUrls`, `keywords`.
- **Cost (paid plans):** USD 0.005 per page audited (each URL is read once); USD 0.007 more for a page from a site that blocks standard addresses. Comparison rows are free; a page that can't be read is not charged.
  - **Example:** the user's page and 2 competitors' ≈ **USD 0.015**: run it straight away. 20 pages ≈ USD 0.10: say so and get a yes.

## 3. Read the results

- **`audit` rows:** `fields: "recordType,url,role,pageType,title,score,grade,passed,warnings,failed,topFixes,checks,partial,notChecked"`. Each check has `id`, `label`, `status`, `weight`, `found`, `fix` and `source` (the guidance it follows).
- **`comparison` rows** (with competitors): `scoreGap`, `behindOn` (checks where a competitor does better, with their finding and the user's fix), `aheadOn`, `summary`.
- **`RUN_SUMMARY`:** pages that couldn't be audited, with the reason (Walmart, Target, Best Buy, REI and some brand sites block automated visitors or draw pages with scripts only).

## 4. Explain it like an expert

- **Lead with the score and grade per page, then the top fixes** (`topFixes`: the five worth the most points), in plain words.
- **Store pages:**
  - **Product structured data, Offer price and currency, availability:** these make a page eligible for Google's merchant listings (price, stock and ratings in results). A missing Offer is the biggest single fix.
  - **GTIN:** helps Google match the product across sellers in Shopping. Missing is a warning (only products that have a barcode need one); a bad check digit is a fail.
  - **Shipping and returns markup** lets Google show delivery and return terms with the listing.
  - **Review markup:** stars shown on the page but not marked up are invisible to Google.
  - **Markup added only by scripts** after the page loads is reported as such: Google's shopping crawl reads it less reliably.
- **Amazon listings:**
  - **Title rules:** Amazon recommends no more than about 60 characters and limits titles to 200; forbidden characters, repeated words and promotional wording can get a listing suppressed.
  - Five bullets, six or more images (a video counts), A+ content, and brand, colour, size and material in the attributes.
  - A row with `partial: true` was served without its lower half: the checks in `notChecked` are left out of the score, not failed.
- **Against a competitor:** name the checks where they're ahead and the user's fix for each; a store page and an Amazon listing are compared on what they share (title, images, attributes).
- **The score is a guide,** built from Google's and Amazon's published guidance; search rankings use many other signals. Say so once.
- End with the cost and the dataset link.

## 5. Ongoing (a listing watch)

For the user's own pages, after a theme update or a catalogue change:
- **The task:** `cleanpull/listing-quality-checker`, named `cw-listing-<name>`, with `productUrls`, `keywords`, `changesOnly: true`, `monitorName: "<name>"`, `maxRunCostUsd`. Weekly is usually enough.
- **What later runs return:** a page only when a check or the score moved (by 5 points by default), with `changedChecks`; a page gone on two runs in a row as a `change` row (`removed`). It sends no messages: the `watchlists` skill reads the results.
- **Cost:** the first run audits every page (USD 0.005 each); later runs USD 0.0006 per unchanged page and USD 0.005 per changed one. **Example:** 20 pages weekly ≈ USD 0.012 a run, **about USD 0.06 a month**; the first run ≈ USD 0.10.
- **`maxRunCostUsd`:** 1.5× the typical run, at least USD 0.02; the baseline run uses the first-run cap (`references/watchlists.md`, step 4).
- **Steps:** follow `references/watchlists.md`.
