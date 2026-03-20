---
created: 2026-03-04
author: Christopher Allen
brief_summary: "Boundary form defining four zones of decision authority — autonomous, propose-and-approve, human-only, and group-deliberative — applicable to any agent (LLM, delegate, automated system) operating within a deep context garden."
tagline: "Four authority zones that determine who may decide what within a garden"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Boundaries](index.html)


- is_a::[\[\[Boundary Form\]\]](../forms/Boundary%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Delegated Decision Authority Spectrum

A system that captures personal reasoning must distinguish between what an agent can decide and what requires human judgment. This is not binary — it is a spectrum with four zones, each carrying different authority levels and different accountability expectations.

The spectrum applies to any agent operating on behalf of a garden's owner: an LLM, a human delegate, an automated pipeline. The zones define what moves each agent may make.

## Authority Zones

| Zone | Authority | Examples |
|------|-----------|---------|
| **Autonomous** | Agent acts without asking | Traverse graph, synthesize glosses from sources, follow existing principles |
| **Propose-and-approve** | Agent drafts, human approves | New typed relations, new references, extracted principles, pattern drafts, inquiry hypotheses |
| **Human-only** | Agent may not decide | Modify principles/values/convictions, resolve principle tensions, change boundaries |
| **Group-deliberative** | Requires collective process | Amend governance boundaries, establish new protocols, publish shared artifacts, resolve inquiry questions marked with `directed_at::` |

## Agent Behavior at Boundaries

When an agent encounters a decision it may not make, it should:

1. Recognize it has reached a boundary
2. Present the context it has gathered (relevant forms, edges, tensions)
3. Frame the decision clearly for the human or group
4. Wait for a decision, then record it as a case

The `directed_at::` predicate on inquiry forms explicitly flags questions requiring a specific person's or group's judgment. An agent encountering `directed_at::` treats this as a hard boundary — it can frame the question and provide supporting context, but it cannot answer on behalf of the named party.

## Amendment

Boundaries themselves are forms in the graph, connected to the values and principles that justify them. They are amendable through deliberative process, never unilaterally by an agent.

### HAAH Spectrum Extension

The four-zone model above describes a single principal and single agent. Peter Kaminski raised the question of what happens when the chain extends: Human → Agent → Agent → Human (HAAH). In multi-agent workflows, a human principal confers authority to an AI agent, which then delegates sub-tasks to other agents, whose outputs eventually reach another human for review or use.

The HAAH spectrum introduces compounding authority questions at each handoff:

- **First H→A boundary**: The principal's conferral to the first agent. Governed by the four zones above.
- **A→A boundary**: Agent-to-agent delegation. The first agent cannot confer more authority than it holds. Scope narrows or stays constant at each hop — it never widens.
- **A→H boundary**: The receiving human may not be the original principal. Their authority to act on the output depends on their own relationship to the principal, not to the agent.

The three conditions for meaningful authority (legibility, boundaries, override) must hold at each boundary in the chain, not only at the endpoints. A chain where the first and last humans have authority but intermediate agents operate opaquely is nominally accountable but structurally unauditable.

This extension remains exploratory. The four-zone model is stable for single-principal single-agent relationships. Multi-agent chains need further analysis of how conferral scope compounds across hops.

## Sources

Extracted from the "Decision Boundaries" section of the deep context architecture.

## Relations

- implements::[\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html)
  - The four-zone authority table and agent behavior guidance originate from the Decision Boundaries section of the architecture document.

- grounded_in::[\[\[Autonomy\]\]↑](../NODES.html#:~:text=Autonomy)
  - The spectrum exists because the garden owner's autonomy requires that agents know where their authority ends.

- embodies::[\[\[Progressive Trust\]\]↑](../NODES.html#:~:text=Progressive%20Trust)
  - Authority is granted progressively — an agent proves competence at lower zones before being trusted with higher-authority actions.

- relates_to::[\[\[Principal-Agent Relationship in Augmented Knowledge Work\]\]](../models/Principal-Agent%20Relationship%20in%20Augmented%20Knowledge%20Work.html)
  - The four authority zones operationalize the model's boundary condition for this vault.

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html)
  - The spectrum implements the principle that human authority must be preserved at every decision level.
