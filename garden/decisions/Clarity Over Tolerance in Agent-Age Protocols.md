---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Inter-Face Protocol explicitly replaces Postel's Law ('be liberal in what you accept') with a clarity-first principle for agent-age protocols. When agents can be updated in minutes, silent tolerance of deviations entrenches errors as workarounds. Strict error reporting with natural-language negotiation enables rapid correction."
tagline: "Why did IFP replace Postel's Law with strict error reporting and conversational resolution?"
---

← [Garden Patch Home](../) · [Decisions](index.html)


- is_a::[\[\[Decision Form\]\]](../forms/Decision%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Clarity Over Tolerance in Agent-Age Protocols

## Context

Postel's Law — "be conservative in what you send, be liberal in what you accept" — has guided internet protocol design since 1981 (RFC 793). It worked when fixing remote bugs was hard: tolerating minor deviations kept communication flowing while the other party updated their implementation over months or years.

## The Decision

Inter-Face Protocol replaces Postel's tolerance principle with a clarity-first approach:

> **Be clear in what you send; be explicit when you don't understand.** (IFP-1 Section 6.1)

## Alternatives Considered

| Approach | Argument For | Argument Against |
|----------|-------------|-----------------|
| **Postel's Law (traditional)** | Proven over 40+ years of internet protocols; maximizes interoperability | Tolerating deviations entrenches errors as undocumented features |
| **Strict rejection** | Clear semantics, no ambiguity | Brittle; minor format variations cause unnecessary failures |
| **Clarity + negotiation (chosen)** | Surfaces errors for correction while allowing conversational resolution | Requires agents capable of natural-language error resolution |

## Reasoning

The assumption behind Postel's Law — that fixing remote bugs is expensive and slow — no longer holds for reasoning agents. An AI agent can be updated in minutes. When one agent sends a malformed message, the receiving agent's explicit error report enables immediate correction. Silent tolerance would instead entrench the deviation, as agents learn that the malformed version "works."

The chosen approach combines strict reporting with a unique mitigation: **errors as negotiation**. Rather than returning a mechanical error code, the receiving agent describes what it did not understand in natural language, giving the sending agent an opportunity to rephrase or clarify. This preserves the spirit of Postel's tolerance (keep communication flowing) while eliminating its failure mode (errors become invisible).

## Consequences

- Agents must implement natural-language error descriptions (not just error codes)
- Deviations from the protocol surface immediately rather than accumulating as silent workarounds
- Protocol evolution happens through explicit proposals (new IFPs), not through tolerated deviations becoming de facto standards
- Requires that agents be sophisticated enough to negotiate — not suitable for simple clients

## Sources

- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Section 6.1
- Jon Postel, RFC 793 (1981), Section 2.10 — original robustness principle
- IFP-1 dedicates itself to Jon Postel, acknowledging the respectful disagreement

## Relations

- relates_to::[\[\[Errors as Negotiation Opportunities\]\]](../patterns/Errors%20as%20Negotiation%20Opportunities.html)
  - The pattern that makes clarity-over-tolerance viable — errors become conversations, not failures.

- relates_to::[\[\[Agent as Human Proxy in Protocol Exchange\]\]](../glosses/Agent%20as%20Human%20Proxy%20in%20Protocol%20Exchange.html)
  - This decision assumes reasoning agents that can negotiate — it would not apply to simple protocol clients.

- relates_to::[\[\[Social Conversation Phases as Protocol Semantics\]\]](../models/Social%20Conversation%20Phases%20as%20Protocol%20Semantics.html)
  - The error phase implements conversational resolution, enabling clarity without brittleness.
- relates_to::[\[\[Structured Schema vs Natural Language for Agent Message Content\]\]](../inquiries/Structured%20Schema%20vs%20Natural%20Language%20for%20Agent%20Message%20Content.html)
  - The clarity principle may be in tension with natural language bodies that resist validation.
