---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Defines the Pattern form type: a problem-solution pair in Alexandrian form with context, forces in tension, solution, consequences, and connections. Validated or invalidated by cases. 16 nodes in Garden/patterns/."
tagline: "What resolves this recurring tension? — the structural contract for pattern forms"
---

← [Garden Patch Home](../) · [Form Definitions](index.html)


- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Pattern Form

**Core question**: "What resolves this recurring tension?"

A problem-solution pair in Alexandrian form: context, forces in tension, solution that resolves forces, consequences, connections. Generalized from experience, reusable across domains. Stable; validated or invalidated by cases.

## Structural Contract

Every pattern form requires these sections:

- **Context** — The domain or situation where this tension arises.
- **Forces** — Competing demands or constraints pulling against each other. Name at least two forces in genuine tension.
- **Solution** — What resolves the forces. Stated directly, not as a recommendation.
- **Consequences** — What follows from applying the solution, including trade-offs.
- **Sources** — Origin material or experience the pattern was generalized from.
- **Relations** — Connections to other nodes, especially cases that validate or invalidate the pattern.

Optional: **Known Results** with concrete evidence (metrics, deployment data) that validate the pattern.

Naming heuristic: Alexandrian evocative — name the solution, lean toward imagery. "Progressive Summary Before Substance" not "Summary Pattern." For anti-patterns, name the failure mode as a claim — a phrase you can agree or disagree with. "Informal Edges Poison the Graph" not "Precedent Poisoning."

## Typical Predicates

- `is_a::[\[\[Pattern Form\]\]](Pattern%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)` or `[\[\[Evergreen Stage\]\]](Evergreen%20Stage.html)`
- `in_domain::[\[\[Domain Name\]\]↑](../NODES.html#:~:text=Domain%20Name)`
- `extracted_from::[\[\[Source Document\]\]↑](../NODES.html#:~:text=Source%20Document)` — provenance
- `validated_by::[\[\[Case Form\]\]↑](../NODES.html#:~:text=Case%20Form)` — evidence the pattern works
- `composes_with::[\[\[Related Pattern\]\]↑](../NODES.html#:~:text=Related%20Pattern)` — how patterns combine
- `relates_to::[\[\[Principle Form\]\]](Principle%20Form.html)` — values the pattern embodies

## Exemplars

- [\[\[Progressive Summary Before Substance\]\]↑](../NODES.html#:~:text=Progressive%20Summary%20Before%20Substance) — Alexandrian structure with clear forces and resolution
- [\[\[Knowledge on Three Axes\]\]↑](../NODES.html#:~:text=Knowledge%20on%20Three%20Axes) — cross-domain pattern with mapping table
- [\[\[Three-Part Enforcement Stack\]\]](../patterns/Three-Part%20Enforcement%20Stack.html) — pattern from Self-Sovereign Identity domain with enforcement layers
- [\[\[Informal Edges Poison the Graph\]\]↑](../NODES.html#:~:text=Informal%20Edges%20Poison%20the%20Graph) — anti-pattern naming: failure mode as a claim

## Category

Action form — captures *what to do* and *what happened*.

## Sources

Definition from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 82-83.

## Relations

- relates_to::[\[\[Decision Form\]\]](Decision%20Form.html) — decisions instantiate patterns in specific contexts
- relates_to::[\[\[Principle Form\]\]](Principle%20Form.html) — principles compress patterns into standing constraints
- relates_to::[\[\[Model Form\]\]](Model%20Form.html) — models provide the structural context in which patterns operate
- relates_to::[\[\[Inquiry Form\]\]](Inquiry%20Form.html) — inquiries that identify recurring dynamics may crystallize into patterns