---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Defines the Gloss form type: an interpretive annotation anchored to specific sources. Thesis-driven synthesis with organized citations. The atomic unit of interpretation. 12 nodes in Garden/glosses/."
tagline: "What does this specific source or concept mean? — the structural contract for gloss forms"
---

← [Garden Patch Home](../) · [Form Definitions](index.html)


- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Gloss Form

**Core question**: "What does this specific source or concept mean?"

An interpretive annotation anchored to particular sources. Thesis-driven synthesis with organized citations. The atomic unit of interpretation. A gloss interprets what specific sources or concepts mean — it doesn't record a choice (decision), state a constraint (principle), or generalize from experience (pattern).

Stable once written; may spawn new glosses as understanding deepens.

## Structural Contract

A gloss form requires:

- **Opening thesis** — A clear interpretive claim about the source or concept, stated in the first paragraph. Not a summary — a position.
- **Interpretation** — The body develops the thesis with evidence from the source(s). Section headings vary by topic.
- **Sources** — Cited sources anchoring the interpretation.
- **Relations** — Connections to other nodes the gloss informs or draws from.

Naming heuristic: source + thesis. Mix based on how strong the interpretation is — a gloss dominated by one source foregrounds the source name; one making a novel synthesis foregrounds the thesis.

## Typical Predicates

- `is_a::[\[\[Gloss Form\]\]](Gloss%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)` or `[\[\[Growing Stage\]\]](Growing%20Stage.html)`
- `in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)`
- `extracted_from::[\[\[Source Document\]\]↑](../NODES.html#:~:text=Source%20Document)` — provenance with optional line numbers
- `relates_to::[\[\[Related Form\]\]↑](../NODES.html#:~:text=Related%20Form)` — lateral connections
- `defines_vocabulary_from::[\[\[Source\]\]↑](../NODES.html#:~:text=Source)` — when defining terms from decisions or research

## Exemplars

- [\[\[Deep Context Graph Vocabulary\]\]](../glosses/Deep%20Context%20Graph%20Vocabulary.html) — consolidates 7 terms from compound document decisions
- [\[\[PARA as Actionability-First Design\]\]↑](../NODES.html#:~:text=PARA%20as%20Actionability-First%20Design) — interprets Forte's PARA through a specific lens
- [\[\[Digital Garden as Growth Ethos\]\]↑](../NODES.html#:~:text=Digital%20Garden%20as%20Growth%20Ethos) — glosses the digital garden concept against vault architecture

## Category

Structural form — captures *how things relate* and *what we understand*.

## Sources

Definition from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 65-66.

## Relations

- relates_to::[\[\[Inquiry Form\]\]](Inquiry%20Form.html) — inquiries may resolve into glosses when interpretation solidifies
- relates_to::[\[\[Decision Form\]\]](Decision%20Form.html) — glosses often define vocabulary used by decisions
- relates_to::[\[\[Model Form\]\]](Model%20Form.html) — glosses interpret concepts that models structure