# IFP-22: Assumptions Registry

**IFP:** 22
**Title:** Assumptions Registry
**Class:** Core
**Status:** Draft
**Authors:** Peter Kaminski, Saga (Pete's agent, Claude Fable 5)
**Created:** 2026-07-29
**Dependencies:** IFP-2, IFP-21
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines the publication format for an **Assumptions Registry**: a service that publishes assumptions — codes of conduct, professional ethics, philosophies, religious commitments, jurisdiction facts, and shared vocabularies — as versioned, immutable, content-addressed entries that IFP-21 declarations cite. A registry is a git repository of markdown files with YAML frontmatter, published as a static site with a machine-readable index; the write path is a pull request, and immutability is enforced in CI. Anyone can host a registry.

## Motivation

IFP-21 citations need somewhere stable to point. The requirements are modest and specific: entries must be resolvable over HTTPS, immutable once published, verifiable against a content hash, mirrorable, and legible to humans in a text editor. A database-backed service would satisfy none of these better than a git repository published statically — and git supplies version history, a review-gated write path, and hosting-anywhere for free.

The registry deliberately does *not* interpret, rank, or endorse what it publishes. It is shelving, not sermon: the SPDX License List holds licenses its maintainers would never choose, and an assumptions registry may hold philosophies its operator does not share. Stance-taking belongs to the principals who cite entries (IFP-21), and to registry operators only in their choice of what to shelve.

## 1. Registry Identity

- A registry is identified by its **base URL** (HTTPS), which is the `registry` field of every citation into it.
- "Assumptions Registry" is the class name. An **instance name** is the operator's chosen label for one registry, conventionally the leading DNS label or path segment of the base URL — `assumptions-registry` in `https://assumptions-registry.example.org` — but any label the operator prefers.
- A registry MUST publish a descriptor at:

```
GET <base>/.well-known/ifp/assumptions-registry.json
```

```json
{
  "ifp": 22,
  "instance": "assumptions-registry",
  "operator": "Example Foundation",
  "ordering": "per-entry; see entries",
  "policy": "<base>/policy",
  "index": "<base>/index.json"
}
```

## 2. Entries

An entry is a set of one or more **language texts** per (name, version): `entries/<name>/<version>.<lang>.md` with `<lang>` a BCP 47 tag (`2.1.en.md`, `2.1.es.md`), or bare `entries/<name>/<version>.md` where a version has a single text. Each language text is one markdown file with its own frontmatter, its own title, and its own CID.

```markdown
---
name: contributor-covenant
version: "2.1"
date: 2026-05-14
category: conduct
title: Contributor Covenant, v2.1
language: en
authentic: true
type: full-text
license: CC-BY-4.0
source_url: https://www.contributor-covenant.org/
supersedes: "2.0"
---

# Contributor Covenant, version 2.1

[the canonical text]
```

Frontmatter fields — REQUIRED: `name` (the handle, Section 2.1), `version` (string), `date` (ISO 8601, locked at publication), `category` (Section 3), `title` (in this text's own language), `language` (BCP 47 — always declared, never implied), `type` (`full-text` | `restatement`, Section 2.3), `license` (the text must be lawfully copyable **verbatim**: what the CID story needs is byte-exact reproduction for mirroring and pinning, not modification rights, so a `verbatim-only` class — permitting exact-copy reproduction without modification — satisfies the requirement as fully as a free license does). OPTIONAL: `authentic` (Section 2.2), `source_url`, `accessed`, `source_hash`, `supersedes`, `codes` (jurisdiction entries: ISO 3166 codes), `kind` (the document's form — creed, oath, code of conduct, and so on; tokens come from a registry `vocabulary` entry, extensible by PR, the same pattern IFP-21's `hosted_on` provider tokens use), `notes`.

### 2.1 Handles

The `name` field is the entry's **handle**: a chosen identifier, not the entry's name. Handles are lowercase ASCII letters, digits, and hyphens; 1–64 characters; no leading or trailing hyphen. This is a constraint on an identifier, not on any language — the handle carries no naming duty, because per-language titles (Section 2.2) are the entry's names.

A handle is **chosen at first publication and never derived**: it may be a romanization in the operator's preferred scheme, a loanword, an initialism, or an arbitrary token — `rinri-kokoroe`, `ethik-2026`, and `e17` are equally conformant, and the registry has no opinion among them. Tooling MUST NOT generate handles from titles. A handle is never renamed; citations resolve through it.

### 2.2 Language texts and authenticity

A version's language texts are parallel renderings, not ordered revisions. Adding a translation to a published version adds a new file and alters none, and is permitted at any time; each published language text is individually write-once (Section 4).

Where a version has several texts, each declares `authentic: true` or `false`. **Authentic** texts are authoritative statements of the assumption — several may be equally authentic, in the manner of plurilingual legal instruments — while non-authentic texts are courtesy translations. A version with a single text is authentic by definition (`authentic` may be omitted). IFP-21, Section 2.1 defines what citing each kind means.

Each language text carries its own `title`, in its own language. The titles are the entry's names, and they are plural.

### 2.3 Full-text and restatement entries

- **`full-text`** — the body IS the instrument's text. The citation's CID pins the words themselves.
- **`restatement`** — the instrument cannot be freely reproduced (or the honest unit of agreement is a summary), so the body is the registry's **own original prose restating what the instrument holds**, and that restatement is itself the canonical cited text. `source_url` (REQUIRED for restatements) points at the original; `accessed` records the as-of date the restatement describes; `source_hash` (sha256 of the external form, when one is stable enough to hash) binds it.

Restatement rules:

- **Original prose, not light editing.** Copyright protects expression, not ideas; a restatement conveys what the instrument requires in genuinely new words. Close paraphrase is not restatement. Naming the original is nominative use and expected.
- **A restatement is a claim about the original as of a date.** Originals get revised silently; `accessed` (and `source_hash` where possible) scope the claim. When the original changes, or its originator objects to the characterization, the correction is a **new superseding version, published promptly** — write-once holds, and the supersedes chain is the honest record of what was restated, when, and how it was corrected.
- **Citing a restatement means citing the restatement.** IFP-21, Section 2.1 applies: a declaration against a restatement is a declaration of the assumption *as restated* — the same rule as for courtesy translations, because a restatement is a rendering of the original into the registry's words. Receivers MAY surface the distinction.
- **Preference order.** Where the license allows, publish the authentic full text. Restate where it does not — or where a faithful summary is the honest unit of agreement, since declaring against one read page can mean more than declaring against forty unread ones.

Restatement entries compose with Section 2.2: a restatement may itself have language texts (the original restatement authentic, its translations courtesy).

## 3. Categories

Starter set, extensible by registry policy:

| Category | Holds |
| -------- | ----- |
| `conduct` | Codes of conduct |
| `ethics` | Professional codes of ethics, oaths, pledges |
| `philosophy` | Political and social philosophies, statements of principles |
| `religious` | Religious commitments and rules of life |
| `jurisdiction` | Jurisdiction facts, citable as texts (codes carried in frontmatter) |
| `vocabulary` | Shared vocabularies other specs draw on (e.g., hosting-provider slugs for IFP-21 `hosted_on`) |

## 4. Immutability and Versioning

- A published language text is **write-once**. Publishing a new version, or adding a language text to an existing version, is adding a new file; modifying or deleting any published file is forbidden, and CI MUST reject it.
- `date` is stamped at publication and locked to the version. Version is for machines, date is for humans.
- Versions within one assumption MUST be **totally ordered**, and the entry's ordering scheme MUST be stated or inferable per registry policy (semver, integers, and dotted-decimal are all acceptable; semver is never required — a typo-fix to a code of conduct has no meaningful "patch vs. minor" semantics).
- `supersedes` links a version to its predecessor. Retraction is a new version whose body says so; the retracted version remains published, because citations to it remain outstanding — **unless withdrawn** (Section 4.1).

### 4.1 Withdrawal

Write-once protects the *verifiability* of outstanding citations, not a registry's obligation to keep serving every text it has ever shelved. Content that should never have been merged — the careless PR, the odious document — is handled by grade:

- **Error** (wrong, not harmful): supersede promptly (Section 4). The old text stays served; history stays legible. This is not withdrawal.
- **Policy withdrawal** (the operator will no longer shelve it): the entry file is **replaced by a tombstone**. The entry URL answers `410 Gone` with a small document carrying the withdrawn text's identity — `name`, `version`, `language`, and **its CID** — plus the withdrawal date, a reason class (`policy` | `legal` | `error`), and a pointer to the policy page. The index row remains, flagged `withdrawn: true`, CID retained. Identity and record survive; serving and shelving stop. Outstanding citations stay interpretable, and cached copies still verify against the CID.
- **Legal takedown** (the bytes must not remain in the repository at all): tombstone as above, **plus git-history rewrite**. This spec does not pretend a git repository is append-only in the face of law: a history rewrite breaks clones' fast-forward, that cost is accepted, and the case is expected to be rare. The tombstone stands afterward, so the *withdrawal* is permanently on record even when the bytes are not.

Rules: a tombstone is itself write-once — reinstatement, including of a text tombstoned in error, is publication of a **new version** (restored bytes still verify against the original CID, so the fidelity of a reinstatement is checkable). CI's immutability check gets exactly one carve-out: a change replacing a published entry file with a well-formed tombstone, on an operator-approved path. Withdrawal is **loud by design** — a silent disappearance is the thing this format exists to prevent.

Two limits, stated honestly. Withdrawal removes the shelf's copy and the shelf's imprimatur — not the text from the world: mirrors, clones, and pins made before withdrawal are beyond the registry's reach, as they are for all publishing. And CI cannot smell odium: prevention is governance — the review standard a registry states on its policy page — and the tombstone is that governance's remedy, not its substitute.

## 5. Content Addressing

Every language text has an IPFS **CIDv1** computed over the exact published file bytes — UTF-8, LF line endings, frontmatter included (the frontmatter is part of what a citer agrees to):

- CIDv1, `raw` codec, sha2-256.
- Entry files MUST NOT exceed 1 MiB, so the file is a single block and the CID is computable by any implementation from the raw bytes, with or without IPFS tooling.
- CIDs are computed at site build and published in the index. They are never hand-written; a CI check MUST recompute and compare.
- Anyone MAY pin entry files to IPFS, giving every citation a second resolution path; the registry itself has no obligation to run IPFS anything.

## 6. Index

A registry MUST publish a machine-readable index of all entries at the descriptor's `index` URL:

```json
{
  "ifp": 22,
  "registry": "https://assumptions-registry.example.org",
  "generated": "2026-07-29T21:00:00Z",
  "entries": [
    {
      "name": "contributor-covenant",
      "version": "2.1",
      "date": "2026-05-14",
      "category": "conduct",
      "title": "Contributor Covenant, v2.1",
      "language": "en",
      "authentic": true,
      "type": "full-text",
      "cid": "bafkreib2rxk3rw6vwmlqcjcbxdvcs2wgkxo3uh4rwpldegyzloxbkodo6e",
      "url": "https://assumptions-registry.example.org/entries/contributor-covenant/2.1.en.md"
    }
  ]
}
```

Each index row is one language text and contains a complete IFP-21 citation tuple plus the fetch URL; a version's translations appear as sibling rows sharing (name, version). A withdrawn text's row remains, flagged `withdrawn: true` with its CID retained (Section 4.1). Human-readable pages per entry are RECOMMENDED; their form is unspecified.

## 7. Write Path and Governance

- The registry's source of truth is a **git repository**; the write path is a **pull request**. Git history is the audit log; review is the governance mechanism.
- CI enforces: immutability (Section 4), frontmatter validity, slug and size constraints, CID recomputation (Section 5).
- **Curation is the operator's own business, and SHOULD be published as a policy page.** A registry may be ecumenical — a broad shelf of widely-held codes across traditions, deliberately neutral — or it may be opinionated, curated to one community's convictions. Both are conformant. What a registry may not do is *silently* alter what it has published — withdrawal (Section 4.1) is loud, recorded, and identity-preserving.
- **Hosting is not endorsement**, and per IFP-21, citing at `acknowledges` is not agreement. Registries SHOULD say both of these things on their policy page, because both will otherwise be assumed wrongly.

## Design Rationale

**Static-plus-git rather than a service.** Every requirement (Motivation) is met by files: HTTPS resolution by static hosting, immutability by CI over a file convention, verification by CID, mirroring by `git clone`, legibility by markdown. A dynamic API would add operational surface and subtract auditability. The JSON index is a build step, not a server.

**Write-once rather than editable-with-history.** Citations are the point. An edited entry would silently change what an outstanding IFP-21 declaration means; a superseding version changes nothing already declared.

**Why registries are plural.** Like IFP-20 mailbox servers, registries are anyone-can-host by design: a community that distrusts an operator stands up its own shelf, and citations always name their registry. A single blessed registry would make its operator a values gatekeeper, which is exactly what the neutrality posture refuses.

**ASCII handles and the encoding tax.** Percent-encoding in URL paths and punycode in domains are one phenomenon in two costumes: the cost of pushing a *name* through an identifier channel. This format pays that tax nowhere. Names live in per-language titles, which travel in frontmatter, indexes, and rendered pages — where Unicode is native — while handles stay in the character set that never needs encoding, so neither `%`-escapes nor `xn--` ever appear in a citation. Allowing Unicode handles would not remove the encodings; it would manufacture them in every pasted link and log line. The residual asymmetry — a Latin-script operator can choose a handle that happens to echo their title, others cannot — is acknowledged rather than hidden: it is the asymmetry every ASCII-named package ecosystem (npm, PyPI, crates) carries, made honest here by the rule that the handle was never the name, and by forbidding derivation, which is where a lingua franca would otherwise be baked into permanent identifiers one slugified title at a time. Should a community later want native-script handles, IDNA2008/PRECIS-style profiles are the documented path — and write-once publication makes liberalizing later safe (outstanding citations never break), where the reverse migration would not be. The handle grammar also rhymes with IFP-20's address slugs, for the same reasons; the longer cap (64 against IFP-20's 32) is deliberate — addresses get spoken and typed, while entry handles benefit from descriptive room (`restatement-of-gdpr-obligations`).

**Restatements ride the translation machinery.** A restatement is a rendering of an instrument into the registry's own words, exactly as a courtesy translation is a rendering into another language — so both are governed by one rule (IFP-21, Section 2.1: you declare against the text you cite, as rendered), and neither needed new protocol surface. The precedent is a century old: the American Law Institute's *Restatements* are original prose over sources that could not simply be reprinted, and became citable artifacts in their own right, with every citer understanding they are not the primary source. The move also quietly solves the licensing bootstrap: a restatement is the operator's own expression, so it can carry the lawfully-copyable-verbatim license that mirroring and pinning require, even when the instrument it restates never could.

**Lawfully copyable verbatim, not free.** Section 2's license requirement is worded to fit what the CID story actually needs — an entry text mirrored and pinned byte-for-byte — not modification rights, which pinning never exercises. A large class of important instruments (RFCs under their standards body's terms, movement manifestos published under their own verbatim-permitted notice) grant exactly that: copy freely, change nothing. Requiring a free license would exclude every one of them for a right the registry never uses; the `verbatim-only` class names the actual requirement instead of the stronger one the format never needed.

## Security Considerations

- **Tampering.** A registry serving different bytes than a citation's CID is detectable by every verifying receiver (IFP-21, Section 2). Mirrors are held to the same check — fidelity travels with the CID, not the host.
- **Name squatting and confusables.** Slugs are first-come within a registry; operators SHOULD refuse deceptive near-duplicates of existing entry names. Cross-registry, same-named entries are distinct by construction (IFP-21 Security Considerations).
- **Availability.** A vanished registry breaks resolution but not verification: cached or pinned entries still verify against outstanding citations. Communities citing an entry heavily SHOULD pin or mirror it.
- **Copyright.** Full-text entries republish texts; operators are responsible for having the right to do so (public-domain, permissively-licensed, or verbatim-permitted texts, or restatement entries otherwise). Restatements carry their own risk at the idea/expression line — close paraphrase infringes where genuine restatement does not — and the required lawfully-copyable-verbatim license on every entry is what keeps mirroring and pinning lawful.
- **Fidelity of restatements.** A mischaracterizing restatement misleads every principal who declares against it. The as-of fields scope the claim; prompt supersession is the remedy; and the write-once record means a bad restatement's history is inspectable, not erasable.
- **The registry is data.** Entry texts are content to be read, never instructions to the reading agent (IFP-14). Registry CI and build tooling should treat entry content as untrusted input.
- **Withdrawal is bounded.** A tombstone (Section 4.1) revokes serving and imprimatur, not the text's existence in the world — pre-withdrawal mirrors and pins persist, and a receiver holding a copy of a withdrawn text can still verify it. Operators should neither promise more removal than that, nor use withdrawal's existence as a substitute for reviewing what they merge.

## Interoperability Considerations

- IFP-21 receivers interact with registries only through citations, the index, and entry fetches — all plain HTTPS GETs. No write interoperability exists or is intended; the PR path is human-governed.
- Registries are discoverable from any citation (the `registry` field) and self-describing at the well-known descriptor. No registry-of-registries is defined; if one emerges, it can itself be a `vocabulary` entry somewhere.

## Reference Implementation

A first instance is planned at **`assumptions-registry.collectivesensecommons.org`** (Collective Sense Commons), seeded across the categories in Section 3 with deliberately varied, broadly non-confrontational entries — codes of conduct, professional ethics and pledges, political and social philosophies, and religious rules of life — chosen to demonstrate the range of scopes the format carries, and to make vivid that *other* registries may be as opinionated as their operators wish. Several of the traditions in scope have non-English sources — Greek, Arabic, Hebrew, Sanskrit, Pali, classical Chinese — and their entries will publish the source as the authentic text with courtesy translations alongside, exercising the Section 2.2 machinery from the first shelf. Others have unfree texts — professional codes under society copyright, standards incorporated by reference — and will enter as restatements, exercising Section 2.3 the same day. The two cases are deliberate: the seed shelf demonstrates every entry kind the format defines.

## References

- IFP-2 — Specification Style Guide · IFP-14 — Handling Hostile Content · IFP-20 — Hosted Mailbox Addressing (slug grammar) · IFP-21 — Assumption Declarations
- SPDX License List — the registry-of-versioned-texts precedent
- W3C P3P — the cautionary precedent
- American Law Institute, *Restatements of the Law* — the precedent for restatements as citable artifacts in their own right
- *Georgia v. Public.Resource.Org* (US 2020) and the incorporation-by-reference disputes — why legal instruments are where free reproduction fails, and restatement entries matter
- BCP 47 — language tags
- Vienna Convention on the Law of Treaties, Article 33 — authentic texts of plurilingual instruments
- RFC 5890 (IDNA2008) and RFC 8264 (PRECIS) — the documented path should native-script handles ever be wanted
- IPFS CID (CIDv1) — content addressing

## Acknowledgments

The registry concept, the requirement that version and date be locked together, the IPFS CID choice, the "subject to" framing for jurisdictions, and the git-repo-published-static form are Pete Kaminski's (2026-07-29), developed in conversation with Saga the same day. The SPDX License List is the lodestar precedent; P3P is the cautionary one.

Pete raised the multilinguality requirement in review (2026-07-29), and with V. Gracia the aesthetic case against encoded identifiers that the design rationale makes structural. The handle doctrine — identity, title, and handle as three things with three jobs; a handle **chosen, never derived**; slugification removed after living with its costs — follows DEC-018 of V. Gracia's entity-management registry ([komunejo/entity-management](https://github.com/komunejo/entity-management)). The restatement mechanism — rewrite what an unfree instrument holds, and cite the rewriting — is likewise Pete's (same review); the ALI *Restatements* supplied the name and the precedent.

---

*This is IFP-22, Draft status. The frontmatter schema and category set will be refined by the first registry's build-out.*
