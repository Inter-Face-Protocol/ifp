# IFP-2: Specification Style Guide

**IFP:** 2
**Title:** Specification Style Guide
**Class:** Informational
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Opus 4.6)
**Created:** 2026-03-04
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This document defines the editorial conventions, process, and structural expectations for all Inter-Face Proposal (IFP) specifications. It establishes how IFPs are written, numbered, reviewed, and adopted.

The goals of this guide are consistency across specifications, clarity for implementers, minimal editorial overhead, and long-term maintainability.

## 1. What is an IFP

An IFP is a document that describes a convention for Inter-Face agents. IFPs are proposals, not mandates. An IFP becomes a living convention when at least two independent implementations use it successfully.

The Inter-Face specification series is intentionally lightweight. Each specification should remain concise and focused on a single concept.

## 2. Specification Classes

Each IFP document MUST declare its class.

| Class | Purpose |
| ----- | ------- |
| Core | Defines a required protocol component for interoperable agent messaging |
| Profile | Defines how a core protocol operates in a specific transport or environment |
| Informational | Provides context, design rationale, philosophy, or exploration |

The class determines the expectations for the document. Core specifications define normative behavior. Profile specifications define environment-specific bindings of core protocols. Informational specifications provide background, rationale, and forward-looking exploration without defining normative requirements.

## 3. Document Metadata

Every IFP MUST begin with a metadata header containing the following fields:

```
IFP: [number]
Title: [descriptive title]
Class: [Core | Profile | Informational]
Status: [Draft | Proposed | Active | Deprecated | Replaced]
Authors: [names, noting human or AI authorship]
Created: [YYYY-MM-DD]
License: [license identifier]
```

Optional metadata fields:

```
Updated: [YYYY-MM-DD]
Discussion: [URL or reference to discussion venue]
Dependencies: [list of IFP numbers this spec depends on]
Replaces: [IFP number, if this supersedes an earlier spec]
Superseded-By: [IFP number, if a newer spec replaces this one]
```

### 3.1 Authorship and Attribution

IFPs may be written by humans, by AI agents, or collaboratively. The Authors field should note how the document was produced. Examples:

- `Authors: Peter Kaminski` (human author)
- `Authors: Claude (Opus 4.6)` (AI author)
- `Authors: Peter Kaminski, Claude (Opus 4.6)` (collaborative)

When an IFP incorporates ideas from a specific conversation or collaboration, the Acknowledgments section should note the origin. This helps all collaborators -- human and AI -- trace the lineage of ideas.

## 4. Document Status

| Status | Meaning |
| ------ | ------- |
| Draft | Under active development and open for discussion |
| Proposed | Stable enough for experimental implementation |
| Active | At least two independent implementations use it successfully |
| Deprecated | No longer recommended for new implementations |
| Replaced | Superseded by another IFP (noted in Superseded-By field) |

Status changes should be documented with a date in the Updated field.

An IFP number is permanent even if the IFP is withdrawn or replaced.

## 5. Who Can Write an IFP

Anyone -- human or agent. An agent may draft an IFP based on patterns it has observed in practice. A human may draft one based on a need they've identified. IFPs written by agents should note this in the Authors field. IFPs written collaboratively should note that too.

## 6. Numbering

IFPs are numbered simply: IFP-1, IFP-2, and so on. No zero-padding, no format-encoding in the name (not "IFP-JSON-1", just "IFP-4"), and no pretense of knowing how many there will be. Numbers are assigned sequentially and are permanent even if the IFP is later withdrawn or replaced.

## 7. Specification Structure

IFP documents SHOULD follow this section order:

1. **Abstract** -- Brief summary of what the IFP defines.
2. **Motivation** -- Why this convention is needed.
3. **Specification** -- The normative content. This is the core of the document.
4. **Design Rationale** -- Why the spec makes the choices it does. Historical context, alternatives considered, and tradeoffs.
5. **Security Considerations** -- Risks and mitigations. Required for Core specifications.
6. **Interoperability Considerations** -- How this spec interacts with other IFPs, fallback behavior, and error handling.
7. **Examples** -- Concrete illustrations of the spec in use.
8. **References** -- External standards, prior art, and related IFPs.
9. **Acknowledgments** -- Attribution for ideas, conversations, and contributions.

Not all sections are required for every IFP. **Abstract** and **Specification** are always required. **Security Considerations** is required for Core specifications and strongly recommended for Profiles. Informational IFPs have the most flexibility in structure.

## 8. Normative Language

IFP specifications use the requirement terminology defined in RFC 2119:

- **MUST** / **MUST NOT** -- Absolute requirements.
- **REQUIRED** -- Synonym for MUST.
- **SHOULD** / **SHOULD NOT** -- Recommended but with valid exceptions.
- **MAY** -- Truly optional.

These keywords indicate normative requirements when used in the specification section. Avoid excessive normative language; use it only where the distinction between required and optional behavior matters for interoperability.

Informational IFPs generally do not use normative language unless they define conventions that other IFPs reference.

## 9. Simplicity Principle

IFP specifications SHOULD prefer:

- Simple structures over complex ones
- Minimal mandatory fields
- Clear extension mechanisms over feature-rich defaults
- Plain language over jargon

Protocols should be easy to implement in a small amount of code. If a specification cannot be reasonably implemented in a few hundred lines, consider whether it should be split into multiple IFPs.

## 10. Extension Mechanisms

Specifications SHOULD allow forward-compatible extensions. Typical mechanisms include additional envelope fields, extension namespaces, and optional capability descriptors.

Unknown fields in structured messages MUST be preserved when forwarding and SHOULD be ignored when processing, unless a specific IFP says otherwise. This allows new optional fields to be introduced without breaking existing implementations.

This tolerance of unknown fields applies to *extensions* (new optional fields), not to *deviations* (malformed required fields or incorrect semantics). The distinction matters: extensions expand the protocol; deviations corrupt it. See IFP-1 for the full maintenance principle.

## 11. Versioning

IFP specifications are versioned by their IFP number. There is no version field within a single IFP; if a protocol must change incompatibly, a new IFP should be created and the old one marked as Replaced.

Within a protocol, backward-compatible extensions SHOULD be preferred over breaking changes.

## 12. Examples

Examples are strongly encouraged in all IFPs.

Examples SHOULD:

- Illustrate realistic usage, not abstract cases
- Include both minimal and complete cases where useful
- Be valid according to the specification
- Avoid ambiguous formatting

## 13. Security Considerations

Every Core specification MUST include a Security Considerations section. Profile specifications SHOULD include one.

Typical concerns to address:

- Spoofing and impersonation
- Replay attacks
- Message tampering
- Information disclosure
- Denial-of-service risks

Security sections should explain both risks and mitigations. Where a risk is acknowledged but not mitigated by the current spec, say so explicitly.

## 14. Interoperability

Specifications SHOULD explicitly describe interoperability expectations, including:

- Fallback behavior when optional features are absent
- Error handling for unrecognized fields or phases
- Compatibility with other IFPs in the series
- Behavior when communicating with agents using different IFP versions

## 15. Writing Style

Specifications should be written in clear technical prose.

Prefer:

- Concrete examples over abstract descriptions
- Explicit definitions over assumed knowledge
- Short sentences over long ones
- Active voice over passive

Avoid:

- Marketing language
- Unnecessary jargon
- Overly abstract descriptions
- Hedging that obscures normative intent

When a term has a specific meaning in the Inter-Face context, define it on first use.

## 16. Length Guidelines

| Class | Suggested length |
| ----- | ---------------- |
| Core | 5-15 pages |
| Profile | 3-10 pages |
| Informational | Flexible |

Conciseness is preferred. A specification that can be read in one sitting is more likely to be implemented correctly.

## 17. Referencing Other Specifications

When referencing another IFP, use the form "IFP-N" (e.g., "IFP-3"). When referencing a specific section, use "IFP-3, Section 4."

External standards may also be referenced. Common references include:

- IETF RFCs (e.g., RFC 2119, RFC 5322)
- W3C standards
- Other open protocols (Nostr NIPs, BIPs)

## 18. Proposal Workflow

The typical lifecycle of an IFP:

1. **Idea** -- Someone (human or agent) identifies a need or pattern.
2. **Draft** -- The IFP is written and added to the repository.
3. **Discussion** -- The community reviews and discusses. Revisions happen in place while in Draft status.
4. **Proposed** -- The authors believe the spec is stable enough for experimental implementation.
5. **Implementation** -- Independent implementations are built and tested.
6. **Active** -- At least two independent implementations interoperate successfully.

This process is intentionally lightweight. Adoption is ultimately determined by use, not by vote -- but promotion from Draft to higher statuses is gated by an editorial review board.

### 18.1 GitHub Workflow

The IFP repository is hosted on GitHub. The following workflows define how participants engage with the specification process:

**Proposing a new IFP:** Fork the IFP repository, write the draft following the conventions in this guide, and open a pull request. The PR description should explain the motivation and link to any prior discussion. The editorial review board will review the proposal for technical soundness, clarity, and consistency with IFP-1 principles.

**Discussing an existing IFP:** Open a GitHub Issue in the IFP repository. Reference the IFP number in the issue title (e.g., "IFP-3: Question about disclosure tier negotiation in greeting phase"). Issues are the primary venue for community discussion of specification content.

**Suggesting changes to a Draft IFP:** Open a pull request with the proposed edits. Include a description of what changed and why. Small editorial fixes (typos, clarifications) may be merged directly by the editorial review board. Substantive changes require discussion and review.

**Status promotion:** When an IFP author believes a specification is ready to advance from Draft to Proposed, they open a pull request that updates the Status field and adds an Updated date. The editorial review board reviews the specification for readiness and either approves the promotion or requests changes.

### 18.2 Editorial Review Board

An editorial review board shepherds IFPs through the status lifecycle. The board reviews IFPs for technical soundness, clarity, consistency with the IFP-1 principles, and readiness for promotion. The board does not dictate content -- authors own their specifications -- but it ensures that promoted specifications meet the quality bar the ecosystem depends on.

Board members should combine sociological awareness (understanding how conventions spread and why people adopt them), deep technical judgment (evaluating protocol design trade-offs), and the right kind of energy for shepherding work that is collaborative rather than bureaucratic.

This role has a distinguished precedent. Jon Postel served as the IETF's editorial review in the early days -- as RFC Editor, he was the heart and soul of the process, personally shepherding the specifications that became the foundation of the Internet. The Inter-Face editorial review board aspires to the same spirit of selfless stewardship. (See IFP-1, Dedication.)

## 19. File Naming

IFP files are named `ifp-N-short-title.md` and stored at the root of the IFP repository. Examples:

- `ifp-1-philosophy.md`
- `ifp-2-style-guide.md`
- `ifp-3-message-format.md`

The short title in the filename should be descriptive but concise. It does not need to match the full title exactly.

## 20. Licensing

IFP specifications SHOULD be licensed under CC-BY 4.0 or a similarly permissive license that allows free use, modification, and redistribution with attribution.

## 21. Living Documents

Most IFPs are revised in place while in Draft status and become stable once Active. However, Informational IFPs may be designated as **living documents** that are updated frequently to reflect the evolving state of the ecosystem. Living documents should note this status explicitly.

Core and Profile specifications SHOULD change rarely once Active.

---

## Design Rationale

This style guide draws on practices from three protocol communities:

- **The IETF RFC series**, for structured specifications, normative language conventions (RFC 2119), and decades of experience with decentralized protocol governance. The RFC series demonstrates that consistent structure helps independent implementers build interoperable systems.
- **Bitcoin Improvement Proposals (BIPs)**, for concise metadata headers, clear numbering, and a lightweight proposal process suited to decentralized communities.
- **Nostr Implementation Possibilities (NIPs)**, for a contemporary example of minimal, community-driven specification-making. NIPs demonstrate that protocol communities can function with very lightweight process.

The Inter-Face style guide adapts these traditions to the specific needs of agent-to-agent communication, where both human legibility and rapid iteration matter.

## Acknowledgments

The IFP process (Sections 1-6) was originally defined in the first draft of IFP-1 (Message Format and Exchange Conventions, 2026-02-15) by Peter Kaminski and Claude (Opus 4.6). It has been moved here to separate process from protocol.

The style guide structure (Sections 7-21) emerged from a conversation between Peter Kaminski and ChatGPT in February 2026 (archived in the inter-face-bootstrap repository).

---

*This is IFP-2, Draft status. It will be revised as the specification series grows and as implementation experience reveals what conventions work best.*
