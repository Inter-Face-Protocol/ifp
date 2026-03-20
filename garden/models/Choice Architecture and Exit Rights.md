---
created: 2026-03-18
author: Christopher Allen
brief_summary: "Model of how initially voluntary digital choices accumulate into coercive dependencies through credential chains, platform lock-in, and exit penalties. When credentials, reputation, and relationships accumulate in one ecosystem, switching means losing recognized standing. Maps to the Exit → Erasure inversion in The Architecture of Autonomy."
tagline: "How voluntary digital choices accumulate into coercive dependencies with prohibitive exit costs"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Self-Sovereign Identity\]\]](../domains/Self-Sovereign%20Identity.html)
- extracted_from::[\[\[Revisiting Self-Sovereign Identity Initiative\]\]↑](../NODES.html#:~:text=Revisiting%20Self-Sovereign%20Identity%20Initiative)

# Choice Architecture and Exit Rights

## Framing

Every digital system offers choices. The architecture of those choices — what's default, what's easy, what's costly — determines whether participation is genuinely voluntary or practically mandatory. This model describes how initially voluntary choices accumulate into coercive dependencies.

## Structure

### The Lock-In Escalation

1. **Voluntary adoption** — user joins a system, creates credentials, builds reputation
2. **Accumulation** — credentials, relationships, and standing accrue over time
3. **Dependency formation** — other systems require the accumulated credentials
4. **Exit penalty** — leaving means losing recognized standing across dependent systems
5. **Practical coercion** — participation is formally voluntary but practically mandatory

### Three Lock-In Mechanisms

**Credential dependency chains**: Can't get job without credential, can't get credential without biometric, can't get biometric without national ID. Each step appears voluntary; the chain is coercive.

**Proprietary format lock-in**: Wallet formats, credential schemas, and attestation infrastructure that don't interoperate. Switching means starting over. The EU Data Act (September 2025) acknowledges this by mandating service switching provisions.

**Network effect penalties**: The value of a credential depends on who accepts it. Leaving a dominant ecosystem means losing recognition even if you keep the credential.

### Connection to the Six Inversions

This model maps directly to the **Exit → Erasure** inversion in The Architecture of Autonomy: "In the physical world, you can walk away with your resources. In the digital world, departure is erasure." Also connects to **Property → Privilege**: you accumulate assets that exist at platform discretion.

In Kolpondinos's taxonomy, this is **Infrastructural Paternalism** — the form where exit is theoretically available but functionally equivalent to digital death.

## Boundaries

This model covers structural lock-in and exit costs. Psychological effects of lock-in awareness (self-censorship) are in [\[\[Self-Coercion Through Surveillance Awareness\]\]↑](../NODES.html#:~:text=Self-Coercion%20Through%20Surveillance%20Awareness). Interface manipulation that creates the initial adoption is in [\[\[Coercion Resistance as Meta-Lens\]\]](Coercion%20Resistance%20as%20Meta-Lens.html).

## Sources

- Allen, C. (2025). Choice Architecture and Exit Rights Lens. Revisiting Self-Sovereign Identity, v0.2.01.
- Kolpondinos, M. (2026). Technology Paternalism — Infrastructural form.
- OECD. Data Portability, Interoperability and Competition.
- European Commission. Data Act (applicable September 2025).

## Relations

relates_to::[\[\[Coercion Resistance as Meta-Lens\]\]](Coercion%20Resistance%20as%20Meta-Lens.html)
relates_to::[\[\[Technology Paternalism Masks Coercion\]\]](../patterns/Technology%20Paternalism%20Masks%20Coercion.html)
relates_to::[\[\[Self-Sovereign Identity\]\]](../domains/Self-Sovereign%20Identity.html)
relates_to::[\[\[Authentic Collaboration Requires Agency\]\]](../convictions/Authentic%20Collaboration%20Requires%20Agency.html)
