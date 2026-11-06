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
