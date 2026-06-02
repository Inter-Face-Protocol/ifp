# IFP-19: Liveness and Heartbeats

**IFP:** 19
**Title:** Liveness and Heartbeats
**Class:** Informational
**Status:** Draft
**Authors:** Peter Kaminski · Freya (Pete's agent) · Sophia (the nameless one's agent) · the nameless one
**Created:** 2026-05-29
**Revised:** 2026-05-31
**Dependencies:** IFP-1, IFP-2, IFP-3, IFP-17
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

IFP-3 specifies how agents exchange messages but not how an agent *notices* that a message has arrived. For agents that exist only when invoked — most current implementations — there is no in-process loop that can wake to inbound work. Some external mechanism must check the channel on a schedule and surface findings to the agent or its principal.

This IFP defines minimal conventions for **liveness**: how an external mechanism (a *heartbeat*) wakes a check on a schedule, how it discovers what has changed in a channel, how it distinguishes a quiet channel from a broken one, and how it surfaces findings to the principal. It also defines how a foreground session communicates the desired heartbeat cadence to the heartbeat itself.

The IFP is implementation-agnostic at the OS layer (cron, launchd, systemd timers, scheduled cloud functions, etc.) and transport-agnostic at the channel layer (it works for any IFP-3 transport, including IFP-16 git and IFP-17 shared folders).

## 1. Motivation

Current IFP transports (IFP-16 git, IFP-17 shared folder) describe how messages are written and how they propagate. They do not specify how the *recipient agent* finds out a message exists.

For continuously-running agents (long-lived processes, daemon services), the recipient process can watch the transport directly — `inotify` on a folder, `git fetch` in a loop, a websocket on a server. For **session-based agents** — agents that exist only when invoked by their principal or by a scheduler — that watching must happen *outside* the agent's own existence.

IFP-17 §6.1 lists several detection options and flags this gap in its Open Questions. This IFP fills it.

A second motivation: a foreground session and a heartbeat have different needs. During active collaboration, the heartbeat should run often (minutes). When the channel is dormant, frequent ticks are waste. The foreground needs a way to *signal* the desired cadence to the heartbeat without modifying the heartbeat's code or restarting it.

## 2. Prior Work

The term "heartbeat" is used broadly in distributed systems; this IFP does not invent it. The reference implementations behind this draft are:

- **Pete's cron-based heartbeat** for Freya: macOS cron invokes a shell wrapper every 15 minutes, which sources a long-lived `CLAUDE_CODE_OAUTH_TOKEN` for headless `claude` and runs a scout-class invocation with a focused prompt.
- **Sophia's launchd-based heartbeat** (implemented 2026-05-31): macOS `launchd` fires a frequent base tick; a wrapper gates the real run on a cadence tier written by the foreground into `heartbeat-state.json`, sources a long-lived token for headless `claude`, and reads the channel from a local Drive-sync mount.

Both are documented in §6 Reference Implementations. Neither is canonical; the spec is written from the seams between them.

An earlier draft of this IFP reused **IFP-1's thermal temperature vocabulary** (cool / warm / hot) for cadence tiers. That coupling was dropped to avoid conflating two independent dimensions: IFP-1 describes a *relationship's* activity; this IFP describes a *poller's* tempo. A warm relationship may be polled slowly (a weekly correspondence is warm but checked daily); a cool channel may need a temporarily fast heartbeat when a single critical reply is expected. The vocabularies are kept separate on purpose.

## 3. Concept

A **heartbeat** is:

- An external mechanism that wakes a *check* on a schedule.
- A scout-class invocation: lightweight, narrowly-scoped, fast, cheap.
- A poller of one or more IFP-3 channels and any related local state (inbox directories, due tasks, etc.).
- A classifier that decides whether what it found is principal-actionable.
- A surfacing mechanism that routes findings to the principal at appropriate urgency.
- A self-stamping component: it records that *it ran*, so a downstream observer can distinguish a quiet channel from a broken-sync channel.

A heartbeat is **not**:

- A long-running daemon. Each tick is a fresh invocation; state lives in files.
- A replacement for in-session intelligence. Findings are classified for *triage*, not acted on substantively.
- A push-notification system. Surfacing is a separate concern this spec touches but does not fully define.

## 4. Cadence — the heartbeat-state file

The foreground session writes a small state file (suggested name: `heartbeat-state.json`) that the heartbeat reads on each tick to determine its own cadence. The file MAY include other fields, but at minimum:

```json
{
  "cadence": "normal",
  "set_at": "2026-05-29T21:00:00Z",
  "set_by": "freya-foreground-session"
}
```

Cadence tiers (suggested mappings; implementations choose literal intervals):

- **`slow`** — daily or longer. The channel is dormant; the heartbeat checks for changes infrequently to avoid waste.
- **`normal`** — every 10–30 minutes (implementations choose). Active collaboration; the human expects responses on the timescale of a coffee.
- **`fast`** — every 1–5 minutes. Live working session; the human is waiting for the next exchange.

The foreground session moves to `fast` when it begins active work and back to `normal` or `slow` when work concludes. The heartbeat respects whatever the foreground last wrote.

A heartbeat MUST NOT modify the cadence field from its own tick (one source of truth: the foreground). A heartbeat MAY produce a *recommendation* to change cadence, surfaced to the principal, but the foreground is the authority on the literal value.

(Open question: should a heartbeat automatically slow itself if the foreground hasn't updated `set_at` in N days? Probably yes, but the rule belongs in §9.)

## 5. Quiet vs. broken-sync

A silent channel can mean two very different things:

1. **Quiet:** no one has sent a message lately. Expected.
2. **Broken sync:** the transport is failing, the heartbeat itself didn't run, or the polling mechanism is misconfigured. Not expected.

This IFP defines a minimum distinction:

- Every heartbeat tick MUST stamp its own "ran at T" timestamp in a known location, recorded **independently of the agent invocation** so that an agent-side failure (auth, crash) still leaves evidence the tick fired.
- A reader observing a quiet channel can check that timestamp: a fresh stamp + reachable transport + no new messages = genuinely quiet. A stale stamp or transport errors = a different alarm.
- Implementations SHOULD route the two alarms differently. Conflating them lets a dead channel masquerade as a calm one.

## 6. Reference Implementations

This section is informative, not normative. Two implementations are sketched so readers can see the seam shapes.

### 6.1 cron-based heartbeat (Pete + Freya)

- **Trigger:** macOS `cron`, every 15 minutes. (The interval is currently fixed; this IFP's cadence model would let it become tier-driven.)
- **Authentication for headless `claude`:** a long-lived `CLAUDE_CODE_OAUTH_TOKEN` stored in a gitignored `.env`, sourced by the shell wrapper before invoking `claude`. This bypasses the interactive keychain flow.
- **Authentication for transports:** `rclone` for Google Drive (its own persistent OAuth grant, independent of the claude.ai Drive MCP connector); SSH keys for git remotes.
- **Authentication for email transports:** Fastmail via a long-lived JMAP API token in the gitignored `.env`; Gmail via the claude.ai Gmail MCP connector (OAuth grant managed by the connector, surfaced as MCP tools to the headless `claude` invocation).
- **Polling steps:** session-lock check; pre-fetched email check; git-log against named repos with `--since` windows; `rclone lsf` against the shared folder, diffed against a `seen-*-files.txt`.
- **Classification:** the scout prompt classifies "found-work" vs "no-op" and writes a brief `inbox/heartbeat-{timestamp}.md` on found-work.
- **Escalation signal:** the scout's last stdout line is `ESCALATE: <reason>` / `NO-OP` / `YIELDED`; the wrapper reads it to decide whether to wake the foreground agent.
- **Surfacing to Pete:** inbox briefings read at next interactive session; routine email summaries sent as a soft phone notification.

### 6.2 launchd-based heartbeat (Sophia) — implemented 2026-05-31

- **Trigger:** macOS `launchd` fires a frequent base tick (`StartInterval`, e.g. 300s). The wrapper gates the real run on the cadence tier (§4): most ticks are a cheap shell no-op that logs a skip; a scout-class headless `claude` runs only when the tier interval is due.
- **Authentication for headless `claude`:** a long-lived `CLAUDE_CODE_OAUTH_TOKEN` in a gitignored `.env`, sourced by the wrapper (§8). Confirmed necessary, not merely convenient — see §8.
- **Authentication for transport:** the IFP-17 shared folder is read from a local **Google Drive desktop-sync mount**, sidestepping cloud auth in the loop. Because a headless `claude` is sandboxed to its working directory, the wrapper grants access to the out-of-tree mount with `--add-dir` (§8); a pre-fetch approach (§6.1) is the alternative.
- **Polling steps:** list the channel mount; diff filenames against `last-seen.json`; archive new files to `inbox/`; judge salience; write a briefing.
- **Liveness stamp:** the wrapper records `START`/`SKIP`/exit independently of the `claude` run, so an auth or runtime failure still leaves a fired-tick trace (§5).
- **Surfacing:** routine → a digest in `briefings/`, read at next session; time-sensitive → push to the principal's phone (planned).

## 7. Surfacing to the Principal

This IFP underspecifies surfacing intentionally — the choice is principal-specific and beyond a single spec. Common patterns:

- **Briefing artifact** — the heartbeat writes a structured file (`inbox/heartbeat-{timestamp}.md`, `briefings/daily.md`) for the foreground to read.
- **Email-as-soft-notification** — a short email summary to an address the principal already monitors on their phone. Works without a custom mobile app.
- **Direct push** — Pushover, ntfy.sh, APNS via a custom app, or similar. Requires per-principal configuration.

Implementations SHOULD distinguish *urgency tiers* in surfacing — at minimum "routine" (briefing artifact) and "time-sensitive" (push or equivalent). The urgency tier of a finding is independent of the heartbeat's cadence tier.

## 8. Authentication Patterns

Both reference implementations hit the same problem: the OS-level invocation (cron, launchd) runs in a stripped environment, and any auth that normally lives in interactive keychain access is absent. Worse, the failure is often *silent* or *intermittent*.

Approaches observed:

- **Token-in-env-file.** A long-lived OAuth token (e.g. `CLAUDE_CODE_OAUTH_TOKEN`) in a gitignored `.env`, sourced by the wrapper. Works for any tool that reads a token from the environment. **This is the recommended baseline for headless agent invocation.**
  - *Minting caveat:* generating the token (e.g. `claude setup-token`) is itself an interactive flow and MUST be run in a real terminal (TTY). A piped or headless invocation yields no token.
- **Keychain auth is unreliable for unattended runs.** Observed empirically: an unattended invocation may authenticate off the OS keychain when the principal has recently been active, then fail (`HTTP 401`) hours later when the keychain is locked or unreadable from the scheduler context. Do not depend on it; prefer the env-token pattern.
- **Service-account token from a separate tool.** `rclone` maintains its own persistent OAuth grant for Drive, independent of any interactive MCP. The heartbeat shells out to it.
- **Local filesystem mount.** Mounting a shared folder via desktop sync sidesteps cloud auth entirely; the heartbeat reads files off disk.

Two host-environment constraints can block a heartbeat *before any auth is attempted*, and both are silent enough to cost a debugging day:

- **OS privacy protection of the home data directories (MUST-level caveat).** On macOS, the cron/launchd execution context is denied even *read* access to files under the protected user directories (`~/Documents`, `~/Desktop`, `~/Downloads`) unless explicitly granted Full Disk Access. A wrapper script placed there fails to open at all (e.g. `exit 127`, "can't open input file"), while the same script run from a Terminal (which holds the grant) succeeds — masking the fault. **Keep agent infrastructure outside the protected directories.**
- **Agent-runtime filesystem sandbox.** A headless agent runtime (e.g. Claude Code) may confine the invocation's filesystem access to its working directory. To poll a transport mounted elsewhere (a Drive-sync folder outside the working tree), the wrapper must explicitly widen access (e.g. `--add-dir <path>`) or use the pre-fetch pattern (the shell lists the folder and passes the result inline, so the agent needs no out-of-tree access).

This IFP does NOT mandate any one pattern. Implementations SHOULD document which they use, since the auth and access patterns shape what the heartbeat can and cannot do.

## 9. Open Questions

- **Self-slowing.** Should a heartbeat automatically drop to `slow` if the foreground hasn't updated `set_at` in N days? Suggested SHOULD: if `set_at` is older than 7 days, treat cadence as `slow` regardless of stated value.
- **Surfacing standardization.** Should this IFP define a `briefing` envelope format so heartbeats from different implementations produce inter-readable digests? (Sophia's principal leans yes.)
- **Multi-channel coordination.** When a heartbeat watches several channels, should each carry its own cadence, or one cadence across all? Implementations to date imply one cadence; reality may want per-channel. (Sophia leans per-channel.)
- **Discovery of `heartbeat-state.json`.** Where should the state file live? Suggested SHOULD: the agent's vault root or a known subdirectory, found relative to a configured path.
- **Cross-agent liveness signaling.** A more ambitious version would let agents signal their own liveness to peers (a last-seen timestamp in the IFP-3 envelope, or a channel-level `liveness:` field). Out of scope for this draft; flagged as future work.
- **Slow-tier broken-sync detection.** A daily (`slow`) heartbeat gives much coarser broken-sync detection than one running every 15 min (`normal`). What is the right SHOULD for slow-tier liveness checks of the transport itself?
- **Heartbeat-state.json schema.** Beyond `cadence`, `set_at`, `set_by`, what else? `watching:` (list of channel identifiers)? `next_check_no_earlier_than:` (explicit timing)?

## 10. Dependencies and Interop

- **IFP-1 (Philosophy):** Defines a cool / warm / hot vocabulary for *relational* temperature. This IFP deliberately uses a separate vocabulary (slow / normal / fast) for poller cadence; see §2 for the rationale.
- **IFP-3 (Message Format):** unchanged by this IFP, though a future revision MAY add an optional `liveness:` field for in-envelope last-seen stamps.
- **IFP-17 (Shared Folder Transport):** IFP-17 §6.1 raises the detection question this IFP answers; IFP-17 implementations SHOULD reference IFP-19 for the heartbeat-side conventions.
- **IFP-18 (Clubs):** a club's heartbeat shape (one per member, or a designated member's heartbeat broadcasting to the roster?) is unspecified by IFP-18 and may be addressed by a future revision of either spec.

---

*This draft is written from the seams between two reference implementations (Pete + Freya's cron heartbeat; Sophia's launchd heartbeat, implemented 2026-05-31). The §9 Open Questions are the next round of work. Proposed as a co-authored revision for the editors' review.*
