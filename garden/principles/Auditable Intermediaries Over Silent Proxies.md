---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Any intermediary that handles messages between agents must leave an auditable trace — recording when it received the message, from whom, and any transformations applied. Silent proxies that forward or modify messages without visible traces violate the human legibility constraint. Trace is mandatory, not optional."
tagline: "Intermediaries must leave auditable traces rather than forwarding silently"
---

← [Garden Patch Home](../) · [Principles](index.html)


- is_a::[\[\[Principle Form\]\]](../forms/Principle%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Auditable Intermediaries Over Silent Proxies

When a relay, proxy, or intermediary handles a message between two agents, it must append a **trace entry** recording its involvement. The trace is mandatory — not a logging convenience, but a protocol requirement.

This principle exists because human legibility is a hard constraint in Inter-Face Protocol (IFP-1 Section 5.3). If an intermediary can silently forward, delay, duplicate, or drop messages without leaving a trace, the human operator cannot verify the path their messages took. The audit log becomes unreliable, and the accountability chain breaks.

## What the Trace Records

Each intermediary appends:
- When it received the message
- From which agent or relay
- Any transformations applied (re-encryption, format conversion)
- Its own identifier

## What the Trace Does Not Prevent

Tracing is accountability, not prevention. A malicious relay can still read unencrypted content, delay delivery, or inject false trace entries. The mitigations are layered:

- **IFP-5 signatures survive relay** — the sending agent's signature covers the message, not the transport. A relay cannot forge the sender's identity.
- **Replay detection** — receiving agents track message IDs and detect duplicates.
- **Body encryption** — agents should encrypt message bodies when routing through untrusted relays.

The trace ensures that relay involvement is *visible*. Detection and response are separate concerns.

## Sources

- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Section 6.4
- [IFP-8: Relay and Pub/Sub Transport](../../ifp-8-relay-transport.md), trace requirements

## Relations

- relates_to::[\[\[Relay as Accountable Store-and-Forward Intermediary\]\]](../glosses/Relay%20as%20Accountable%20Store-and-Forward%20Intermediary.html)
  - Relays are the primary implementation of this principle.

- relates_to::[\[\[Three-Part Enforcement Stack\]\]](../patterns/Three-Part%20Enforcement%20Stack.html)
  - Mandatory tracing is the technical enforcement layer; accountability also requires legal duties and exit rights.

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](Human%20Authority%20Over%20Augmentation%20Systems.html)
  - Auditable traces enable the human to verify what happened — a precondition for meaningful authority.

- relates_to::[\[\[Authority Flows from the Person\]\]](Authority%20Flows%20from%20the%20Person.html)
  - Transparency through mandatory tracing ensures the person can verify the path their delegated communications took.
