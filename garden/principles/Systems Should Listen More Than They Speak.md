---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Herbert Simon's design principle applied to information systems: subsystems should absorb more information than they produce. The input/output ratio of a component is measurable. Effective designs compress and filter at each stage; naive designs amplify volume. Protocol success is measured by attention saved, not information delivered."
tagline: "Well-designed subsystems compress information at every stage — measure attention saved, not data delivered"
---

← [Garden Patch Home](../) · [Principles](index.html)


- is_a::[\[\[Principle Form\]\]](../forms/Principle%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Systems Should Listen More Than They Speak

**A well-designed information subsystem absorbs more than it emits.** Herbert Simon argued in 1971 that information-rich environments demand attention-efficient design. The scarce resource is never information itself — it is the attention of the agents who must process it. Every component in a system either compresses the information flowing through it or amplifies it. There is no neutral pass-through.

## The Input/Output Ratio

This principle is measurable. Take any node, agent, or process in a system and compare its inputs to its outputs. A filter has a ratio greater than 1:1 — it absorbs ten signals and emits three. An amplifier has a ratio less than 1:1 — it takes one signal and produces five notifications, three summaries, and a dashboard update.

Naive system designs chain amplifiers together. Each stage adds metadata, reformats, cross-references, and forwards. The result is exponential volume growth. By the time information reaches a human decision-maker, the signal is buried under layers of system-generated commentary.

Effective designs chain filters. Each stage strips irrelevant detail, merges redundant signals, and passes forward only what the next stage needs. The information reaching the decision-maker is smaller than what entered the pipeline, not larger.

## Application to Agent Protocols

An agent that responds to every message with a longer message is an amplifier. An agent that absorbs a conversation thread and produces a single actionable summary is a filter. Protocol designers should set explicit compression targets: a coordination message should be shorter than the work it coordinates.

This applies directly to knowledge management. A garden node that synthesizes five source documents into one page of claims is filtering. A node that quotes all five sources in full and adds commentary is amplifying. The garden's value comes from compression, not accumulation.

## Sources

Grounded in [\[\[Simon (1971) Designing Organizations for an Information-Rich World\]\]](../citations/Simon%20%281971%29%20Designing%20Organizations%20for%20an%20Information-Rich%20World/Simon%20%281971%29%20Designing%20Organizations%20for%20an%20Information-Rich%20World.html), where Simon introduced the attention scarcity framing that inverts the usual information-delivery optimization.

## Relations

- relates_to::[\[\[Filtering Is More Valuable Than Connecting\]\]](../convictions/Filtering%20Is%20More%20Valuable%20Than%20Connecting.html)
  - Filtering is the mechanism; this principle is the design standard that demands it.

- relates_to::[\[\[Gossip as Social Sensing Filter\]\]](../glosses/Gossip%20as%20Social%20Sensing%20Filter.html)
  - Social gossip networks are natural examples of listen-more-than-speak systems — many observations compress into few transmitted judgments.

- relates_to::[\[\[Gossip Duality Between Human Silence and Agent Noise\]\]](../inquiries/Gossip%20Duality%20Between%20Human%20Silence%20and%20Agent%20Noise.html)
  - The listening principle manifests as the human-silence side of the gossip duality.
