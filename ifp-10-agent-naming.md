# IFP-10: Agent Naming Convention

**IFP:** 10
**Title:** Agent Naming Convention
**Class:** Core
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Opus 4.6)
**Created:** 2026-03-05
**Dependencies:** IFP-1, IFP-2, IFP-5
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines a structured naming convention for Inter-Face agents. It provides a human-readable, hierarchical identifier format that connects agents to their human operators and to external identity namespaces. The convention complements the cryptographic identity mechanisms in IFP-5 by giving agents names that people can read, remember, speak aloud, and reason about.

## Motivation

IFP-5 defines three identifier formats: simple names (`pete-agent`), URLs (`https://pete.example/.well-known/iface`), and DIDs (`did:key:z6Mk...`). These serve their purposes -- human readability, endpoint resolution, and cryptographic identity respectively -- but none of them answers a basic question: **whose agent is this, and which one?**

A person may operate multiple agents for different purposes (a general assistant, a calendar scheduler, a research agent). Each of those agents may have sub-agents. And the person themselves may be known across multiple identity platforms. We need a naming structure that:

- Identifies the human operator
- Identifies which agent (and optionally which sub-agent)
- Anchors the name to a verifiable external identity
- Is readable and pronounceable by humans
- Works in message headers, audit logs, capability documents, and conversation

The naming convention defined here is a **display-layer** convention. It sits above the cryptographic identity layer (IFP-5) and below the application layer. An agent name is not a security credential -- it is a human-legible label that can be resolved to one.

## 1. Name Structure

### 1.1 Format

An agent name follows the structure:

```
namespace:human_name.agent_name[.sub_agent_name]
```

Where:

- `namespace` -- An identity provider or namespace authority (see Section 3).
- `human_name` -- The human operator's username or handle within that namespace.
- `agent_name` -- The name of the agent.
- `sub_agent_name` -- Optional. A subordinate agent or specialized function within the parent agent.

The colon (`:`) separates namespace from the rest. Dots (`.`) separate the hierarchical components of the name.

### 1.2 Examples

| Agent name | Meaning |
| ---------- | ------- |
| `github:peterkaminski.freya` | Pete's agent "Freya" anchored to his GitHub identity |
| `github:peterkaminski.freya.nightlight` | A sub-agent of Freya called "Nightlight" |
| `bsky:pete.kaminski.kai` | Pete's agent "Kai" anchored to his Bluesky handle |
| `x:peterkaminski.scout` | Pete's agent "Scout" anchored to his X/Twitter handle |
| `matrix:@pete:kaminski.org.atlas` | Pete's agent "Atlas" anchored to his Matrix ID |
| `indieweb:peterkaminski.com.herald` | Pete's agent "Herald" anchored to his personal domain |
| `did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnEGta2doK.envoy` | Agent "Envoy" anchored to a DID |
| `fediverse:@pete@social.coop.relay` | Pete's agent "Relay" anchored to his fediverse identity |
| `keybase:peterkaminski.courier` | Pete's agent "Courier" anchored to Keybase |
| `dns:kaminski.org.concierge` | Pete's agent "Concierge" anchored to a domain he controls |

### 1.3 Component Rules

**Namespace**: Lowercase. Identifies the identity authority. See Section 3 for registered namespaces.

**Human name**: The human's identifier as it appears in the namespace. Preserved as-is (including dots, underscores, or other characters that the namespace allows in usernames). The boundary between `human_name` and `agent_name` is the **last dot before the agent name** -- see Section 2 for parsing rules.

**Agent name**: Lowercase alphanumeric and hyphens. Chosen by the human operator. SHOULD be a real name or descriptive word, not a UUID or hash. Agent names are part of the social layer -- they appear in greetings, audit logs, and conversation.

**Sub-agent name**: Same character rules as agent name. Represents a specialized function, module, or delegate within the parent agent.

## 2. Parsing

### 2.1 Parsing Rules

1. Split on the first `:` to separate `namespace` from `path`.
2. The `path` is `human_name.agent_name[.sub_agent_name]`.
3. The boundary between `human_name` and `agent_name` is **declared in the agent's identity document** (see Section 4), not inferred from syntax alone.

This is necessary because namespaces differ in what characters they allow in usernames. A Bluesky handle like `pete.kaminski` contains a dot, which is also the hierarchy separator.

### 2.2 Ambiguity Resolution

When an agent name is encountered without a prior identity document, the following heuristics MAY be used:

- If the namespace has a known username format (e.g., GitHub usernames cannot contain dots), parsing is unambiguous.
- If the namespace allows dots in usernames (e.g., Bluesky, Matrix), the name is ambiguous without the identity document. Agents SHOULD resolve the identity document before assuming a parse.
- If resolution is not possible, agents SHOULD treat the name as an opaque string for display purposes and request clarification during the greeting phase.

### 2.3 Display Forms

Implementations SHOULD support these display forms:

| Form | Example | Use |
| ---- | ------- | --- |
| Full | `github:peterkaminski.freya` | Message headers, identity documents |
| Short | `freya` | Conversation, informal reference |
| Qualified | `peterkaminski.freya` | When namespace is implied by context |
| Human-focused | `peterkaminski's freya` | Audit logs, human-facing displays |

## 3. Namespaces

### 3.1 Registered Namespaces

The following namespaces are defined for interoperability:

| Namespace | Authority | Username format | Notes |
| --------- | --------- | --------------- | ----- |
| `github` | GitHub | `username` (no dots) | Unambiguous parsing |
| `bsky` | Bluesky / AT Protocol | `handle.tld` or DID | Dots in handles; requires identity document for parsing |
| `x` | X (formerly Twitter) | `username` (no dots) | Unambiguous parsing |
| `matrix` | Matrix / Element | `@user:server` | Includes colons; entire Matrix ID is the human_name |
| `fediverse` | ActivityPub / Mastodon | `@user@instance` | Full fediverse address is the human_name |
| `indieweb` | IndieWeb / personal domain | `domain.tld` | Domain is the human_name |
| `dns` | DNS domain control | `domain.tld` | Identity verified via DNS TXT record or well-known URL |
| `did` | Decentralized Identifiers | DID string | Full DID is the human_name; formal but not human-friendly |
| `keybase` | Keybase | `username` (no dots) | Unambiguous parsing |
| `nostr` | Nostr | `npub...` or NIP-05 address | NIP-05 may contain dots |
| `email` | Email address | `user@domain` | The email address is the human_name |

### 3.2 Namespace Registration

New namespaces MAY be introduced by any implementation. A namespace becomes conventional when two or more independent implementations recognize it.

Namespace identifiers MUST be lowercase ASCII, and SHOULD be short (under 12 characters).

### 3.3 Multi-Namespace Identity

A single agent MAY be known by multiple names across different namespaces:

```json
{
  "names": [
    "github:peterkaminski.freya",
    "bsky:pete.kaminski.freya",
    "indieweb:peterkaminski.com.freya"
  ]
}
```

These are all names for the same agent, linked by the identity document (IFP-5). The agent's canonical name is whichever the human operator designates as primary. The others are aliases.

## 4. Integration with IFP-5

### 4.1 Identity Document Extension

The IFP-5 identity document is extended with naming fields:

```json
{
  "ifp": 5,
  "agent_id": "https://pete.example/.well-known/iface",
  "name": {
    "canonical": "github:peterkaminski.freya",
    "aliases": [
      "bsky:pete.kaminski.freya",
      "indieweb:peterkaminski.com.freya"
    ],
    "human": "peterkaminski",
    "agent": "freya",
    "display": "Freya (Pete's agent)"
  },
  "keys": [ ... ],
  "endpoints": { ... }
}
```

The `name` object explicitly declares the parse boundaries:

- `human` -- the human_name component
- `agent` -- the agent_name component
- `canonical` -- the primary name
- `aliases` -- alternative names in other namespaces
- `display` -- a human-friendly display string

This eliminates parsing ambiguity entirely: the identity document is authoritative for how the name decomposes.

### 4.2 Message Header Usage

In IFP-4 structured messages, the `from` and `to` fields MAY use the agent name:

```json
{
  "from": {
    "agent": "github:peterkaminski.freya",
    "human": "Pete Kaminski"
  },
  "to": {
    "agent": "github:victoriatanner.sage",
    "human": "Victoria Tanner"
  }
}
```

### 4.3 Relationship to IFP-5 Identifiers

The agent name is not a replacement for the IFP-5 identifiers. It is a complement:

| Identifier type | Purpose | Example |
| --------------- | ------- | ------- |
| Agent name (this IFP) | Human-readable, social layer | `github:peterkaminski.freya` |
| URL (IFP-5) | Endpoint resolution | `https://pete.example/.well-known/iface` |
| DID (IFP-5) | Cryptographic identity | `did:key:z6Mk...` |

An agent name tells you *whose* agent it is and *what* it's called. A URL tells you *where* it is. A DID tells you *cryptographically who* it is. A complete identity includes all three.

## 5. Alternate Syntax Consideration

The `namespace:human.agent` syntax was chosen after considering several alternatives. This section documents the alternatives and the rationale for the choice.

### 5.1 Slash Syntax

```
namespace:human/agent/sub_agent
```

Examples: `github:peterkaminski/freya`, `github:peterkaminski/freya/nightlight`

**Pros**: Slashes clearly separate hierarchy levels. No ambiguity with dots in usernames. Familiar from file paths and GitHub repo paths (`owner/repo`).

**Cons**: Looks like a URL path, which may cause confusion with the IFP-5 URL identifier format. Copy-pasting into URLs requires encoding.

### 5.2 At-Sign Syntax

```
agent@human.namespace
```

Examples: `freya@peterkaminski.github`, `nightlight.freya@peterkaminski.github`

**Pros**: Familiar email-like pattern. Clearly separates agent from human identity. Reads naturally as "Freya at Pete's GitHub."

**Cons**: Inverts the namespace-first ordering (namespaces are top-level but appear last). Collides with email addresses and fediverse handles, both of which use `@`. Sub-agents become awkward (`nightlight.freya@...` reads backwards).

### 5.3 Double-Colon Syntax

```
namespace::human::agent::sub_agent
```

Examples: `github::peterkaminski::freya`, `github::peterkaminski::freya::nightlight`

**Pros**: Completely unambiguous separators. No collision with any existing identifier format. Familiar from C++/Rust namespacing.

**Cons**: Verbose. Looks like programming syntax rather than a social identifier. Harder to speak aloud.

### 5.4 Tilde Syntax

```
namespace:~human/agent
```

Examples: `github:~peterkaminski/freya`, `bsky:~pete.kaminski/freya/nightlight`

**Pros**: The tilde clearly marks the human component (Unix home directory convention). Slashes separate agents. No dot ambiguity.

**Cons**: Tilde has no universal meaning outside Unix. Less familiar. Mixes conventions (tilde from Unix, colon from URIs, slash from paths).

### 5.5 URI-Style Syntax

```
iface://namespace/human/agent
```

Examples: `iface://github/peterkaminski/freya`, `iface://bsky/pete.kaminski/freya/nightlight`

**Pros**: Formally structured as a URI. Clear hierarchy. Could be registered as an IANA URI scheme. Machine-parseable with standard URI libraries.

**Cons**: Verbose. Looks overly formal for a social identifier. The `iface://` prefix adds length without information. May imply the name is resolvable as a URL.

### 5.6 Comparison

| Criterion | `ns:human.agent` | `ns:human/agent` | `agent@human.ns` | `ns::human::agent` | `ns:~human/agent` | `iface://ns/human/agent` |
| --------- | :---: | :---: | :---: | :---: | :---: | :---: |
| Readable | Good | Good | Good | Fair | Fair | Fair |
| Pronounceable | Good | Good | Best | Poor | Fair | Poor |
| Compact | Best | Good | Good | Poor | Good | Poor |
| Unambiguous | Fair | Best | Good | Best | Best | Best |
| Familiar | Good | Good | Best | Fair | Fair | Good |
| Extensible | Good | Good | Fair | Good | Good | Best |

The `namespace:human.agent` syntax offers the best balance of readability, compactness, and familiarity. The dot ambiguity (Section 2) is a known trade-off, mitigated by the identity document declaring parse boundaries explicitly. The slash syntax (`ns:human/agent`) is a strong alternative and implementations MAY accept it as equivalent.

## 6. Sub-Agents

### 6.1 Sub-Agent Semantics

A sub-agent is a specialized function or delegate within a parent agent. Sub-agents:

- Act under the authority of the parent agent
- Share the parent agent's human operator
- MAY have their own keys (signed by the parent agent's key)
- MAY have limited capabilities compared to the parent

### 6.2 Sub-Agent Depth

This IFP defines a maximum depth of **one sub-agent level**:

```
namespace:human.agent.sub_agent     -- valid
namespace:human.agent.sub.sub       -- NOT valid
```

Deeper hierarchies are a sign that agent architecture, not naming, needs attention. If a sub-agent needs its own sub-agents, it should be promoted to a top-level agent.

### 6.3 Sub-Agent Examples

| Name | Purpose |
| ---- | ------- |
| `github:peterkaminski.freya.nightlight` | Freya's sleep/do-not-disturb mode agent |
| `github:peterkaminski.freya.calendar` | Freya's calendar-specialized delegate |
| `github:peterkaminski.freya.research` | Freya's research assistant |

## 7. Naming Recommendations

### 7.1 Agent Names

- SHOULD be real names, mythological names, or descriptive words
- SHOULD be easy to pronounce and remember
- SHOULD NOT be UUIDs, hashes, or sequential numbers
- SHOULD NOT be generic (`agent`, `bot`, `assistant`) -- these names carry no identity

### 7.2 Uniqueness

Agent names are unique **within the scope of a human operator within a namespace**. There is no global uniqueness requirement. `github:alice.freya` and `github:bob.freya` are different agents.

### 7.3 Case Sensitivity

Agent names are **case-insensitive** for matching but **case-preserving** for display. Implementations MUST normalize to lowercase for comparison.

## Security Considerations

- **Agent names are not credentials.** An agent claiming to be `github:peterkaminski.freya` is not authenticated by the name alone. Authentication requires IFP-5 signature verification. The name is a claim; the signature is the proof.
- **Namespace squatting.** An attacker could register a GitHub account `peterkaminski-fake` and create agents under that namespace. The defense is identity verification (IFP-5 Level 2+), not the naming convention itself.
- **Name impersonation.** Similar names (`github:peterkaminskl.freya` with an L) could be used for social engineering. Implementations SHOULD display the full canonical name in security-relevant contexts (audit logs, first-contact greetings).
- **Namespace authority trust.** The naming convention trusts the namespace to authenticate the human. If GitHub is compromised, all `github:` names are suspect. This is no different from trusting DNS for URL identifiers.

## Interoperability Considerations

- Agents that do not implement IFP-10 can still use IFP-5 identifiers. The agent name is an optional layer that improves human readability.
- When communicating with an agent that does not advertise a structured name, implementations SHOULD fall back to the IFP-5 `agent_id` for display.
- The `from.agent` and `to.agent` fields in IFP-4 messages MAY contain either an IFP-10 name or an IFP-5 identifier. Implementations MUST accept both.

## References

- IFP-1 -- Philosophy and Design Principles (Section 5.3: Human legibility)
- IFP-2 -- Specification Style Guide
- IFP-4 -- Structured Message Representation (from/to fields)
- IFP-5 -- Identity and Message Signing (agent identity model)
- RFC 4512 -- Lightweight Directory Access Protocol (LDAP): Directory Information Models (naming conventions precedent)
- W3C DID Core -- Decentralized Identifiers

## Acknowledgments

The agent naming convention was proposed by Peter Kaminski on 2026-03-05. The namespace-colon-dot syntax was selected after evaluating six alternative syntaxes. The draft was developed in conversation between Peter Kaminski and Claude (Opus 4.6).

---

*This is IFP-10, Draft status. The namespace registry and parsing rules will be refined as agents adopt structured names in practice.*
