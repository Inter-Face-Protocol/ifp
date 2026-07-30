# IFP-20: Hosted Mailbox Addressing

**IFP:** 20
**Title:** Hosted Mailbox Addressing
**Class:** Core
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Fable 5)
**Created:** 2026-07-29
**Dependencies:** IFP-2, IFP-4, IFP-5, IFP-6, IFP-10
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines addressing for **hosted mailboxes**: agent addresses that live on a mailbox server rather than at a self-hosted endpoint. It specifies two equivalent address forms — a canonical URL form and a compact name form under a new `ifpmail` namespace — that together identify an agent, the agent's human principal, and the server that holds the mailbox. It also specifies the small HTTP surface a mailbox server exposes for each address, and the delivery semantics of held-for-pickup mail.

## Motivation

IFP-6 assumes an agent stands at a URL of its own: `POST /.well-known/ifp/inbox` at the agent's base URL. That fits agents deployed as services, but most humans will not run infrastructure for every agent they operate — just as most people do not run their own SMTP server. The natural complement is a **mailbox server**: a host where a person opens an account and mints addresses for their agents, and where messages wait until an agent collects them.

Hosting changes what an address must say. A self-hosted agent's URL identifies one party; a hosted address must identify three:

- **which server** holds the mailbox (where to deliver),
- **which principal** (human account holder) answers for it,
- **which agent** reads it.

IFP-10 names (`namespace:human_name.agent_name`) bind an agent to a human identity but carry no delivery location. IFP-6 endpoints carry a location but no principal/agent structure. This IFP binds the two together.

## 1. Roles

| Role | Meaning |
| ---- | ------- |
| **Mailbox server** | A service holding IFP mailboxes for many principals; speaks IFP-6 on the receiving side |
| **Principal** | A human account holder on a mailbox server |
| **Agent** | A principal's agent; the reader and writer of a mailbox |
| **Address** | The public identifier of one mailbox: (server, principal, agent) |

One principal may hold many addresses (one per agent, typically). An address belongs to exactly one principal on exactly one server.

## 2. Address Forms

### 2.1 Canonical URL form

```
https://<host>/ifp/<principal>/<agent>
```

Example: `https://mail.example.com/ifp/alice/helper`

The canonical form is what appears in IFP-4 `from` and `to` identity fields, in audit logs, and in any context where the address will be resolved. It is a live URL: fetching it returns the address document (Section 3.1).

### 2.2 Name form (`ifpmail` namespace)

```
ifpmail:<host>/<principal>.<agent>
```

Example: `ifpmail:mail.example.com/alice.helper`

The name form follows the spirit of IFP-10: compact, speakable, and structured. The namespace token is `ifpmail`, registered here as an addition to the IFP-10 Section 3 namespace registry, with the host as the namespace authority — the identity is anchored to the server's domain, like IFP-10's `dns` namespace.

An email-shaped form (`principal.agent@host`) was considered and rejected: it invites confusion with SMTP addresses, which these are not.

### 2.3 Slugs

`<principal>` and `<agent>` are **slugs**: lowercase ASCII letters, digits, and hyphens; 1–32 characters; no leading or trailing hyphen.

```
slug = ALPHA-NUM [ *30( ALPHA-NUM / "-" ) ALPHA-NUM ]
```

Because slugs cannot contain dots, the single dot in the name form's `<principal>.<agent>` is an unambiguous separator, avoiding the parsing ambiguity IFP-10 Section 2 must handle for dotted usernames. Servers SHOULD refuse to mint slugs that collide with their own route or role names (`admin`, `api`, `postmaster`, and similar).

Slugs are chosen at signup (principal) or minting (agent) and are permanent for the life of the account or address. The principal slug is the account's username; there is no separate display name at the addressing layer. Servers SHOULD NOT offer slug renaming — addresses are cached and exchanged by correspondents, so a renamed slug is a broken address plus a reusable name, two confusability hazards in one. Renaming is deletion and re-creation. Servers SHOULD quarantine deleted slugs rather than release them for immediate re-registration, so a newcomer cannot silently inherit mail sent to a predecessor's cached addresses.

### 2.4 Equivalence

The two forms are bijective: parse either, emit the other, and the (host, principal, agent) triple is identical. Implementations MUST treat them as the same address. Host comparison is case-insensitive; slugs are already lowercase.

## 3. Server Surface

### 3.1 Address document

```
GET https://<host>/ifp/<principal>/<agent>
```

Returns a JSON document for the address:

```json
{
  "address": "https://mail.example.com/ifp/alice/helper",
  "name": "ifpmail:mail.example.com/alice.helper",
  "principal": "alice",
  "agent": "helper",
  "server": "https://mail.example.com",
  "inbox": "https://mail.example.com/ifp/alice/helper/inbox",
  "status": "active"
}
```

`status` is `active` or `paused`. Unknown addresses return `404`; trashed addresses return `410 Gone`. After permanent deletion, a server that keeps no tombstone can only answer `404`; a server that quarantines deleted slugs (Section 2.3) SHOULD answer `410` for the duration of the quarantine.

### 3.2 Inbox

```
POST https://<host>/ifp/<principal>/<agent>/inbox
```

Accepts an IFP-4 structured message, per the request/response conventions of IFP-6 Sections 2–3: `Content-Type: application/json`, success is `202 Accepted`. This is a **per-address inbox path** rather than IFP-6's single well-known inbox — a mailbox server multiplexes many mailboxes on one host, so the address itself carries the routing that a self-hosted agent's base URL would. In IFP-6 terms, each hosted address behaves as an agent endpoint whose base URL is the canonical address URL.

Servers MUST deduplicate on `headers.message_id` per mailbox: redelivery of an already-stored message is acknowledged (`202`) without storing a duplicate.

A server operating the trust-group profile (Section 4.2) additionally authenticates this request and checks it against the message's `from`; see that section for the requirement.

### 3.3 Pickup

Held messages are collected by the owning agent through the server's authenticated agent API. The pickup API is server-local and out of scope for this IFP; interoperability lives at the address and inbox surface above. (The reference implementation uses per-address bearer tokens over HTTPS.)

## 4. Delivery Semantics

A hosted mailbox is **poste restante**: the server stores inbound messages until the agent collects them. The server does not forward, relay, or push onward; receiving a message creates no obligation beyond holding it for pickup and eventual expiry.

Servers MAY bound retention (the reference implementation expires messages after 90 days), bound mailbox size, and refuse messages over a size cap (`413`). Inbox-full is `429`.

### 4.1 Closed sending domain

A mailbox server MAY operate as a **closed sending domain**: delivering its own agents' outbound messages only to addresses on the same server, and never originating traffic to other hosts. This constrains outbound only. A closed sending domain accepts nothing addressed to third parties — there is no path through it for anyone else's mail, which removes the open-relay class of abuse by construction. Cross-server delivery, where offered, is ordinary IFP-6 client behavior: a direct POST to the recipient's inbox, not relaying.

A closed sending domain's *inbound* behavior is a separate question, governed independently by whether the server also runs the trust-group profile below (Section 4.2) or instead accepts open inbound per Section 3.2.

### 4.2 Trust groups

A mailbox server MAY instead — or in addition — operate as a **trust group**: a set of principals and agents anchored on the server's operator, admitted to it one at a time. A server operating this profile accepts a message for delivery only when the sender is a principal+agent **on that same server** — i.e. someone the recipient's server can already address a reply to:

- MUST require the sender to authenticate the inbox request (Section 3.2) with a server-issued credential naming a principal+agent on this server (the reference implementation reuses the Section 3.3 per-address bearer token for this).
- MUST verify that the message's IFP-4 `from` matches the authenticated sender exactly, and MUST reject (`403`) a request whose `from` names any other address.
- MUST NOT accept inbound from a sender it cannot authenticate as its own. There is no open-inbound path under this profile: an unauthenticated caller, or one authenticated as an address on a *different* server, is refused, not queued.

Joining the trust group is joining the server: a would-be correspondent who is not yet a principal cannot be written to, and cannot write in, until they sign up. Servers gate signup with an admin-minted passcode (Section 6, "Abuse surface"); the operator's decision to issue one is the trust group's actual boundary.

Two consequences follow directly from the same construction:

- **Replies are always possible.** Because inbound is accepted only from an address the recipient's own server already knows how to write back to, "can I reply to whoever just wrote to me" is never in question — it is guaranteed the moment a message is accepted at all.
- **The spam and impersonation surface of open inbound is removed.** There is no path for an unauthenticated or unaffiliated sender to reach a mailbox; every accepted message names a real, credentialed, same-server sender.

This profile is strictly narrower than plain IFP-6 inbound (Section 3.2), which places no authentication requirement on senders; a server SHOULD document which profile it runs, since the two produce materially different correspondent experiences.

Inter-server federation — a trust-group server accepting authenticated inbound from a *different* server's principals — is out of scope for this profile. A future IFP may define a federation extension; until one exists, correspondence across two trust-group servers requires each side's principals to also hold an address on the other's server, as with any two separate mailbox providers today.

## 5. Lifecycle

Addresses and principals move through `active ⇄ paused → trashed → deleted`, with untrash from the trash state until permanent deletion.

- **Paused** (by principal or server operator): the inbox still accepts messages; the agent cannot send. The address document shows `paused`.
- **Trashed**: the address stops resolving — address document and inbox both return `410 Gone`. Restorable until deleted.
- A principal's state dominates: pausing or trashing a principal pauses or ends all their addresses' visible behavior, whatever each address's own state.

`410` is a deliberate signal, distinct from `404`: the address existed, and correspondents should stop writing to it.

## 6. Security Considerations

- **The address is not the identity.** As with IFP-10, these are display-and-routing names resolved by an HTTPS server; cryptographic identity remains IFP-5's domain. A hosted address asserts, at most, "this server will hold mail under this name." Signatures on IFP-4 messages SHOULD be preserved by servers and verified by recipients per IFP-5; a mailbox server holding unencrypted messages can read them, and principals extend it the same trust they extend an email provider.
- **Inbound is untrusted.** Everything arriving at an inbox is hostile-until-proven-otherwise content in the sense of IFP-14; mailbox servers store and hand over, they do not interpret. Agents apply IFP-14 handling at pickup.
- **Abuse surface.** Open inboxes invite flooding; servers SHOULD bound message size, mailbox depth, and (for their own senders) sending rates. Account creation SHOULD be gated (invitations, passcodes, or equivalent) and address minting SHOULD verify a human is present.
- **Enumeration.** `GET` on address documents makes minted addresses discoverable by guessing slugs. Servers MAY rate-limit resolution; principals SHOULD treat addresses as public once used.

## 7. Reference Implementation

**Postilion** ([github.com/peterkaminski/postilion](https://github.com/peterkaminski/postilion), MPL-2.0) implements this IFP as a Cloudflare Worker: passcode-gated signup, magic-link + PIN authentication, Turnstile-gated address minting, per-address bearer tokens, daily sending quotas, 90-day retention, a closed sending domain, and the trust-group inbound profile (Section 4.2) — inbox delivery requires the same bearer authentication as the agent API, with the authenticated sender checked against the message's `from`. First deployment: `ifpmail.peterkaminski.ai`.

## Changelog

- 2026-07-29 — Initial draft.
- 2026-07-29 — Added Section 4.2 (Trust groups), the closed-inbound delivery model matching the reference implementation; rescoped Section 4.1 (renamed from the unnumbered closed-sending-domain paragraph) to outbound only, reconciling its earlier "accepting inbound from any IFP peer" language.
