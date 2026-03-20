---
created: 2026-03-07
author: Christopher Allen
brief_summary: "Inquiry into when a garden needs the trust layer — Gordian Envelope's signing, elision, and verified exchange capabilities. The architecture defines the trust layer as a future phase but leaves activation criteria undefined. Explores what triggers the transition from markdown-only to cryptographically-verified exchange."
tagline: "When does a garden need signing, elision, and verified exchange — what triggers the trust layer?"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Inquiries](index.html)


- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Trust Layer Activation Criteria

## Thesis

The deep context architecture defines three layers: authoring (markdown), semantic (agent traversal), and trust ([\[\[Gordian Envelope as Agent Memory Layer|Gordian Envelope\]\]↑](../NODES.html#:~:text=Gordian%20Envelope%20as%20Agent%20Memory%20Layer%7CGordian%20Envelope) for signing, elision, and verified exchange). The first two layers are operational. The trust layer is described as "a future phase, not a prerequisite" — a garden operates at full value without it.

But "future phase" is not a criterion. The question is: what conditions make the trust layer worth activating? Signing, elision, and content addressing add complexity. The architecture needs criteria for when that complexity is justified.

## Current State

The architecture document describes four trust layer capabilities:

- **Signing**: Cryptographic proof of who authored or asserted a node
- **Elision**: Replace assertions with their digest while preserving signature validity — holder controls what to reveal
- **Progressive trust**: Compose elision with progressive disclosure — reveal more as trust builds between gardens
- **Content addressing**: Reference nodes by content hash for deduplication and integrity

No garden currently uses these capabilities. The first garden operates entirely at the authoring and semantic layers.

## Open Questions

1. **Is sharing the trigger?** The most obvious activation criterion: when a garden's nodes need to be shared with someone who doesn't have full trust access. If the garden stays personal and private, the trust layer adds no value. But "sharing" covers a wide range — sharing with a close collaborator is different from sharing with an unknown audience.

2. **Is multi-agent the trigger?** When multiple AI agents operate on the same garden (or exchange nodes between gardens), provenance verification becomes important. An agent receiving a principle from another agent needs to know whether the principal authorized that principle. Without signing, agent-to-agent exchange relies on filesystem trust.

3. **Is publication the trigger?** Publishing garden nodes (via static site, shared repo, or API) makes them available to parties the gardener may not know. Signing proves authorship. Elision enables selective publication. But many publication scenarios work fine with unsigned content — blog posts don't need cryptographic signatures.

4. **Could activation be incremental?** Rather than activating the full trust layer at once, could specific capabilities activate independently? Signing might activate first (when provenance matters), elision later (when selective sharing matters), content addressing later still (when deduplication across gardens matters).

## Sources

- [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html) — Open Question 11 and the Trust Layer section
- [\[\[Gordian Envelope as Agent Memory Layer\]\]↑](../NODES.html#:~:text=Gordian%20Envelope%20as%20Agent%20Memory%20Layer) — full technical evaluation of Envelope capabilities
- [\[\[Captured Reasoning Exchange Pipeline\]\]↑](../NODES.html#:~:text=Captured%20Reasoning%20Exchange%20Pipeline) — the three-layer model where the trust layer sits

## Relations

- relates_to::[\[\[Captured Reasoning Exchange Pipeline\]\]↑](../NODES.html#:~:text=Captured%20Reasoning%20Exchange%20Pipeline)
  - This inquiry addresses when the pipeline's third layer (trust) should activate.

- relates_to::[\[\[Progressive Trust\]\]↑](../NODES.html#:~:text=Progressive%20Trust)
  - Progressive trust is both a pattern the trust layer enables and a potential activation criterion — trust builds through interaction, and the trust layer supports that building.

- relates_to::[\[\[Delegated Decision Authority Spectrum\]\]](../boundaries/Delegated%20Decision%20Authority%20Spectrum.html)
  - Multi-agent scenarios (HAAH chains) where authority must be verified across hops are a potential activation trigger.
