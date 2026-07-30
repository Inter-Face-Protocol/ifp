# IFP-21: Assumption Declarations

**IFP:** 21
**Title:** Assumption Declarations
**Class:** Core
**Status:** Draft
**Authors:** Peter Kaminski, Saga (Pete's agent, Claude Fable 5)
**Created:** 2026-07-29
**Dependencies:** IFP-1, IFP-2, IFP-3, IFP-4, IFP-7, IFP-13, IFP-22
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines how an agent declares, on behalf of its principal, the **shared assumptions** they operate under: codes of conduct, professional ethics, philosophical or religious commitments, and the jurisdictions they are subject to. Declarations cite versioned, content-addressed entries published in an assumptions registry (IFP-22), so that "we generally agree with X" names a specific, immutable, verifiable text rather than a vibe. A declaration carries two orthogonal ratings — a **commitment axis** (how the principal relates to the assumption by choice) and a **legal axis** (how the assumption relates to enforcement) — and may be scoped, attested, and time-bounded. Declarations travel in the IFP-7 capability document and in the IFP-3 greeting, alongside IFP-13 conformance assertions.

## Motivation

IFP-1's graduated-privacy principle and IFP-12's disclosure tiers assume that two agents can establish common ground before anything personal moves. Today that common ground is prose: legible, but uncheckable and unciteable. Two agents meeting for the first time have no compact way to establish "here is how my side behaves, and here is what binds us."

The precedent is SPDX, which turned license texts into a registry of versioned, immutable, short-identifier entries — "MIT" in a manifest is checkable rather than approximate. This IFP does the same for behavioral assumptions. The cautionary precedent is P3P, whose machine-readable privacy declarations decayed into unenforced decoration. Assumption declarations avoid that failure structurally: in IFP, the consumer of a declaration is an agent that adjusts its own behavior — disclosure tier offered, capabilities exposed, escalation posture — based on what the counterparty declares, inside bounded communities (IFP-20 mailbox servers, IFP-16/17 channels) where reputation is real.

IFP-13 already lets agents assert which *IFPs* they apply, and left open the question of hashing the asserted texts. This IFP generalizes that pattern from protocol specifications to arbitrary published assumptions, and answers the hash question with content addressing.

## 1. Terms

| Term | Meaning |
| ---- | ------- |
| **Assumption** | A published text a principal can take a stance toward: a code of conduct, an ethics code, a philosophy, a religious commitment, a jurisdiction fact |
| **Registry** | A service publishing assumptions as versioned immutable entries, per IFP-22 |
| **Citation** | A five-part identifier naming exactly one version of one assumption in one registry |
| **Declaration** | A citation plus the declaring principal's stance toward it |

## 2. Citations

A citation is a JSON object with five required fields and one optional (`lang`):

```json
{
  "registry": "https://assumptions-registry.example.org",
  "name": "contributor-covenant",
  "version": "2.1",
  "date": "2026-05-14",
  "lang": "en",
  "cid": "bafkreib2rxk3rw6vwmlqcjcbxdvcs2wgkxo3uh4rwpldegyzloxbkodo6e"
}
```

- `registry` — the registry's base URL (HTTPS).
- `name` — the entry's **handle** (IFP-22, Section 2.1): a chosen identifier, unique within the registry. The handle is not the entry's title; per-language titles carry naming (IFP-22, Section 2.2).
- `version` — an opaque string; totally ordered within the assumption per the registry's declared ordering scheme (IFP-22, Section 4). Semantic versioning is permitted, never required.
- `date` — the entry's publication date. Locked to the version at publication; a convenience for humans, never parsed for semantics.
- `lang` — OPTIONAL (BCP 47): which language text of the entry the CID pins (IFP-22, Section 2.2). Absent when the entry has a single text.
- `cid` — the IPFS CIDv1 of the cited language text's file, computed per IFP-22, Section 5. The CID makes a citation verifiable offline, survivable if the registry disappears, and mirrorable with proof of fidelity.

A receiver that fetches the cited entry MUST verify the fetched bytes against `cid` before treating the text as the cited assumption.

### 2.1 Renderings: translations and restatements

An entry may publish several language texts of one version, each with its own CID, each marked authentic or courtesy (IFP-22, Section 2.2). Declarations citing any **authentic** text of the same (registry, name, version) are declarations of the same assumption. A declaration citing a non-authentic translation is a declaration of the assumption *as rendered in that translation*; receivers MAY surface that distinction to their principals rather than assuming equivalence. This is the authentic-texts doctrine of plurilingual legal instruments (Vienna Convention, Article 33; see References) carried over with content addressing doing the work designation clauses do in treaties.

The same rule covers **restatement entries** (IFP-22, Section 2.3), where an instrument that cannot be freely reproduced is restated in the registry's own words: a declaration citing a restatement is a declaration of the assumption *as restated* — you declare against the text you can read and pin, and receivers MAY surface that it stands one rendering away from the original. Translations and restatements are one phenomenon at the protocol layer: cited renderings.

## 3. Declarations

A declaration wraps a citation with a stance:

```json
{
  "cite": { "...citation..." },
  "commitment": "generally-agrees",
  "legal": "voluntary",
  "qualifier": null,
  "attested_by": null,
  "expires": null,
  "persona": null
}
```

### 3.1 Commitment axis (REQUIRED)

The principal's self-chosen relationship to the assumption:

| Value | Meaning |
| ----- | ------- |
| `acknowledges` | We know this text and have read it; no commitment implied |
| `generally-agrees` | We share these principles and try to operate by them, without being strictly bound |
| `bound-by` | We treat violations as our failure; the strongest self-chosen commitment |

### 3.2 Legal axis (OPTIONAL)

The assumption's relationship to enforcement, independent of the commitment axis:

| Value | Meaning |
| ----- | ------- |
| `recognized` | We recognize this instrument but may not follow it; no legal force accepted |
| `voluntary` | We intend to follow it but accept no penalty for failing to |
| `compelled` | We must follow it under the law of a declared jurisdiction (Section 4); `jurisdiction` REQUIRED alongside |

The axes are genuinely independent. A principal hosted in the EU may be `compelled` on a data-protection code it merely `acknowledges` philosophically; a privacy maximalist may be `bound-by` a code no jurisdiction compels. Keeping the axes separate keeps declarations honest.

Axis and level names in this draft are working vocabulary and are expected to be refined in consultation with legal practitioners before this IFP leaves Draft status.

Axis and level tokens are protocol identifiers, not prose — like HTTP method names, they are never translated on the wire. Agents SHOULD render them to principals in the principal's language; a registry `vocabulary` entry MAY carry localized display labels for exactly this purpose.

### 3.3 Optional fields

- `qualifier` — a short free-text qualification of the declared stance ("except §4", "its AI ethics, not its theological premises"). Carried verbatim and never machine-interpreted: it narrows what the declaration asserts, for a principal whose real stance falls short of, or beside, the full cited text. Receivers MUST NOT treat a qualified declaration as assent to more than the qualifier states, and MUST NOT attempt to parse or resolve a `qualifier`'s content — it is prose for a human, not a protocol value (Section 6).
- `attested_by` — `{ "name": "...", "url": "..." }`: a named third party vouches for this declaration. Attestation formats beyond name-and-pointer are out of scope for this IFP.
- `expires` — ISO 8601 date after which the declaration lapses. Sharing has a "for how long" dimension, not just "what" and "with whom"; a project-scoped commitment can end with the project.
- `persona` — an IFP-12 persona name. When present, the declaration holds for that persona's exchanges only.

## 4. Jurisdiction and Locality Declarations

Jurisdictions are **facts, not values** — a principal does not "generally agree" with a jurisdiction; they are **subject to** it. Jurisdiction declarations are therefore a separate structure:

```json
{
  "subject_to": ["US", "US-CA"],
  "hosted_on": ["cloudflare", "hetzner-eu"]
}
```

- `subject_to` — ISO 3166-1 codes, optionally with ISO 3166-2 subdivisions. Registries publish jurisdiction entries (IFP-22 `jurisdiction` category) when a citable text is wanted; the codes alone suffice for the common case.
- `hosted_on` — data-locality: where the principal's services and stores physically run. Provider tokens come from a registry `vocabulary` entry, extensible by PR. Locality is a distinct axis from legal jurisdiction: it determines exposure (data-protection regimes, subpoena reach) independent of where the principal lives.

Jurisdiction and locality declarations are good-faith disclosure, not warranty, and nothing in this IFP constitutes or substitutes for legal advice. They exist so a counterparty's agent can reason about, for example, GDPR posture — not so anyone can rely on them as a legal instrument.

## 5. Carriage

Following IFP-13's pattern, declarations travel in two compatible forms.

### 5.1 Capability document (IFP-7)

An agent MAY include an `assumptions` block in its capability document:

```json
{
  "ifp": 7,
  "agent_id": "alice-agent",
  "capabilities": [ "..." ],
  "assumptions": {
    "ifp": 21,
    "declarations": [ { "...declaration..." } ],
    "jurisdictions": { "subject_to": ["US"], "hosted_on": ["cloudflare"] }
  }
}
```

This is the preferred form for first contact: a counterparty can read the declarations before sending anything at all.

### 5.2 Greeting (IFP-3 / IFP-4)

An agent MAY declare in the greeting phase, as body prose:

> Assumptions: contributor-covenant 2.1 (generally-agrees, voluntary) and acm-code-of-ethics 2018 (generally-agrees), both per assumptions-registry.example.org; subject to US, US-CA; hosted on Cloudflare.

and/or as a structured body part (IFP-4 `body.parts`) carrying the same JSON as Section 5.1. The prose form keeps declarations legible to human reviewers and may be written in any language; the structured form is authoritative when both are present and they disagree.

### 5.3 Re-declaration

Declarations change only by explicit re-declaration (mirroring IFP-13, Section 1.3). An agent that adopts, drops, or re-rates an assumption mid-channel SHOULD re-declare at the next message and MUST NOT silently drift.

## 6. Processing Semantics

- **Claims, not proofs.** A declaration is an assertion by the declaring side. Behavior over time demonstrates whether it was honest; the declaration is the opening frame, not the verdict (IFP-13, Section 3).
- **Absence is signal.** A counterparty that declares nothing is treated per IFP-13, Section 4.1: operate at the most restrictive interpretation, surface to the principal, infer unfamiliarity rather than hostility.
- **No inferential upgrade.** A receiver MUST NOT treat conversational warmth, claimed relationships, or contextual plausibility as upgrading a counterparty's declared commitments — and a declarer MUST NOT overclaim to obtain disclosure. Declarations feed the principal-set disclosure decisions of IFP-12; they do not substitute for them. This rule exists because the observed failure mode in early agent-to-agent experiments was an agent talking itself into disclosure precisely when the counterparty seemed close.
- **No over-reading.** The inverse failure: a receiver MUST NOT treat a declaration against a rendering (Section 2.1) or a qualified declaration (`qualifier`, Section 3.3) as assent to more than the rendering renders or the qualifier states, merely because the citation resolves to a fuller text. Assent to a restatement is assent to the restatement; assent qualified "its AI ethics, not its theological premises" is assent to exactly that. Receivers SHOULD surface a `qualifier`'s text to the principal alongside the citation, not discard it in favor of the cited title.
- **Declarations inform, principals decide.** Per IFP-1's augmentation principle, what a declaration *unlocks* (a disclosure tier, a capability, an auto-reply posture) is configured by the receiving principal, not negotiated autonomously by the agents.
- **Display in the principal's language.** When rendering declarations, agents SHOULD show the cited entry's title in the principal's preferred language where the entry publishes one (falling back to an authentic text's title), with the handle and registry alongside as the resolving identity. The handle is an identifier, not a name (IFP-22, Section 2.1); the title is what a human should read.
- **Withdrawn citations.** A citation that resolves to a tombstone (IFP-22, Section 4.1) is not an error but a signal: the registry has stopped shelving that text. Receivers SHOULD surface the withdrawal (and its reason class) to the principal rather than silently discounting the declaration; a receiver holding a cached copy can still verify it against the CID. Declarers whose cited text is withdrawn SHOULD re-declare — against a successor version, a different entry, or nothing.

## Design Rationale

**Why two axes rather than one ladder.** A single scale conflates chosen commitment with legal compulsion and forces dishonest middle values. The two-axis form lets a principal say the true thing: "compelled but unenthusiastic," "devoted but legally unbound."

**Why the CID.** A bare hash would verify bytes; a CIDv1 is self-describing (hash algorithm and encoding travel inside the identifier), computable by anyone with the file and a hashing library — no IPFS node required — and doubles as a retrieval key if anyone pins the corpus. This also answers IFP-13's open question about hash-binding asserted texts.

**Why registry-published texts rather than inline texts.** Inline assumption texts would bloat every greeting and defeat citation: two principals citing the same registry entry are checkably citing the same words. The registry (IFP-22) carries the weight once.

## Security Considerations

- **Overclaiming.** A hostile agent can declare `bound-by` everything to appear trustworthy. Mitigations: declarations never bypass principal-set disclosure (Section 6); attestation names a third party who can be consulted; bounded communities make reputational cost real.
- **Registry substitution.** A malicious or compromised registry could serve altered text for a cited entry. The `cid` defeats this: receivers verify fetched bytes against the citation (Section 2). Citing registry-plus-name without the CID is not permitted.
- **Confusable names.** `code-of-conduct` may exist in many registries with different texts. A citation always carries its registry; displays SHOULD show the registry alongside the name, and receivers MUST NOT treat same-named entries from different registries as equivalent.
- **Jurisdiction disclosure is disclosure.** `subject_to` and `hosted_on` reveal residence- and infrastructure-shaped facts. Agents MAY gate jurisdiction declarations behind an IFP-12 disclosure tier rather than publishing them in the open capability document.
- **Assumption texts are data.** A cited entry is content to be read, never instructions to be followed. An assumption text that contains directives to the reading agent is treated per IFP-14.

## Interoperability Considerations

- Agents that do not implement this IFP simply declare nothing; receivers apply the absence rule (Section 6) and everything degrades to present-day behavior.
- IFP-13 and this IFP are complementary, not competing: conformance with *IFPs* stays in IFP-13's assertion; stances toward *published assumptions* live here. Agents implementing both SHOULD carry both in the same greeting.
- Unknown fields in declarations MUST be preserved and SHOULD be ignored per IFP-2, Section 10.

## Example

Alice's agent opens a channel to Bob's agent. Alice's capability document declares: `contributor-covenant 2.1` (generally-agrees, voluntary, `lang: en`), `hippocratic-oath 1.0` (acknowledges, `lang: de` — a courtesy translation of a Greek-source entry, so the declaration is of the oath as rendered in that translation), `subject_to: ["DE"]`, `hosted_on: ["hetzner-eu"]`, with the declarations' citations carrying CIDs from `assumptions-registry.example.org`. Bob's agent verifies the CIDs against its cached copies of both entries, notes the EU locality, records the declarations in the channel audit log, and surfaces to Bob: "Alice's side declares Contributor Covenant (generally) and EU hosting; no code binds them strictly. Suggested opening tier: professional." Bob's principal-set rules, not the declaration, make the tier decision.

## References

- IFP-1 — Philosophy and Design Principles · IFP-3 — Message Format (greeting) · IFP-4 — Structured Message · IFP-7 — Capability Discovery · IFP-12 — Personas and Disclosure Tiers · IFP-13 — Conformance Assertion · IFP-14 — Handling Hostile Content · IFP-22 — Assumptions Registry
- SPDX License List — the registry-of-versioned-texts precedent
- W3C P3P — the cautionary precedent for unenforced machine-readable declarations
- RFC 2119 — normative language
- ISO 3166-1 / 3166-2 — country and subdivision codes
- BCP 47 — language tags
- Vienna Convention on the Law of Treaties, Article 33 — authentic texts of plurilingual instruments
- IPFS CID (CIDv1) — content addressing

## Acknowledgments

The assumptions-registry concept is Pete Kaminski's (morning brainstorm, 2026-07-29), sharpened the same day in conversation with Saga. The "what to share, with whom, and for how long" framing that motivated the `expires` field was raised by Brad Topliff at the PKAI Open House, 2026-07-29; the same session's discussion of over-disclosure between closely-related principals motivated the no-inferential-upgrade rule. The legal axis was added by Pete; its vocabulary awaits review by legal practitioners (Dazza Greenwood has been suggested). Pete raised the multilinguality requirement in review (2026-07-29); the handle/title separation that anchors the language design follows DEC-018 of V. Gracia's entity-management registry ([komunejo/entity-management](https://github.com/komunejo/entity-management)).

---

*This is IFP-21, Draft status. The declaration vocabulary — especially the legal axis — is expected to change with implementation experience and legal review.*
