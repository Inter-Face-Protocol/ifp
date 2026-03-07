# IFP-4: Structured Message Representation

**IFP:** 4
**Title:** Structured Message Representation
**Class:** Core
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Opus 4.6)
**Created:** 2026-03-04
**Dependencies:** IFP-1, IFP-2, IFP-3
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines the canonical structured representation of Inter-Face messages. While IFP-3 defines a human-readable message format (YAML envelope + natural language body), IFP-4 defines a machine-optimized representation of the same logical message model, encoded in JSON.

IFP-3 and IFP-4 are dual representations. A message can be converted between them without loss of meaning. Agents transmit messages in IFP-4 form; humans read them in IFP-3 form; either side can round-trip.

## Motivation

The IFP-3 human-readable format is designed for legibility in a text editor. This makes it excellent for auditing, debugging, and manual composition, but unsuitable for:

- **Deterministic parsing.** YAML permits variation in whitespace, quoting, and field ordering that makes byte-level comparison unreliable.
- **Message signing.** Cryptographic signatures require a canonical byte sequence. YAML's flexibility makes signing the raw text fragile.
- **Transport efficiency.** JSON is more widely supported across programming languages, message queues, and HTTP APIs.
- **Schema validation.** JSON Schema provides robust, widely-tooled validation.

IFP-4 addresses these needs while maintaining a clear, lossless mapping to IFP-3.

## 1. Design Lineage

IFP-4 is the agent-messaging analogue to the email standards family. It plays the same role for Inter-Face that RFC 822/5322 headers play for email: a canonical, machine-processable envelope that carries identity, threading, routing, and content metadata.

| Email standard | Role | IFP-4 analogue |
| -------------- | ---- | -------------- |
| RFC 822 / RFC 5322 | Internet Message Format (headers + body) | `headers` + `body` |
| RFC 2045 / RFC 2046 (MIME) | Multipart body structure, media types | `body.parts[]` with `content_type` |
| RFC 5321 (SMTP) | Message transfer between hosts | IFP-6 (HTTPS), IFP-8 (relay) |
| RFC 6376 (DKIM) | Cryptographic message signing | `security.signatures[]` + IFP-5 |

The goal is not to reinvent email but to learn from its 40+ years of evolution. The structural lessons -- separate message format from transport, sign messages not connections, support threading and tracing -- are directly applicable to agent messaging.

## 2. Message Structure

An IFP-4 message is a JSON object with four top-level sections:

```json
{
  "ifp": 4,
  "headers": { ... },
  "body": { ... },
  "trace": { ... },
  "security": { ... }
}
```

The `ifp` field identifies which IFP the message conforms to.

### 2.1 Headers

Headers carry message metadata. Required fields:

| Field | Type | Description |
| ----- | ---- | ----------- |
| `message_id` | string | Unique message identifier (MUST be globally unique; recommended: UUID or ULID) |
| `date` | string | ISO 8601 timestamp of message creation |
| `from` | object | Sending agent identity (see Section 2.1.1) |
| `to` | array | Receiving agent identity/identities |
| `conversation_id` | string | Shared conversation identifier across a full exchange |
| `sequence` | integer | Message number within this conversation |
| `phase` | string | Conversation phase (see IFP-3, Section 2) |
| `content_type` | string | Media type of the body text (default: `text/markdown; charset=utf-8`) |

Optional fields:

| Field | Type | Description |
| ----- | ---- | ----------- |
| `subject` | string | Brief description of the message topic |
| `thread` | object | Threading information (see Section 2.1.2) |
| `languages` | object | Language information (see Section 2.1.3) |
| `disclosure` | string | Disclosure tier for this exchange |
| `persona` | string | The human's active persona |
| `priority` | string | Message priority: `low`, `normal`, `urgent` (default: `normal`) |
| `ttl_seconds` | integer | Time-to-live in seconds; message may be discarded after this |
| `capabilities` | object | Capability request/offer (see Section 2.1.4) |
| `extensions` | object | Extension fields (see Section 2.5) |

#### 2.1.1 Identity Fields

The `from` field is an object:

```json
"from": {
  "agent": "pete-agent",
  "display": "Pete's agent"
}
```

The `agent` field is the stable agent identifier (see IFP-5). The `display` field is a human-readable name for audit log readability.

The `to` field is an array of identity objects:

```json
"to": [
  { "agent": "alice-agent" }
]
```

#### 2.1.2 Threading

Threading fields enable conversation tracking, modeled on RFC 5322 Message-ID, In-Reply-To, and References:

```json
"thread": {
  "in_reply_to": "msg:01abc...",
  "references": ["msg:01xyz...", "msg:01abc..."]
}
```

- `in_reply_to` -- The `message_id` of the message this is responding to.
- `references` -- An ordered list of `message_id` values in the conversation thread, oldest first.

These fields are OPTIONAL. The `conversation_id` and `sequence` fields in the main headers provide the primary conversation tracking; threading fields provide additional context for complex exchanges.

#### 2.1.3 Language Fields

```json
"languages": {
  "content": "en",
  "preferred": ["en", "es"],
  "human": ["en"]
}
```

These correspond directly to the IFP-3 `languages` envelope fields.

#### 2.1.4 Capability Fields

```json
"capabilities": {
  "request": ["calendar.availability", "doc.summarize"],
  "offer": ["summarize", "translate"]
}
```

Capabilities may be included in any message to request or advertise services. See IFP-7 for the full capability discovery protocol.

### 2.2 Body

The body contains the message content:

```json
"body": {
  "text": "Here's what's current for Pete:\n\n**Active projects:** ...",
  "parts": []
}
```

- `text` -- The primary message content, a UTF-8 string. This corresponds to the natural-language body in IFP-3.
- `parts` -- An array of additional content parts, modeled on MIME multipart (RFC 2045/2046). Each part is an object:

```json
{
  "content_type": "application/json",
  "name": "task",
  "content": { "intent": "meeting_request", "windows": ["..."] }
}
```

Parts allow agents to include structured data alongside natural-language text. The `content_type` field uses standard media types (RFC 2046). The `name` field is a human-readable label for audit purposes.

The `parts` array is OPTIONAL. Most gossip exchanges will only use the `text` field.

### 2.3 Trace

Trace information tracks message transit across intermediaries, modeled on email Received headers:

```json
"trace": {
  "received": [
    {
      "by": "relay:https://relay.example",
      "with": "https+ifp-4",
      "at": "2026-03-04T23:58:13Z",
      "from": "pete-agent"
    }
  ]
}
```

Each entry in the `received` array represents one hop in the message's delivery path. Entries are appended by intermediaries; the most recent hop is last.

Per IFP-1 Section 6.4, intermediaries must be accountable. Any relay or proxy that handles an IFP-4 message MUST append a trace entry.

The `trace` section is OPTIONAL for direct peer-to-peer delivery (IFP-6). It is REQUIRED when messages pass through relays (IFP-8).

### 2.4 Security

The security section carries signatures and optional encryption metadata:

```json
"security": {
  "signatures": [
    {
      "alg": "ed25519",
      "key_id": "pete-agent#key-1",
      "created": "2026-03-04T23:58:12Z",
      "signed_headers": [
        "message_id", "date", "from", "to",
        "conversation_id", "sequence", "phase", "content_type"
      ],
      "signed_body": true,
      "sig": "base64url..."
    }
  ],
  "encryption": {
    "scheme": "sealed_box",
    "recipients": ["alice-agent"]
  }
}
```

- `signatures` -- Array of message signatures. See IFP-5 for signing procedures.
- `encryption` -- Optional encryption metadata. See IFP-5 for encryption support.

The `security` section is OPTIONAL but RECOMMENDED for all messages. See IFP-5 for identity and signing conventions.

### 2.5 Extensions

The `headers.extensions` object provides a namespace for fields not defined by any IFP, similar to X- headers in email:

```json
"extensions": {
  "x-iface-context": "prism-vault",
  "x-custom-field": "value"
}
```

Unknown extensions MUST be preserved when forwarding and SHOULD be ignored when processing (see IFP-2, Section 10). Extension field names SHOULD use a descriptive prefix to avoid collisions.

## 3. Canonicalization

Deterministic serialization is required for message signing. IFP-4 messages MUST be canonicalized before signing using the following rules, based on JCS (JSON Canonicalization Scheme, RFC 8785):

1. **No whitespace** between tokens (no pretty-printing).
2. **Object keys sorted** lexicographically by Unicode code point.
3. **Numbers** represented without unnecessary leading zeros or trailing decimal zeros.
4. **Strings** use minimal escaping (only required escapes per JSON spec).
5. **No trailing commas.**
6. **UTF-8 encoding** without BOM.

The canonical form is used only for signing and verification. Messages in transit or storage MAY use pretty-printed JSON for readability.

## 4. Mapping Between IFP-3 and IFP-4

IFP-3 and IFP-4 represent the same logical message model. The following table defines the field mapping:

| IFP-3 (YAML envelope) | IFP-4 (JSON headers) |
| ---------------------- | -------------------- |
| `ifp` | `ifp` |
| `from` | `headers.from.agent` |
| `to` | `headers.to[0].agent` |
| `date` | `headers.date` |
| `conversation` | `headers.conversation_id` |
| `sequence` | `headers.sequence` |
| `phase` | `headers.phase` |
| `languages.*` | `headers.languages.*` |
| `disclosure` | `headers.disclosure` |
| `reply-to` | `headers.thread.in_reply_to` (by sequence → message_id lookup) |
| `persona` | `headers.persona` |
| `translation.*` | (included in body text with translation markers) |
| (body text) | `body.text` |

**IFP-3 → IFP-4 conversion:**

- Generate a `message_id` if one does not exist.
- Map YAML envelope fields to JSON header fields per the table above.
- The `reply-to` field (a sequence number in IFP-3) maps to `thread.in_reply_to` (a message_id in IFP-4). This requires looking up the message_id of the referenced sequence number in the conversation.
- The natural-language body becomes `body.text`.
- `content_type` defaults to `text/markdown; charset=utf-8`.

**IFP-4 → IFP-3 conversion:**

- Map JSON header fields to YAML envelope fields per the table above.
- The `thread.in_reply_to` (a message_id) maps to `reply-to` (a sequence number). This requires looking up the sequence number of the referenced message_id.
- `body.text` becomes the natural-language body.
- `body.parts[]`, `trace`, and `security` have no direct IFP-3 representation. They may be included as a comment block or appendix in the IFP-3 rendering for human review.

The round-trip is lossless for the core message model (envelope + body). Fields that exist only in IFP-4 (trace, security, parts) are preserved in IFP-4 form and may be rendered as supplementary information in IFP-3.

## 5. JSON Schema

A JSON Schema for IFP-4 messages will be published alongside this specification. The schema defines:

- Required and optional fields
- Field types and formats
- Constraints (e.g., `message_id` uniqueness, `sequence` as positive integer)

The schema is normative: a valid IFP-4 message MUST pass schema validation. The schema will be maintained in the Inter-Face repository.

## Security Considerations

- **Signing scope.** Signatures cover specific header fields and the body (as indicated by `signed_headers` and `signed_body`). Fields not listed in `signed_headers` are not integrity-protected. Implementations SHOULD sign all required header fields.
- **Canonicalization attacks.** The canonicalization rules (Section 3) must be followed exactly. Differences in canonicalization between signer and verifier will cause signature verification to fail. This is preferable to accepting improperly verified messages.
- **Extension injection.** Extensions (`headers.extensions`) are not signed by default. A malicious intermediary could add, modify, or remove extension fields. If an extension carries security-relevant information, it SHOULD be added to the `signed_headers` list.
- **Trace manipulation.** Trace entries are appended by intermediaries, which means they are added after the original signature. Relay integrity must be verified separately (see IFP-8).
- **Body parts.** Structured data in `body.parts[]` should be treated as untrusted input. Agents MUST NOT execute code received in body parts without explicit authorization from their human.

## Interoperability Considerations

- IFP-4 is the wire format for IFP-6 (HTTPS transport) and IFP-8 (relay transport). Transport profiles carry IFP-4 messages.
- IFP-3 is the human-facing format. Agents SHOULD be able to convert between IFP-3 and IFP-4 in both directions.
- Agents that only implement IFP-3 (e.g., during early experimentation) can still participate by converting manually or using a bridge. The ecosystem should not require IFP-4 support as a prerequisite for all participation.

## Design Rationale

The email standards family (RFC 822/5322, MIME, SMTP, DKIM) has evolved over 40 years of decentralized, federated messaging. IFP-4 deliberately adopts the structural patterns that have proven durable:

- **Separate headers from body** (RFC 822) -- keeps metadata parseable without interpreting content.
- **Support multipart content** (MIME, RFC 2045/2046) -- allows structured data alongside natural language.
- **Thread by message reference** (RFC 5322 In-Reply-To/References) -- enables conversation reconstruction.
- **Trace message routing** (SMTP Received headers) -- enables debugging and accountability.
- **Sign messages, not connections** (DKIM, RFC 6376) -- integrity survives relay and storage.

The analogy breaks in important places: agents are not mailboxes, gossip phases have no email equivalent, and trust is progressive rather than binary. But the structural lessons are directly applicable.

## References

- RFC 822 -- Standard for the Format of ARPA Internet Text Messages
- RFC 5322 -- Internet Message Format
- RFC 2045 -- MIME Part One: Format of Internet Message Bodies
- RFC 2046 -- MIME Part Two: Media Types
- RFC 5321 -- Simple Mail Transfer Protocol
- RFC 6376 -- DomainKeys Identified Mail (DKIM) Signatures
- RFC 8785 -- JSON Canonicalization Scheme (JCS)
- IFP-1 -- Philosophy and Design Principles
- IFP-3 -- Inter-Face Message Format (human-readable dual representation)
- IFP-5 -- Identity and Message Signing

## Acknowledgments

The "JSON 822" concept emerged from a conversation between Peter Kaminski and ChatGPT in February 2026 (archived in the inter-face-bootstrap repository). The field-by-field mapping to email concepts and the overall architecture were developed in that conversation.

---

*This is IFP-4, Draft status. It will be revised as implementations reveal what works and what needs refinement.*
