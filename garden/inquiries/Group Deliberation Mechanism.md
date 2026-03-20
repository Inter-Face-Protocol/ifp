---
created: 2026-03-07
author: Christopher Allen
brief_summary: "Inquiry into how the deep context architecture handles decisions requiring group input — what practical mechanism does an agent use when it reaches a group-deliberative boundary? Explores structured proposals, agenda generation, and the gap between Polis Play philosophy and operational implementation."
tagline: "When an agent hits a group-deliberative boundary, what happens next — practically?"
---

← [Garden Patch Home](../) · [Inquiries](index.html)


- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Group Deliberation Mechanism

## Thesis

The [\[\[Delegated Decision Authority Spectrum\]\]](../boundaries/Delegated%20Decision%20Authority%20Spectrum.html) defines a "group-deliberative" zone where decisions require collective process — amending governance boundaries, establishing new protocols, publishing shared artifacts, resolving inquiry questions marked with `directed_at::`. But the architecture describes the *philosophy* (Polis Play — rules about who gets to play and what moves they can make) without specifying the *mechanism*.

When an LLM agent traversing the garden identifies a decision that falls in the group-deliberative zone, what does it actually do? The current guidance says "recognize, present context, frame the decision, wait." But wait how? Through what channel? In what format? The gap between "this requires group input" and "here is how group input is gathered" remains unspecified.

## Current State

The architecture currently handles this through the `directed_at::` predicate on inquiry nodes, which flags questions requiring a specific person's or group's judgment. This is a marking mechanism, not a deliberation mechanism. It tells the agent *who* needs to decide but not *how* the decision process works.

In practice within this vault, group-deliberative decisions have not yet arisen — the garden has a single owner. The question becomes urgent when:

- The garden is shared with collaborators
- Multiple agents operate on the same garden
- Published garden nodes need review from a community

## Open Questions

1. **What artifact does the agent produce?** When an agent reaches a group-deliberative boundary, should it generate a structured proposal (context, options, recommendation, request for decision)? An agenda item? A new inquiry node with `directed_at::` predicates? The output format determines how the decision enters the group's workflow.

2. **How does the decision return to the garden?** Once a group deliberates and decides, the result needs to be recorded as a decision node (or a case, if the deliberation itself is the narrative). Who writes this — the agent, the group facilitator, the gardener? What approval gate ensures the recorded decision accurately reflects the group's intent?

3. **Does protocol form fill this gap?** The architecture defines Protocol as "how independent parties coordinate reliably." A group deliberation process *is* a protocol — multiple parties following agreed rules to reach a decision. Perhaps the answer is not a new mechanism but a specific protocol form documenting how deliberation works in this garden.

4. **What about asynchronous deliberation?** Not all group decisions happen in real-time meetings. Some require async review (pull request model), some require voting, some require facilitated discussion. The mechanism needs to accommodate different deliberation modes without prescribing a single approach.

## Sources

- [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html) — Open Question 8 raises this question
- [\[\[Delegated Decision Authority Spectrum\]\]](../boundaries/Delegated%20Decision%20Authority%20Spectrum.html) — defines the group-deliberative zone

## Relations

- relates_to::[\[\[Delegated Decision Authority Spectrum\]\]](../boundaries/Delegated%20Decision%20Authority%20Spectrum.html)
  - This inquiry explores the practical implementation of the boundary's group-deliberative zone.

- relates_to::[\[\[Protocol Form\]\]↑](../NODES.html#:~:text=Protocol%20Form)
  - The deliberation mechanism may itself be a protocol — a form type with zero DCA instances that could be instantiated here.

- relates_to::[\[\[Authentic Collaboration Requires Agency\]\]](../convictions/Authentic%20Collaboration%20Requires%20Agency.html)
  - Group deliberation that respects agency requires that each participant's reasoning is heard, not just their vote.
