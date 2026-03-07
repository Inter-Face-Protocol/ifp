# IFP-8: Relay and Pub/Sub Transport

**IFP:** 8
**Title:** Relay and Pub/Sub Transport
**Class:** Profile
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Opus 4.6)
**Created:** 2026-03-04
**Dependencies:** IFP-2, IFP-4, IFP-5
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines a relay-based transport profile for Inter-Face messages. It enables communication between agents that cannot directly reach each other, using intermediary relay nodes that store and forward messages.

## Motivation

IFP-6 (HTTPS transport) requires that both agents have publicly reachable HTTPS endpoints. This works for agents running on cloud infrastructure but not for agents behind NATs, firewalls, or on intermittently connected devices (laptops, phones).

A relay transport allows agents to communicate indirectly:

```
Agent A → Relay → Agent B
```

This is analogous to SMTP relay (RFC 5321), where mail servers accept, store, and forward messages on behalf of recipients. It also draws on the relay model used by Nostr (relay servers) and Matrix (homeservers).

## 1. Relay Model

### 1.1 What is a Relay

A relay is a service that accepts IFP-4 messages on behalf of agents and makes them available for retrieval. A relay does not process messages -- it stores and forwards them.

Relays are **accountable intermediaries** (IFP-1, Section 6.4). They may be intelligent, but they must leave an auditable trace.

### 1.2 Relay Operations

A relay supports three operations:

| Operation | Description |
| --------- | ----------- |
| **Publish** | An agent sends a message to the relay for delivery |
| **Subscribe** | An agent registers interest in messages addressed to it |
| **Retrieve** | An agent fetches messages waiting for it |

### 1.3 Relay Endpoints

Relays that use HTTPS expose the following endpoints:

```
POST   /relay/publish         -- submit a message for delivery
POST   /relay/subscribe       -- register for message delivery
GET    /relay/messages        -- retrieve waiting messages
DELETE /relay/messages/{id}   -- acknowledge receipt of a message
```

These endpoints are illustrative. The specific API contract for relays will be refined as implementations develop. Relays using other transports (WebSocket, SSE, message queues) may define different interfaces.

## 2. Message Flow

### 2.1 Store-and-Forward

The basic message flow through a relay:

```
Agent A                    Relay                    Agent B
   |                         |                         |
   |-- publish(message) ---->|                         |
   |<-- 202 Accepted --------|                         |
   |                         |                         |
   |                         |<--- retrieve ---------- |
   |                         |--- messages[] --------->|
   |                         |<--- acknowledge --------|
   |                         |                         |
```

### 2.2 Subscription-Based Delivery

Relays MAY support push delivery via subscription:

```
Agent B                    Relay                    Agent A
   |                         |                         |
   |-- subscribe ----------->|                         |
   |                         |                         |
   |                         |<-- publish(message) --- |
   |<-- push(message) -------|                         |
   |                         |                         |
```

Push delivery may use WebSocket, Server-Sent Events (SSE), or webhook callbacks. The mechanism is relay-specific.

### 2.3 Relay Selection

Agents advertise their relay preferences in their identity document (IFP-5) or capability document (IFP-7):

```json
{
  "relay": {
    "urls": ["https://relay1.example", "https://relay2.example"],
    "preference": "any"
  }
}
```

When Agent A wants to send a message to Agent B:

1. Look up Agent B's relay preferences.
2. Publish the message to one of Agent B's relays.
3. If delivery fails, try the next relay.

## 3. Trace Requirements

Per IFP-1 Section 6.4 (accountable intermediaries), relays MUST append a trace entry to every message they handle:

```json
{
  "by": "relay:https://relay1.example",
  "with": "https+ifp-4",
  "at": "2026-03-04T23:58:13Z",
  "from": "pete-agent"
}
```

This entry is added to the `trace.received[]` array in the IFP-4 message before the message is made available to the recipient.

Trace entries allow:

- The recipient to see how the message was routed.
- The human to audit the delivery path.
- Debugging of delivery failures.

## 4. Relay Trust

Relays introduce trust considerations that do not exist in direct peer-to-peer communication.

### 4.1 What Relays Can See

A relay that handles an IFP-4 message can see:

- **Message headers** (from, to, conversation_id, phase) -- always in plaintext.
- **Message body** -- in plaintext unless the message is encrypted (IFP-5, Section 6).
- **Trace information** -- the relay appends to and can read the trace chain.

A relay CANNOT:

- **Forge signatures** -- the relay does not have the sender's private key. Message signatures (IFP-5) remain valid through relay.
- **Modify signed content** -- any modification to signed headers or body would invalidate the signature.

### 4.2 Relay Trust Levels

| Trust level | Description | Requirements |
| ----------- | ----------- | ------------ |
| Untrusted | Relay may log or leak message content | Agents SHOULD encrypt message bodies |
| Trusted | Relay is operated by a known party | Agents MAY send unencrypted messages |
| Self-operated | Relay is run by one of the communicating parties | Maximum convenience, inherent trust |

Agents SHOULD assume untrusted relays by default and encrypt message bodies for sensitive exchanges.

### 4.3 Relay Misbehavior

Possible relay misbehavior includes:

- **Dropping messages** -- refusing to deliver. Detectable by the sender when no reply arrives.
- **Delaying messages** -- holding messages beyond reasonable time. Detectable via the `date` field vs. delivery time.
- **Duplicating messages** -- delivering the same message multiple times. Handled by IFP-5 replay detection.
- **Reading content** -- if unencrypted. Mitigated by body encryption.
- **Injecting trace entries** -- a relay could add false trace entries. Mitigated by agents verifying relay identity.

Agents SHOULD verify message signatures after relay delivery to confirm no tampering occurred.

## 5. Pub/Sub Patterns

Beyond point-to-point relay, some scenarios benefit from publish/subscribe:

### 5.1 Topic-Based Subscription

A relay MAY support topic-based subscriptions where agents subscribe to categories of messages:

```json
{
  "subscribe": {
    "topics": ["gossip.exchange", "capabilities.update"],
    "agent": "alice-agent"
  }
}
```

This is useful for group exchanges or broadcast announcements (e.g., an agent announcing updated capabilities to all peers).

### 5.2 Relationship to Group Exchanges

Pub/sub relay patterns may support future group exchange protocols (noted as an open question in IFP-3). This IFP defines the transport mechanism; the semantics of group gossip are left for a future IFP.

## 6. Message Persistence

Relays SHOULD persist messages for at least **7 days** or until acknowledged by the recipient, whichever comes first.

Messages with a `ttl_seconds` header (IFP-4) SHOULD be discarded after the TTL expires.

Relays MAY offer configurable persistence periods.

## Security Considerations

- **Relay operators can observe metadata.** Even with encrypted bodies, the relay sees who is communicating, when, and at what phase. Agents concerned about metadata privacy should consider using multiple relays or onion-routing patterns (not defined in this IFP).
- **Relay identity verification.** Agents SHOULD verify relay identity via TLS certificates. A malicious entity impersonating a relay could intercept or drop messages.
- **Message encryption is strongly recommended** for relay transport. Unlike IFP-6 (where TLS provides end-to-end encryption between peers), relay transport means TLS only protects each hop, not the full path.
- **Relay availability.** A relay going offline makes its agents unreachable. Agents SHOULD advertise multiple relays for resilience.

## Interoperability Considerations

- Messages delivered via relay are identical to messages delivered via IFP-6 (HTTPS direct), except for the additional trace entries. Receiving agents process them the same way.
- An agent MAY support both IFP-6 and IFP-8 simultaneously, accepting direct messages and relay-forwarded messages at the same inbox.
- Relay protocols are deliberately underspecified in this draft. The relay API defined here is illustrative; concrete relay implementations may use WebSocket, NATS, Kafka, or other pub/sub infrastructure.

## Design Rationale

The relay model draws on several precedents:

- **SMTP relay** (RFC 5321) -- store-and-forward mail delivery between servers, with relay trust as a central concern (open relay abuse, relay authentication).
- **Nostr relays** -- simple message relay servers with pub/sub semantics, demonstrating that lightweight relay infrastructure can support decentralized communication.
- **Matrix homeservers** -- federated relay with message persistence and room-based pub/sub.

IFP-8 is intentionally less specified than IFP-6 because the relay ecosystem is less mature and may need to accommodate diverse infrastructure choices. The core requirements (trace, message integrity, persistence) are stable; the API details will be refined by implementation.

## References

- RFC 5321 -- Simple Mail Transfer Protocol (relay model)
- IFP-1 -- Philosophy and Design Principles (Section 6.4: Accountable intermediaries)
- IFP-4 -- Structured Message Representation (trace information)
- IFP-5 -- Identity and Message Signing (signatures survive relay)

## Acknowledgments

The relay transport concept was outlined in a conversation between Peter Kaminski and ChatGPT in February 2026 (archived in the inter-face-bootstrap repository).

---

*This is IFP-8, Draft status. The relay API will be refined substantially as implementations test different relay architectures.*
