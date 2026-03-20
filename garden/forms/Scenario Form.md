---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Scenario form type: a plausible narrative of how the future could unfold given specific drivers and conditions. Scenarios don't predict — they prepare. Value lies in spanning the possibility space. Names state the hypothetical trajectory, not the driving forces."
tagline: "What might happen if these forces play out? — the structural contract for scenario forms"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Forms](index.html)


- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Scenario Form

**Core question**: "What might happen if these forces play out?"

A plausible narrative of how the future could unfold given specific drivers and conditions. Distinguished from a case (which records what happened) by being hypothetical and forward-looking. Distinguished from an inquiry (which asks what to investigate) by committing to a specific imagined trajectory.

Scenarios don't predict — they prepare. Their value lies in spanning the possibility space, not picking the most likely future. Often come in sets (the Dator archetypes: growth, constraint, collapse, transformation). A scenario validated by events becomes a case; one that reveals recurring dynamics may crystallize into a pattern.

## Structural Contract

Every scenario form requires:

- **Drivers and forces** — What conditions and trends drive this scenario.
- **Narrative** — How the forces interact and play out over time.
- **Implications** — What follows for the system or actor if this scenario unfolds.
- **Signals** — What to watch for that would confirm or disconfirm this trajectory.
- **Sources** — Data, trends, or analyses informing the scenario.
- **Relations** — Connections to other scenarios in the same set, patterns it might validate, cases it could become.

Naming heuristic: state the hypothetical trajectory or end state. Name what might happen, not the forces driving it. "Knowledge Graph as Digital Twin of Principal Reasoning" not "Delegation Scenario."

## Typical Predicates

- `is_a::[[Scenario Form]]`
- `has_status::[[Seed Stage]]` or `[[Growing Stage]]`
- `in_domain::[[Domain Name]]`
- `set_with::[[Scenario Form]]` — other scenarios in the same possibility set
- `may_validate::[[Pattern Form]]` — patterns this scenario could confirm
- `driven_by::[[Model Form]]` — models that inform this scenario's drivers

## Exemplars

- [\[\[Thousand Gardens with Autonomous Trust\]\]](../scenarios/Thousand%20Gardens%20with%20Autonomous%20Trust.html) — what happens when gardens become autonomous cryptographic objects that trust each other progressively
- [\[\[Knowledge Graph as Digital Twin of Principal Reasoning\]\]↑](../NODES.html#:~:text=Knowledge%20Graph%20as%20Digital%20Twin) — what happens when gardens grow dense enough that agents shift from augmentation toward delegation

## Category

Generative form — drives the creation of new knowledge by imagining futures.

## Sources

Definition from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 110-111.

## Relations

- relates_to::[\[\[Inquiry Form\]\]](Inquiry%20Form.html) — inquiries investigate; scenarios imagine specific trajectories
- relates_to::[\[\[Case Form\]\]↑](../NODES.html#:~:text=Case%20Form) — validated scenarios become cases
- relates_to::[\[\[Pattern Form\]\]](Pattern%20Form.html) — scenarios revealing recurring dynamics may crystallize into patterns
- relates_to::[\[\[Model Form\]\]](Model%20Form.html) — models provide the structural context scenarios project forward
