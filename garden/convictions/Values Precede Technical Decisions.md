---
created: 2026-03-06
author: Christopher Allen
brief_summary: "The conviction that technical architecture must be grounded in human values — not derived from technical capability, market pressure, or implementation convenience. Every design choice in the deep context architecture traces to a value: augmentation over autonomy, portability over power, simplicity over sophistication, human reasoning over system output. When values and technical convenience conflict, values win."
tagline: "Ground technical decisions in human values — when values and convenience conflict, values win"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Convictions](index.html)


- is_a::[\[\[Conviction Form\]\]](../forms/Conviction%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Values Precede Technical Decisions

## The Conviction

Technical architecture must be grounded in human values. Not derived from what's technically possible, not from what the market demands, not from what's convenient to implement. Values come first; technical decisions follow.

This is not a claim that values are sufficient — technical competence still matters, constraints still bind. The claim is about sequence and authority: when a technical choice and a value conflict, the value wins. You redesign the technical approach, not the value.

The alternative — letting technical capability drive values — produces systems that work for their builders and extract from their users. It produces surveillance architectures justified by "we can, so we should." It produces knowledge systems that lock users in because lock-in is profitable. It produces AI systems that substitute for human judgment because substitution is easier than augmentation.

## Grounding

This conviction emerges from decades of building systems where the technical-values ordering was tested:

- **SSL/TLS**: The pivot from groupware to security infrastructure happened because privacy (a value) turned out to be a precondition for the collaboration tools (a technical goal). Building the tools first without the values infrastructure produced tools nobody trusted.
- **Self-sovereign identity**: The 10 Principles (2016) were values statements that preceded and directed the technical standards (DIDs, Verifiable Credentials, DIDComm). Projects that started with the technology and tried to retrofit the values produced centralized identity platforms with self-sovereign branding.
- **Deep context architecture**: Human authority over augmentation systems, zero-tooling floor, content over container — each architectural principle traces to a value (agency, portability, substance over format). The architecture document begins with values and derives structure from them.
- **Blockchain Commons design principles**: The values-to-design pipeline is explicit — human dignity, autonomy, privacy by design, progressive trust, resilience against exploitation. Each value produces specific technical requirements. The ordering is not decorative.

The pattern across all these domains: projects that start with values and derive technical decisions produce systems that serve their users. Projects that start with technical capability and try to add values later produce systems that serve their builders.

## Implications

- **For the deep context architecture**: Every architectural decision should have a values justification chain. If a technical choice can't trace back to a human value, it's either unjustified or the value is implicit and needs to be made explicit.
- **For knowledge systems**: A knowledge architecture that optimizes for retrieval speed over human comprehension, or for agent convenience over human authority, has inverted the ordering. The architecture exists to serve the person's reasoning, not the system's performance.
- **For design practice**: Values-first design requires stating the values before the design phase, not discovering them after implementation. This is why the deep context architecture has conviction and value forms — they are the foundation layer, not an afterthought.

## Sources

- Allen, C. (2016). "The Path to Self-Sovereign Identity" — values as preconditions for technical standards
- [Blockchain Commons Values & Design Principles](https://www.blockchaincommons.com/musings/ValuesDesign/) — explicit values-to-design pipeline
- [Open Development](https://www.blockchaincommons.com/articles/Open-Development/) — values (accessibility, diversity, transparency, sustainability) preceding technical practice
- [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html) — values-grounded architectural decisions throughout

## Relations

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html) — one of the principles this conviction produces: augmentation over autonomy is a values choice
- relates_to::[\[\[Zero-Tooling Floor for Knowledge Architecture\]\]](../principles/Zero-Tooling%20Floor%20for%20Knowledge%20Architecture.html) — portability over power is a values choice
- relates_to::[\[\[Content Over Container\]\]](../principles/Content%20Over%20Container.html) — substance over format is a values choice
- relates_to::[\[\[Authentic Collaboration Requires Agency\]\]](Authentic%20Collaboration%20Requires%20Agency.html) — the Synpraxis conviction that agency infrastructure must precede collaboration tools follows the same values-first pattern
- relates_to::[\[\[Authority Flows from the Person\]\]](../principles/Authority%20Flows%20from%20the%20Person.html) — the Self-Sovereign Identity principle that identity sovereignty precedes technical identity systems
