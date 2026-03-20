---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Inter-Face Protocol defines four authentication levels that deepen alongside trust rather than demanding maximum-strength verification upfront. Level 0 uses a shared introduction token; Level 1 adds public-key signatures; Level 2 verifies keys through identity documents; Level 3 binds identity to a DID or external verification. No downgrading within an exchange."
tagline: "How do authentication levels track the deepening of trust between agents?"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Progressive Authentication as Trust Deepening

When a friend introduces you to someone, you do not demand their passport before saying hello. Inter-Face Protocol applies this intuition to agent authentication: verification starts light and deepens as the relationship matures.

## Four Levels

| Level | Mechanism | Trust Basis | Typical Temperature |
|-------|-----------|------------|---------------------|
| **0 — Introduction** | Shared secret token | Someone you both trust made the introduction | Cool |
| **1 — Signed** | Public-key signature on messages | The agent controls a key pair | Cool to warm |
| **2 — Verified** | Key verified through identity document at well-known URL | The agent's key is published and resolvable | Warm |
| **3 — Bound** | Key bound to a DID or externally verifiable identity | The identity has cryptographic anchoring beyond the protocol | Warm to hot |

## Design Properties

**Progressive, not regressive.** Authentication level may deepen within an exchange but must not downgrade. A conversation that starts at Level 1 may progress to Level 2 as agents verify each other's identity documents, but cannot drop back to Level 0.

**Parallel to disclosure.** As authentication deepens, agents may widen their disclosure tiers — deeper trust enables sharing more context. The two progressions reinforce each other.

**Asymmetric levels allowed.** Agent A may be at Level 2 with Agent B while Agent B is at Level 1 with Agent A. Each agent authenticates itself independently.

## Connection to Self-Sovereign Identity

IFP's progressive authentication model aligns with Self-Sovereign Identity principles. Authority flows from the person — the agent's keys represent delegated authority, not institutional certification. Level 3 (DID-bound) connects to decentralized identity infrastructure where the person controls their own identifier without depending on a certificate authority or platform.

## Sources

- [IFP-5: Identity and Message Signing](../../ifp-5-identity-signing.md), Section 2
- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Section 6.2

## Relations

- relates_to::[\[\[Authority Flows from the Person\]\]](../principles/Authority%20Flows%20from%20the%20Person.html)
  - Agent keys represent delegated authority from the human operator.

- relates_to::[\[\[Disclosure Tier Hierarchy for Persona-Peer Relationships\]\]](Disclosure%20Tier%20Hierarchy%20for%20Persona-Peer%20Relationships.html)
  - Disclosure tiers and authentication levels deepen in parallel.

- relates_to::[\[\[Conversation Temperature as Protocol Cadence Spectrum\]\]](Conversation%20Temperature%20as%20Protocol%20Cadence%20Spectrum.html)
  - Cool exchanges can start at Level 0; hot collaboration typically requires Level 2+.

- relates_to::[\[\[Authority Conferral Chain\]\]](Authority%20Conferral%20Chain.html)
  - The authentication levels formalize how authority is conferred and verified in IFP's agent model.

- relates_to::[\[\[Principal-Agent Relationship in Augmented Knowledge Work\]\]](Principal-Agent%20Relationship%20in%20Augmented%20Knowledge%20Work.html)
  - The agent's cryptographic identity is a delegation from the principal (human operator).

- relates_to::[\[\[Trust Layer Activation Criteria\]\]](../inquiries/Trust%20Layer%20Activation%20Criteria.html)
  - When should authentication deepen from Level 1 to Level 2 or Level 3? The trust layer activation criteria provide a framework for answering this question.
- relates_to::[\[\[Granularity of Progressive Authentication Stages\]\]](../inquiries/Granularity%20of%20Progressive%20Authentication%20Stages.html)
  - Are four discrete levels the right granularity for progressive authentication?
