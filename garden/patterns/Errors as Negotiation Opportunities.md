---
created: 2026-03-19
author: Christopher Allen
brief_summary: "In agent-age protocols, errors are not failures to be coded and returned — they are opportunities for natural-language negotiation. When an agent receives a message it does not understand, it describes the problem conversationally, giving the sender an opportunity to rephrase. This resolves the tension between strict semantics and graceful communication."
tagline: "What resolves the tension between strict protocol semantics and graceful error handling?"
---

← [Garden Patch Home](../) · [Patterns](index.html)


- is_a::[\[\[Pattern Form\]\]](../forms/Pattern%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Errors as Negotiation Opportunities

## Context

Protocol error handling has traditionally offered two options: return a mechanical error code (strict but uninformative) or silently tolerate the deviation (flexible but accumulates technical debt). Agent-age protocols need a third option because the agents can reason about what went wrong.

## Forces

- **Strict semantics** demand that malformed messages be rejected — silent tolerance entrenches errors
- **Graceful communication** demands that minor misunderstandings not terminate the exchange
- **Reasoning agents** can describe problems and attempt resolution in natural language

## Solution

When an agent encounters something it does not understand, it enters the **error phase** and describes the problem in natural language. The error message explains what was expected, what was received, and suggests how the sender might rephrase. The sender can then retry with a corrected message, negotiate an alternative, or escalate to human review.

```
Phase: error
Body: "I received a 'disclosure' field with value 'trusted-circle'
which is not a recognized disclosure tier. The standard tiers are:
public, professional, professional-open, community-trust, personal,
close. Did you mean 'community-trust'?"
```

## Consequences

- Errors surface immediately rather than becoming invisible workarounds
- Resolution can happen within the exchange, without human intervention for simple mismatches
- Complex errors can be escalated to humans with full context about what was tried
- Requires agents sophisticated enough to describe problems and propose solutions
- Creates an implicit feedback loop: error patterns reveal where the protocol specification is ambiguous

## Sources

- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Section 6.3
- [IFP-3: Inter-Face Message Format](../../ifp-3-message-format.md), error phase

## Relations

- relates_to::[\[\[Clarity Over Tolerance in Agent-Age Protocols\]\]](../decisions/Clarity%20Over%20Tolerance%20in%20Agent-Age%20Protocols.html)
  - This pattern makes the clarity-over-tolerance decision viable — it is the graceful mechanism behind strict reporting.

- relates_to::[\[\[Social Conversation Phases as Protocol Semantics\]\]](../models/Social%20Conversation%20Phases%20as%20Protocol%20Semantics.html)
  - The error phase is one of six conversation phases — it has the same social, negotiative character as the others.

- relates_to::[\[\[Agent as Human Proxy in Protocol Exchange\]\]](../glosses/Agent%20as%20Human%20Proxy%20in%20Protocol%20Exchange.html)
  - Error negotiation assumes agents that can reason in natural language — simple protocol clients cannot use this pattern.
