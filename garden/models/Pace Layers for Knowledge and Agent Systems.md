---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Stewart Brand's six pace layers — fashion, commerce, infrastructure, governance, culture, nature — mapped to both garden form types and agent platform components. Fast layers experiment, slow layers remember. Forced synchronization between layers at different rates destroys the system. Each component has a characteristic rate of change."
tagline: "Fast learns, slow remembers — forced synchronization across different rates of change destroys systems"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Pace Layers for Knowledge and Agent Systems

**Each component in a system has a characteristic rate of change, and forcing components at different rates into synchronization destroys the system.** Stewart Brand formalized this insight in his pace layering model: civilization operates as a stack of layers moving at different speeds, from fast-changing fashion at the top to slow-changing nature at the bottom. The health of the whole depends on each layer moving at its own pace while the layers interact at their boundaries.

## Brand's Six Layers

From fastest to slowest: fashion, commerce, infrastructure, governance, culture, nature. Fast layers innovate and absorb shocks. Slow layers provide continuity and integrate tested innovations. "Fast learns, slow remembers. Fast proposes, slow disposes."

Brand's example of forced coupling: the Soviet Union attempted to run governance at the speed of fashion — constant policy change driven by ideology rather than tested results. The system collapsed because governance needs stability to function, and the layers beneath it (culture, nature) could not adapt at the pace being demanded.

## Mapping to Garden Form Types

| Pace Layer | Garden Equivalent | Rate of Change |
|---|---|---|
| Fashion | Seeds, inbox captures, clippings | Days to weeks — high creation, high abandonment |
| Commerce | Inquiries, citations, research notes | Weeks to months — active investigation |
| Infrastructure | Models, patterns, references | Months to years — structural knowledge |
| Governance | Conventions, form definitions | Years — change requires community alignment |
| Culture | Principles, convictions | Years to decades — deep commitments |
| Nature | Domain definitions | Decades — fundamental categories |

A seed note may be created and abandoned in a single session. A principle takes months of accumulated evidence before it earns confidence. Treating seeds with the rigor appropriate to principles wastes effort; treating principles with the casualness appropriate to seeds erodes trust in the garden.

## Mapping to Agent Platform Components

| Pace Layer | Agent System Equivalent | Rate of Change |
|---|---|---|
| Fashion | Prompts, session configuration | Per-session |
| Commerce | Skills, tools, workflows | Per-sprint |
| Infrastructure | APIs, data schemas, protocols | Per-quarter |
| Governance | Access control, compliance rules | Per-year |
| Culture | Organizational trust, norms | Multi-year |
| Nature | Core identity, mission | Foundational |

An agent platform that changes its API at the speed it changes prompts will break every downstream consumer. A platform that changes its prompts at the speed it changes compliance rules will be unable to experiment. The design imperative is to identify each component's natural pace and resist the pressure to synchronize them.

## The Living Document Connection

This model explains why [\[\[Living Documents Over Static Publications\]\]](../principles/Living%20Documents%20Over%20Static%20Publications.html) works in a garden but would fail in a legal code. Garden nodes are designed to change at the fashion-to-infrastructure pace range. Legal codes operate at the governance layer and need the stability of formal amendment processes. The form type determines the appropriate pace; the pace determines the appropriate editing discipline.

## Sources

Grounded in [\[\[Brand (2018) Pace Layering\]\]](../citations/Brand%20%282018%29%20Pace%20Layering/Brand%20%282018%29%20Pace%20Layering.html), which extended his earlier work in *How Buildings Learn* (1994) to civilization-scale systems.

## Relations

- relates_to::[\[\[Living Documents Over Static Publications\]\]](../principles/Living%20Documents%20Over%20Static%20Publications.html)
  - Living documents work because garden nodes operate at pace layers where continuous revision is appropriate.

- relates_to::[\[\[Systems Thinking\]\]↑](../NODES.html#:~:text=Systems%20Thinking)
  - Pace layering is a systems thinking pattern — the health of the whole depends on the interaction dynamics between layers, not the behavior of any single layer.

- relates_to::[\[\[Collaborative Meeting as Composable Knowledge Pipeline\]\]](Collaborative%20Meeting%20as%20Composable%20Knowledge%20Pipeline.html)
  - The seven pipeline stages operate at different pace layers — transcript cleanup (minutes) to garden seeding (hours) to workstream closure (days).
