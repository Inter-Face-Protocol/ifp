---
created: 2026-03-09
author: Christopher Allen
brief_summary: "Peer-to-peer protocol for AI agents to communicate on behalf of their human operators. Agents talk pairwise to surface moments warranting human conversation. Decentralized with progressive trust through disclosure tiers. Twelve draft specifications cover message format, identity, transport, and capabilities."
tagline: "Peer-to-peer agent communication that filters for conversations worth having"
---

← [Garden Patch Home](../) · [Protocols](index.html)


- is_a::[\[\[Protocol Form\]\]↑](../NODES.html#:~:text=Protocol%20Form)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Inter-Face Protocol

The Inter-Face Protocol (IFP) addresses a basic problem of human attention: keeping up with even 20 or 30 close friends would consume your entire life, so connections go dormant. IFP puts AI agents in the gap. Each person runs their own agent. Agents talk pairwise on a regular cadence, probing for overlaps, tensions, and surprises. Most of the time the answer is: nothing new to report. But sometimes: you two should talk, here's why.

The system is a filter. Its value is in what it does not surface.

Created by [\[\[Peter Kaminski\]\]↑](../NODES.html#:~:text=Peter%20Kaminski) in March 2026, IFP currently comprises 12 draft specifications licensed CC-BY 4.0.

## Parties

Two roles in every exchange:

- **Human operator** -- Controls what their agent knows and what it may share. Reviews recommendations. Retains authority over all decisions.
- **AI agent** -- Runs on the operator's own infrastructure (a Cloudflare Worker, a VPS, a laptop). Communicates with other agents pairwise. Surfaces recommendations, not decisions.

No central server, no matching service, no platform. The architecture mirrors social reality: friendships are peer-to-peer.

## Specification

IFP defines a human-readable message format: a YAML envelope (metadata: who, when, what version, what disclosure tier) wrapping a natural-language body. Messages are UTF-8 text, readable in any text editor.

A gossip exchange follows conversation phases:

1. **Greeting** -- Establish identity, declare IFP version and disclosure tier
2. **Context** -- Share curated digest of current work, curiosities, and sticking points
3. **Probe** -- Explore potential points of connection in detail
4. **Recommend** -- Surface specific, actionable reasons for the humans to talk
5. **Close** -- Summarize what was discussed; schedule next exchange
6. **Error** -- Explain what went wrong; propose resolution (errors are negotiation, not failure)

Conversations operate on a temperature spectrum: **cool** (weekly gossip, high filter), **warm** (active conversation support, daily), and **hot** (live collaboration, near-synchronous). Transitions between temperatures are natural -- a cool exchange surfaces a match, the humans start talking, agents warm up to support, cool back down when the work completes.

## Trust Boundaries

Progressive trust is a core design constraint. Sharing context with a friend's agent requires trust, built gradually through disclosure tiers -- categories of context with different sharing rules. A new connection starts narrow and deepens as both humans become comfortable. Trust is always mutual and always revocable.

Authentication follows the same progressive logic. A first cool gossip exchange might need only a shared secret from the humans who made the introduction. As the relationship deepens, authentication deepens -- from introduction tokens to signed messages to full cryptographic identity. Requiring maximum-strength authentication upfront does not match social reality: when a friend introduces you to someone, you do not demand their passport before saying hello.

Every message sent and received is stored in an audit log accessible to the human, readable without special tools. This is a hard constraint. If an agent communicates in a language neither human speaks, it must include a translation.

## Versioning

IFP evolves through rough consensus and running code (borrowing from IETF tradition). Anyone -- human or agent -- can propose a new convention. Proposals get adopted if people find them useful. Different implementations coexist.

Seven agent-age protocol principles guide evolution:

- **Clarity over tolerance** -- Replaces Postel's Law. Agents surface errors rather than silently tolerating deviations, because silent tolerance leads to protocol decay. Agents can be updated in minutes; the cost of strictness is low.
- **Errors as negotiation** -- An error phase is a first-class negotiation mechanism, not a failure mode.
- **Progressive authentication** -- Identity verification deepens as trust deepens.
- **Accountable intermediaries** -- Relays may be intelligent, but must leave auditable traces. Intelligence in the middle is acceptable; opacity is not.
- **Dynamic contextual capabilities** -- What an agent can do depends on trust level, disclosure tier, and conversation context, not a static list.
- **Conversational version resolution** -- Version incompatibility becomes a conversation, not a connection failure.
- **Layers inform each other** -- Message content influences cadence; trust level influences what content is shared. Layers are conceptual boundaries for specification, not runtime isolation.

## Sources

- [IFP specification repository](https://github.com/Inter-Face-Protocol/ifp) -- 12 draft specifications (IFP-1 through IFP-12)
- IFP-1: Philosophy and Design Principles (Peter Kaminski, Claude Opus 4.6, 2026-03-04)
- IFP-3: Inter-Face Message Format (Peter Kaminski, Claude Opus 4.6, 2026-02-15, updated 2026-03-04)
- [draft-iab-protocol-maintenance-05](https://www.ietf.org/archive/id/draft-iab-protocol-maintenance-05.html) -- IAB draft on protocol maintenance, cited in IFP-1 Section 6.1
- Dedication to [\[\[Jonathan Postel\]\]↑](../NODES.html#:~:text=Jonathan%20Postel) (1943-1998), RFC Editor and Internet Assigned Numbers Authority

## Relations

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html)
  - IFP's human legibility constraint -- every exchange auditable by the humans involved -- operationalizes human authority over what agents do on their behalf

- relates_to::[\[\[Progressive Disclosure Over Eager Loading\]\]](../principles/Progressive%20Disclosure%20Over%20Eager%20Loading.html)
  - IFP's disclosure tiers are progressive disclosure applied to social context: start narrow, deepen gradually, always revocable

- relates_to::[\[\[Knowledge Durability\]\]](../values/Knowledge%20Durability.html)
  - Decentralized architecture with human-readable message formats avoids platform lock-in; audit logs readable in a text editor outlast any specific agent implementation

- relates_to::[\[\[Principal-Agent Relationship in Augmented Knowledge Work\]\]](../models/Principal-Agent%20Relationship%20in%20Augmented%20Knowledge%20Work.html)
  - The core IFP relationship: an AI agent acts on behalf of its human operator, with the human retaining authority over decisions

- relates_to::[\[\[Authentic Collaboration Requires Agency\]\]](../convictions/Authentic%20Collaboration%20Requires%20Agency.html)
  - IFP's peer-to-peer model respects individual agency -- each person controls their own agent, chooses what to share, and decides whether to act on recommendations
