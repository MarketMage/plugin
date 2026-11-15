#!/usr/bin/env python3
"""Live smoke test: runs each skill's actor calls, small, through the Apify API (the same actors
and inputs the skills pass to `call-actor`), each with a spending cap. It checks that every run
succeeds and that the fields the skills read are present.

    python3 scripts/smoke.py [skill ...]

Needs the Apify CLI signed in. It bills the signed-in account; the whole set costs about $0.45
(each run is capped; the per-skill totals are printed). Every actor is public, so every skill that
runs an actor has a case. A case's input may hold "{prev}", replaced by the previous run's dataset
ID in the same skill (gaps reads catalogues, then matches them).

The export case writes to a Google Sheet: set SMOKE_SHEET_URL to a sheet shared with
cleanpull-sheets-1@cleanpull-sheets.iam.gserviceaccount.com as Editor, or the case is skipped.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time

CASES = {
    'find-products': [
        ('amazon-bestsellers-tracker', {'categories': ['kitchen'], 'marketplaces': ['US'], 'charts': ['best-sellers'], 'maxItemsPerChart': 10, 'includeSummary': True}, 0.04, ['rank', 'title', 'price', 'rating', 'reviewCount']),
        ('tiktok-shop-sales-tracker', {'keywords': ['lip gloss'], 'maxProductsPerKeyword': 10, 'includeSummaries': True}, 0.06, ['title', 'price', 'unitsSold', 'shopName']),
        ('google-trends-scraper', {'mode': 'explore', 'searchTerms': ['air fryer', 'rice cooker'], 'timeRange': 'past-12-months', 'dataTypes': ['interestOverTime', 'relatedQueries'], 'geo': 'US'}, 0.02, ['searchTerm', 'relatedQueries_rising']),
    ],
    'validate': [
        ('amazon-product-scraper', {'searches': ['silicone stretch lids'], 'maxResultsPerSearch': 5, 'marketplace': 'US'}, 0.03, ['price', 'rating', 'reviewCount', 'rank', 'starBreakdown', 'boughtPastMonthMin', 'soldByAmazon']),
        ('google-trends-scraper', {'mode': 'explore', 'searchTerms': ['silicone stretch lids', 'silicone lids'], 'compare': True, 'timeRange': 'past-5-years', 'dataTypes': ['interestOverTime', 'relatedQueries'], 'geo': 'US'}, 0.02, []),
    ],
    'spy-store': [
        ('tech-stack-detector', {'domains': ['ruffwear.com'], 'maxPagesPerDomain': 1}, 0.01, ['ecommerce', 'marketingAutomation', 'payments']),
        ('shopify-store-scraper', {'stores': ['ruffwear.com'], 'maxProductsPerStore': 50, 'storeSummary': True, 'bestSellerRank': True, 'bestSellerDepth': 20}, 0.08, ['title', 'priceMin', 'onSale', 'available', 'publishedAt']),
    ],
    'price-check': [
        ('barcode-price-checker', {'products': ['027242923232']}, 0.03, ['lowestPrice', 'lowestPriceStore', 'highestPrice', 'priceSpreadPercent', 'storeCount', 'offerCount', 'offers', 'sources']),
        ('any-store-product-monitor', {'productUrls': ['https://www.allbirds.com/products/mens-tree-runners'], 'includeVariants': True}, 0.01, ['price', 'currency', 'inStock', 'onSale']),
        ('amazon-product-scraper', {'asins': ['B0BZYCJK89'], 'marketplace': 'US'}, 0.01, ['price', 'buyBoxSeller', 'rank']),
    ],
    'map-watch': [
        ('barcode-price-checker', {'products': ['027242923232'], 'mapPrices': {'027242923232': 329.99}, 'sources': ['amazon', 'bestbuy', 'google']}, 0.03, ['mapViolations', 'lowestPrice', 'storeCount']),
    ],
    'reviews-watch': [
        ('reviews-monitor', {'productUrls': ['https://www.tentree.com/products/kessler-sweater-warm-oak-heather-fade'], 'maxReviewsPerProduct': 5}, 0.01, ['average', 'count', 'histogram', 'themes', 'rating', 'text']),
        ('reviews-monitor', {'trustpilotDomains': ['allbirds.com'], 'maxReviewsPerProduct': 0}, 0.03, ['average', 'count', 'histogram']),
    ],
    'promo-watch': [
        ('promotions-monitor', {'stores': ['tentree.com'], 'maxLaunchesPerStore': 5}, 0.03, ['type', 'text', 'threshold', 'kind', 'launchedAt']),
    ],
    'gaps': [
        ('shopify-store-scraper', {'stores': ['ruffwear.com', 'tentree.com'], 'maxProductsPerStore': 20, 'storeSummary': False}, 0.05, ['title', 'priceMin']),
        ('catalog-matcher', {'competitorDatasetIds': ['{prev}'], 'yourStore': 'ruffwear.com'}, 0.10, ['recordType', 'matched', 'medianPriceIndex', 'byMethod']),
    ],
    'market-scan': [
        ('marketplace-search-scanner', {'keywords': ['cork yoga block'], 'sources': ['amazon', 'ebay'], 'amazonMarketplaces': ['US'], 'maxResults': 5, 'listingRows': False}, 0.10, ['priceP25', 'priceMedian', 'priceP75', 'top3SellerShare', 'medianReviews', 'under100Reviews']),
    ],
    'suppliers': [
        ('supplier-price-finder', {'products': ['silicone baking mat'], 'sources': ['made-in-china'], 'maxOffersPerSource': 5, 'offerPagesPerSource': 1}, 0.04, ['unitPriceMedian', 'moqMedian', 'supplierYears', 'supplierVerified']),
    ],
    'ads-watch': [
        ('ad-library-monitor', {'advertisers': ['Allbirds'], 'platforms': ['google', 'meta'], 'activeOnly': True, 'maxAdsPerTarget': 5}, 0.05, ['platform', 'advertiser', 'firstShown', 'adUrl']),
    ],
    'listing-audit': [
        ('listing-quality-checker', {'productUrls': ['https://www.allbirds.com/products/mens-tree-runners'], 'competitorUrls': ['https://www.tentree.com/products/kessler-sweater-warm-oak-heather-fade']}, 0.03, ['score', 'grade', 'topFixes', 'scoreGap']),
    ],
    'export': [
        ('google-sheets-sync', {'spreadsheet': os.environ.get('SMOKE_SHEET_URL', ''), 'tab': 'smoke-{date}', 'mode': 'append', 'rawData': [{'url': 'https://example.com/a', 'price': 1}, {'url': 'https://example.com/b', 'price': 2}]}, 0.01, []),
    ],
    'rank-watch': [
        ('amazon-keyword-rank-tracker', {'keywords': ['stainless steel water bottle'], 'asins': ['B0BZYCJK89'], 'marketplace': 'US', 'maxResults': 48, 'stopWhenFound': True}, 0.03, ['organicRank', 'organicPage', 'sponsoredRank', 'outrankedBy', 'adsShown']),
    ],
}


def api(method: str, path: str, body: object | None = None):
    cmd = ['npx', '-y', 'apify-cli@1.10.0', 'api', method, path]
    r = subprocess.run(cmd + (['-d', '-'] if body is not None else []), input=json.dumps(body) if body is not None else None, capture_output=True, text=True, timeout=600)
    d = json.loads(r.stdout)
    return d.get('data', d) if isinstance(d, dict) else d


def run(actor: str, inp: dict, cap: float, want: list[str]) -> dict:
    memory = '&memory=512' if actor == 'google-trends-scraper' else ''  # as the skills start it
    r = api('POST', f'/v2/acts/cleanpull~{actor}/runs?maxTotalChargeUsd={cap}{memory}', inp)
    rid = r['id']
    while True:
        r = api('GET', f'/v2/actor-runs/{rid}?waitForFinish=60')
        if r['status'] in ('SUCCEEDED', 'FAILED', 'ABORTED', 'TIMED-OUT'):
            break
        time.sleep(2)
    time.sleep(3)  # charged events settle a moment after the run ends
    r = api('GET', f'/v2/actor-runs/{rid}')
    items = api('GET', f"/v2/datasets/{r['defaultDatasetId']}/items?clean=1&limit=200")
    items = items if isinstance(items, list) else []
    keys: set[str] = set()
    for it in items:
        keys.update(it.keys())
    ev = r.get('pricingInfo', {}).get('pricingPerEvent', {}).get('actorChargeEvents', {})
    def price(e: str) -> float:
        x = ev.get(e, {})
        return x.get('eventPriceUsd') or (x.get('eventTieredPricingUsd') or {}).get('FREE', {}).get('tieredEventPriceUsd') or 0

    cost = sum(n * price(e) for e, n in (r.get('chargedEventCounts') or {}).items())
    return {
        'actor': actor, 'status': r['status'], 'runId': rid, 'rows': len(items),
        'missing': [k for k in want if k not in keys], 'cost': round(cost, 4),
        'secs': round(r['stats'].get('runTimeSecs') or 0, 1), 'message': r.get('statusMessage'),
        'datasetId': r['defaultDatasetId'],
    }


def main() -> None:
    only = sys.argv[1:] or list(CASES)
    total = 0.0
    per_skill: dict[str, float] = {}
    for skill in only:
        prev = None
        for actor, inp, cap, want in CASES[skill]:
            if actor == 'google-sheets-sync' and not inp.get('spreadsheet'):
                print(skill, 'skipped: set SMOKE_SHEET_URL to a sheet shared with the service account', flush=True)
                continue
            inp = json.loads(json.dumps(inp).replace('{prev}', prev or ''))
            res = run(actor, inp, cap, want)
            prev = res['datasetId']
            total += res['cost']
            per_skill[skill] = round(per_skill.get(skill, 0) + res['cost'], 4)
            print(skill, json.dumps(res), flush=True)
    for skill, cost in per_skill.items():
        print('skill total', skill, cost)
    print('total', round(total, 4))


if __name__ == '__main__':
    main()
