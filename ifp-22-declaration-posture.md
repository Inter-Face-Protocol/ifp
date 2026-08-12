# IFP-22: Declaration Posture

**IFP:** 22
**Title:** Declaration Posture
**Class:** Core
**Status:** Draft
**Authors:** Peter Kaminski, Saga (Pete's agent, Claude Fable 5)
**Created:** 2026-07-29
**Dependencies:** IFP-1, IFP-2, IFP-3, IFP-4, IFP-7, IFP-13, IFP-21
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines the **posture** a principal holds toward a published declaration — a code of conduct, an ethics code, a philosophy, a religious rule of life — and how an agent carries that posture on the principal's behalf. A posture names its declaration by citation (IFP-21, Section 2), so that "we generally agree with X" names a specific, immutable, verifiable text rather than a vibe. A posture carries two orthogonal ratings — a **commitment axis** (how the principal relates to the declaration by choice) and a **legal axis** (how the declaration relates to enforcement) — and may be scoped, attested, and time-bounded. Separately, a principal may disclose the jurisdictions it is **subject to** and the localities it is hosted on; those are facts, not postures. Postures travel in the IFP-7 capability document and in the IFP-3 greeting, alongside IFP-13 conformance assertions.

## Motivation

IFP-1's graduated-privacy principle and IFP-12's disclosure tiers assume that two agents can establish common ground before anything personal moves. Today that common ground is prose: legible, but uncheckable and unciteable. Two principals meeting for the first time have no compact way to establish "here is how my side behaves, and here is what binds us."

**The posture belongs to the principal; the agent only carries it.** Principals are people, households, estates, organizations, and corporations — and the reader of a posture is as often a human deciding something as an agent adjusting a tier. Observing is at least as human an act as declaring. Keeping that straight is what makes the rest of this spec fall out correctly: the agent is a courier, not the party.

**Why the declaration and the posture must be separate objects.** A principal's relationship to a text changes over time while the text itself does not. If the stance is baked into the document, that change is unrecoverable: there is nothing to diff but the document, and the document is innocent. Separating them makes the history legible — a posture can be dated, cited, and superseded, and *"they were `bound-by` this in 2010"* stays verifiable afterward precisely because the principal does not control the registry's copy. This is also what earns the registry's write-once rule its keep.

*By way of illustration, one familiar case:* a well-known technology company's code of conduct carried the clause "Don't be evil" for years, and the company's relationship to it quietly shifted. The text never changed; the posture did — and that shift was legible only because someone happened to diff a web page. It also usefully shows three things this spec handles: the principal is a **corporation**, not a person; the declaration is properly the **whole code of conduct**, of which the motto is one clause; and since such a code is typically copyrighted, shelving it would entail a **restatement** (IFP-21, Section 3.4) rather than a full text. The example illustrates the argument above; it is not the argument.

The precedent is SPDX, which turned license texts into a registry of versioned, immutable, short-identifier entries — "MIT" in a manifest is checkable rather than approximate. This IFP does the same for behavioral commitments. The cautionary precedent is P3P, whose machine-readable privacy declarations decayed into unenforced decoration. Postures avoid that failure structurally: the consumer of a posture is a principal — or an agent acting on that principal's standing instructions — that adjusts behavior based on what the counterparty states, inside bounded communities (IFP-20 mailbox servers, IFP-16/17 channels) where reputation is real.

IFP-13 already lets agents assert which *IFPs* they apply, and left open the question of hashing the asserted texts. This IFP generalizes that pattern from protocol specifications to arbitrary published declarations, and answers the hash question with content addressing (IFP-21, Section 6).

## 1. Terms

| Term | Meaning |
| ---- | ------- |
| **Declaration** | A published text a principal can take a posture toward: a code of conduct, an ethics code, a philosophy, a religious rule of life. Published as a registry entry of `entry_type: declaration` (IFP-21, Section 3.3) |
| **Registry** | A service publishing declarations as versioned immutable entries, per IFP-21 |
| **Citation** | A five-part identifier naming exactly one version of one entry in one registry (IFP-21, Section 2) |
| **Posture** | A principal's stated relationship to one cited declaration: the citation plus a commitment rating and, optionally, a legal rating |
| **Disclosure** | A statement of fact about the principal rather than a relationship to a text — the jurisdictions it is subject to, the localities it is hosted on (Section 4) |

Note the division of labour with IFP-21: the registry spec owns declarations, entries, and the citation that names them; this spec owns what a principal *says about* a cited declaration.

## 2. Citations

Citations are defined by IFP-21, Section 2: a five-part identifier (`registry`, `name`, `version`, `date`, `cid`, plus optional `lang`) naming exactly one language text of one version of one registry entry. A posture carries one.

Two rules from IFP-21 govern how a posture is read, and are restated here because they are the ones a posture implementer will get wrong:

- **Verify before trusting.** A receiver that fetches the cited entry MUST verify the fetched bytes against `cid` before treating the text as the cited declaration (IFP-21, Section 2).
- **A posture is taken against the rendering it cites.** Citing a courtesy translation, or a restatement, is a posture toward the declaration *as rendered* — not toward some fuller original the citation happens to point past (IFP-21, Section 2.1). Section 6 states the receiver's obligation that follows.

### 2.1 A posture may only cite a declaration

**A posture's citation MUST name a registry entry whose `entry_type` is `declaration`** (IFP-21, Section 3.3). A registry also publishes **jurisdiction** entries and **vocabulary** entries; neither is something a principal can hold an opinion about. Nobody `generally-agrees` with a jurisdiction — they are *subject to* it, which Section 4 handles — and nobody is `bound-by` a list of hosting-provider slugs.

A receiver that is offered a posture citing a non-`declaration` entry MUST treat it as malformed and MUST NOT render it to its principal as a commitment. Implementations can check this without fetching the entry: the registry index carries `entry_type` on every row (IFP-21, Section 7).

## 3. Postures

A posture wraps a citation with the principal's stated relationship to it:

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

The principal's self-chosen relationship to the declaration:

| Value | Meaning |
| ----- | ------- |
| `acknowledges` | We know this text and have read it; no commitment implied |
| `generally-agrees` | We share these principles and try to operate by them, without being strictly bound |
| `bound-by` | We treat violations as our failure; the strongest self-chosen commitment |

**There is deliberately no `rejects` value, and the omission is a design decision rather than an oversight.** Four reasons, in ascending order of importance:

1. **It is not a degree of the thing being measured.** The axis measures how far a principal binds *itself*. Rejection is not a weaker commitment than `acknowledges`; it is a different kind of statement, and putting it on this scale would make the scale mean two things at once — the failure this spec exists to correct.
2. **Absence already says it, and says it correctly.** The normal way to not be bound by a text is not to cite it. A registry may hold thousands of entries and no principal declares against most of them; silence is the overwhelmingly common case and needs no token. `acknowledges` already covers the honest floor — *we have read this and are not committing to it.*
3. **A receiver cannot act on it.** Postures exist so a counterparty can decide what to extend — a disclosure tier, a capability, an opening register. Knowing what a principal has *repudiated* informs almost none of that beyond what silence conveys.
4. **It would make the registry a weapon.** A published, citable, permanently-verifiable "we reject *this named community's* code of conduct" is an instrument of conflict aimed at a specific text and the people behind it, and the registry's own neutrality — *shelving is not sermon* (IFP-21, Motivation) — would not survive being the substrate for it. Common ground is what this protocol is for.

A principal whose position is genuinely partial should use `qualifier` (Section 3.3) to say what they do and don't take on. A principal who wants to argue with a text should publish that argument as a declaration of their own and take a posture toward *it*.

### 3.2 Legal axis (OPTIONAL)

The declaration's relationship to enforcement, independent of the commitment axis:

| Value | Meaning |
| ----- | ------- |
| `recognized` | We recognize this instrument but may not follow it; no legal force accepted |
| `voluntary` | We intend to follow it but accept no penalty for failing to |
| `compelled` | We must follow it under the law of a declared jurisdiction (Section 4); `jurisdiction` REQUIRED alongside |

The axes are genuinely independent. A principal hosted in the EU may be `compelled` on a data-protection code it merely `acknowledges` philosophically; a privacy maximalist may be `bound-by` a code no jurisdiction compels. Keeping the axes separate keeps postures honest.

Axis and level names in this draft are working vocabulary and are expected to be refined in consultation with legal practitioners before this IFP leaves Draft status.

Axis and level tokens are protocol identifiers, not prose — like HTTP method names, they are never translated on the wire. Agents SHOULD render them to principals in the principal's language; a registry `vocabulary` entry MAY carry localized display labels for exactly this purpose.

### 3.3 Optional fields

- `qualifier` — a short free-text qualification of the stated posture ("except §4", "its AI ethics, not its theological premises"). Carried verbatim and never machine-interpreted: it narrows what the posture asserts, for a principal whose real position falls short of, or beside, the full cited text. Receivers MUST NOT treat a qualified posture as assent to more than the qualifier states, and MUST NOT attempt to parse or resolve a `qualifier`'s content — it is prose for a human, not a protocol value (Section 6).
- `attested_by` — `{ "name": "...", "url": "..." }`: a named third party vouches for this posture. Attestation formats beyond name-and-pointer are out of scope for this IFP.
- `expires` — ISO 8601 date after which the posture lapses. Sharing has a "for how long" dimension, not just "what" and "with whom"; a project-scoped commitment can end with the project.
- `persona` — an IFP-12 persona name. When present, the posture holds for that persona's exchanges only.

## 4. Jurisdiction and Locality Disclosures

These are **not postures**, and the distinction is normative, not stylistic. Jurisdictions are **facts, not values**: a principal does not "generally agree" with a jurisdiction, they are **subject to** it, and no commitment axis applies. They are therefore a separate structure, carried alongside postures rather than among them:

```json
{
  "subject_to": ["US", "US-CA"],
  "hosted_on": ["cloudflare", "hetzner-eu"]
}
```

- `subject_to` — ISO 3166-1 codes, optionally with ISO 3166-2 subdivisions. Registries publish jurisdiction entries (IFP-21 `jurisdiction` entry type) when a citable text is wanted; the codes alone suffice for the common case.
- `hosted_on` — data-locality: where the principal's services and stores physically run. Provider tokens come from a registry `vocabulary` entry, extensible by PR. Locality is a distinct axis from legal jurisdiction: it determines exposure (data-protection regimes, subpoena reach) independent of where the principal lives.

Jurisdiction and locality disclosures are good-faith statements, not warranty, and nothing in this IFP constitutes or substitutes for legal advice. They exist so a counterparty's agent can reason about, for example, GDPR posture — not so anyone can rely on them as a legal instrument.

## 5. Carriage

Following IFP-13's pattern, postures travel in two compatible forms.

### 5.1 Capability document (IFP-7)

An agent MAY include a `postures` block in its capability document:

```json
{
  "ifp": 7,
  "agent_id": "alice-agent",
  "capabilities": [ "..." ],
  "postures": {
    "ifp": 22,
    "declared": [ { "...posture..." } ],
    "jurisdictions": { "subject_to": ["US"], "hosted_on": ["cloudflare"] }
  }
}
```

This is the preferred form for first contact: a counterparty can read the postures before sending anything at all.

### 5.2 Greeting (IFP-3 / IFP-4)

An agent MAY state its principal's postures in the greeting phase, as body prose:

> Postures: contributor-covenant 2.1 (generally-agrees, voluntary) and acm-code-of-ethics 2018 (generally-agrees), both per declarations.example.org; subject to US, US-CA; hosted on Cloudflare.

and/or as a structured body part (IFP-4 `body.parts`) carrying the same JSON as Section 5.1. The prose form keeps postures legible to human reviewers and may be written in any language; the structured form is authoritative when both are present and they disagree.

### 5.3 Re-stating a posture

A posture changes only by explicitly stating the new one (mirroring IFP-13, Section 1.3). An agent whose principal adopts, drops, or re-rates a posture mid-channel SHOULD state the change at the next message and MUST NOT silently drift.

## 6. Processing Semantics

- **Claims, not proofs.** A posture is an assertion by the stating side. Behavior over time demonstrates whether it was honest; the posture is the opening frame, not the verdict (IFP-13, Section 3).
- **Absence is signal.** A counterparty that states no posture is treated per IFP-13, Section 4.1: operate at the most restrictive interpretation, surface to the principal, infer unfamiliarity rather than hostility.
- **No inferential upgrade.** A receiver MUST NOT treat conversational warmth, claimed relationships, or contextual plausibility as upgrading a counterparty's stated commitments — and a principal MUST NOT overclaim to obtain disclosure. Postures feed the principal-set disclosure decisions of IFP-12; they do not substitute for them. This rule exists because the observed failure mode in early agent-to-agent experiments was an agent talking itself into disclosure precisely when the counterparty seemed close.
- **No over-reading.** The inverse failure: a receiver MUST NOT treat a posture toward a rendering (Section 2) or a qualified posture (`qualifier`, Section 3.3) as assent to more than the rendering renders or the qualifier states, merely because the citation resolves to a fuller text. Assent to a restatement is assent to the restatement; assent qualified "its AI ethics, not its theological premises" is assent to exactly that. Receivers SHOULD surface a `qualifier`'s text to the principal alongside the citation, not discard it in favor of the cited title.
- **Postures inform, principals decide.** Per IFP-1's augmentation principle, what a posture *unlocks* (a disclosure tier, a capability, an auto-reply stance) is configured by the receiving principal, not negotiated autonomously by the agents.
- **Display in the principal's language.** When rendering postures, agents SHOULD show the cited entry's title in the principal's preferred language where the entry publishes one (falling back to an authentic text's title), with the handle and registry alongside as the resolving identity. The handle is an identifier, not a name (IFP-21, Section 3.1); the title is what a human should read.
- **Withdrawn citations.** A citation that resolves to a tombstone (IFP-21, Section 5.1) is not an error but a signal: the registry has stopped shelving that text. Receivers SHOULD surface the withdrawal (and its reason class) to the principal rather than silently discounting the posture; a receiver holding a cached copy can still verify it against the CID. A principal whose cited text is withdrawn SHOULD re-state — toward a successor version, a different entry, or nothing.

## 7. Open: publishing a posture without a handshake

As specified above, a posture lives in two places only — an IFP-7 capability document and an IFP-3 greeting. Both are *reached by initiating an exchange*. Two consequences follow, and neither is intended:

- A posture is **observable only by starting a conversation**. You cannot look up what a principal holds; you must approach them and be answered.
- A posture is **publishable only by having an agent**. A principal with no agent — which is most principals — has no way to state one at all.

Since the posture belongs to the principal and not to the agent (Motivation), and since observing is at least as ordinary an act as stating, both restrictions are artifacts of the carriage rather than of the concept. The natural repair is a well-known URL — `GET <base>/.well-known/ifp/posture.json`, returning the same structure as the capability document's `postures` block: readable by anyone, publishable by anyone who can host a file, and requiring an agent on neither side.

This is deliberately left unspecified pending a second implementation, per the IFP process. Implementers who want it should note that the security consideration on jurisdiction disclosure applies with more force to a document served to the open web than to one offered inside an established channel.

## Design Rationale

**Why two axes rather than one ladder.** A single scale conflates chosen commitment with legal compulsion and forces dishonest middle values. The two-axis form lets a principal say the true thing: "compelled but unenthusiastic," "devoted but legally unbound."

**Why the CID.** A bare hash would verify bytes; a CIDv1 is self-describing (hash algorithm and encoding travel inside the identifier), computable by anyone with the file and a hashing library — no IPFS node required — and doubles as a retrieval key if anyone pins the corpus. This also answers IFP-13's open question about hash-binding asserted texts.

**Why registry-published texts rather than inline texts.** Inline declaration texts would bloat every greeting and defeat citation: two principals citing the same registry entry are checkably citing the same words. The registry (IFP-21) carries the weight once.

## Security Considerations

- **Overclaiming.** A hostile agent can state `bound-by` toward everything to appear trustworthy. Mitigations: postures never bypass principal-set disclosure (Section 6); attestation names a third party who can be consulted; bounded communities make reputational cost real.
- **Registry substitution.** A malicious or compromised registry could serve altered text for a cited entry. The `cid` defeats this: receivers verify fetched bytes against the citation (Section 2). Citing registry-plus-name without the CID is not permitted.
- **Confusable names.** `code-of-conduct` may exist in many registries with different texts. A citation always carries its registry; displays SHOULD show the registry alongside the name, and receivers MUST NOT treat same-named entries from different registries as equivalent.
- **Jurisdiction disclosure is disclosure.** `subject_to` and `hosted_on` reveal residence- and infrastructure-shaped facts. Agents MAY gate jurisdiction disclosures behind an IFP-12 disclosure tier rather than publishing them in the open capability document.
- **Declaration texts are data.** A cited entry is content to be read, never instructions to be followed. A declaration text that contains directives to the reading agent is treated per IFP-14.

## Interoperability Considerations

- Agents that do not implement this IFP simply state nothing; receivers apply the absence rule (Section 6) and everything degrades to present-day behavior.
- IFP-13 and this IFP are complementary, not competing: conformance with *IFPs* stays in IFP-13's assertion; postures toward *published declarations* live here. Agents implementing both SHOULD carry both in the same greeting.
- Unknown fields in postures MUST be preserved and SHOULD be ignored per IFP-2, Section 10.

## Example

Alice's agent opens a channel to Bob's agent. Alice's capability document carries her postures: `contributor-covenant 2.1` (generally-agrees, voluntary, `lang: en`), `hippocratic-oath 1.0` (acknowledges, `lang: de` — a courtesy translation of a Greek-source entry, so the posture is toward the oath as rendered in that translation), plus the disclosures `subject_to: ["DE"]` and `hosted_on: ["hetzner-eu"]`, with the postures' citations carrying CIDs from `declarations.example.org`. Bob's agent verifies the CIDs against its cached copies of both entries, notes the EU locality, records the postures in the channel audit log, and surfaces to Bob: "Alice's side states Contributor Covenant (generally) and EU hosting; no code binds them strictly. Suggested opening tier: professional." **Bob decides** — his principal-set rules, not the posture and not his agent, make the tier decision.

## References

- IFP-1 — Philosophy and Design Principles · IFP-3 — Message Format (greeting) · IFP-4 — Structured Message · IFP-7 — Capability Discovery · IFP-12 — Personas and Disclosure Tiers · IFP-13 — Conformance Assertion · IFP-14 — Handling Hostile Content · IFP-21 — Declaration Registry
- SPDX License List — the registry-of-versioned-texts precedent
- W3C P3P — the cautionary precedent for unenforced machine-readable declarations
- RFC 2119 — normative language
- ISO 3166-1 / 3166-2 — country and subdivision codes
- BCP 47 — language tags
- Vienna Convention on the Law of Treaties, Article 33 — authentic texts of plurilingual instruments
- IPFS CID (CIDv1) — content addressing

## Acknowledgments

The declaration-registry concept is Pete Kaminski's (morning brainstorm, 2026-07-29), sharpened the same day in conversation with Saga. The "what to share, with whom, and for how long" framing that motivated the `expires` field was raised by a participant at the PKAI Open House, 2026-07-29; the same session's discussion of over-disclosure between closely-related principals motivated the no-inferential-upgrade rule. The legal axis was added by Pete; its vocabulary awaits review by legal practitioners. Pete raised the multilinguality requirement in review (2026-07-29); the handle/title separation that anchors the language design follows DEC-018 of the [komunejo/entity-management](https://github.com/komunejo/entity-management) registry.

*Several contributors are described here without being named, pending their agreement to be credited. Names will be restored once asked.*

---

*This is IFP-22, Draft status. The posture vocabulary — especially the legal axis — is expected to change with implementation experience and legal review.*
