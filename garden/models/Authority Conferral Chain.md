---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Model defining the formal predicate vocabulary for principal authority relationships in BCR-2026-xxx. Seven predicates encode who directed work, who asserts authority was conferred, what scope and constraints apply, and the full chain from principal to agent. Includes three conditions for meaningful authority and a Type A/B/C classification of delegation relationships."
tagline: "Seven predicates encoding authority chains from principal through agent with scope and constraints"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Self-Sovereign Identity\]\]](../domains/Self-Sovereign%20Identity.html)

# Authority Conferral Chain

The authority conferral chain is a formal model for encoding who directed work, who performed it, and what authority was granted. BCR-2026-xxx defines seven predicates that make these relationships machine-readable, enabling systems to distinguish genuine authority from nominal attribution.

## Seven Predicates

| Codepoint | Predicate | Function |
|-----------|-----------|----------|
| 1040 | `principalAuthority` | Identifies who directed work and bears responsibility |
| 1041 | `assertsConferralFrom` | Agent asserts authority was conferred by principal |
| 1042 | `conferralScope` | Boundaries of what the conferral covers |
| 1043 | `conferralConstraints` | Limitations or conditions on conferred authority |
| 1044 | `conferredBy` | Immediate source of authority (single-hop) |
| 1045 | `conferralChain` | Full chain of authority conferral (multi-hop) |
| 1046 | `confersTo` | Principal declares conferral to an agent |

The predicates separate into two directions: the principal's declaration (`confersTo`) and the agent's assertion (`assertsConferralFrom`). Both are needed — a principal may confer authority the agent doesn't claim, and an agent may assert authority the principal didn't grant. The `conferralChain` predicate captures multi-hop delegation where authority passes through intermediaries.

## Three Conditions for Meaningful Authority

For authority to be genuine rather than nominal, three conditions hold:

1. **Legibility** — The principal can observe what the agent does and comprehend why. Without legibility, oversight is performative.
2. **Boundaries** — The agent operates within constraints the principal established. Without boundaries, authority is unbounded and therefore unaccountable.
3. **Override** — The principal can intervene, revoke, or redirect at any time. Without override, the relationship is coerced regardless of initial consent.

Remove any condition and the authority relationship degrades. Legibility without boundaries produces informed helplessness. Boundaries without override produces contractual lock-in. Override without legibility produces arbitrary intervention.

## Delegation Classification

Three types classify the quality of authority relationships in digital systems:

**Type A: Genuine Agency** — All five duties honored, authority revocable, relationship mutually beneficial. The agent serves the principal's interests within clear boundaries. Rare in current digital ecosystems.

**Type B: Nominal Agency** — Platform claims to serve the user but systematically violates duties. Terms of service assert agency while business models extract value. The principal has formal authority but no practical enforcement. Most current platforms operate here.

**Type C: Coerced Participation** — No meaningful alternatives, no real revocability, duties impossible to enforce. Network effects, data lock-in, or regulatory requirements make participation effectively mandatory. The agency relationship is fiction.

The classification serves as a diagnostic: given a system, which type describes its actual authority relationship? The gap between claimed type (usually A) and actual type (usually B or C) measures the system's integrity.

## Sources

- BCR-2026-xxx — formal predicate specification (codepoints 1040-1046, Community Assigned range)
- Wyoming SF0039-2021 — statutory grounding
- Christopher Allen, "Principal Authority" (2021) — published framework

## Relations

- depends_on::[\[\[Principal Authority as Agency Law for Digital Identity\]\]](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html)
  - The predicates encode the legal concepts defined in the gloss.

- depends_on::[\[\[Authority Flows from the Person\]\]](../principles/Authority%20Flows%20from%20the%20Person.html)
  - The chain model assumes authority originates with the person and flows outward.

- relates_to::[\[\[Three-Part Enforcement Stack\]\]](../patterns/Three-Part%20Enforcement%20Stack.html)
  - The predicates provide the technical layer; enforcement requires all three layers.
- relates_to::[\[\[Agent as Human Proxy in Protocol Exchange\]\]](../glosses/Agent%20as%20Human%20Proxy%20in%20Protocol%20Exchange.html)
  - The authority conferral chain formalizes the Human-Agent-Agent-Human delegation model that IFP operationalizes.
