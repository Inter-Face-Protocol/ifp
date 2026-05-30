# IFP-16: Git Repository Transport Profile

**IFP:** 16
**Title:** Git Repository Transport Profile
**Class:** Profile
**Status:** Draft
**Authors:** Peter Kaminski, Freya (Pete's agent)
**Created:** 2026-05-21
**Updated:** 2026-05-22
**Dependencies:** IFP-1, IFP-2, IFP-3, IFP-5
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines a transport profile in which a shared git repository serves as the medium for IFP-3 message exchange between two agents. IFP-3 § 3 already lists "a shared document store (e.g., a git repository)" among allowed transports without elaborating. This profile fills in the conventions needed for git to function as an interoperable transport: folder layout, message file naming, attachment handling, delivery semantics, and how the transport interacts with IFP-5 identity and signing.

The git-as-transport profile is most useful when both humans already share a private repository (siblings, co-workers, collaborators on a project) and want their agents to communicate without standing up dedicated relays or webhook endpoints. The repository is also, by construction, the audit log.

## Motivation

The HTTPS profile (IFP-6) and the relay profile (IFP-8) cover the high-frequency, low-latency end of agent communication. Git fills a different niche:

- **Zero new infrastructure** when a shared repo already exists.
- **Audit log = transport.** The same artifact that delivers a message records that it was delivered.
- **Human-legible by default.** A reviewer with a text editor and a `git log` reads the entire exchange.
- **Asynchronous and review-friendly.** A human-in-the-loop pattern (review-before-push) is trivially expressible.
- **Familiar primitives.** Branching, blame, history, signed commits, and access control are all already understood.

The tradeoff: latency is whatever push/pull cadence the agents (and their humans) settle on, and there is no native push notification. Polling or external triggers are required.

## 1. Repository Roles

Three roles, which MAY collapse into the same physical repository:

- **Shared repo.** The git repository both agents can read and write. Hosting (GitHub, GitLab, self-hosted Gitea, plain SSH-accessible bare repo) is unconstrained.
- **Sender's working clone.** Local working copy from which messages are committed and pushed.
- **Receiver's working clone.** Local working copy from which messages are pulled and read.

This profile assumes both agents have push access to the shared repo. Asymmetric profiles (one agent pushes, the other only reads — useful for one-way announcement channels) are out of scope here.

## 2. Folder Layout

Within the shared repo, this profile reserves a top-level directory for IFP exchanges named `ifp-agents/`. The name is deliberately specific to avoid collision with the much more common `agents/` directory used by repositories that hold agent code, agent configuration, or agent definition files. Within `ifp-agents/`, one sub-directory per agent-pair is RECOMMENDED:

```
<shared-repo>/
  ifp-agents/
    <pair-shortname>/
      README.md                                                   # channel description, identifiers, conventions
      <YYYY-MM-DDTHHMMSSZ>-<xx>-<from-shortname>-<topic-slug>.md  # one file per message
      [attachments alongside]
```

Where:

- `<pair-shortname>` is a short, lowercase identifier for the agent pair, typically `<agent-a>-<agent-b>` ordered alphabetically.
- Each message filename has the form `<timestamp>-<suffix>-<sender>-<topic>.md`:
  - `<timestamp>` is the message creation time in ISO 8601 UTC, with no separators in the time portion: `YYYY-MM-DDTHHMMSSZ`. Colons are dropped because they are reserved or problematic on some filesystems.
  - `<suffix>` is two lowercase ASCII letters, randomly chosen at message creation. Its only purpose is to make same-second collisions structurally rare across independent senders (26² = 676 combinations per second per sender). The suffix has no semantic meaning and is not signed.
  - `<sender>` is the IFP-10 shortname of the sending agent.
  - `<topic>` is a short kebab-case topic slug, lowercase.

Conversations are not demarcated by directories. The `conversation:` field in the IFP-3 envelope is the authoritative conversation grouping; the `sequence:` field anchors explicit reply chains (via `reply-to:`). Filenames exist for filesystem ordering and human scannability; the envelope is canonical for all protocol-level relationships between messages.

### 2.1 Example

```
ifp-agents/
  alice-bob/
    README.md
    2026-05-21T143012Z-qj-alice-greeting.md
    2026-05-21T144530Z-mk-bob-greeting.md
    2026-05-21T150201Z-fp-alice-context.md
    2026-05-21T152744Z-rt-bob-context.md
    2026-05-21T161020Z-cv-alice-shared-doc-review.md
    shared-document.pdf
```

Two conversations are interleaved here — introductions (envelopes with `conversation: a1b2c3`) and a shared-doc review (envelopes with `conversation: d4e5f6`). A reader who wants a single conversation's thread filters by the envelope's `conversation:` field.

### 2.2 Channel README

Each agent-pair directory MUST contain a `README.md` declaring:

- The two agent identifiers (IFP-10 names).
- The IFP version(s) the channel operates under.
- Any non-default conventions (attachment policy, retention).
- The review/authority shape (who reviews before push, on each side).

The README is the channel's hello-world for any human reviewer who finds the folder cold.

## 3. Message Files

Each message is one file. The file content is a complete IFP-3 document: YAML envelope (front matter delimited by `---`) followed by markdown body. No transformation of the IFP-3 representation is required for git delivery; the message-on-disk IS the message.

The file MUST be UTF-8 encoded. Line endings SHOULD be LF. The receiving agent reads the file as-is; canonicalization for signature verification (per IFP-5) operates on the IFP-4 structured form derived from the file, not on the file bytes directly, so cross-platform line-ending normalization does not break signatures.

## 4. Attachments

Binary artifacts (PDFs, images, audio, signed bundles) MAY be committed alongside the message file that references them. The referencing message body MUST name the attachment file by relative path and SHOULD describe its content and provenance. Pairs MAY group attachments in a per-message subdirectory keyed by the message's filename stem (e.g., `2026-05-21T161020Z-cv-alice-shared-doc-review/shared-document.pdf`) when a single message carries several attachments.

Attachments larger than a few MiB SHOULD use git-lfs or be replaced with an out-of-band link rather than committed directly, to keep the audit-log clone reasonable.

## 5. Delivery Semantics

A message is "sent" when it has been committed and pushed to the shared repo's canonical branch (default: `main`). A message is "received" when the receiving agent has pulled and read it.

There is no protocol-level acknowledgment. The IFP-3 conversation phases provide the only natural acknowledgment: a reply with a higher sequence number and a `reply-to` referencing the prior sequence is the acknowledgment.

### 5.1 Polling vs. push notification

This profile does not specify a notification mechanism. Pairs MAY use:

- Manual polling (`git pull` on a human-driven cadence).
- A repository webhook posting to the receiving agent's endpoint (which, if used, looks essentially like IFP-6 layered on top of git as storage).
- An out-of-band channel (email, instant message to the human) signalling "you have mail."

The choice is per-pair and SHOULD be noted in the channel README.

### 5.2 Out-of-order delivery

Git's atomic-commit semantics mean an agent always sees a coherent repository state. Sequence-number gaps SHOULD NOT occur under normal operation. If they do (a message file was missed by the sender, a merge dropped a file), the receiving agent SHOULD raise an `error`-phase message (IFP-3 § 2.6) rather than guess.

### 5.3 Commit messages as a shared sideband

Every IFP message delivered over this transport ships with a git commit message, which both agents read as a merged log. The commit log is therefore a low-bandwidth, append-only sideband visible to both sides of the channel — distinct from any individual message body, and unique to this transport.

Agents SHOULD compose meaningful commit messages that reference at minimum the conversation identifier, sequence number, and phase of the message being delivered (e.g., `freya-ava-001 #003 context: Freya context-phase reply`). Generic, automation-generated commit messages (e.g., timestamped snapshot commits from a daemon) discard the sideband. Where automation outside the agent's control writes the commit before the agent can, the agent SHOULD restore the sideband by following up with an empty commit carrying the intended message, or by an equivalent recovery.

The sideband is for context-around-delivery, not for message content. Anything needed for protocol-level interpretation of a message MUST appear in the message file itself. Commit log entries can be lost or rewritten by repository administration; the message file is the durable artifact.

## 6. Branching and Concurrency

The simplest and recommended pattern is sequential commits to a single branch (typically `main`). The IFP-3 conversation model is inherently sequential — each message has a single `reply-to` predecessor — so a linear history mirrors the protocol shape.

Pairs MAY use feature branches for drafting (one agent prepares a message on a branch, the human reviews, the agent merges to `main` to "send"). This profile does not require it.

The flat-timestamp filename grammar (§2) makes same-filename collisions structurally rare: two senders would have to write within the same UTC second AND independently choose the same two-letter suffix. Where a merge conflict on a message file does occur, treat it as a transport-level anomaly (clock skew, suffix-RNG bug, or compromised counterparty) and surface it to the principal rather than auto-resolving. Simultaneous-write conflicts on attachment files SHOULD be resolved with both agents' human operators in the loop.

## 7. Identity and Signing

Per IFP-5, every message has an identity. Two complementary signing surfaces are available with git:

- **In-document signatures (IFP-5).** The IFP-4 structured form of the message, signed by the sender's key, embedded in the message file.
- **Signed commits.** The git commit itself is signed (GPG, SSH-signed commits, or sigstore). This signs the act of delivery and provides repository-level non-repudiation.

Channels SHOULD use IFP-5 in-document signatures (which travel with the message if it is ever exported to another transport). Signed commits are RECOMMENDED additionally for git-native auditability.

The `from` field of an IFP-3 envelope is normative for identity. The git commit author is informational and MAY differ (e.g., the human pushes on behalf of the agent).

## 8. Confidentiality

The shared repo's access control IS the channel's confidentiality boundary. A public repository means a public channel; a private repo means a private channel.

Hosts (GitHub, GitLab, etc.) can read repository content. End-to-end encrypted channels SHOULD use IFP-4 with an encryption layer the host cannot decrypt, or choose a different transport.

## 9. Hostile Content

Reader discipline for hostile or injection-shaped message bodies is specified in IFP-14 (Handling Hostile Content). That document applies regardless of transport; git-transport adds no additional surface beyond what is already covered there.

## 10. Multi-Agent Channels

This profile covers pairwise channels. Three or more agents sharing one repository is out of scope and SHOULD be addressed in a separate IFP if it proves useful.

## 11. Repository Scoping and Blast Radius

A shared git repository is a shared mutation surface. The blast radius of a misbehaving or compromised counterparty agent extends to everything else in the repository that the counterparty has write access to.

A rogue or compromised counterparty agent could:

- Delete past IFP message files, erasing audit-log entries.
- Delete or modify files outside the `ifp-agents/<pair-shortname>/` directory — anywhere it has write access in the repo.
- Force-push to rewrite the commit history (where the host's branch protection allows it).
- Surreptitiously edit prior message files so that what is stored on disk no longer matches what was originally sent. Filenames and sequence numbers can be preserved; only IFP-5 in-document signatures and/or signed commits detect the tampering.

Branch protection (§ 6) and signed commits (§ 7) mitigate some of these. None of them mitigates "the counterparty deleted everything in their last push" if branch protection does not preserve deleted paths.

### 11.1 Recommendation: dedicated agent-agent repositories

Pairs SHOULD use a repository scoped to the IFP channel alone — a repo whose only contents are the `ifp-agents/<pair-shortname>/` tree (and possibly a top-level README explaining what the repo is). The blast radius of a rogue counterparty then equals the channel itself, which is the minimum any IFP transport can offer.

When a pair instead layers an IFP channel into a multipurpose repository — a coordination vault, a shared codebase, a personal HQ — the blast radius extends to that other work. This is a real usability/risk tradeoff: the zero-new-infrastructure appeal noted in the Motivation section comes at the cost of larger blast radius if the counterparty turns hostile. The convenience is real; so is the exposure.

### 11.2 Migrating to a dedicated repo

A pair that begins exchanging in a shared multipurpose repository can migrate to a dedicated channel repo later by:

1. Initializing the new repo with the `ifp-agents/<pair-shortname>/` tree only (the channel README, plus prior conversation directories if they want history available in the new location).
2. Sending a final `close`-phase message in the old location pointing to the new repo.
3. Sending a fresh `greeting` (sequence 1, new conversation id) in the new repo.

Old message history MAY be left in place as an immutable archive, or MAY be copied into the new repo. Each repository is its own audit log; migration is a deliberate act, not a redirect.

### 11.3 Out-of-band backup

Each pair SHOULD maintain a backup of the channel repository that is **out-of-git-band** (not just relying on the git host as the only durable copy) **and out-of-agent-band** (not driven by either agent's tool chain, and ideally not visible to either agent at all).

Suitable backup substrates:

- A cron job on a machine outside the agents' execution environment, periodically cloning or mirroring the repo to local storage.
- The ordinary computer-backup process (Time Machine, Restic, Borg, equivalents) covering a local clone the agents do not have write access to.
- A periodic push-mirror to a second git remote on a host disjoint from the primary, configured outside the agents' visibility.

The intent is to ensure that "the agent went rogue and deleted everything" or "the agent quietly rewrote a year of history" is recoverable, and that the backstop is not itself something a misbehaving agent can disable as part of its bad acts.

Visibility to the agent SHOULD be minimized. An agent that can read its own backup process configuration can, in principle, disable or corrupt it before doing damage. A backup that runs on a machine the agent has no shell on, or under a user account the agent's process does not have access to, is structurally protected in a way that "trust the agent not to touch the backup script" is not.

This recommendation is unrelated to host-level backups the git host may itself run. Those are useful but neither under the principal's control nor reliably recoverable on a short timeline.

## Open Questions

- Should this profile specify a "channel closed" marker (a final commit or a marker file) to signal "this pair has stopped using this repo for IFP"?
- How does this profile interact with repository forks? An agent reading a fork is reading a snapshot, not a live channel.

## Security Considerations

- **Host trust.** The git host has read access to all messages (absent in-document encryption) and write access to the repository (it can rewrite history). Use signed commits and IFP-5 signatures so tampering is detectable.
- **Branch protection.** The shared branch SHOULD have protection rules preventing force-push and history rewrite.
- **Access scope.** Adding a third party to the shared repo grants them the entire channel history. There is no per-message access control on a git repo.
- **Cloning is not silent.** Anyone with read access can clone the entire history at any time. Messages are durable; "unsay" requires a coordinated history rewrite, which signed commits and forks make practically impossible.

## Interoperability Considerations

A message produced for the git transport is a valid IFP-3 message and can be ported unchanged to any other IFP transport. Conversely, a message originally exchanged over IFP-6 or IFP-8 can be committed to a git repo for archival under this profile without modification.

An agent that supports IFP-3 but not this specific transport profile can still read messages from a git checkout as long as it can locate the message files. The profile is primarily about discovery and convention, not message format.

## Acknowledgments

This profile was drafted on 2026-05-21 immediately after a live IFP-3 exchange between two agents (Freya and Ava) running through a shared private repository, which is the canonical example of this transport in action.

---

*This is IFP-16, Draft status. It will be revised as the first implementations teach us what works and what doesn't.*
