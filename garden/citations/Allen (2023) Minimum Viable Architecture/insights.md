---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Insights from applying the minimum viable architecture principle to IFP — what the exercise reveals about protocol design methodology, the relationship between architecture and experimentation, and patterns transferable to other agent protocol efforts."
tagline: "What does the architectural/tactical distinction reveal about agent protocol design?"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)

# Insights: Minimum Viable Architecture and Agent Protocol Design

## Insight 1: IFP's Load-Bearing Decisions Are Philosophical, Not Technical

The most load-bearing IFP decisions are not about message formats or transport protocols. They are about the relationship between humans and agents: gossip-as-filter, human legibility, progressive trust. The minimum viable architecture of an agent protocol is a **philosophy of human-agent interaction**, not a technical specification.

This suggests that agent protocol design should start with philosophical commitments (what is the human's role? what is the agent's role? who holds authority?) and derive technical decisions from those commitments — not the other way around.

## Insight 2: The "Uncertain" Category Is Where Dialogue Lives

The most productive area for dialogue between the garden patch and IFP's specifications is not the clearly architectural decisions (which are well-reasoned) or the clearly tactical ones (which can change freely). It is the **uncertain decisions** — the ones where it is not yet clear whether the choice is load-bearing or tactical.

Each of the six inquiries in this patch targets an uncertain decision. The dialogue value is in helping Peter Kaminski and the IFP community distinguish which of these deserve architectural commitment and which should remain open to refinement.

## Insight 3: Minimum Viable Architecture as a Protocol Maturity Test

Applying the minimum viable architecture principle to an existing specification set functions as a **maturity test**. A specification that has clearly separated its load-bearing decisions from its tactical choices is ready for implementation experimentation. One that has not may find that implementers accidentally treat tactical choices as constraints, or inadvertently change load-bearing decisions.

IFP's current state: the load-bearing decisions are well-articulated (IFP-1 is strong), but the boundary between architectural and tactical in IFP-5, IFP-11, and IFP-12 could be made more explicit.

## Sources

- [\[\[Allen (2023) Minimum Viable Architecture\]\]](Allen%20%282023%29%20Minimum%20Viable%20Architecture.html) — the source principle
- Analysis in this compound citation
