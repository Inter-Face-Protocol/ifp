---
created: 2026-03-19
author: Christopher Allen
brief_summary: "In Inter-Face Protocol, a relay is a store-and-forward service that accepts, stores, and delivers messages between agents that cannot reach each other directly. Unlike opaque intermediaries, IFP relays must append trace entries to every message — making their involvement visible and auditable by humans."
tagline: "Relays forward messages between agents while leaving an auditable trace"
---

← [Garden Patch Home](../) · [Glosses](index.html)


- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Relay as Accountable Store-and-Forward Intermediary

When two agents cannot communicate directly — one is behind a firewall, the other is intermittently connected — a relay accepts messages from the sender, stores them, and delivers them when the recipient is reachable. This is the same pattern as email's SMTP relay infrastructure, adapted for agent-to-agent communication.

What distinguishes an IFP relay from a generic message broker is **mandatory accountability**. Every relay must append a trace entry to every message it handles (IFP-8, implementing IFP-1 Section 6.4). The trace records when the relay received the message, from whom, and any transformations applied. This trace is visible to the receiving agent and, through the audit log, to the human operator.

Relays exist on a trust spectrum. An untrusted relay (the default assumption) may log message content — agents should encrypt bodies when routing through untrusted relays. A trusted relay has a known operator. A self-operated relay is run by one of the communicating parties.

The relay model preserves two properties that matter for human agency: **signatures survive relay** (IFP-5 signing covers the message, not the transport — a relay cannot forge the sender's signature), and **trace cannot be hidden** (mandatory trace entries make relay involvement visible to humans reviewing the audit log).

## Sources

- [IFP-8: Relay and Pub/Sub Transport](../../ifp-8-relay-transport.md)
- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Section 6.4 (accountable intermediaries)

## Relations

- defines_vocabulary_from::[\[\[Inter-Face Protocol\]\]](../protocols/Inter-Face%20Protocol.html)
  - "Relay" is IFP's term for store-and-forward intermediary services.

- relates_to::[\[\[Auditable Intermediaries Over Silent Proxies\]\]](../principles/Auditable%20Intermediaries%20Over%20Silent%20Proxies.html)
  - The principle that intermediaries must leave traces — relays are the primary implementation.

- relates_to::[\[\[Three-Part Enforcement Stack\]\]](../patterns/Three-Part%20Enforcement%20Stack.html)
  - Relay accountability requires technical enforcement (mandatory trace) alongside legal duties and exit rights.

- relates_to::[\[\[Authority Flows from the Person\]\]](../principles/Authority%20Flows%20from%20the%20Person.html)
  - Relay transparency ensures the human can verify the path their messages took.
