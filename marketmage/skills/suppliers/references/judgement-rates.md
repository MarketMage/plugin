# Judgement: reference rates, dated and sourced

Part of the judgement rules (`judgement.md` is the core). Read only at the step that needs one of these figures: a margin on an EU marketplace other than the UK and Germany, a launch plan's start-up list, an Etsy payout for a seller in Canada, or an EU risk note's link. Each figure here is a reference in the sense of `judgement.md`, "Every fee and rate has a source, never memory": quote it with its source and the date it was read, and say it can change ("as of <date>; check the link before relying on it"). A figure the user gives for their own case replaces it, labelled as theirs. Nothing here is from memory: when a figure isn't in this file, the run's data or the user's words, it is unknown.

## EU standard VAT rates

The standard rate per EU country, from the European Commission's Your Europe page "VAT rules and rates" (https://europa.eu/youreurope/business/taxation/vat/vat-rules-rates/index_en.htm; the page's own "last checked" date 13 Jul 2026; read 4 Nov 2026). Reduced, super-reduced and zero rates apply to some categories in every country and are **not** listed here: when the product could take one, say so and ask, as for the UK and Germany.

| Country (Amazon site) | Standard rate | Net price = price ÷ |
| --- | --- | --- |
| Austria | 20% | 1.20 |
| Belgium (amazon.com.be) | 21% | 1.21 |
| Bulgaria | 20% | 1.20 |
| Croatia | 25% | 1.25 |
| Cyprus | 19% | 1.19 |
| Czechia | 21% | 1.21 |
| Denmark | 25% | 1.25 |
| Estonia | 24% | 1.24 |
| Finland | 25.5% | 1.255 |
| France (amazon.fr) | 20% | 1.20 |
| Germany (amazon.de) | 19% | 1.19 |
| Greece | 24% | 1.24 |
| Hungary | 27% | 1.27 |
| Ireland | 23% | 1.23 |
| Italy (amazon.it) | 22% | 1.22 |
| Latvia | 21% | 1.21 |
| Lithuania | 21% | 1.21 |
| Luxembourg | 17% | 1.17 |
| Malta | 18% | 1.18 |
| Netherlands (amazon.nl) | 21% | 1.21 |
| Poland (amazon.pl) | 23% | 1.23 |
| Portugal | 23% | 1.23 |
| Romania | 21% | 1.21 |
| Slovakia | 23% | 1.23 |
| Slovenia | 22% | 1.22 |
| Spain (amazon.es) | 21% | 1.21 |
| Sweden (amazon.se) | 25% | 1.25 |

The UK (not in the EU) is 20%, as `judgement.md` already says. Which country's rate applies to a sale (where the buyer is, the one-stop shop, a registration in the selling country) is the user's and their accountant's call: by default the rate of the marketplace's own country, said as that assumption in the VAT line.

## Etsy fees for sellers in Canada

From Etsy's Help Centre (read 4 Nov 2026): "What are Payment Processing Fees for Selling on Etsy?" (https://help.etsy.com/hc/en-us/articles/115015628847), "What is a Regulatory Operating Fee?" (https://help.etsy.com/hc/en-us/articles/1500011073202) and "What are the Fees and Taxes for Selling on Etsy?" (https://help.etsy.com/hc/en-us/articles/115014483627):
- **transaction fee:** 6.5% of the order total in the listing currency, shipping and gift wrap included (the same as for US sellers);
- **payment processing:** 3% + CAD 0.25 for orders from Canada or the US; 4% + CAD 0.25 for other international orders (US sellers: 3% + USD 0.25);
- **regulatory operating fee:** 0.50% of the item price and shipping (Canada);
- **listing fee:** USD 0.20 a listing, published in US dollars and converted by Etsy to the payment account's currency at the market rate when charged, so it moves with the exchange rate;
- **currency conversion:** 2.5% when the listing currency differs from the payment account's currency (for example listing in USD, paid out in CAD).

So a typical domestic sale costs about 6.5% + 3% + 0.50% = **10%** of the order + CAD 0.25, plus the listing fee (USD 0.20, charged in CAD at Etsy's rate), against 9.5% + USD 0.45 for a US seller. The CAD note, said once: Etsy is read on the US site in US dollars, so the band's prices are US-dollar prices; their payout is worked in CAD on their CAD price, and a US-dollar price is converted only at a rate they give.

## Start-up costs before the first sale

For a launch plan's start-up list (`launch-plan`, first-order maths). Each line names the cost and its source; a figure appears only where the source states one. Say them as "to check for your case", never as a requirement Claude has judged.
- **US sales-tax permit:** most US states that charge sales tax ask a business selling taxable goods there to register with the state's tax agency for a sales-tax permit. In Texas, a business selling tangible goods in Texas applies to the Comptroller (https://comptroller.texas.gov/taxes/permit/: "Allow 2-3 weeks to receive your permit"; the page names no fee). Whether a seller who sells only through a marketplace still needs one depends on the state: their state's tax agency says. Other states: their own tax agency's site, never a rule from memory.
- **Barcodes (GS1):** GS1 US sells a single GTIN (barcode number) for USD 30 with no annual renewal, or a company prefix for 10 products at USD 250 plus USD 50 a year (https://www.gs1us.org/upcs-barcodes-prefixes/how-to-get-a-upc-barcode, read 4 Nov 2026). Outside the US, the national GS1 organisation sets its own prices. Whether a marketplace asks for one for their product is that marketplace's rule, read in its seller help.
- **Etsy listing fees:** USD 0.20 a listing, renewed every four months or after each sale (`marketplaceFees` when the run read Etsy; else the Etsy help article above). A shop that lists 20 products pays about USD 4 to list them, and again as they sell or renew.
- **Amazon's seller plan, samples and their shipping, freight and duty, product photos:** as `launch-plan` names them, with figures only from the user or a read.

## EU product rules (for the EU risk notes)

Neutral facts behind the risk notes in `judgement-abroad.md` ("EU risk notes"), each with its official page (read 4 Nov 2026):
- **CE marking:** EU law requires CE marking for "toys, drones, electrical and electronic equipment, pyrotechnic products, recreational crafts and watercraft", "some kinds of pressure equipment, gas appliances, batteries, and machinery", "weighing and measuring equipment", "personal protective equipment" and "medical appliances, including diagnostic equipment" (Your Europe, "CE marking", https://europa.eu/youreurope/business/product-requirements/labels-markings/ce-marking/index_en.htm, last checked 17 Jul 2026; the list is not exhaustive).
- **GPSR (a responsible person in the EU):** the General Product Safety Regulation (Regulation (EU) 2023/988, https://eur-lex.europa.eu/eli/reg/2023/988/oj), applying since 13 Dec 2024, requires that a consumer product placed on the EU market has an economic operator established in the EU responsible for it (Article 16): a seller outside the EU names one (an importer, an authorised representative, or a fulfilment service provider).
- **Packaging (Germany, LUCID):** anyone distributing packaged goods in Germany must be registered in the LUCID Packaging Register of the Zentrale Stelle Verpackungsregister (https://www.verpackungsregister.org/en/; register at https://lucid.verpackungsregister.org/). Other EU countries run their own packaging schemes (extended producer responsibility); their own authority's site says what applies.

## Shipping in the margin, for sellers who ship themselves

For a seller with their own stock who ships their own orders on any channel other than Amazon (their own store, TikTok Shop, Etsy; not FBA), the headline margin includes an **estimated** shipping cost per order, from the weight read in this run (the Amazon leaders' `fees.shippingWeightLb`, labelled as the leaders' weight; or the weight the user gives), taken as the packed weight and rounded up to the band:

USPS Ground Advantage, commercial prices per parcel within the US (USPS Notice 123, effective 4 October 2026, https://pe.usps.com/text/dmm300/Notice123.htm, read 7 Nov 2026):

| Packed weight up to | Mid-distance (zone 5): used in the margin | Near to far (zones 1 to 8) |
| --- | --- | --- |
| under 1 lb | USD 8.24 | USD 7.33 to 8.95 |
| 1 lb | USD 9.29 | USD 8.01 to 11.22 |
| 2 lb | USD 10.50 | USD 8.39 to 13.42 |
| 3 lb | USD 12.12 | USD 9.04 to 16.30 |
| 5 lb | USD 14.53 | USD 10.35 to 20.24 |
| 10 lb | USD 17.81 | USD 12.56 to 26.39 |

- **Say it as an estimate, with the weight used:** "about USD 10.50 to ship a 2 lb pack (USPS Ground Advantage, mid-distance; an estimate from the leaders' weight)". The near-to-far range goes in the table's margin cell. Packaging, and what the buyer pays for shipping, are theirs to add: when they say they charge shipping, the estimate comes off what they charge.
- **The sum:** price − card fee (2.9% + USD 0.30, an assumption) − unit or landed cost − shipping estimate = what a sale leaves, before ads; then at USD 8 and USD 12 of ads per sale. The waterfall gets a bar labelled "shipping (estimate)".
- **Over 10 lb:** no band here: the margin is before shipping, and their carrier's price is asked once.
- **No weight read and none given:** the margin is "before shipping", said once, and the one question that completes it is the pack's weight.
- **A dropshipper** already has shipping in a landed cost or labels the cost "plus shipping, still to add" (the cold-traffic lens; never "free shipping"); no estimate is added there. **FBA sellers:** the FBA fee covers delivery to the buyer; no estimate. **Outside the US:** no table here: the margin is before shipping, and their carrier's price is asked once.
- These are reference prices, sourced and dated (`judgement.md`, "Every fee and rate has a source, never memory"): never another carrier's figure from memory.

## Reference exchange rates

The European Central Bank's euro reference rates of 6 Nov 2026 (https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml, read 8 Nov 2026), worked into US dollars. Used for a cost and a price in different currencies when the user hasn't given a rate of their own (`judgement-abroad.md`, "Mixed currencies"), always said as approximate, with this date and source: "at about USD 1.34 to £1 (the ECB's rate of 6 Nov 2026)".

| Currency | 1 unit in USD | 1 USD in it |
| --- | --- | --- |
| GBP (£) | 1.3385 | 0.7471 |
| EUR (€) | 1.1165 | 0.8957 |
| CAD | 0.7109 | 1.4066 |
| AUD | 0.6871 | 1.4554 |
| CNY (RMB) | 0.1499 | 6.6713 |
