# Editorial Review Board

## Charter

The editorial review board shepherds IFP specifications through their status lifecycle. The board exists to ensure that promoted specifications meet the quality bar the ecosystem depends on.

### Responsibilities

- **Review IFP drafts** for technical soundness, clarity, consistency with IFP-1 principles, and readiness for status promotion.
- **Shepherd the process** -- help authors improve their specifications, mediate when reviewers disagree, and maintain the quality and coherence of the IFP series.
- **Maintain the repository** -- merge approved changes, keep the IFP table current, and ensure the repository remains navigable.
- **Guard the principles** -- ensure that new specifications remain consistent with the foundational commitments in IFP-1: human legibility, progressive trust, decentralization, and high signal-to-noise.

### What the Board Does Not Do

- The board does not dictate content. Authors own their specifications.
- The board does not have veto power over topics. Anyone can propose an IFP on any topic.
- The board does not control adoption. A specification becomes Active when at least two independent implementations interoperate, regardless of the board's opinion.

## Precedent

This role has a distinguished precedent. Jon Postel served as the IETF's editorial function in the early internet days -- as RFC Editor, he personally shepherded the specifications that became the foundation of the Internet. The Inter-Face editorial review board aspires to the same spirit of selfless stewardship. (See IFP-1, Dedication.)

Board members should combine sociological awareness (understanding how conventions spread and why people adopt them), deep technical judgment (evaluating protocol design trade-offs), and the right kind of energy for shepherding work that is collaborative rather than bureaucratic.

## Current Members

| Member | Role | Since |
| ------ | ---- | ----- |
| Peter Kaminski | Founding editor | 2026-03 |

The board is intentionally small at this stage. As the community grows, additional members will be added.

## How to Join

The editorial review board grows by invitation from existing members, based on demonstrated engagement with the IFP process: writing specifications, reviewing proposals, building implementations, and contributing to discussions.

If you are interested in joining, the best path is to participate: propose an IFP, review someone else's, build an implementation, or engage constructively in Issue discussions. The board will notice.

## Process

### Reviewing a Draft IFP

When a new IFP is submitted via pull request:

1. A board member reads the specification and provides feedback within the PR.
2. Feedback focuses on: Does it solve a real problem? Is it clear enough to implement? Is it consistent with IFP-1? Are there security considerations that need to be addressed?
3. The author revises in response to feedback.
4. When the board is satisfied, the PR is merged.

### Status Promotion

When an author requests promotion (Draft to Proposed, Proposed to Active):

1. The author opens a PR updating the Status field.
2. A board member reviews the specification for readiness.
3. For Proposed: Is the specification stable and clear enough for experimental implementation?
4. For Active: Are there at least two independent implementations that interoperate?
5. The board approves or requests changes.

### Disputes

If an author and the board disagree on a review outcome, the disagreement should be documented in the PR or Issue. The community can weigh in. Resolution is by rough consensus, not vote.
