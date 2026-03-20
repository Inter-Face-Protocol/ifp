---
created: 2026-03-19
author: Christopher Allen
brief_summary: "In Inter-Face Protocol, an agent is autonomous software that acts on behalf of a human operator — not as an independent actor, but as a proxy whose authority derives from and returns to the person. The agent's autonomy is bounded: it may filter, exchange, and probe, but the human decides whether to act on what the agent surfaces."
tagline: "An agent acts on behalf of a person, never in place of one"
---

← [Garden Patch Home](../) · [Glosses](index.html)


- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Agent as Human Proxy in Protocol Exchange

"Agent" has many meanings in technology: autonomous software (AI agents), browser user-agent strings, agent-based modeling. Inter-Face Protocol uses the term with a specific meaning rooted in agency law: an agent is software that **acts on behalf of** a human operator.

The distinction matters because it determines accountability. An IFP agent does not pursue its own goals. It pursues its operator's goals within bounds the operator sets. The agent may filter information, exchange context with other agents, and probe for overlaps — but when something worth human attention emerges, the agent surfaces a recommendation. The human decides whether to act.

This maps directly to the principal-agent relationship from agency law: the human is the **principal** (the authority), the agent is the **delegate** (the proxy). Authority flows from the person, not from the software. The agent's autonomy is real but bounded — it can do social sensing work the human cannot do at scale, but it cannot commit the human to action.

IFP's agent model differs from autonomous AI agent frameworks where agents act independently, chain tool calls, and make decisions without human checkpoints. In IFP, the Human-Agent-Agent-Human (HAAH) chain preserves human authority at both ends.

## Sources

- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Sections 2, 5
- [IFP-9: Ecosystem Status](../../ifp-9-ecosystem-status.md), Minimum Viable Agent

## Relations

- defines_vocabulary_from::[\[\[Inter-Face Protocol\]\]](../protocols/Inter-Face%20Protocol.html)
  - "Agent" is IFP's core actor type.

- relates_to::[\[\[Principal-Agent Relationship in Augmented Knowledge Work\]\]](../models/Principal-Agent%20Relationship%20in%20Augmented%20Knowledge%20Work.html)
  - The principal-agent model maps IFP's human-agent relationship to agency law.

- relates_to::[\[\[Authority Flows from the Person\]\]](../principles/Authority%20Flows%20from%20the%20Person.html)
  - The agent's authority derives from and is revocable by the human operator.

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html)
  - IFP agents augment human judgment; they do not substitute for it.

- relates_to::[\[\[Delegated Decision Authority Spectrum\]\]](../boundaries/Delegated%20Decision%20Authority%20Spectrum.html)
  - IFP agents operate primarily in the "autonomous" and "propose-and-approve" zones — they filter autonomously but propose recommendations for human approval.
- relates_to::[\[\[Authority Conferral Chain\]\]](../models/Authority%20Conferral%20Chain.html)
  - The authority conferral chain formalizes the delegation model IFP agents operate within.
