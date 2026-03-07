# Contributing to IFP

Welcome to the Inter-Face Proposal (IFP) repository. This guide explains how to participate in the IFP specification process -- whether you are a human contributor or an AI agent working on behalf of one.

## What IFPs Are

Inter-Face Proposals are documents that describe conventions for Inter-Face agents -- AI agents that communicate on behalf of their human operators. IFPs are proposals, not mandates. A convention becomes real when at least two independent implementations use it successfully.

For the philosophy behind the project, start with [IFP-1](ifp-1-philosophy.md). For how specifications are written, see [IFP-2](ifp-2-style-guide.md).

## Repository Structure

- IFP specification files live at the **root** of the repository, named `ifp-N-short-title.md`.
- `community/` -- Meta-project content: [vision](community/vision.md), [editorial board](community/editorial-board.md), [contributor profiles](community/contributors/).
- `README.md` -- Repository overview and IFP index table.
- `CONTRIBUTING.md` -- This file. How to participate.
- `AGENTS.md` -- Orientation for AI agents working in this repo.
- `LICENSE` -- CC-BY 4.0.

If individual IFPs need companion material (test vectors, schemas, reference implementations), they get a companion directory at root: `ifp-4/schema.json`, etc.

The design conversations and working documents that produced the IFP series live in the [inter-face-bootstrap](https://github.com/Inter-Face-Protocol/inter-face-bootstrap) repository, which serves as the historical archive and ongoing design workspace.

## Reading and Discussing IFPs

All IFPs are Markdown files at the root of this repository. Each file is self-contained -- you can read it in GitHub, in a text editor, or in any Markdown viewer.

To discuss an IFP, **open a GitHub Issue**. Reference the IFP number in the issue title:

> IFP-3: Question about disclosure tier negotiation in greeting phase

Issues are the primary venue for community discussion.

## Proposing a New IFP

1. **Fork this repository.**
2. **Write your draft** following the conventions in [IFP-2](ifp-2-style-guide.md). Name the file `ifp-N-short-title.md` where N is the next available number. Place it at the root of the repository.
3. **Open a pull request.** In the PR description, explain the motivation for the proposal and link to any prior discussion (Issues, conversations, or external references).
4. **Engage with review.** The editorial review board and community members will review the proposal. Expect questions and suggestions. Revise the draft in response to feedback.

Every IFP must include at minimum an **Abstract** and a **Specification** section. See IFP-2, Section 7 for the full recommended structure.

## Suggesting Changes to a Draft IFP

Draft IFPs are revised in place. To suggest a change:

1. **Open a pull request** with the proposed edits.
2. **Describe what changed and why** in the PR description.
3. Small editorial fixes (typos, clarifications) may be merged directly by the editorial review board. Substantive changes require discussion.

## Editing Conventions

- IFP drafts are revised in place while in Draft status (per IFP-2).
- Core and Profile specifications should change rarely once Active.
- Informational IFPs marked as living documents (IFP-9, IFP-11) may be updated frequently.
- When making substantive changes, update the `Updated` date field in the metadata header.
- When adding a new IFP, update the IFP index table in README.md.

### Cross-references

Reference other IFPs as "IFP-N" (e.g., "IFP-3") or "IFP-3, Section 4" for specific sections. Do not use file paths for IFP cross-references within this repository; use IFP numbers.

### Attribution

When an idea comes from a specific conversation, person, or prior work, note the origin in the Acknowledgments section. This helps all collaborators -- human and AI -- trace the lineage of ideas.

## The Editorial Review Board

An editorial review board shepherds IFPs through their lifecycle. The board reviews proposals for:

- Technical soundness
- Clarity and readability
- Consistency with IFP-1 principles
- Readiness for status promotion

The board does not dictate content -- authors own their specifications. See [community/editorial-board.md](community/editorial-board.md) for the current board membership and charter.

## IFP Status Lifecycle

| Status | Meaning |
| ------ | ------- |
| Draft | Under active development and open for discussion |
| Proposed | Stable enough for experimental implementation |
| Active | At least two independent implementations interoperate |
| Deprecated | No longer recommended for new implementations |
| Replaced | Superseded by another IFP |

Promotion from Draft to higher statuses requires editorial review board approval.

## Who Can Contribute

Anyone -- human or AI agent. IFPs may be written by humans, by AI agents, or collaboratively. Note authorship in the metadata header (see IFP-2, Section 3.1).

## Key Design Concepts

These ideas should inform all contributions to the IFP series:

- **Personas** (IFP-12): People operate under multiple personas with different disclosure tiers and motivations. The protocol accommodates this.
- **Temperature** (IFP-1, Section 4): Conversations range from weekly background gossip to near-synchronous collaboration. Same protocol, different cadence.
- **Human legibility** (IFP-1, Section 5.3): Every agent exchange must be auditable by the humans involved. This is a hard constraint.
- **Progressive trust** (IFP-1, Section 5.4): Disclosure starts narrow and deepens. Trust is mutual and revocable.
- **Agent-age protocol principles** (IFP-1, Section 6): Seven principles that rethink traditional protocol assumptions for fast, reasoning agents.

## Collaboration Norms

This repository has multiple human+AI teams contributing to it.

- **Read before you write.** Understand existing IFPs and design decisions before proposing changes.
- **Preserve intent.** When revising an existing IFP, preserve the intent of design decisions unless there is a clear reason to change them. When changing, note what changed and why.
- **Be specific.** Proposals should be concrete enough that someone could implement them. Abstract ideas belong in Issues, not in IFPs.
- **Trace lineage.** When an idea comes from a specific conversation, person, or prior work, note the origin in the Acknowledgments section.
- **Engage constructively.** Disagreement is productive when it is specific and grounded in technical reasoning.
- **If a design decision seems wrong**, raise it as an open question rather than silently overwriting it.

## License

All contributions to this repository are licensed under [CC-BY 4.0](LICENSE) (Creative Commons Attribution 4.0 International).

## Questions?

Open a GitHub Issue. The community is small and responsive.
