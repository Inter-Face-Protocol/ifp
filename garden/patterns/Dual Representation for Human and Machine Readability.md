---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Inter-Face Protocol maintains two equivalent representations of every message: IFP-3 (YAML envelope plus natural-language body, human-readable) and IFP-4 (JSON canonical form, machine-processable for signing and transport). Conversion between them is lossless. This resolves the tension between human legibility and cryptographic operations."
tagline: "What resolves the tension between human-readable messages and machine-processable signing?"
---

← [Garden Patch Home](../) · [Patterns](index.html)


- is_a::[\[\[Pattern Form\]\]](../forms/Pattern%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Dual Representation for Human and Machine Readability

## Context

Protocols that prioritize human readability (YAML, Markdown, plain text) resist deterministic serialization — whitespace variations, key ordering, and encoding differences make cryptographic signing unreliable. Protocols that prioritize machine processing (JSON, Protocol Buffers) are difficult for humans to read in a text editor.

Inter-Face Protocol requires both: every message must be auditable by a human in a text editor (IFP-1 Section 5.3), and every message must be signable with deterministic cryptographic operations (IFP-5).

## Forces

- **Human legibility** is a non-negotiable design constraint — humans must audit agent exchanges without special tools
- **Cryptographic signing** requires deterministic serialization — YAML parsing introduces variation that breaks signature verification
- **Lossless conversion** is needed if both representations exist — information must not be lost when converting between them

## Solution

Maintain two **equivalent** representations:

| Representation | Format | Purpose | Canonical For |
|---------------|--------|---------|--------------|
| **IFP-3** | YAML envelope + Markdown body | Human reading, text editor review, email rendering | Human audit |
| **IFP-4** | JSON (RFC 8785 JCS canonical) | Signing, transport, machine parsing | Cryptographic operations |

Conversion between IFP-3 and IFP-4 is defined as lossless for the core message model (IFP-4 Section 4). An agent stores messages in IFP-3 for human audit and converts to IFP-4 for signing and sending.

## Consequences

- Humans can audit agent exchanges by reading YAML files in any text editor
- Signatures are computed on deterministic JSON, eliminating serialization ambiguity
- Two implementations must stay in sync — a change to the message model must update both representations
- The pattern is reusable: any system needing both human legibility and cryptographic operations can maintain parallel representations with defined conversion

## Sources

- [IFP-3: Inter-Face Message Format](../../ifp-3-message-format.md)
- [IFP-4: Structured Message Representation](../../ifp-4-structured-message.md), Section 4 (mapping)
- [IFP-5: Identity and Message Signing](../../ifp-5-identity-signing.md), canonicalization

## Relations

- relates_to::[\[\[Content Over Container\]\]](../principles/Content%20Over%20Container.html)
  - Both representations preserve the same content; the container changes to serve different consumers.

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html)
  - The IFP-3 representation exists specifically to ensure humans can audit what their agents do.

- relates_to::[\[\[Relay as Accountable Store-and-Forward Intermediary\]\]](../glosses/Relay%20as%20Accountable%20Store-and-Forward%20Intermediary.html)
  - Relays append trace entries in IFP-4 (JSON) format; the human reads them rendered in IFP-3.

- relates_to::[\[\[Zero-Tooling Floor for Knowledge Architecture\]\]](../principles/Zero-Tooling%20Floor%20for%20Knowledge%20Architecture.html)
  - IFP-3's YAML + Markdown format is readable with zero tools — any text editor works.
- relates_to::[\[\[Structured Schema vs Natural Language for Agent Message Content\]\]](../inquiries/Structured%20Schema%20vs%20Natural%20Language%20for%20Agent%20Message%20Content.html)
  - Dual representation preserves both readability and processability for envelopes — but the body remains natural language only.
