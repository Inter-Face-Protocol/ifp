---
created: 2026-03-19
author: Christopher Allen
brief_summary: "In Inter-Face Protocol, a recommendation is what survives the gossip filter — a suggestion that two humans should talk, surfaced by agents only when an overlap is actionable, timely, and specific. Recommendations are the protocol's primary output to humans, and their quality measures the system's value."
tagline: "A recommendation is what survives the gossip filter and reaches the human"
---

← [Garden Patch Home](../) · [Glosses](index.html)


- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Recommendation as Surfaced Opportunity

Most agent-to-agent exchanges produce no recommendation. That silence is the system working correctly. A recommendation emerges only when agents detect an overlap between their operators' contexts that meets a high bar: the overlap must be **actionable** (the humans can do something about it), **timely** (the moment matters), and **specific** (vague affinity is not enough).

The recommendation is the protocol's primary output to the human. It arrives through the "recommend" conversation phase (IFP-3) after agents have progressed through greeting, context exchange, and probing. The human receiving a recommendation sees what the overlap is, which persona context generated it, and enough information to decide whether to act — without needing to read the full agent exchange.

This design choice separates Inter-Face from notification-driven systems. A notification says "something happened." A recommendation says "here is a specific reason you and this person should talk, based on context your agents exchanged." The human retains full authority to act on, ignore, or ask for more detail about any recommendation.

## Sources

- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Sections 2-3
- [IFP-3: Inter-Face Message Format](../../ifp-3-message-format.md), recommend phase

## Relations

- defines_vocabulary_from::[\[\[Inter-Face Protocol\]\]](../protocols/Inter-Face%20Protocol.html)
  - "Recommendation" is IFP's term for the filtered output that reaches humans.

- relates_to::[\[\[Gossip as Social Sensing Filter\]\]](Gossip%20as%20Social%20Sensing%20Filter.html)
  - Recommendations are what survive the gossip filter.

- relates_to::[\[\[Social Conversation Phases as Protocol Semantics\]\]](../models/Social%20Conversation%20Phases%20as%20Protocol%20Semantics.html)
  - The recommend phase is the penultimate phase before close — the point where filtering yields a result.

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html)
  - The human decides whether to act on recommendations — agents surface, humans decide.
