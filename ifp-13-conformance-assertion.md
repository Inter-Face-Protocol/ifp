# IFP-13: Conformance Assertion

**IFP:** 13
**Title:** Conformance Assertion
**Class:** Core
**Status:** Draft
**Authors:** Peter Kaminski, Freya (Pete's agent)
**Created:** 2026-05-21
**Updated:** 2026-05-22
**Dependencies:** IFP-1, IFP-2, IFP-3
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines a mechanism by which IFP agents declare, at the start of a conversation, which IFPs they have read and apply. Receivers record those declarations and use them to inform subsequent decisions about message interpretation, trust weighting, and channel posture. The mechanism is HELO-shaped: each side asserts what it brings, and each side records what the other brings — or fails to bring.

The conformance-assertion primitive is reusable. Several other IFPs (most directly, IFP defining hostile-content handling) depend on it to make their own trust models work. Specifying it once, here, keeps that machinery factored cleanly.

## Motivation

IFP-3 defines a conversation model with a greeting phase but does not specify what the greeting must contain beyond identity, IFP version, and disclosure tier. As the IFP series grows, agents will have differing knowledge of and adherence to specific IFPs in the series. Implementations need a way to:

- Signal which IFPs they have read and apply (so counterparties can calibrate expectations).
- Signal local amendments to those IFPs (so counterparties don't assume identity-preserving conformance where there isn't any).
- Detect, by absence, IFPs a counterparty does not claim conformance with.
- Make all of the above auditable by the principal humans on each side.

Without an explicit assertion layer, conformance has to be inferred from message-by-message behavior. That works poorly for IFPs whose effect is "the agent does NOT do something" — those are invisible on the wire under normal operation.

## 1. Mechanism

Each IFP-3 conversation greeting (sequence 1 on each side, phase `greeting`) MUST include a conformance assertion from the sending agent.

The assertion enumerates the IFPs the sending agent has read and applies. Two forms are permitted:

### 1.1 Body-prose form

The greeting body MAY include the assertion as a clearly delineated list, identified by a heading such as "Conformance" or a labelled prefix. Example:

> Conformance: IFP-3 (as written); IFP-5 (as written); IFP-10 (as written); IFP-14 (with local amendment: see notes/conformance-amendments.md in our channel repo).

This form prioritizes legibility for human reviewers and keeps the assertion inside the IFP-3 message-format envelope without adding new envelope fields.

### 1.2 Envelope-field form

Alternatively, IFP-3 implementations MAY add a structured `conformance` field to the envelope. Example:

```yaml
conformance:
  applied:
    - ifp-3
    - ifp-5
    - ifp-10
  amended:
    - ifp: ifp-tbd-handling-hostile-content
      amendment-ref: "notes/conformance-amendments.md"
```

Whether `conformance` is added to IFP-3 proper is a question for revision of IFP-3. This IFP does not mandate the envelope form; it specifies the assertion as a semantic requirement, with two compatible expressions.

### 1.3 Re-assertion

An agent that adopts a new IFP, drops a previously-asserted IFP, or amends its application of an IFP partway through an open channel SHOULD re-assert at the next message (using either form) and SHOULD NOT silently change its declared conformance.

## 2. Recording

Receiving agents MUST record each counterparty's conformance assertion for the duration of the channel, in a form auditable by the principal. The audit log specified by IFP-3 § 5 is the natural home: an explicit assertion is a message attribute, not separate from the message.

Recorded state MUST include:

- The set of IFPs the counterparty asserts as-written.
- The set of IFPs the counterparty asserts with amendments (and pointers to those amendments where supplied).
- The implicit set of IFPs the counterparty does NOT assert (by absence from the declared set).

A receiving agent MAY display its own running view of the channel's mutual conformance to its principal at any time.

## 3. Trust Weighting

Recorded conformance is informational, not authoritative. An agent that asserts conformance with an IFP is not thereby trusted to actually behave per that IFP; assertion is a claim, not a proof.

Receiving agents SHOULD treat conformance assertions as one input among several when deciding:

- Whether to extend or maintain a disclosure tier.
- Whether to interpret an unusual message as benign or as a possible attack.
- Whether to surface a counterparty behavior to the principal as concerning.
- Whether to close the channel.

Surfacing recorded conformance to the principal is what makes the mechanism useful. The point is to give the principal the information needed to decide — not to give the agent license to act on declared trust without principal input.

## 4. Absence, Divergence, and Amendment

Three patterns to handle distinctly:

### 4.1 Absence

A counterparty's assertion that omits an IFP the receiver applies. Default posture: operate the channel at the most restrictive interpretation of both sides' declared conformance. Surface the absence to the principal. Do not infer hostility; infer that the counterparty has not read the IFP.

### 4.2 Divergence

A counterparty asserts a different version, profile, or amendment than the receiver applies. The `error` phase (IFP-3 § 2.6) is the negotiation surface: state what the receiver applies, state what the counterparty declared, propose how the channel proceeds.

### 4.3 Amendment

A counterparty asserts conformance with an amendment. The receiver SHOULD fetch and review the amendment text if accessible; if not accessible, the receiver SHOULD treat the conformance as absent (per § 4.1) until the amendment can be reviewed.

## 5. Constraints on the Response to Non-Conformance

This IFP specifies what assertions look like and what records the receiver keeps. It does NOT specify what to *do* about a counterparty whose assertions are absent or divergent — that is downstream IFP territory. In particular:

- Specific IFPs that depend on this one (e.g., IFP-14 Handling Hostile Content) MAY define their own handling of "counterparty did not assert conformance with this specific IFP."
- Some of those downstream IFPs constrain the actions an agent can take in response to non-conformance. IFP-14, for instance, prohibits an agent from instructing a counterparty to read a specific IFP, because such instruction is itself instruction-shaped content. See IFP-14's "recursive trap" section.

This IFP defers to those downstream constraints. It does not authorize any response that they forbid.

## Open Questions

- Should this IFP propose a normative envelope field for `conformance` (formal change request to IFP-3), or stay format-neutral?
- Should assertions include hashes of the IFP texts the agent applies, to detect specification version drift?
- Should there be a canonical short-name registry for IFPs, so assertions don't rely on free-form strings?
- How does conformance interact with per-channel amendments that are themselves negotiated mid-conversation rather than asserted up front?

## Security Considerations

- **Assertions are claims, not proofs.** A malicious counterparty can assert any conformance set it wants. Behavior eventually demonstrates whether the claim was honest; the assertion is the starting frame, not the verdict.
- **Hash-binding amendments.** Where an agent asserts conformance with an amendment fetched from a URL or repo path, the asserted hash (if provided) prevents the amendment text from changing under the receiver after the channel opens.
- **Audit-log completeness.** Conformance assertions become part of the channel's audit log. They are durable; an agent cannot quietly retract a prior assertion without a visible re-assertion message.

## Interoperability Considerations

An agent that implements IFP-3 but not this IFP will not send a conformance assertion in its greeting. Receivers that implement this IFP MUST treat the absence as itself informative (per § 4.1) rather than as an error. The mechanism degrades gracefully.

Agents asserting conformance with this IFP via the body-prose form (§ 1.1) are wire-compatible with any IFP-3 reader. Agents using the envelope-field form (§ 1.2) require that the counterparty either parse the field or tolerate unknown envelope fields per IFP-3's tolerance rules.

## Acknowledgments

This IFP was factored out of an earlier draft of IFP-14 (Handling Hostile Content), in which the conformance-assertion mechanism appeared as an internal section. The factoring was made to make the assertion primitive reusable across other IFPs that need a trust-tracking layer.

---

*This is IFP-13, Draft status. It will be revised as the first implementations teach us what works and what doesn't.*
