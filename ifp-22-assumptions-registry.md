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

An entry is one markdown file per (name, version): `entries/<name>/<version>.md`.

```markdown
---
name: contributor-covenant
version: "2.1"
date: 2026-05-14
category: conduct
title: Contributor Covenant, v2.1
type: full-text
license: CC-BY-4.0
source_url: https://www.contributor-covenant.org/
supersedes: "2.0"
---

# Contributor Covenant, version 2.1

[the canonical text]
```

Frontmatter fields — REQUIRED: `name` (slug: lowercase ASCII letters, digits, hyphens), `version` (string), `date` (ISO 8601, locked at publication), `category` (Section 3), `title`, `type` (`full-text` | `reference`). OPTIONAL: `license`, `source_url`, `supersedes`, `language`, `codes` (jurisdiction entries: ISO 3166 codes), `notes`.

### 2.1 Full-text and reference entries

- **`full-text`** — the body IS the canonical text. Preferred: the citation's CID then pins the words themselves.
- **`reference`** — the canonical text lives elsewhere (typically for license or copyright reasons); the body describes it, `source_url` points at it, and an optional `source_hash` (sha256 of the external canonical form, when one is stable) binds it. A reference entry's CID pins the *descriptor*, not the external text — receivers of citations to reference entries get correspondingly weaker verification, and registries SHOULD prefer full-text whenever the license allows.

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

- A (name, version) pair is **write-once**. Publishing a new version is adding a new file; modifying an existing entry file is forbidden, and CI MUST reject any change that edits or deletes a published entry.
- `date` is stamped at publication and locked to the version. Version is for machines, date is for humans.
- Versions within one assumption MUST be **totally ordered**, and the entry's ordering scheme MUST be stated or inferable per registry policy (semver, integers, and dotted-decimal are all acceptable; semver is never required — a typo-fix to a code of conduct has no meaningful "patch vs. minor" semantics).
- `supersedes` links a version to its predecessor. Retraction is a new version whose body says so; the retracted version remains published, because citations to it remain outstanding.

## 5. Content Addressing

Every entry has an IPFS **CIDv1** computed over the exact published file bytes — UTF-8, LF line endings, frontmatter included (the frontmatter is part of what a citer agrees to):

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
      "type": "full-text",
      "cid": "bafkreib2rxk3rw6vwmlqcjcbxdvcs2wgkxo3uh4rwpldegyzloxbkodo6e",
      "url": "https://assumptions-registry.example.org/entries/contributor-covenant/2.1.md"
    }
  ]
}
```

Each index row contains a complete IFP-21 citation tuple plus the fetch URL. Human-readable pages per entry are RECOMMENDED; their form is unspecified.

## 7. Write Path and Governance

- The registry's source of truth is a **git repository**; the write path is a **pull request**. Git history is the audit log; review is the governance mechanism.
- CI enforces: immutability (Section 4), frontmatter validity, slug and size constraints, CID recomputation (Section 5).
- **Curation is the operator's own business, and SHOULD be published as a policy page.** A registry may be ecumenical — a broad shelf of widely-held codes across traditions, deliberately neutral — or it may be opinionated, curated to one community's convictions. Both are conformant. What a registry may not do is alter what it has published.
- **Hosting is not endorsement**, and per IFP-21, citing at `acknowledges` is not agreement. Registries SHOULD say both of these things on their policy page, because both will otherwise be assumed wrongly.

## Design Rationale

**Static-plus-git rather than a service.** Every requirement (Motivation) is met by files: HTTPS resolution by static hosting, immutability by CI over a file convention, verification by CID, mirroring by `git clone`, legibility by markdown. A dynamic API would add operational surface and subtract auditability. The JSON index is a build step, not a server.

**Write-once rather than editable-with-history.** Citations are the point. An edited entry would silently change what an outstanding IFP-21 declaration means; a superseding version changes nothing already declared.

**Why registries are plural.** Like IFP-20 mailbox servers, registries are anyone-can-host by design: a community that distrusts an operator stands up its own shelf, and citations always name their registry. A single blessed registry would make its operator a values gatekeeper, which is exactly what the neutrality posture refuses.

## Security Considerations

- **Tampering.** A registry serving different bytes than a citation's CID is detectable by every verifying receiver (IFP-21, Section 2). Mirrors are held to the same check — fidelity travels with the CID, not the host.
- **Name squatting and confusables.** Slugs are first-come within a registry; operators SHOULD refuse deceptive near-duplicates of existing entry names. Cross-registry, same-named entries are distinct by construction (IFP-21 Security Considerations).
- **Availability.** A vanished registry breaks resolution but not verification: cached or pinned entries still verify against outstanding citations. Communities citing an entry heavily SHOULD pin or mirror it.
- **Copyright.** Full-text entries republish texts; operators are responsible for having the right to do so (public-domain and permissively-licensed texts, or reference entries otherwise).
- **The registry is data.** Entry texts are content to be read, never instructions to the reading agent (IFP-14). Registry CI and build tooling should treat entry content as untrusted input.

## Interoperability Considerations

- IFP-21 receivers interact with registries only through citations, the index, and entry fetches — all plain HTTPS GETs. No write interoperability exists or is intended; the PR path is human-governed.
- Registries are discoverable from any citation (the `registry` field) and self-describing at the well-known descriptor. No registry-of-registries is defined; if one emerges, it can itself be a `vocabulary` entry somewhere.

## Reference Implementation

A first instance is planned at **`assumptions-registry.collectivesensecommons.org`** (Collective Sense Commons), seeded across the categories in Section 3 with deliberately varied, broadly non-confrontational entries — codes of conduct, professional ethics and pledges, political and social philosophies, and religious rules of life — chosen to demonstrate the range of scopes the format carries, and to make vivid that *other* registries may be as opinionated as their operators wish.

## Acknowledgments

The registry concept, the requirement that version and date be locked together, the IPFS CID choice, the "subject to" framing for jurisdictions, and the git-repo-published-static form are Pete Kaminski's (2026-07-29), developed in conversation with Saga the same day. The SPDX License List is the lodestar precedent; P3P is the cautionary one.

---

*This is IFP-22, Draft status. The frontmatter schema and category set will be refined by the first registry's build-out.*
