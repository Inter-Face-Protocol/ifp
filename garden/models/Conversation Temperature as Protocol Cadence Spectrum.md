---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Temperature in Inter-Face Protocol describes conversation intensity as a spectrum — cool (weekly background gossip), warm (daily to hourly active interest), and hot (near-synchronous collaboration). Same protocols, same message formats, different cadences. Temperature shapes rate limiting, capability availability, and escalation thresholds."
tagline: "How do conversation intensity levels shape protocol behavior across the same message format?"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Conversation Temperature as Protocol Cadence Spectrum

Inter-Face Protocol uses a single message format and protocol stack across all conversation intensities. What changes is the **cadence** — how frequently agents exchange messages and how quickly they expect responses.

## The Spectrum

| Temperature | Cadence | Agent Behavior | Human Involvement |
|-------------|---------|----------------|-------------------|
| **Cool** | Weekly or less | Background gossip, context exchange, slow probe | Receives occasional recommendations |
| **Warm** | Daily to hourly | Active interest tracking, faster probe cycles | Reviews recommendations more frequently |
| **Hot** | Near-synchronous | Real-time collaboration support, rapid exchange | Actively engaged, agent supports rather than filters |

## What Temperature Affects

Temperature is not a separate protocol layer — it is inherited from IFP-1 and shapes behavior across the stack:

- **Rate limiting** (IFP-6): 10 messages/minute for cool, 60 messages/minute for hot
- **Capability availability** (IFP-7): Some capabilities condition on temperature — `calendar.availability` might require warm or hot
- **Disclosure depth** (IFP-12): Cool exchanges tend toward narrower disclosure; hot exchanges may deepen as collaboration intensifies
- **Escalation**: Conversations can warm up (cool → warm → hot) as agents detect increasing overlap or urgency

## Temperature as Design Pattern

The temperature model is reusable beyond IFP. Any system where the same participants interact at varying intensities — from background monitoring to active collaboration — can benefit from a cadence spectrum that shapes protocol behavior without requiring separate protocols for each intensity level.

## Sources

- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Section 4
- [IFP-6: HTTPS Transport Profile](../../ifp-6-https-transport.md), rate limiting
- [IFP-7: Agent Capability Discovery](../../ifp-7-capability-discovery.md), temperature conditions

## Relations

- relates_to::[\[\[Gossip as Social Sensing Filter\]\]](../glosses/Gossip%20as%20Social%20Sensing%20Filter.html)
  - Most gossip operates at cool temperature — the filter runs in the background.

- relates_to::[\[\[Progressive Authentication as Trust Deepening\]\]](Progressive%20Authentication%20as%20Trust%20Deepening.html)
  - Hot exchanges typically require deeper authentication than cool ones.

- relates_to::[\[\[Capability as Advertised Agent Function\]\]](../glosses/Capability%20as%20Advertised%20Agent%20Function.html)
  - Capabilities condition on temperature — some functions require warm or hot cadence.

- relates_to::[\[\[Social Conversation Phases as Protocol Semantics\]\]](Social%20Conversation%20Phases%20as%20Protocol%20Semantics.html)
  - Phases progress at the rate the temperature allows — cool phases take days, hot phases take minutes.
- relates_to::[\[\[Organizing Principle for Agent Application Domains\]\]](../inquiries/Organizing%20Principle%20for%20Agent%20Application%20Domains.html)
  - Temperature is one candidate organizing principle for the application platform taxonomy.
