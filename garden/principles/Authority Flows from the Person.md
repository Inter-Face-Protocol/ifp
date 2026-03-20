---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Principle establishing that identity and authority originate with the person, not institutions or platforms. Identity is delegable but not alienable — it can be conferred to agents but never transferred as property. Grounded in Wyoming SF0039's statutory shift from property law to agency law for digital identity."
tagline: "Identity is delegable, not alienable — authority originates with the person"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Principles](index.html)


- is_a::[\[\[Principle Form\]\]](../forms/Principle%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Self-Sovereign Identity\]\]](../domains/Self-Sovereign%20Identity.html)

# Authority Flows from the Person

Authority over identity originates with the person. It can be conferred to agents — software, platforms, delegates — but it cannot be transferred, sold, or alienated. The person remains the source. Revocation is always available because the authority was never given away, only lent.

This is the property-to-agency shift that Wyoming SF0039 made statutory in 2021. Property law treats identity as an asset: ownable, transferable, divisible. Agency law treats identity as a relationship: the principal directs, agents act within boundaries, duties flow both ways, and the principal can always revoke.

The distinction matters because property framing enables identity markets. If identity is property, it can be commodified — bought, aggregated, resold. If identity is a delegable relationship, commodification violates the structure. You cannot sell what was never yours to own; you can only abuse a delegation.

## Implications

**For digital systems**: Platforms that collect identity data are agents, not owners. Their authority extends only as far as the user conferred it, subject to the five agency duties (specificity, responsibility, representation, fidelity, disclosure). Data retention beyond conferred scope violates the specificity duty.

**For AI systems**: An AI agent operating on a person's behalf holds conferred authority, not inherent authority. The agent's actions are the principal's actions, attributed through the conferral chain. The agent cannot claim independent authority over outputs it generated — authorship and responsibility are distinct.

**For augmentation systems**: The person's authority over their knowledge system is not diminished by delegating tasks to AI. The system augments the person's capability while the person retains accountability. Removing the person from the authority chain converts augmentation into substitution.

## Sources

- Wyoming SF0039-2021 — statutory shift from property to agency law
- Christopher Allen, "The Path to Self-Sovereign Identity" (2016) — principle of control
- Christopher Allen, "Principal Authority" (2021)

## Relations

- implements::[\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html)
  - The principle underlies the vault's commitment to human authority over augmentation.

- relates_to::[\[\[Principal Authority as Agency Law for Digital Identity\]\]](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html)
  - The gloss elaborates the legal framework this principle establishes.

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](Human%20Authority%20Over%20Augmentation%20Systems.html)
  - The Deep Context Architecture principle that applies this Self-Sovereign Identity principle to knowledge work.
