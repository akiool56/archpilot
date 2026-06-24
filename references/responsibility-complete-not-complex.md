# Responsibility Complete, Not Technically Complex

## Core principle

**责任完整，不是技术复杂。**

For beginners, architecture must be complete enough to prevent code chaos, but simple enough to build.

## Required responsibility coverage

The architecture must explicitly cover:

1. Page/UI layer: layout, visible interaction, UI language, UI style, empty/loading/error states.
2. User input layer: input fields, upload controls, user action triggers.
3. Validation layer: empty input, file type, file size, required fields, sensitive-data warnings.
4. Business flow orchestration layer: validation → prompt → LLM → parsing → response.
5. Prompt management layer: prompt templates, variable filling, output schema instructions.
6. Real LLM provider call layer: server-side config, provider calls, provider error mapping.
7. Result parsing layer: raw model output → structured result.
8. Data structure/type layer: UserInput, AnalyzeRequest, AnalyzeResult, FileMeta, ExportResult, ErrorState, AppConfig.
9. File processing layer: file reading, text extraction, file constraints.
10. Result display layer: result hierarchy, sections, copy/export trigger.
11. Export/copy layer: copy Markdown, export Markdown/CSV, future PDF/DOCX.
12. Error handling layer: validation failure, missing API key, provider failure, parse failure.
13. Configuration layer: env vars, model provider, model name, feature flags.
14. UI language and style layer: Chinese/English/i18n, style/color consistency.
15. Extension point layer: login, history, model switching, export formats, batch jobs.
16. Run-check and verification layer: build/lint/dev/test commands and pass/fail reports.

## What counts as overcomplexity

Avoid by default:

- microservices
- message queues
- distributed jobs
- complex DDD
- CQRS/event sourcing
- plugin architecture
- multi-tenant permission system
- enterprise SSO
- full payment subsystem
- excessive base classes
- generic framework wrappers
- unused abstraction layers
- dependencies without clear need

## Correct implementation philosophy

Use a modular monolith:

- one repository
- one app
- simple deployment
- clear internal modules
- explicit contracts
- no fake complexity
- no one-file chaos

## Required final section

The final design package must include **责任完整但不过度复杂的架构说明**, explaining responsibilities covered, enterprise features excluded, why modular monolith is enough, and which future capabilities are reserved through interfaces.
