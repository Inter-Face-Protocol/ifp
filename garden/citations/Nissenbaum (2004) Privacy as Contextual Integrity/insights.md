---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Insights from Nissenbaum's contextual integrity framework — disclosure as normative governance rather than access control, personas and contexts as the same boundary, aggregation as context collapse, and a testable standard for privacy evaluation."
tagline: "Disclosure tiers define normative contexts, not just access levels — and aggregation is context collapse"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)

# Insights: Privacy as Contextual Integrity

## Disclosure as Normative Governance, Not Access Control

The garden's existing Disclosure Tier concept frames disclosure as a boundary problem: which information crosses which boundary under which conditions. This is access control with graduated permissions. Contextual integrity reframes disclosure as normative governance: each tier is not a permission level but a social context with its own norms about what flows are appropriate.

The difference matters in practice. Access control asks "does this entity have permission to see this data?" Normative governance asks "is this flow appropriate given the relationship, the information type, and the terms of exchange?" The second question catches violations that the first misses — a party may have been granted access but use the information in ways that violate the norms of the context where it was shared. Revoking access after the fact does not undo the norm breach. The Disclosure Tier gloss could strengthen by explicitly stating that tiers define normative contexts, not just access levels.

## Personas and Contexts as the Same Boundary

If contexts define appropriate information flows, and personas emerge from the contexts a person participates in, then disclosure tiers and persona boundaries describe the same structure from different angles. A disclosure tier viewed from the information's perspective is: "this data flows within this context." A persona viewed from the identity holder's perspective is: "I present this facet within this context." The tier boundary and the persona boundary coincide because they are both expressions of the context boundary.

This convergence has a design implication. Systems that manage personas separately from disclosure policies are maintaining two representations of the same thing. A persona IS a disclosure policy — the set of claims, behaviors, and history that a person makes available within a given context. When a new context forms (a new peer relationship, a new institutional role), both a new persona facet and a new disclosure tier emerge simultaneously. They do not need to be created and managed as separate objects.

## Aggregation as Context Collapse

Nissenbaum's explanation of why aggregating public data violates privacy maps directly to the "context collapse" problem in social media research. Each individual datum was shared in a specific context with specific norms. Aggregation creates a new composite that exists in no natural context — it was never shared as a bundle under any set of norms. The aggregator has constructed an information type that the data subject never consented to, in a transmission context that never existed.

For agent systems, this means that data minimization is not just a technical efficiency — it is a normative requirement. An agent that collects minimal data per context and does not aggregate across contexts preserves contextual integrity. An agent that builds comprehensive profiles by combining disclosures from multiple contexts violates it, regardless of whether each individual disclosure was consensual.

## What This Adds to the Garden

The existing Self-Sovereign Identity domain treats privacy as a design goal. Contextual integrity provides the philosophical mechanism that explains when and why privacy is maintained or violated. It converts privacy from a vague aspiration ("we respect privacy") into a testable property ("does this flow conform to the norms of this context?"). The five-parameter model gives the garden a shared vocabulary for evaluating any proposed disclosure mechanism against a single standard.
