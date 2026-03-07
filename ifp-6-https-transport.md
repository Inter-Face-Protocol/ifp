# IFP-6: HTTPS Transport Profile

**IFP:** 6
**Title:** HTTPS Transport Profile
**Class:** Profile
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Opus 4.6)
**Created:** 2026-03-04
**Dependencies:** IFP-2, IFP-4, IFP-5
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines how Inter-Face messages are transmitted between agents using HTTPS. It specifies endpoint conventions, request and response formats, delivery semantics, retry behavior, and security requirements.

IFP-6 plays the same architectural role as SMTP (RFC 5321) in the email world: it defines how messages move between agents. Where SMTP defines envelope routing, delivery semantics, retry behavior, and error codes, IFP-6 defines the analogous concerns for HTTPS-based agent communication.

## Motivation

HTTPS is the simplest transport for peer-to-peer agent communication. It requires no special infrastructure beyond a web server, works through firewalls and NATs, and provides transport-layer security via TLS. For agents deployed as Cloudflare Workers, VPS services, or similar web infrastructure, HTTPS is the natural choice.

## 1. Agent Endpoints

An Inter-Face agent MUST expose the following HTTPS endpoints:

### 1.1 Inbox

```
POST /.well-known/iface/inbox
```

Accepts inbound IFP-4 structured messages. This is the primary message delivery endpoint.

### 1.2 Identity (optional)

```
GET /.well-known/iface/identity
```

Returns the agent's identity document (see IFP-5, Section 1.2).

### 1.3 Capabilities (optional)

```
GET /.well-known/iface/capabilities
```

Returns the agent's capability description document (see IFP-7).

### 1.4 Endpoint Discovery

An agent's base URL (e.g., `https://pete.example`) combined with the well-known paths defines the complete set of endpoints. Agents may advertise their base URL through:

- The identity document
- Out-of-band exchange between humans
- A capability discovery response
- The `from.agent` field in a message (if the agent_id is a URL)

Agents MAY support additional endpoint paths, but MUST support the `/.well-known/iface/` paths for interoperability.

## 2. Request Format

### 2.1 Inbound Message Delivery

Messages are delivered via HTTP POST to the inbox endpoint:

```
POST /.well-known/iface/inbox HTTP/1.1
Host: alice.example
Content-Type: application/json; charset=utf-8
Accept: application/json

{IFP-4 message JSON}
```

The request body is a complete IFP-4 structured message (see IFP-4).

### 2.2 Required Headers

| HTTP Header | Value |
| ----------- | ----- |
| `Content-Type` | `application/json; charset=utf-8` |
| `Accept` | `application/json` |

### 2.3 Optional Headers

| HTTP Header | Value | Purpose |
| ----------- | ----- | ------- |
| `Idempotency-Key` | Unique string (recommended: the `message_id`) | Prevents duplicate processing |

## 3. Response Format

### 3.1 Success

```
HTTP/1.1 202 Accepted
Content-Type: application/json

{
  "status": "accepted",
  "message_id": "msg:01abc..."
}
```

A `202 Accepted` response means the message has been received and queued for processing. It does not mean the message has been fully processed or that a reply will be sent.

The response body SHOULD include the `message_id` of the accepted message as confirmation.

### 3.2 Errors

| HTTP Status | Meaning | When to use |
| ----------- | ------- | ----------- |
| `400 Bad Request` | Message is malformed or fails schema validation | Invalid JSON, missing required fields |
| `401 Unauthorized` | Signature missing, invalid, or insufficient auth level | Failed IFP-5 verification |
| `404 Not Found` | Endpoint does not exist | Wrong URL |
| `413 Payload Too Large` | Message exceeds size limit | See Section 5 |
| `429 Too Many Requests` | Rate limit exceeded | See Section 6 |
| `500 Internal Server Error` | Unexpected failure | Agent-side error |
| `503 Service Unavailable` | Agent temporarily unable to process | Maintenance, overload |

Error responses SHOULD include a JSON body with details:

```json
{
  "status": "error",
  "code": "invalid_signature",
  "message": "Signature verification failed for key_id pete-agent#key-1"
}
```

Error codes are strings. Standard codes:

- `invalid_format` -- Message does not conform to IFP-4 structure
- `invalid_signature` -- Signature verification failed
- `unknown_sender` -- Sender identity cannot be verified
- `rate_limited` -- Too many requests from this sender
- `payload_too_large` -- Message exceeds size limit
- `internal_error` -- Unexpected server-side error

Note: HTTP-level errors are the mechanical layer. For protocol-level negotiation (e.g., version mismatch, unknown phase), agents should respond with `202 Accepted` and then send an IFP-3/4 error phase message asynchronously. This separates transport errors from conversation errors.

## 4. Delivery Semantics

### 4.1 Asynchronous Reply

Message delivery is asynchronous. When Agent A sends a message to Agent B:

1. Agent A POSTs the message to Agent B's inbox.
2. Agent B returns `202 Accepted`.
3. Agent B processes the message (which may involve LLM inference and tool calls).
4. Agent B sends a reply by POSTing a new message to Agent A's inbox.

There is no synchronous request-response for conversation messages. The HTTP response is purely a delivery acknowledgment.

### 4.2 Idempotency

Agents SHOULD use the `message_id` as an `Idempotency-Key`. If a message with a previously received `message_id` arrives, the agent SHOULD return `202 Accepted` without reprocessing.

This allows senders to safely retry delivery without causing duplicate processing.

## 5. Message Size

Agents SHOULD accept messages up to **1 MB** in size. Messages exceeding this limit MAY be rejected with `413 Payload Too Large`.

For most gossip exchanges, messages will be far smaller (a few KB). The 1 MB limit accommodates messages with structured data in `body.parts[]`.

## 6. Rate Limiting

Agents SHOULD implement rate limiting per sender identity.

Recommended defaults:

- **10 messages per minute** per sender for cool exchanges
- **60 messages per minute** per sender for hot exchanges

When rate-limited, the agent SHOULD return `429 Too Many Requests` with a `Retry-After` header indicating when the sender may try again.

Rate limits MAY be negotiated between agents during the greeting phase.

## 7. Retry Behavior

When a delivery attempt fails (network error, 5xx response), the sender SHOULD retry with exponential backoff:

- First retry: 1 minute
- Second retry: 5 minutes
- Third retry: 30 minutes
- Subsequent retries: hourly, up to 24 hours

After 24 hours of failed delivery, the sender SHOULD stop retrying and notify its human that the message could not be delivered.

Agents MUST NOT retry on 4xx responses (client errors), as these indicate a problem with the message itself.

## 8. TLS Requirements

All IFP-6 communication MUST use TLS 1.2 or later. Plain HTTP MUST NOT be used.

Agents SHOULD verify TLS certificates using the standard web PKI. Self-signed certificates MAY be accepted during early experimentation if both agents' humans have explicitly agreed.

## Security Considerations

- **TLS provides transport security** (encryption in transit, server authentication) but does not provide message-level security. For message integrity and sender authentication, use IFP-5 message signing.
- **TLS alone does not authenticate the sending agent.** TLS authenticates the server (receiving agent's domain), not the client (sending agent). IFP-5 signatures provide sender authentication.
- **Rate limiting is essential** to prevent denial-of-service. Without rate limiting, a malicious agent could flood an inbox with messages, consuming the receiving agent's LLM inference budget.
- **Message size limits** prevent resource exhaustion from oversized payloads.

## Interoperability Considerations

- Agents that do not support IFP-6 can still exchange messages through other transports (email, shared document stores, IFP-8 relays). IFP-6 is one transport option, not the only one.
- The `/.well-known/iface/` path convention follows the pattern established by RFC 8615 (Well-Known URIs).
- HTTP/2 and HTTP/3 are acceptable; the protocol does not depend on HTTP version.

## Design Rationale

IFP-6 is deliberately minimal. It defines:

- Where to send messages (endpoint convention)
- What to send (IFP-4 JSON)
- What to expect back (status codes)
- What to do when things go wrong (retry, rate limiting)

It does not define message queuing, webhook registration, subscription management, or other features that might be needed in the future. These can be added in supplementary IFPs without changing the core transport.

The SMTP analogy (RFC 5321) is informative: SMTP defines message transfer between mail servers but does not define message format (that's RFC 5322) or message security (that's DKIM/SPF). Similarly, IFP-6 defines message transfer but delegates format to IFP-4 and security to IFP-5.

## References

- RFC 5321 -- Simple Mail Transfer Protocol (architectural analogue)
- RFC 8615 -- Well-Known Uniform Resource Identifiers
- IFP-4 -- Structured Message Representation
- IFP-5 -- Identity and Message Signing

## Acknowledgments

The HTTPS transport approach was outlined in a conversation between Peter Kaminski and ChatGPT in February 2026 (archived in the inter-face-bootstrap repository).

---

*This is IFP-6, Draft status. It will be revised as the first agent implementations test delivery in practice.*
