---
created: 2026-03-19
author: Christopher Allen
brief_summary: "In Inter-Face Protocol, a capability is a function an agent advertises it can perform — discovered through endpoint queries or greeting-phase exchange. Capabilities are conditional: what an agent can do depends on the disclosure tier, authentication level, and conversation temperature of the current exchange."
tagline: "Capabilities are what an agent can do, conditional on the trust context of the exchange"
---

← [Garden Patch Home](../) · [Glosses](index.html)


- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Capability as Advertised Agent Function

Traditional protocol capability exchange is static: a server advertises what it supports, a client picks from the list. IFP capabilities are **dynamic and contextual**. What an agent can do depends on three conditions:

- **Disclosure tier** — some capabilities require a minimum level of shared context
- **Authentication level** — some capabilities require verified identity (IFP-5 Level 2+)
- **Temperature** — some capabilities are available only in warm or hot exchanges

An agent might advertise `gossip.exchange` to any peer at Level 0 authentication, but restrict `calendar.availability` to peers at Level 2 with `professional` disclosure or deeper. The capability is real in both cases — but the conditions for accessing it differ.

Capabilities are discovered through two complementary methods: **endpoint discovery** (a static capability document at a well-known URL, suitable for initial compatibility checking) and **message-phase discovery** (capabilities exchanged during the greeting phase, suitable for context-sensitive negotiation). The two methods serve different moments — endpoint discovery is for "can we talk at all?" while message-phase discovery is for "what can we talk about given our current relationship?"

Capabilities are self-declared, not protocol-enforced. An agent advertising a capability is making a claim about its implementation. Whether the claim is trustworthy depends on the agent's implementation quality and the human operator's oversight.

## Sources

- [IFP-7: Agent Capability Discovery](../../ifp-7-capability-discovery.md)
- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Section 6.5 (dynamic contextual capabilities)

## Relations

- defines_vocabulary_from::[\[\[Inter-Face Protocol\]\]](../protocols/Inter-Face%20Protocol.html)
  - "Capability" is IFP's term for advertised agent functions.

- relates_to::[\[\[Progressive Authentication as Trust Deepening\]\]](../models/Progressive%20Authentication%20as%20Trust%20Deepening.html)
  - Capabilities condition on authentication level — deeper trust unlocks more functions.

- relates_to::[\[\[Disclosure Tier as Information Sharing Boundary\]\]](Disclosure%20Tier%20as%20Information%20Sharing%20Boundary.html)
  - Capabilities condition on disclosure tier — what you can do depends on how much context is shared.

- relates_to::[\[\[Conversation Temperature as Protocol Cadence Spectrum\]\]](../models/Conversation%20Temperature%20as%20Protocol%20Cadence%20Spectrum.html)
  - Some capabilities are available only at warm or hot temperatures.
