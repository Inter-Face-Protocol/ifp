---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Insights from Simon's attention-scarcity essay — a missing principle (systems should listen more than they speak), protocol success reframed as attention saved, and the unnamed inversion from information scarcity to attention scarcity."
tagline: "What Simon's 1971 framing reveals about measuring protocol success and naming architectural inversions"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)

# Insights: Designing Organizations for an Information-Rich World

## A Missing Principle: Systems Should Listen More Than They Speak

The garden has convictions about filtering ([\[\[Filtering Is More Valuable Than Connecting\]\]](../../convictions/Filtering%20Is%20More%20Valuable%20Than%20Connecting.html)) and patterns about gossip as a filtering mechanism ([\[\[Gossip as Social Sensing Filter\]\]](../../glosses/Gossip%20as%20Social%20Sensing%20Filter.html)), but no principle that states the underlying design rule in Simon's terms. "Systems should listen more than they speak" is a candidate Principle Form grounded directly in Simon's essay. It would serve as the architectural rationale beneath both the conviction and the pattern — the principle from which they derive.

The principle is not "filter more." It is specifically about the input/output ratio of system components. A component that listens more than it speaks is one where the volume of information absorbed exceeds the volume of information produced. This is measurable in protocol contexts: how many messages does a node receive versus transmit? How many edges does a garden node have inbound versus outbound? The principle gives designers a concrete test rather than a vague preference.

## Reframing Protocol Design

Simon's attention-poverty framing changes what counts as a successful protocol. The default framing for communication protocols is "enable more connections" — success means more messages delivered, more participants reached, more information flowing. Under Simon's framing, this is the wrong metric. More connections without more filtering means more attention demanded from each participant.

The reframe: protocol success should be measured by attention saved, not information delivered. A protocol that enables ten people to coordinate while reading five messages each is better than one that enables the same coordination while reading fifty messages each. The coordination outcome is the same; the attention cost differs by an order of magnitude.

This reframe applies directly to IFP's design space. An inter-face protocol that structures interaction so that each party receives only the information relevant to their role — and nothing else — is optimizing for Simon's constraint. The protocol is an attention-allocation mechanism, not an information-distribution mechanism. That distinction, stated clearly in 1971, still gets overlooked in protocol design fifty-five years later.

## What the Garden Does Not Yet Name

The garden has nodes about filtering, gossip, and attention — but it does not have a node that names the *inversion* itself. The shift from information scarcity to attention scarcity is a paradigm change, and paradigm changes deserve their own nodes. Something like "The Attention Scarcity Inversion" as an Inquiry Form or Pattern Form would capture the structural observation that design principles reverse when the binding constraint flips. This is distinct from the filtering conviction (which states what to do about it) and the gossip pattern (which shows one way to do it). The inversion itself — the observation that abundance of X creates scarcity of Y for the resource that processes X — is a general pattern that applies beyond information and attention.

Simon's essay is the earliest clear articulation of this inversion in design terms. Citing it grounds the observation historically and prevents it from appearing as unsupported assertion.
