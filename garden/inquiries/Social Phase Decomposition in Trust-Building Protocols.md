---
created: 2026-03-19
author: Christopher Allen
brief_summary: "IFP-3 defines six conversation phases — greeting, context, probe, recommend, close, error — modeled as social interactions rather than mechanical request-response. This inquiry asks whether this decomposition captures the right stages of trust-building conversation, whether phases are missing or redundant, and whether the social framing holds under adversarial conditions."
tagline: "Do six social phases capture the right decomposition of trust-building agent conversation?"
---

← [Garden Patch Home](../) · [Inquiries](index.html)


- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Social Phase Decomposition in Trust-Building Protocols

## The Question

IFP-3 decomposes agent conversation into six phases:

```
greeting → context → probe → recommend → close → error
```

These phases are described as social — they model how trust-building conversations naturally progress between people. But trust-building is hard, and social framing raises questions that mechanical framing would not.

## What Makes This Worth Investigating

**Is "probe" doing too much work?** The probe phase is where agents explore overlaps between their operators' contexts. This is the hardest part of the protocol — the step where the gossip filter either finds something or doesn't. A single phase covering all exploratory exchange may be underspecified.

**Is there a missing "negotiate" phase?** When agents discover an overlap during probing, the transition from "we found something" to "here is a recommendation" may involve negotiation about framing, timing, and disclosure. The current model jumps from probe to recommend without an explicit negotiation stage.

**Does the social framing hold under adversarial conditions?** Social phases assume good-faith interaction. When one agent is misbehaving (probing for information without genuine overlap, gaming disclosure tiers, injecting false context), the social metaphor may obscure the adversarial dynamic. The error phase handles protocol violations, but social manipulation is harder to detect than protocol violations.

**Is the phase model linear enough?** IFP-3 says phases are advisory and revisitable. But the spec describes them as a progression (greeting before context, context before probe). How much non-linearity is expected in practice? Does the protocol handle backtracking well?

**Trust-building as the frame.** The phases assume that the goal is to build trust toward a recommendation. But some exchanges may have different goals — maintaining an existing relationship, checking in without probing, or deliberately cooling a warm exchange. Do the phases accommodate non-progressive conversations?

## Possible Directions

- Six phases may be correct — they provide enough structure without over-specifying
- The probe phase might split into "explore" (broad context scanning) and "focus" (narrowing to specific overlaps)
- A negotiate phase between probe and recommend might make the transition explicit
- The phase model might need a "maintain" phase for check-in exchanges that are not seeking new overlaps
- Social framing might need explicit adversarial-mode transitions, not just the error phase

## Sources

- [IFP-3: Inter-Face Message Format](../../ifp-3-message-format.md), Section 2
- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Sections 6.1, 6.3

## Relations

- relates_to::[\[\[Social Conversation Phases as Protocol Semantics\]\]](../models/Social%20Conversation%20Phases%20as%20Protocol%20Semantics.html)
  - The model this inquiry questions.

- relates_to::[\[\[Errors as Negotiation Opportunities\]\]](../patterns/Errors%20as%20Negotiation%20Opportunities.html)
  - The error phase handles protocol violations — but what handles social manipulation?

- relates_to::[\[\[Gossip as Social Sensing Filter\]\]](../glosses/Gossip%20as%20Social%20Sensing%20Filter.html)
  - The probe phase is where filtering happens — the most complex and least specified phase.

- relates_to::[\[\[Allen (2024) Progressive Trust\]\]](../citations/Allen%20%282024%29%20Progressive%20Trust/Allen%20%282024%29%20Progressive%20Trust.html)
  - Progressive trust describes stages of trust deepening — do the phases map to those stages?
