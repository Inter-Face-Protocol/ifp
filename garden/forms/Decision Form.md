---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Defines the Decision form type: a recorded choice with reasoning, alternatives considered, and consequences. Structural contract requires Context, Decision, Consequences, and Alternatives Considered sections in order. Distinguished from cases (which narrate what happened) by being forward-looking and from principles by being situation-specific."
tagline: "Why did we choose this over the alternatives? — the structural contract for decision forms"
---

← [Garden Patch Home](../) · [Form Definitions](index.html)


- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Decision Form

**Core question**: "Why did we choose this over the alternatives?"

A recorded choice with its reasoning, alternatives considered, and consequences. Distinguished from a case (which narrates what happened) by being forward-looking at time of writing. Distinguished from a principle (which states a standing constraint) by being specific and contextual — a decision applies to a particular situation, while a principle applies broadly.

## Structural Contract

Every decision form requires these sections in order:

- **Context** — Why this decision was needed. What problem or tension prompted it.
- **Decision** — What was chosen. State the choice clearly and directly.
- **Consequences** — What follows, both positive and negative.
- **Alternatives Considered** — What else was evaluated and why it was rejected.

Decisions carry a `status` field in frontmatter (`proposed`, `accepted`, `deprecated`, `superseded`). The `supersedes::` predicate chains decisions when a choice is revisited. Each decision has a descriptive name, not a number.

## Typical Predicates

- `is_a::[\[\[Decision Form\]\]](Decision%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)` or `[\[\[Growing Stage\]\]](Growing%20Stage.html)`
- `in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)`
- `supersedes::[\[\[Previous Decision\]\]↑](../NODES.html#:~:text=Previous%20Decision)` — chains revised decisions
- `extended_by::[\[\[Follow-Up Decision\]\]↑](../NODES.html#:~:text=Follow-Up%20Decision)` — marks refinements
- `extracted_from::[\[\[Source Document\]\]↑](../NODES.html#:~:text=Source%20Document)` — provenance
- `informs::[\[\[Related Form\]\]↑](../NODES.html#:~:text=Related%20Form)` — downstream effects

## Exemplars

- [\[\[Classification via Predicates Not Tags\]\]↑](../NODES.html#:~:text=Classification%20via%20Predicates%20Not%20Tags) — canonical example with clear context/decision/consequences/alternatives
- [\[\[Artifact Predicate for Binary Metadata\]\]↑](../NODES.html#:~:text=Artifact%20Predicate%20for%20Binary%20Metadata) — introduces a new predicate with rationale
- [\[\[Extraction Model for Garden Migration\]\]↑](../NODES.html#:~:text=Extraction%20Model%20for%20Garden%20Migration) — reframes an entire approach (D6)

## Category

Action form — captures *what to do* and *what happened*.

## Sources

Definition from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 90-95.

## Relations

- relates_to::[\[\[Boundary Form\]\]](Boundary%20Form.html) — boundaries constrain what decisions an agent can make
- relates_to::[\[\[Principle Form\]\]](Principle%20Form.html) — principles provide standing constraints; decisions apply them to specific situations
- relates_to::[\[\[Pattern Form\]\]](Pattern%20Form.html) — patterns generalize from decisions; decisions instantiate patterns