# IFP-17: Shared Folder Transport Profile

**IFP:** 17
**Title:** Shared Folder Transport Profile
**Class:** Profile
**Status:** Draft
**Authors:** Peter Kaminski, Freya (Pete's agent)
**Created:** 2026-05-21
**Updated:** 2026-05-22
**Dependencies:** IFP-1, IFP-2, IFP-3, IFP-5
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines a transport profile in which a shared cloud folder — Dropbox, Google Drive, iCloud Drive, OneDrive, Syncthing, or any equivalent file-sync service — serves as the medium for IFP-3 message exchange between two agents. IFP-3 § 3 lists "a shared document store" among allowed transports; this profile fills in the conventions needed for a shared folder to function as an interoperable transport: folder layout, message file naming, attachment handling, delivery detection, conflict handling, and how the transport interacts with IFP-5 identity and signing.

The shared-folder transport is intended for pairs whose humans are not technical users. The user-facing surface is a folder in Finder, the Files app, or the equivalent. Both agents read and write files; the cloud provider syncs. No version control, no command line, no new accounts beyond the shared-folder service they already use.

## Motivation

The git-transport profile (peer to this one) is the obvious choice for technical users who already share repositories. Most users do not. They share folders. They drop files into Dropbox, attach things in Google Drive, and accept share invitations as a normal part of their lives.

A shared-folder transport gives those users an IFP channel with effectively zero technical setup beyond what they already do. The user can open the folder in their normal file browser and see the conversation directly.

The tradeoffs versus git-transport:

- No native version history (provider-dependent).
- No commit-message sideband.
- Real deletes are real (the audit-log property must come from out-of-band backup, not from the transport itself).
- Conflict resolution is provider-specific and sometimes lossy.

This profile addresses those tradeoffs explicitly.

## 1. Provider Choice

Suitable providers share these properties:

- Sync a folder hierarchy between machines belonging to (at least) two distinct humans.
- Support share-with-another-user with read+write permission.
- Notify the operating system on file changes (so agents can watch rather than poll).

Providers vary in three properties this profile cares about:

| Property                    | Examples that have it                          | Examples that don't reliably           |
| --------------------------- | ---------------------------------------------- | --------------------------------------- |
| Server-side version history | Dropbox, Google Drive, OneDrive                | iCloud Drive (limited), Syncthing      |
| Conflict-copy file creation | Dropbox, Syncthing                             | iCloud Drive (silently picks a winner) |
| File-system notification    | All listed providers via OS-level facilities   | —                                       |

Pairs SHOULD prefer a provider with server-side version history. Pairs MUST NOT rely on the provider's version history as the channel's audit log — see § 11.

## 2. Folder Roles

Three roles, which MAY collapse:

- **Shared folder.** The cloud-synced folder both humans (and therefore both agents) have read+write access to.
- **Sender's local mirror.** The synced copy on the sending agent's machine.
- **Receiver's local mirror.** The synced copy on the receiving agent's machine.

This profile assumes both agents have read+write access. Read-only-on-one-side channels (one-way announcement) are out of scope.

## 3. Folder Layout

Within the shared folder, this profile follows the same layout convention as the git-transport profile (IFP-16 §2), so message format and folder shape are portable:

```
<shared-folder>/
  README.md                                                   # what this folder is, channel description
  <YYYY-MM-DDTHHMMSSZ>-<xx>-<from-shortname>-<topic-slug>.md  # one file per message
  [attachments alongside]
```

The filename grammar is defined canonically in IFP-16 §2. Conversations are not demarcated by directories; the `conversation:` field in the IFP-3 envelope is the authoritative conversation grouping.

If the shared folder hosts multiple IFP channels (the two humans share a folder for several agent pairs), each pair SHOULD use its own subdirectory under `ifp-agents/`. The `ifp-agents/` name is deliberately specific to avoid collision with other uses of `agents/` in repositories or shared folders:

```
<shared-folder>/
  ifp-agents/
    <pair-shortname>/
      README.md
      <YYYY-MM-DDTHHMMSSZ>-<xx>-<from-shortname>-<topic-slug>.md
      ...
```

A shared folder dedicated to a single channel MAY omit the `ifp-agents/<pair-shortname>/` layer and use the layout directly.

### 3.1 README

The folder MUST contain a `README.md` at the channel root declaring:

- The two agent identifiers (IFP-10 names).
- The IFP version(s) the channel operates under.
- Provider in use (Dropbox, etc.), so that recovery and conflict-handling expectations are explicit.
- Any non-default conventions.
- The review/authority shape (who reviews before send, on each side).

## 4. Message Files

Each message is one file: a complete IFP-3 document, YAML envelope + markdown body, UTF-8 encoded. The on-disk file IS the message. This profile adds no transformation, framing, or header layer over IFP-3.

Line endings SHOULD be LF. Cross-platform sync providers preserve file contents byte-for-byte for files that are not opened by their native editors; agents SHOULD NOT open message files with applications that may rewrite them (e.g., Word, some PDF tools).

## 5. Attachments

Binary artifacts MAY be placed alongside the message file that references them, or grouped in a per-message subdirectory keyed by the message's filename stem when a single message carries several attachments. The referencing message body MUST name the attachment by relative path.

Providers impose size limits and may sync large files slowly. Attachments larger than a few MiB SHOULD be replaced with an out-of-band link (a download URL the receiver can fetch separately).

Some providers handle a flood of small files poorly. Pairs with high-frequency channels SHOULD batch or rate-limit message commits, or migrate to a different transport.

## 6. Delivery Semantics

A message is "sent" when its file appears in the sender's local mirror of the shared folder and has been confirmed by the provider as uploaded (provider-specific UI signal: "Synced," a checkmark, etc.). A message is "received" when the file has appeared in the receiver's local mirror.

Sender's machine being offline at the time of write does not invalidate the send; the provider syncs when the machine reconnects.

There is no protocol-level acknowledgment. Reply messages with increasing sequence numbers are the only acknowledgment.

### 6.1 Detection

Receiving agents MAY detect new messages by:

- Subscribing to file-system change events (preferred — zero polling, near-instant).
- Polling the conversation directory on a fixed cadence.
- Receiving a notification from the cloud provider's notification system (if available).

The method SHOULD be noted in the channel README.

### 6.2 Out-of-order delivery and partial sync

Cloud sync is eventually consistent. A receiver MAY momentarily see a partial conversation directory (some files synced, others still uploading on the sender's side). Receiving agents SHOULD wait for sync stability — typically a few seconds without further changes in the directory — before treating a state as "the message" rather than "an in-progress sync."

If sequence-number gaps persist after sync stability, the receiving agent SHOULD raise an `error`-phase message (IFP-3 § 2.6).

### 6.3 Conflict copies

When both agents write to the same file path or attempt to create files with the same name simultaneously, providers respond differently:

- **Dropbox** creates a file named `…(<user>'s conflicted copy <date>).md` alongside the original.
- **Syncthing** creates `*.sync-conflict-<timestamp>-<id>.md`.
- **Google Drive** may create a second file with the same name but a different file-id (visible only via the API).
- **iCloud Drive** may silently pick a winner with no conflict file.

The flat-timestamp filename grammar (IFP-16 §2) makes same-filename collisions structurally rare: two senders would have to write within the same UTC second AND independently choose the same two-letter suffix. Where a conflict file does appear, treat it as a transport-level anomaly (clock skew, suffix-RNG bug, or compromised counterparty) rather than ordinary protocol behavior.

When a conflict file appears, the receiving agent MUST surface it to the principal rather than silently merging or deleting. Conflict resolution is a human-in-the-loop activity.

## 7. Identity and Signing

Per IFP-5, every message has an identity. This profile has no transport-native signature surface (unlike git-transport's signed commits). The IFP-5 in-document signature is therefore the only signing surface and SHOULD be present on every message.

A receiving agent MUST verify the IFP-5 signature against the IFP-4 structured form of the message. The on-disk file's path and name are not authoritative; the envelope is.

## 8. Confidentiality

The cloud provider has read access to all files in the shared folder. The provider is a participant in any non-encrypted IFP channel.

End-to-end-encrypted channels SHOULD use IFP-4 with an encryption layer the provider cannot decrypt, or choose a different transport.

For pairs comfortable with their provider's confidentiality posture, the standard share-with-one-other-user permission MUST be configured before any IFP message is written; messages written before sharing is in place are not delivered.

## 9. Hostile Content

Reader discipline for hostile or injection-shaped message bodies is specified in IFP-14 (Handling Hostile Content). That document applies regardless of transport.

## 10. Folder Scoping and Blast Radius

A shared folder is a shared mutation surface. The blast radius of a misbehaving counterparty extends to everything in the folder both agents have write access to.

A rogue or compromised counterparty agent could:

- Delete past IFP message files.
- Delete or modify any file in the shared folder (including files outside the IFP channel's subdirectory, if the folder hosts other content).
- Overwrite a prior message file with new content, breaking the audit-log property unless IFP-5 in-document signatures are verified against an external copy.

Unlike git-transport, this profile has no native immutable history. The provider's version history (where present) helps but does not substitute for an out-of-band backup; see § 11.

### 10.1 Recommendation: dedicated channel folder

Pairs SHOULD use a folder scoped to the IFP channel alone — a top-level shared folder whose contents are the channel layout from § 3 and nothing else. The blast radius then equals the channel itself.

When a pair instead places the channel inside a folder that holds other shared work (a project folder, a household folder), the blast radius extends to that other work. Convenient; not safe.

### 10.2 Migrating to a dedicated folder

A pair that begins exchanging in a multipurpose shared folder can migrate by:

1. Creating a new shared folder containing only the channel layout.
2. Sending a final `close`-phase message in the old location pointing to the new folder.
3. Sending a fresh `greeting` (sequence 1, new conversation id) in the new folder.

Old message history MAY be left in place as an archive, or MAY be copied. Each folder is its own audit log.

## 11. Out-of-band Backup

Because this profile has no native immutable history, out-of-band backup is more than a recommendation — it is the only mechanism by which the channel's audit-log property is preserved.

Each pair SHOULD maintain a backup of the shared-folder contents that is **out-of-provider-band** (not dependent on the cloud provider's own version history as the only durable copy) **and out-of-agent-band** (not driven by either agent's tool chain, ideally invisible to both agents).

Suitable substrates:

- An ordinary computer-backup process (Time Machine, Restic, Borg) covering the synced local mirror.
- A cron job on a machine outside the agents' execution environment, periodically rsync-mirroring the synced mirror to local storage.
- A periodic push-mirror to a second storage location on infrastructure disjoint from the primary, configured outside the agents' visibility.

The principle and the visibility argument are the same as in IFP-16 § 11.3 and § 11 generally: a backup that runs where the agent cannot reach it is structurally protected in a way that "trust the agent" is not. The intent is to ensure that "the agent went rogue and deleted everything" or "the agent quietly rewrote a year of files" is recoverable.

The provider's own version history is useful but is neither under the principal's control (the provider may purge it on a schedule or after account closure) nor reliably recoverable on a short timeline. Treat it as a convenience, not as the audit log.

## 12. Multi-Agent Channels

This profile covers pairwise channels. Three or more agents sharing one folder is out of scope and SHOULD be addressed in a separate IFP if it proves useful.

## Open Questions

- Should this profile recommend a specific provider list, or stay provider-neutral? Provider-neutral is more durable; a recommended-list is more useful to readers picking one.
- How should pairs handle a provider that silently picks conflict winners (e.g., iCloud Drive)? Forbid such providers? Specify a manual reconciliation step?
- Is there a tractable way to encode "the file at time T was X" in a shared-folder transport, given no native version control, beyond external backup?
- Should the profile specify a heartbeat or keep-alive convention so a long-quiet channel can be distinguished from a channel where one side's sync has silently failed?

## Security Considerations

- **Provider trust.** The provider has full read access and full write access. Treat the provider as a participant in the channel.
- **Account compromise.** If either human's provider account is compromised, the channel is compromised. The provider's account security IS the channel's security floor.
- **Conflict files surface intent.** A conflict file is evidence that two writes raced. It can also be the signature of a hostile counterparty trying to inject content under the cover of a conflict. Treat conflict files as needing principal review (§ 6.3).
- **Sync failure mode.** A long quiet period in the channel may indicate either no activity or a sync that silently stopped working. § 4 Open Question on heartbeats addresses this.

## Interoperability Considerations

A message produced for this transport is a valid IFP-3 message and can be ported unchanged to any other IFP transport — including IFP-16 (git-transport). The folder layout convention here is intentionally identical to IFP-16's so that a pair can migrate between the two without restructuring.

An agent that supports IFP-3 but not this specific transport profile can still read messages from a local copy of the shared folder, as long as it can locate the message files. The profile is primarily about discovery, conflict-handling, and recovery convention, not message format.

## Acknowledgments

This profile was drafted on 2026-05-21 as a peer to IFP-16, motivated by the observation that non-technical users will not adopt a git-based transport regardless of how convenient it is for the agents. A shared folder is the next-easiest substrate after email.

---

*This is IFP-17, Draft status. It will be revised as the first implementations teach us what works and what doesn't.*
