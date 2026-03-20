---
created: 2026-03-19
author: Christopher Allen
brief_summary: "IFP-3 uses natural language for message bodies rather than structured schemas. This is one of IFP's most consequential architectural decisions, yet the justification is thin: 'agents are good at NLP.' This inquiry examines the trade-offs — what natural language enables, what it makes harder, and whether hybrid approaches might preserve the benefits of both."
tagline: "Should agent protocol messages use natural language bodies or structured schemas?"
---

← [Garden Patch Home](../) · [Inquiries](index.html)


- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Structured Schema vs Natural Language for Agent Message Content

## The Question

IFP-3 makes a bold architectural choice: message bodies are natural language (Markdown-formatted), not structured schemas. The envelope (metadata) is structured (YAML in IFP-3, JSON in IFP-4), but the content — the actual information agents exchange about their operators' contexts — is free-form text.

The stated justification: "Agents are good at NLP; rigid structures lose nuance."

Is this sufficient reasoning for one of the protocol's most load-bearing decisions?

## What Makes This Worth Investigating

**What natural language enables.** Nuance, ambiguity tolerance, context-dependent meaning, emotional register, cultural expression. A natural language body can say "my human is going through a rough patch and might appreciate hearing from old friends" in ways that no schema can capture.

**What natural language makes harder.** Validation, interoperability testing, deterministic processing, automated compliance checking. When the body is free text, there is no machine-checkable way to verify that a message contains the required information for its phase.

**The IFP-1 tension.** IFP-1 Section 6.1 replaces Postel's Law with "be clear in what you send; be explicit when you don't understand." But natural language bodies resist clarity enforcement — a message can be grammatically correct and semantically ambiguous. The clarity principle and the NL body choice may be in tension.

**Validation gap.** IFP-4 provides structured envelopes that can be schema-validated. But the body — where the actual content lives — cannot be validated by machine. An agent could send a syntactically valid IFP message with a body that says nothing useful.

**Hybrid approaches exist.** Some protocols use structured fields for machine processing alongside free-text fields for human context (e.g., git commit messages: structured header + free-text body). IFP-4's `body.parts[]` mechanism could carry both structured data and natural language — but the spec does not require structured parts.

## Possible Directions

- Natural language bodies may be correct — the nuance they preserve outweighs the validation they sacrifice
- A hybrid approach (required structured fields + optional NL context) might preserve both validation and nuance
- Different phases might warrant different structure levels — greeting could be NL, probe might benefit from structured capability matching
- The `body.parts[]` mechanism in IFP-4 already supports hybrid — the question is whether some structured parts should be required

## Sources

- [IFP-3: Inter-Face Message Format](../../ifp-3-message-format.md), body format
- [IFP-4: Structured Message Representation](../../ifp-4-structured-message.md), body.parts[]
- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Section 6.1

## Relations

- relates_to::[\[\[Dual Representation for Human and Machine Readability\]\]](../patterns/Dual%20Representation%20for%20Human%20and%20Machine%20Readability.html)
  - The dual representation pattern preserves both human readability and machine processability for the envelope — but the body is NL-only.

- relates_to::[\[\[Clarity Over Tolerance in Agent-Age Protocols\]\]](../decisions/Clarity%20Over%20Tolerance%20in%20Agent-Age%20Protocols.html)
  - The clarity principle may be in tension with natural language bodies that resist validation.

- relates_to::[\[\[Allen (2023) Minimum Viable Architecture\]\]](../citations/Allen%20%282023%29%20Minimum%20Viable%20Architecture/Allen%20%282023%29%20Minimum%20Viable%20Architecture.html)
  - Is NL-for-bodies a load-bearing architectural choice or a deferrable tactical one?

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html)
  - Natural language bodies are human-readable by definition — but are they human-auditable? Can a person verify that their agent said what they intended?
