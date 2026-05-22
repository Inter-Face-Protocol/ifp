# IFP Drafts

Working drafts of proposed additions to the IFP series, kept under `drafts/` until they have been through editorial review and assigned IFP numbers. At that point they graduate up to the repository root and join the numbered series (`ifp-1-*.md` … `ifp-12-*.md`).

## Drafts in this folder

- **[ifp-git-transport-profile.md](ifp-git-transport-profile.md)** — Profile-class IFP defining how a git repository serves as an IFP message transport. Originated from running an IFP-3 conversation between two agents through a shared private repo on 2026-05-21.
- **[ifp-shared-folder-transport-profile.md](ifp-shared-folder-transport-profile.md)** — Profile-class IFP defining how a shared cloud folder (Dropbox, Google Drive, iCloud Drive, OneDrive, Syncthing) serves as an IFP transport. Same folder layout convention as the git-transport profile, but tuned for non-technical users; addresses conflict copies, provider trust, and the fact that the audit-log property requires explicit out-of-band backup.
- **[ifp-conformance-assertion.md](ifp-conformance-assertion.md)** — Core-class IFP defining the HELO-shaped greeting-time mechanism by which agents declare which IFPs they apply, and how receivers record and use those declarations. General-purpose primitive that other IFPs depend on.
- **[ifp-cross-family-negotiation.md](ifp-cross-family-negotiation.md)** — Informational-class IFP noting that the in-family conformance-assertion pattern is the local case of a broader expected pattern across protocol families (IFP, A2A, MCP-derived, ANP, Swamp, others). Records the direction without specifying a mechanism.
- **[ifp-handling-hostile-content.md](ifp-handling-hostile-content.md)** — Core-class IFP defining reader discipline for hostile or injection-shaped message bodies. Ports the harness-discipline principles from Swamp § 15 to IFP's pairwise model and adapts the broadcast blacklist mechanism into a pairwise close-and-signal response. Depends on `ifp-conformance-assertion` for the trust-tracking layer.

## How the drafts relate

```
ifp-git-transport-profile             ← independent (Profile class)
ifp-shared-folder-transport-profile   ← independent (Profile class)
                                        peer to git-transport; same folder layout

ifp-conformance-assertion             ← independent primitive (Core class)
        ▲
        │ depends on
        │
ifp-cross-family-negotiation             (Informational, anticipates a broader pattern)
ifp-handling-hostile-content             (Core, uses the primitive for trust-tracking)
```

## Status

Drafts. Not yet IFPs. Numbers will be assigned by the IFP editorial process at submission.
