---
type: llm
focus: last_message
---

The conversation is in Spanish, so the verdict labels are the plugin's fixed Spanish translations, word for word. For the person ("Para ti:"), exactly one of: "encaja muy bien", "encaja, con un ajuste", "una apuesta arriesgada", "este no". For the market ("Para el mercado:"), exactly one of: "Sólido", "Prometedor, con un ajuste", "Esta versión no: esta otra podría funcionar" (shortened to "Esta versión no" in running text). Bold, the confidence and counts, or an explanation after the label are fine.

PASS if all of these hold:
- the reply is in Spanish;
- it has a "Para ti:" verdict and a "Para el mercado:" verdict, each with one of the fixed Spanish labels above, word for word;
- no English verdict label appears anywhere ("For you:", "For the market:", "a strong fit", "a fit, with one fix", "a long shot", "not this one", "Strong", "Promising, with one fix", "Not this version"), neither alone nor with a Spanish gloss in brackets.

FAIL if any verdict uses an English label, mixes English and Spanish in a label, adds a gloss inside the label ("(en claro: …)"), or uses a Spanish wording other than the fixed ones (for example "buen encaje", "prometedora, con una corrección", "no es para ti").
