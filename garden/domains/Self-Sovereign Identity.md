---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Domain index for Self-Sovereign Identity in the garden — 4 nodes covering the principal authority framework from agency law. Self-Sovereign Identity provides the first non-Deep Context Architecture domain content, bridging identity principles to the vault's augmented knowledge architecture."
tagline: "Identity owned by the individual — the first non-Deep Context Architecture domain in the garden"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Domains](index.html)


- is_a::[\[\[Domain Form\]\]](../forms/Domain%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)

# Self-Sovereign Identity

Self-sovereign identity is the principle that individuals should own and control their digital identity without depending on any external authority. Christopher Allen's 2016 articulation of the 10 Principles of Self-Sovereign Identity established the framework. In this garden, self-sovereign identity nodes focus on the principal authority framework from agency law — how identity rights are delegated, enforced, and protected.

## Scope

**Covers**: The principal authority model (agency law applied to digital identity), authority delegation patterns, enforcement mechanisms, and the bridge between self-sovereign identity principles and the vault's augmented knowledge architecture.

**Does not cover**: Technical standards implementation (DIDs, Verifiable Credentials, DIDComm) — those belong in a future technical self-sovereign identity domain or in [\[\[Digital Identity\]\]↑](../NODES.html#:~:text=Digital%20Identity). Also excludes the broader digital identity landscape beyond self-sovereign identity.

## Key Forms

### Principal Authority Framework

- [\[\[Principal Authority as Agency Law for Digital Identity\]\]](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html) — gloss: self-sovereign identity duties and definitions through agency law lens
- [\[\[Authority Conferral Chain\]\]](../models/Authority%20Conferral%20Chain.html) — model: three delegation types (Type A: full, Type B: constrained, Type C: revocable)
- [\[\[Authority Flows from the Person\]\]](../principles/Authority%20Flows%20from%20the%20Person.html) — principle: authority is delegable but not alienable
- [\[\[Three-Part Enforcement Stack\]\]](../patterns/Three-Part%20Enforcement%20Stack.html) — pattern: three layers of enforcement (technical, legal, social)

All 4 nodes were extracted from plan-principal-authority-forms in session 7 of the garden-foundation workstream. They draw on Christopher Allen's self-sovereign identity article (2016), BCR-2026-xxx spec drafts, and chat archives from Blockchain Commons discussions.

## Candidate Forms

Potential forms identified from [Blockchain Commons Values & Design Principles](https://www.blockchaincommons.com/musings/ValuesDesign/) — not yet extracted:

### Convictions

- Digital Rights as Fundamental Human Rights — digital rights deserve the same standing as other human rights; not a policy preference but a claim about what rights are

### Principles

- Privacy by Design as Standing Constraint — embed privacy protections into every system as default practice, not as an add-on feature
- Resilience Against Exploitation — architect systems to withstand adversarial threats; autonomy must remain intact under pressure
- Revocable Permissions as Agency Preservation — users retain ongoing control over delegated information; relationships change, permissions must follow
- Data Minimization as Default Practice — minimize data collected; reduces vulnerability surface and respects dignity

### Patterns

- Selective Disclosure and Elision — choices for redaction and elision to control what individuals share; prevents reduction to digital records
- Progressive Trust as Relationship Evolution — systems that reflect the natural evolution of trust, enabling selective disclosure incrementally (bridges [\[\[Synpraxis\]\]](Synpraxis.html))

### Models

- Membrane Analogy for Identity Boundaries — digital identity as a selective boundary (from Living Systems Theory): enabling both individual autonomy and collective participation, like cell membranes that filter while remaining part of a larger ecosystem

## Open Questions

- What additional self-sovereign identity nodes should be extracted? The 10 Principles alone could yield 10 principle nodes.
- How does self-sovereign identity relate to the [\[\[Delegated Decision Authority Spectrum\]\]](../boundaries/Delegated%20Decision%20Authority%20Spectrum.html) boundary? (Currently the spectrum is tagged Deep Context Architecture; the authority concepts bridge both domains.)
- Should technical self-sovereign identity standards (DIDs, VCs) be a sub-domain or a separate domain page?

## Sources

- Allen, Christopher. "The Path to Self-Sovereign Identity." (2016)
- BCR-2026-xxx spec drafts (Blockchain Commons)
- [\[\[Digital Identity\]\]↑](../NODES.html#:~:text=Digital%20Identity) — parent map of content in Categories/

## Relations

- relates_to::[\[\[Deep Context Architecture\]\]](Deep%20Context%20Architecture.html) — Self-sovereign identity agency law concepts inform the vault's principal authority model
- relates_to::[\[\[Digital Identity\]\]↑](../NODES.html#:~:text=Digital%20Identity) — Self-sovereign identity is a subset of the broader digital identity field