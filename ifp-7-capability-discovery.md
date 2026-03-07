# IFP-7: Agent Capability Discovery

**IFP:** 7
**Title:** Agent Capability Discovery
**Class:** Core
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Opus 4.6)
**Created:** 2026-03-04
**Dependencies:** IFP-1, IFP-2, IFP-3, IFP-4
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines how Inter-Face agents advertise and discover each other's capabilities. It specifies a capability schema (transport-independent), an HTTPS endpoint binding (via IFP-6), and a message-phase negotiation pattern for dynamic capability exchange.

## Motivation

When two agents first communicate, neither knows what the other can do. Capability discovery allows agents to learn what services a peer offers, what information it can share, and what protocols it supports -- before investing in a full gossip exchange.

Per IFP-1 Section 6.5 (dynamic contextual capabilities), an agent's capabilities may depend on context: trust level, disclosure tier, current workload, and the specific conversation. IFP-7 supports both static capability documents (for initial discovery) and dynamic capability negotiation during conversation (for context-sensitive cooperation).

## 1. Capability Schema

A capability is described by a JSON object:

```json
{
  "name": "gossip.exchange",
  "version": "1",
  "description": "Participate in IFP-3 gossip exchanges",
  "parameters": {},
  "conditions": {}
}
```

### 1.1 Capability Fields

| Field | Type | Required | Description |
| ----- | ---- | -------- | ----------- |
| `name` | string | Yes | Capability identifier using dot notation |
| `version` | string | No | Version of this capability (default: `"1"`) |
| `description` | string | Yes | Human-readable description of what this capability does |
| `parameters` | object | No | Expected input parameters |
| `conditions` | object | No | Conditions under which this capability is available |

### 1.2 Standard Capabilities

The following capabilities are defined for interoperability:

| Name | Description |
| ---- | ----------- |
| `gossip.exchange` | Can participate in IFP-3 gossip exchanges (greeting through close) |
| `message.receive` | Can receive IFP-4 structured messages |
| `message.reply` | Can reply to messages with correct threading |
| `identity.verify` | Supports IFP-5 message signing and verification |
| `capabilities.get` | Returns capability information (this protocol) |
| `ping` | Responds to connectivity tests |

Additional capabilities MAY be defined by agents. Capability names SHOULD use dot notation to indicate category (e.g., `calendar.availability`, `doc.summarize`, `translate.text`).

### 1.3 Conditional Capabilities

Capabilities may be conditional on context:

```json
{
  "name": "calendar.availability",
  "description": "Share calendar availability windows",
  "conditions": {
    "min_disclosure": "professional",
    "min_auth_level": 1
  }
}
```

The `conditions` object describes when the capability is available. Standard condition fields:

| Field | Type | Description |
| ----- | ---- | ----------- |
| `min_disclosure` | string | Minimum disclosure tier required |
| `min_auth_level` | integer | Minimum IFP-5 authentication level required |
| `temperature` | string | Required conversation temperature (`cool`, `warm`, `hot`) |

Agents receiving a capability document SHOULD respect the stated conditions. Requesting a conditional capability without meeting its conditions SHOULD result in an error phase message explaining the mismatch.

## 2. Capability Document

A capability document is a JSON object listing an agent's capabilities:

```json
{
  "ifp": 7,
  "agent_id": "pete-agent",
  "capabilities": [
    {
      "name": "gossip.exchange",
      "version": "1",
      "description": "Participate in IFP-3 gossip exchanges"
    },
    {
      "name": "message.receive",
      "description": "Accept IFP-4 structured messages"
    },
    {
      "name": "identity.verify",
      "description": "IFP-5 message signing (Ed25519)"
    },
    {
      "name": "capabilities.get",
      "description": "Return this capability document"
    }
  ],
  "ifp_support": [3, 4, 5, 6, 7],
  "updated": "2026-03-04T12:00:00Z"
}
```

The `ifp_support` field lists the IFP numbers this agent implements. This allows quick compatibility checking before attempting communication.

## 3. Discovery Methods

IFP-7 supports two discovery methods. Both return the same logical information; they differ in transport and timing.

### 3.1 Endpoint Discovery (via IFP-6)

An agent MAY publish its capability document at the well-known HTTPS endpoint:

```
GET /.well-known/iface/capabilities
```

This returns the capability document as JSON with `Content-Type: application/json`.

This method is suitable for initial discovery before any conversation has started. It returns the agent's base capabilities without context-dependent conditions.

### 3.2 Message-Phase Discovery (transport-independent)

Agents MAY exchange capabilities during the greeting phase of an IFP-3 conversation. This works over any transport (IFP-6 HTTPS, IFP-8 relay, or others).

An agent includes capability information in the greeting message body:

> I'm Pete's agent. I support IFP-3 gossip exchanges, IFP-5 signing (Ed25519), and can share calendar availability at the professional disclosure tier.

For machine-processable capability exchange, the agent MAY include a capability document as a body part in the IFP-4 message:

```json
"body": {
  "text": "I'm Pete's agent. Here are my capabilities...",
  "parts": [
    {
      "content_type": "application/json",
      "name": "capabilities",
      "content": {
        "ifp": 7,
        "capabilities": [ ... ]
      }
    }
  ]
}
```

This method is preferred when:

- The agents don't have HTTPS endpoints (e.g., communicating via relay or email)
- The capabilities are context-dependent (varying by disclosure tier or trust level)
- The agents want to negotiate capabilities as part of the conversation

### 3.3 Choosing a Method

| Situation | Recommended method |
| --------- | ------------------ |
| First contact, both have HTTPS endpoints | Endpoint discovery, then greeting exchange |
| Communicating via relay (IFP-8) | Message-phase discovery in greeting |
| Context-dependent capabilities | Message-phase discovery |
| Automated compatibility checking | Endpoint discovery |

Agents MAY use both methods. The endpoint document provides a baseline; the greeting exchange can refine it based on context.

## 4. Versioning

Capability documents include an `updated` timestamp. Agents SHOULD cache capability documents and refresh them periodically or when a conversation suggests capabilities have changed.

Individual capabilities include an optional `version` field. When a capability's behavior changes, its version SHOULD be incremented.

## Security Considerations

- **Capability documents are self-declared.** An agent claiming a capability may not actually implement it correctly. Implementations should handle capability failures gracefully.
- **The endpoint capability document is public.** Any agent (or human) can fetch it. Do not include sensitive information in the capability document. Context-dependent capabilities should use conditions to restrict availability, not rely on the document being private.
- **Capability negotiation via message-phase** is subject to the same authentication considerations as any IFP-3/4 message. Verify the sender's identity (IFP-5) before trusting claimed capabilities.

## Interoperability Considerations

- Agents that do not implement IFP-7 can still participate in gossip exchanges. Capability discovery is helpful but not required for basic IFP-3 communication.
- Unknown capabilities SHOULD be ignored rather than treated as errors. This allows agents to advertise new capabilities without breaking existing peers.
- The `ifp_support` field provides a quick way to check protocol compatibility without examining individual capabilities.

## References

- IFP-1 -- Philosophy and Design Principles (Section 6.5: Dynamic contextual capabilities)
- IFP-3 -- Inter-Face Message Format (greeting phase)
- IFP-4 -- Structured Message Representation (body.parts for capability exchange)
- IFP-5 -- Identity and Message Signing (authentication levels in conditions)
- IFP-6 -- HTTPS Transport Profile (well-known endpoint)

## Acknowledgments

The capability discovery concept was outlined in a conversation between Peter Kaminski and ChatGPT in February 2026 (archived in the inter-face-bootstrap repository). The dual discovery model (static endpoint + message-phase negotiation) was developed during plan review with Claude (Opus 4.6) on 2026-03-04.

---

*This is IFP-7, Draft status. The standard capability set will grow as implementations discover what agents need to advertise.*
