---
created: 2026-03-07
author: Christopher Allen
brief_summary: "The value that a knowledge system should capture how its owner actually reasons — the web of values, principles, patterns, and cases that inform decisions — not merely store facts and documents. Fidelity means an agent working from the garden can make decisions consistent with how the owner actually thinks."
tagline: "Capture how someone reasons, not just what they know — so agents can decide as their owner would"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Values](index.html)


- is_a::[\[\[Value Form\]\]](../forms/Value%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Reasoning Fidelity

## The Value

A knowledge system should capture how its owner actually reasons. Not what they've read, not what they've bookmarked, not what they've tagged — but the reasoning substrate: the values they hold, the principles they apply, the patterns they've observed, the cases they've lived through, and the connections between all of these.

Fidelity here means correspondence between the garden and the gardener's mind. An agent traversing a garden with high reasoning fidelity can make decisions consistent with how the owner actually thinks. An agent traversing a garden with low reasoning fidelity — one that stores facts but not reasoning — produces answers that are technically informed but personally wrong.

## Scope

Reasoning fidelity applies wherever a knowledge system serves decision-making, not just information retrieval. It distinguishes deep context architecture from encyclopedic knowledge management, from document management, and from AI fine-tuning approaches that try to replicate personality rather than capture reasoning.

The value does not demand completeness. A garden with three well-connected principles and two grounding cases has higher reasoning fidelity than a vault with a thousand loosely-tagged notes. Fidelity is about the quality of the reasoning web, not the volume of captured knowledge.

## Tensions

- **Reasoning fidelity vs. comprehensiveness**: A gardener might capture everything they encounter, producing a comprehensive but low-fidelity archive. Reasoning fidelity asks: does this knowledge help an agent decide as I would? If not, it's reference material, not reasoning substrate.
- **Reasoning fidelity vs. efficiency**: Capturing reasoning is slower than capturing facts. Writing a conviction with grounding and implications takes more effort than clipping an article. The value says the effort is worth it because the downstream decisions will be better.
- **Reasoning fidelity vs. objectivity**: A garden faithful to one person's reasoning is inherently subjective. This is a feature, not a bug — the goal is fidelity to *this person's* reasoning, not to some universal truth. Different gardeners may hold different convictions and reach different conclusions from the same evidence.

## Sources

- [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html) — "The Problem" section articulates the gap between storing facts and capturing reasoning substrate
- The five requirements in the architecture doc (typed forms, traversable relations, progressive disclosure, decision boundaries, learning through use) all serve reasoning fidelity

## Relations

- generates::[\[\[Values Precede Technical Decisions\]\]](../convictions/Values%20Precede%20Technical%20Decisions.html)
  - Reasoning fidelity is one of the values that precedes and directs technical decisions in the architecture.

- generates::[\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html)
  - Fidelity to *human* reasoning requires that the human remains the authority — an agent that overrides the owner's reasoning has broken fidelity.

- generates::[\[\[Progressive Summary Before Substance\]\]↑](../NODES.html#:~:text=Progressive%20Summary%20Before%20Substance)
  - Progressive disclosure serves reasoning fidelity by loading reasoning context on demand rather than requiring the full graph.

- relates_to::[\[\[Knowledge Durability\]\]](Knowledge%20Durability.html)
  - Reasoning captured in a format that doesn't survive tool changes loses its fidelity over time.

- contradicts::[\[\[Autonomy\]\]↑](../NODES.html#:~:text=Autonomy)
  - Mild tension: a fully autonomous agent might reason differently than its owner. Reasoning fidelity constrains agent autonomy to stay within the owner's reasoning patterns.
