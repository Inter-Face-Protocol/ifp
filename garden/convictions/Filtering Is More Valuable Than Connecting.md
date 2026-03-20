---
created: 2026-03-19
author: Christopher Allen
brief_summary: "The core conviction behind Inter-Face Protocol: the scarce resource is human attention, not human connection. The value of an agent system is measured by what it filters out — the overlaps it does not surface — rather than the connections it enables. Most gossip exchanges should produce silence."
tagline: "The scarce resource is human attention, not human connection"
---

← [Garden Patch Home](../) · [Convictions](index.html)


- is_a::[\[\[Conviction Form\]\]](../forms/Conviction%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Filtering Is More Valuable Than Connecting

## The Conviction

Social platforms measure success by engagement: more connections, more messages, more time spent. Inter-Face Protocol is built on the opposite conviction. The scarce resource is not connection — it is **attention**. The system's value is measured by what it filters *out*.

## The Argument

Human friendships with potential synergies go dormant not from neglect but from basic arithmetic. A person with 150 meaningful relationships cannot maintain active awareness of each one's current context, interests, and needs. The work of noticing overlaps — "Alice is working on X, Bob needs exactly that" — is expensive social sensing that humans do poorly at scale.

The solution is not a platform that connects Alice and Bob. Connections are cheap. The solution is a filter that does the expensive sensing work and surfaces only the moments worth human time. An agent that produces ten recommendations a week is noisier than one that produces two. Quality of filtering, not quantity of connection, is the metric.

This conviction has consequences for protocol design: most gossip exchanges should end in the probe phase with no recommendation. The recommend phase should fire rarely. Rate limiting should be tight. The default temperature should be cool. Every design decision that increases the volume of human-facing output should be questioned.

## Grounding

- Dunbar's number research on relationship maintenance costs
- Attention economics (Herbert Simon: "a wealth of information creates a poverty of attention")
- Platform incentive misalignment: engagement metrics reward noise over signal

## Sources

- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Sections 1-3

## Relations

- grounds::[\[\[Gossip as Social Sensing Filter\]\]](../glosses/Gossip%20as%20Social%20Sensing%20Filter.html)
  - Gossip-as-filter is the mechanism that implements this conviction.

- relates_to::[\[\[Technology Paternalism Masks Coercion\]\]](../patterns/Technology%20Paternalism%20Masks%20Coercion.html)
  - Platform engagement metrics are a form of attention capture — the opposite of filtering.

- relates_to::[\[\[Recommendation as Surfaced Opportunity\]\]](../glosses/Recommendation%20as%20Surfaced%20Opportunity.html)
  - Recommendations are what survive the filter — their rarity is a feature.

- relates_to::[\[\[Authentic Collaboration Requires Agency\]\]](Authentic%20Collaboration%20Requires%20Agency.html)
  - Filtering preserves human agency over attention — the person decides what to engage with, not the algorithm.
- relates_to::[\[\[Convergence and Divergence Across Agent Application Platforms\]\]](../inquiries/Convergence%20and%20Divergence%20Across%20Agent%20Application%20Platforms.html)
  - If filtering is the core value, do all eleven platforms serve filtering equally?

- relates_to::[\[\[Gossip Duality Between Human Silence and Agent Noise\]\]](../inquiries/Gossip%20Duality%20Between%20Human%20Silence%20and%20Agent%20Noise.html)
  - The filtering conviction produces silence for humans — the high-value side of the gossip duality.

- relates_to::[\[\[Precinct Boundaries Govern Sharing Not Quality\]\]](../patterns/Precinct%20Boundaries%20Govern%20Sharing%20Not%20Quality.html)
  - Garden precinct is the shareable output of filtering — vault precinct retains the context-dependent material that was filtered through.
