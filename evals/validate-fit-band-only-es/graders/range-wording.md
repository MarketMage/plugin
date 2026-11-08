---
type: llm
---

The user gave only a budget band, USD 1,000 to 5,000 (no exact amount). The first order at the supplier medians is 200 × USD 4.80 = about USD 960, at or under the band's low end. The band's top (USD 5,000) is not their budget: the plugin speaks of the range they picked ("fits the $1k–5k range you picked", "inside the $1k–5k range you picked"; in Spanish, for example "cabe en la franja de 1.000–5.000 $ que elegiste").

PASS if the For you line or the fit check says the first order fits or sits inside the range or band they picked, and never presents USD 5,000 (the band's top) as their budget ("within your up-to-$5k budget", "dentro de tu presupuesto de hasta 5.000 $", "your $5,000").

FAIL if the band's top is presented as their budget anywhere in the reply.
