# Inter-Face Proposals (IFP)

**Your AI talks to your friends' AIs so you know when to talk to each other.**

This repository contains the Inter-Face Proposal (IFP) specification series -- open conventions for AI agents to communicate on behalf of their human operators.

## IFP Index

| IFP                                       | Title                                  | Class         | Status |
| ----------------------------------------- | -------------------------------------- | ------------- | ------ |
| [IFP-1](ifp-1-philosophy.md)              | Philosophy and Design Principles       | Informational | Draft  |
| [IFP-2](ifp-2-style-guide.md)             | Specification Style Guide              | Informational | Draft  |
| [IFP-3](ifp-3-message-format.md)          | Inter-Face Message Format              | Core          | Draft  |
| [IFP-4](ifp-4-structured-message.md)      | Structured Message Representation      | Core          | Draft  |
| [IFP-5](ifp-5-identity-signing.md)        | Identity and Message Signing           | Core          | Draft  |
| [IFP-6](ifp-6-https-transport.md)         | HTTPS Transport Profile                | Profile       | Draft  |
| [IFP-7](ifp-7-capability-discovery.md)    | Agent Capability Discovery             | Core          | Draft  |
| [IFP-8](ifp-8-relay-transport.md)         | Relay and Pub/Sub Transport            | Profile       | Draft  |
| [IFP-9](ifp-9-ecosystem-status.md)        | Ecosystem Status and Future Directions | Informational | Draft  |
| [IFP-10](ifp-10-agent-naming.md)          | Agent Naming Convention                | Core          | Draft  |
| [IFP-11](ifp-11-application-platforms.md) | Application Platforms                  | Informational | Draft  |
| [IFP-12](ifp-12-personas.md)              | Personas and Disclosure Tiers          | Core          | Draft  |

## Where to Start

- **[IFP-1](ifp-1-philosophy.md)** -- The philosophy and design principles behind Inter-Face. Start here.
- **[IFP-9](ifp-9-ecosystem-status.md)** -- The big picture: how the pieces fit together, what exists today, and where we're headed.
- **[IFP-11](ifp-11-application-platforms.md)** -- What you can build on Inter-Face: the application platforms that these protocols enable.

## Participating

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for how to propose, discuss, and improve IFPs.

The **[community/](community/)** directory has information about the people behind the project:
- [Vision](community/vision.md) -- Why we're doing this and what we aspire to
- [Editorial board](community/editorial-board.md) -- Who shepherds the specifications
- [Contributors](community/contributors/) -- The people building Inter-Face

## Specification Classes

| Class | Purpose |
| ----- | ------- |
| **Core** | Required protocol components for interoperable agent messaging |
| **Profile** | How a core protocol operates in a specific transport or environment |
| **Informational** | Context, design rationale, philosophy, or exploration |

## Design Workspace

The design conversations and working documents that produced the IFP series live in the [inter-face-bootstrap](https://github.com/Inter-Face-Protocol/inter-face-bootstrap) repository. That repository serves as the historical archive and ongoing design workspace.

## License

All specifications in this repository are licensed under [CC-BY 4.0](LICENSE) (Creative Commons Attribution 4.0 International).
