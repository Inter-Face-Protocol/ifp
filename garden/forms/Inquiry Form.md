---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Defines the Inquiry form type: a thesis-driven investigation that marshals evidence, proposes hypotheses, and directs questions at specific people. The primary generative form — inquiries produce cases, patterns, and references. 11 nodes in Garden/inquiries/."
tagline: "What should we think about X, and how would we find out? — the structural contract for inquiry forms"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Form Definitions](index.html)


- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Inquiry Form

**Core question**: "What should we think about X, and how would we find out?"

A thesis-driven investigation that marshals existing evidence, proposes hypotheses, and directs specific questions at specific people or groups. Distinguished from a gloss (which interprets existing sources) by being forward-looking rather than retrospective.

Inquiries are the primary generative form: their hypotheses, if tested, produce cases; their parallels, if validated, become patterns; their syntheses, if completed, become references. An inquiry may be resolved (producing other nodes) or persist as an open research thread.

## Structural Contract

An inquiry form requires:

- **Research question** — Clear framing of what's being investigated.
- **Current state** — What's known, what hypotheses exist, what evidence has been gathered.
- **Open questions** — Specific, answerable questions. Not vague wonderings.
- **Sources** — Evidence and references marshaled so far.
- **Relations** — Connections to nodes the inquiry draws on or may produce.

Optional: **Directed questions** using the `directed_at::` predicate to mark questions requiring a specific person's judgment. These are boundary markers — places where the system recognizes it has reached the limit of what it can resolve without human input.

Naming heuristic: scope of investigation + what's being determined.

## Typical Predicates

- `is_a::[\[\[Inquiry Form\]\]](Inquiry%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)` or `[\[\[Growing Stage\]\]](Growing%20Stage.html)`
- `in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)`
- `directed_at::[\[\[Person Name\]\]↑](../NODES.html#:~:text=Person%20Name)` — flags questions for specific people
- `extracted_from::[\[\[Research Note\]\]↑](../NODES.html#:~:text=Research%20Note)` — provenance
- `extends::[\[\[Related Form\]\]↑](../NODES.html#:~:text=Related%20Form)` — applies a concept to new domain
- `relates_to::[\[\[Gloss Form\]\]](Gloss%20Form.html)`, `[\[\[Pattern Form\]\]](Pattern%20Form.html)`

## Exemplars

- [\[\[Compound Node Meeting Structure\]\]↑](../NODES.html#:~:text=Compound%20Node%20Meeting%20Structure) — directed questions about meeting compound node design
- [\[\[Personal Knowledge Management Method Adoption for Vault Architecture\]\]↑](../NODES.html#:~:text=Personal%20Knowledge%20Management%20Method%20Adoption%20for%20Vault%20Architecture) — comparative inquiry across personal knowledge management methods
- [\[\[Vault-Wide Compound Node Adoption\]\]↑](../NODES.html#:~:text=Vault-Wide%20Compound%20Node%20Adoption) — investigation with resolved structure and remaining questions

## Category

Generative form — drives the creation of new knowledge by posing questions.

## Sources

Definition from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 107-108.

## Relations

- relates_to::[\[\[Gloss Form\]\]](Gloss%20Form.html) — inquiries that resolve interpretive questions produce glosses
- relates_to::[\[\[Pattern Form\]\]](Pattern%20Form.html) — inquiries that identify recurring dynamics may crystallize into patterns
- relates_to::[\[\[Decision Form\]\]](Decision%20Form.html) — inquiries that require a choice produce decisions
- relates_to::[\[\[Model Form\]\]](Model%20Form.html) — inquiries that map relationships produce models