---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Gloss interpreting principal authority as the application of centuries-old agency law to digital identity. Defines five key terms (principal, agent, conferral, authorship, responsibility), five agency duties, and revocability as the diagnostic test for voluntariness. Rooted in Wyoming SF0039's shift from property to agency law for digital identity."
tagline: "Agency law applied to digital identity — five duties, five definitions, revocability as litmus test"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Glosses](index.html)


- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Self-Sovereign Identity\]\]](../domains/Self-Sovereign%20Identity.html)

# Principal Authority as Agency Law for Digital Identity

Principal authority applies centuries-old agency doctrine to digital identity. The framework is not new law — it adapts established legal relationships (principal directs, agent acts, duties flow both ways) to contexts where humans delegate identity operations to software, platforms, and other intermediaries.

Wyoming's SF0039 legislation (2021) made this shift statutory: digital identity is grounded in agency law, not property law. Identity cannot be bought, sold, or alienated like property. It can only be delegated by its subject, and delegation carries legal duties.

## Definitions

Five terms distinguish who does what and who bears responsibility:

- **Principal**: An entity with ultimate authority over a work or action, who takes responsibility for it and to whom agents owe duties.
- **Agent**: An entity that acts on behalf of a principal, within conferred authority boundaries.
- **Conferral**: The grant of authority from principal to agent. The specification uses "conferral" rather than "delegation" to avoid collision with XID's cryptographic `delegate` predicate, which grants signing privileges — a narrower technical operation.
- **Authorship**: The act of creating content — writing, coding, generating. Authorship describes *who made it*, distinct from who directed it.
- **Responsibility**: The authority over and accountability for content — directing, reviewing, standing behind. Responsibility describes *who owns the decision*, regardless of who performed the work.

The authorship/responsibility distinction matters when humans direct AI agents. The human may not author a single word yet bears full responsibility for the output. Existing metadata schemas conflate these roles, attributing both creation and accountability to the same party.

## Five Agency Duties

Agency law imposes duties on the agent toward the principal:

1. **Specificity** — Act only within the delegated scope. No behavioral profiling beyond what authority was conferred for.
2. **Responsibility** — Exercise reasonable care. A duty of competence in carrying out the principal's direction.
3. **Representation** — Act in the principal's interest, not the agent's profit. The agent serves the principal, not its own business model.
4. **Fidelity** — Act in good faith without manipulation or dark patterns. No exploiting the trust relationship.
5. **Disclosure** — Full transparency about actions, conflicts, and compensation. The principal must be able to see what the agent does and why.

## Revocability as Diagnostic Test

Revocability is the litmus test for voluntariness. A principal can revoke delegated authority at any time. When revocation is impossible or prohibitively costly, the relationship is coerced, not genuinely delegated.

Current digital ecosystems fail this test routinely. Platform lock-in, data portability barriers, and network effects make revocation costly enough to be nominal. The user technically *can* leave but practically cannot — consent theater replaces genuine consent.

## Consent Theater

Consent theater is performative consent without understanding. Users would need 76 work days annually to read all privacy policies they encounter. Clicking "I agree" satisfies the disclosure form but violates the disclosure duty — agents must ensure principals comprehend what authority they are delegating, not merely collect ritualized assent.

## Sources

- Wyoming SF0039-2021 — statutory grounding of digital identity in principal authority
- Christopher Allen, "Principal Authority" (2021) — published at blockchaincommons.com
- BCR-2026-xxx — formal predicate specification for principal authority chains
- Christopher Allen, "The Path to Self-Sovereign Identity" (2016) — 10 principles

## Relations

- implements::[\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html)
  - Principal authority concept applied from Self-Sovereign Identity domain to vault design.

- depends_on::[\[\[Authority Flows from the Person\]\]](../principles/Authority%20Flows%20from%20the%20Person.html)
  - The legal framework rests on the principle that authority originates with the person.

- relates_to::[\[\[Authority Conferral Chain\]\]](../models/Authority%20Conferral%20Chain.html)
  - The formal predicate model that encodes these concepts as machine-readable metadata.

- relates_to::[\[\[Opus Form\]\]](../forms/Opus%20Form.html) — Opus Form's principal:: predicate operationalizes this framework for authored works
