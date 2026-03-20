---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Pattern identifying three interdependent layers required for accountable authority in digital identity systems: legal duties (agency law), technical delegation (cryptographic enforcement), and anti-lock-in design (real alternatives and proportionate exit costs). Removing any single layer collapses accountability — legal without enforcement is nominal, technical without legal is unaccountable, both without exit is lock-in."
tagline: "Legal duties plus technical enforcement plus exit rights — remove any layer and accountability collapses"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Patterns](index.html)


- is_a::[\[\[Pattern Form\]\]](../forms/Pattern%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Self-Sovereign Identity\]\]](../domains/Self-Sovereign%20Identity.html)

# Three-Part Enforcement Stack

## Context

Digital identity systems claim to serve users but lack mechanisms to enforce that claim. Agency law defines duties ([\[\[Principal Authority as Agency Law for Digital Identity\]\]](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html)) and predicates encode authority chains ([\[\[Authority Conferral Chain\]\]](../models/Authority%20Conferral%20Chain.html)), but neither legal definitions nor technical encodings alone produce accountability.

## Forces

- Legal duties without technical enforcement are nominal — platforms violate duties with no structural consequence.
- Technical delegation without legal grounding is unaccountable — cryptographic tools enforce rules but cannot define rights.
- Legal duties and technical enforcement without exit rights produce lock-in — the user has rights they cannot exercise because leaving is prohibitively costly.
- Each layer appears sufficient in isolation but fails without the others.

## Solution

Accountability requires all three layers operating together:

**Legal duties** (agency law and fiduciary obligations) — Define what agents owe principals. The five agency duties (specificity, responsibility, representation, fidelity, disclosure) set the standard. Wyoming SF0039 makes this statutory for digital identity.

**Technical delegation mechanisms** (cryptographic enforcement of scope, revocation, auditability) — Encode authority boundaries in the system architecture. The BCR-2026-xxx predicates (`conferralScope`, `conferralConstraints`) make boundaries machine-readable. Revocation is a technical operation, not just a legal right.

**Anti-lock-in design** (choice architecture ensuring real alternatives and proportionate exit costs) — Guarantee that revocation is practically available, not just theoretically possible. Data portability, interoperable standards, and reasonable exit costs make the right to revoke meaningful.

## Consequences

Diagnosing a system requires checking all three layers:

- If legal duties exist but no technical enforcement: consent theater. Users sign terms of service that platforms ignore structurally.
- If technical enforcement exists but no legal framework: autonomous systems with no accountability path. Smart contracts without legal recourse.
- If both exist but exit is prohibitively costly: gilded cage. Rights on paper, lock-in in practice.

The stack also applies to principal-agent relationships in augmentation systems. An AI agent with rules (legal/policy), technical constraints (sandboxing, approval gates), and replaceable tooling (no vendor lock-in) satisfies all three layers. Remove replaceability and the user depends on a system they cannot leave.

## Sources

- Christopher Allen, "Principal Authority" (2021) — integration equation
- Wyoming SF0039-2021 — legal layer
- BCR-2026-xxx — technical layer predicates
- Chat archive: principle-authority.md — extended discussion of enforcement layers

## Relations

- depends_on::[\[\[Principal Authority as Agency Law for Digital Identity\]\]](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html)
  - The legal layer draws its duties from the agency law framework.

- depends_on::[\[\[Authority Conferral Chain\]\]](../models/Authority%20Conferral%20Chain.html)
  - The technical layer uses the predicate vocabulary for encoding boundaries.

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html)
  - The stack applies to knowledge work augmentation systems, not only digital identity.
- relates_to::[\[\[Auditable Intermediaries Over Silent Proxies\]\]](../principles/Auditable%20Intermediaries%20Over%20Silent%20Proxies.html)
  - Mandatory relay tracing in IFP is the technical enforcement layer in this three-part accountability stack.
