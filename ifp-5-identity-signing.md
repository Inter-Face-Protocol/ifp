# IFP-5: Identity and Message Signing

**IFP:** 5
**Title:** Identity and Message Signing
**Class:** Core
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Opus 4.6)
**Created:** 2026-03-04
**Dependencies:** IFP-1, IFP-2, IFP-4
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines how Inter-Face agents identify themselves and how messages are authenticated. It establishes the identity model, message signing conventions, and verification procedures that form the trust foundation for agent communication.

## Motivation

Without identity and authentication, agents cannot distinguish legitimate peers from imposters, and humans cannot verify that messages attributed to a friend's agent were actually sent by that agent.

IFP-3 notes that "the receiving agent must be able to identify the sender and verify the message was not tampered with in transit." This IFP provides the conventions for doing so.

Per IFP-1 Section 6.2 (progressive authentication), the identity system supports multiple authentication levels corresponding to different trust depths. A first gossip exchange does not require the same authentication strength as a hot collaboration.

## 1. Agent Identity Model

An Inter-Face agent identity consists of:

- **A stable identifier** -- a string that uniquely identifies the agent across exchanges.
- **One or more public keys** -- used for message signing and optional encryption.
- **A display name** -- a human-readable label for audit log readability.

### 1.1 Identifier Formats

This IFP supports three identifier formats, in order of increasing formality:

| Format | Example | Use case |
| ------ | ------- | -------- |
| Simple name | `pete-agent` | Early experimentation, human-readable |
| URL | `https://pete.example/.well-known/iface` | Web-based agents with HTTPS endpoints |
| DID | `did:key:z6Mk...` | Decentralized, self-sovereign identity |

Agents SHOULD use a URL or DID identifier for production use. Simple names are acceptable during early experimentation but provide no cryptographic identity guarantees.

### 1.2 Agent Identity Document

An agent MAY publish an identity document at its well-known URL:

```
GET /.well-known/iface/identity
```

The identity document is a JSON object:

```json
{
  "ifp": 5,
  "agent_id": "https://pete.example/.well-known/iface",
  "display": "Pete's agent",
  "keys": [
    {
      "key_id": "key-1",
      "type": "ed25519",
      "public_key": "base64url...",
      "created": "2026-03-01T00:00:00Z",
      "status": "active"
    }
  ],
  "endpoints": {
    "inbox": "https://pete.example/.well-known/iface/inbox",
    "capabilities": "https://pete.example/.well-known/iface/capabilities"
  }
}
```

## 2. Authentication Levels

Per IFP-1 Section 6.2 (progressive authentication), Inter-Face supports escalating levels of authentication that correspond to the temperature model:

| Level | Name | Mechanism | Typical use |
| ----- | ---- | --------- | ----------- |
| 0 | Introduction | Shared secret or introduction token from the humans | First contact between agents |
| 1 | Signed | Message signatures using public keys | Cool gossip exchanges |
| 2 | Verified | Key verified via identity document or out-of-band confirmation | Warm collaboration |
| 3 | Bound | Key bound to a DID or other externally verifiable identity | Hot collaboration, sensitive exchanges |

Agents SHOULD negotiate authentication level during the greeting phase. The required level for a given exchange depends on the disclosure tier and temperature.

A new connection MAY start at Level 0 and escalate. Agents MUST NOT downgrade authentication level within a conversation without explicit renegotiation.

## 3. Message Signing

Message signing uses the IFP-4 structured representation. Signatures are computed over the canonical form of the message (see IFP-4, Section 3).

### 3.1 What is Signed

A signature covers:

- **Specified header fields** -- listed in the signature's `signed_headers` array. At minimum, agents SHOULD sign: `message_id`, `date`, `from`, `to`, `conversation_id`, `sequence`, `phase`, `content_type`.
- **The body** -- when `signed_body` is `true`, the signature covers `body.text` and `body.parts[]`.

Fields not listed in `signed_headers` are not integrity-protected by that signature.

### 3.2 Signature Structure

Signatures are carried in the `security.signatures` array of the IFP-4 message:

```json
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
```

- `alg` -- The signing algorithm.
- `key_id` -- Identifies the key used, in the form `agent_id#key_name`.
- `created` -- When the signature was created.
- `signed_headers` -- Which header fields are covered.
- `signed_body` -- Whether the body is covered.
- `sig` -- The signature value, base64url-encoded.

### 3.3 Signing Procedure

1. Construct the canonical form of the message per IFP-4 Section 3.
2. Extract the values of the fields listed in `signed_headers`, in the order listed.
3. If `signed_body` is true, include the canonical form of the body.
4. Concatenate the extracted values into a signing input.
5. Sign the input using the specified algorithm and key.
6. Encode the signature as base64url and place it in the `sig` field.

### 3.4 Supported Algorithms

This IFP defines the following algorithms:

| Algorithm | Identifier | Key type | Notes |
| --------- | ---------- | -------- | ----- |
| Ed25519 | `ed25519` | Ed25519 public key | Recommended default |
| HMAC-SHA256 | `hmac-sha256` | Shared secret | For Level 0 (introduction) only |

Additional algorithms MAY be defined in future IFPs. Agents SHOULD support Ed25519 at minimum.

HMAC-SHA256 is included for Level 0 authentication, where two agents share an introduction token provided by their humans. It MUST NOT be used for Level 1 or above.

## 4. Verification

### 4.1 Verification Procedure

1. Extract the signature from `security.signatures[]`.
2. Look up the signing key using `key_id` (via the sender's identity document, or a cached key).
3. Reconstruct the signing input from the specified `signed_headers` and body.
4. Verify the signature against the signing input using the specified algorithm.
5. If verification fails, reject the message and respond with an `error` phase message.

### 4.2 Replay Protection

Agents MUST track `message_id` values to detect replayed messages. A message with a previously seen `message_id` SHOULD be rejected.

Agents MAY also check that:

- The `date` field is within an acceptable time window (e.g., 24 hours).
- The `sequence` number is consistent with the conversation state.

### 4.3 Key Lookup

When verifying a signature, the agent needs the signer's public key. Key lookup may proceed through:

1. **Cached keys** from previous exchanges.
2. **Identity document** fetched from the sender's well-known URL.
3. **DID resolution** if the agent_id is a DID.
4. **Out-of-band exchange** (e.g., the humans shared the key directly).

If the key cannot be found, the agent SHOULD respond with an error explaining the situation rather than silently dropping the message.

## 5. Key Management

### 5.1 Key Rotation

Agents SHOULD support key rotation. When rotating keys:

1. Add the new key to the identity document with status `active`.
2. Change the old key's status to `retired` (with a `retired_date` field).
3. Continue to accept signatures made with the old key for a transition period.
4. After the transition period, change the old key's status to `revoked`.

### 5.2 Key Revocation

A revoked key MUST NOT be accepted for new signatures. If a message arrives signed with a revoked key, the agent SHOULD respond with an error explaining that the key has been revoked.

## 6. Optional Encryption

This IFP defines a minimal encryption model for messages that require confidentiality. Encryption is OPTIONAL.

```json
"encryption": {
  "scheme": "sealed_box",
  "recipients": ["alice-agent"]
}
```

When a message is encrypted:

- The `body` section is replaced with the encrypted ciphertext.
- The `headers` remain in plaintext (to allow routing and trace).
- The `security.encryption` section describes the scheme and recipients.

Encryption details (key exchange, algorithms, sealed box construction) are deliberately underspecified in this draft. A future revision or supplementary IFP will define concrete encryption schemes once the signing infrastructure is established and tested.

## Threat Model

### Threats addressed

- **Spoofing.** Message signing prevents an attacker from forging messages that appear to come from a legitimate agent.
- **Tampering.** Signatures detect modification of signed header fields and body.
- **Replay.** Message ID tracking and timestamp checking detect replayed messages.

### Threats partially addressed

- **Key compromise.** Key rotation limits the damage window, but a compromised key allows impersonation until the compromise is detected.
- **Metadata exposure.** Headers are not encrypted by default. An observer can see who is communicating, when, and at what phase, even if the body is encrypted.

### Threats not addressed

- **Malicious agent.** This protocol does not prevent an agent from deliberately misrepresenting its human's intentions. Trust in the agent is ultimately trust in its implementation and its human's oversight.
- **Compromised infrastructure.** If the agent's hosting environment is compromised, all keys and messages are exposed. This is an operational concern, not a protocol concern.

## Security Considerations

- Ed25519 is recommended as the default signing algorithm because it provides strong security with small key and signature sizes, and has wide library support.
- HMAC-SHA256 (Level 0) provides weaker guarantees than public-key signatures because the shared secret must be known to both parties. It is intended only for bootstrapping new relationships and MUST NOT be used for ongoing communication.
- Agents SHOULD validate the `date` field to prevent acceptance of very old messages, even if the signature is valid.
- The signing input construction (Section 3.3) must be implemented identically by signer and verifier. Interoperability testing is essential.

## Interoperability Considerations

- Agents that do not implement IFP-5 can still participate in the ecosystem at reduced trust. Other agents SHOULD treat unsigned messages as unauthenticated and limit the disclosure tier accordingly.
- Authentication level negotiation happens during the greeting phase of IFP-3. If two agents cannot agree on a sufficient authentication level, they SHOULD explain the mismatch in an error message rather than silently proceeding at an inadequate level.

## References

- RFC 6376 -- DomainKeys Identified Mail (DKIM) Signatures
- RFC 8785 -- JSON Canonicalization Scheme (JCS)
- RFC 8032 -- Edwards-Curve Digital Signature Algorithm (Ed25519)
- IFP-1 -- Philosophy and Design Principles (Section 6.2: Progressive authentication)
- IFP-4 -- Structured Message Representation (Section 3: Canonicalization)

## Acknowledgments

The progressive authentication model was developed during a conversation between Peter Kaminski and Claude (Opus 4.6) on 2026-03-04, building on the progressive trust principle from the Inter-Face manifesto. The DKIM-like signature structure was proposed in a conversation between Peter Kaminski and ChatGPT in February 2026.

---

*This is IFP-5, Draft status. Cryptographic algorithm choices and encryption details will be refined as implementation experience develops.*
