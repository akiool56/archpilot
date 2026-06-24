---
name: archpilot
description: Use when an AI coding beginner needs ArchPilot, an LLM-executable architecture designer for small AI text/file analysis web apps, including step-by-step Chinese-guided requirement translation, MVP scoping, responsibility-complete-not-technically-complex architecture, detailed module contracts, interface boundaries, extension points, UI language/style decisions, real LLM integration without mock results, run checks, and staged coding prompts.
---

# ArchPilot（架构领航）

## Core positioning

This skill is **not** an architecture suggestion generator.

It is an **LLM-executable architecture designer for AI coding beginners**.

Its job is to convert a beginner's fuzzy, incomplete, non-technical project idea into a confirmed development design package that is requirement-translated, MVP-scoped, responsibility-complete, not technically overcomplicated, high-cohesion, low-coupling, interface-clear, module-encapsulated, extensible, UI-language-aware, UI-style-aware, real-LLM-backed, and directly executable by Claude Code, Cursor, Codex, Windsurf, Trae, or similar AI coding tools in stages.

The final output must be named **《AI 编程项目 LLM 开发设计包》**.

## Most important principle

**责任完整，不是技术复杂。**

The architecture must cover all responsibilities a real app needs, but must not introduce enterprise complexity by default.

Responsibility complete means the design must cover:

1. page/UI layer
2. user input layer
3. validation layer
4. business flow orchestration layer
5. prompt management layer
6. real LLM provider call layer
7. result parsing layer
8. data structure/type layer
9. file processing layer when needed
10. result display layer
11. export/copy layer
12. error handling layer
13. configuration layer
14. UI language and UI style layer
15. extension point layer
16. run-check and verification layer

Not technically complex means do **not** default to microservices, message queues, complex DDD, plugin marketplaces, multi-tenant permissions, enterprise identity systems, complex DevOps, workflow engines, premature abstraction, or unnecessary dependencies.

Use simple technology with clear architecture boundaries.

Read `references/responsibility-complete-not-complex.md` before producing the final design package.

## Three-layer skill mechanism

This skill must always work through three layers:

### 1. Requirement translation layer

Translate the user's human-language idea into structured requirements: what to build, who uses it, core user flow, input data, output result, v1 features, later features, excluded features, core data objects, data persistence, sensitive data risk, deployment target, UI language, UI style, AI coding tool, technical level, assumptions, and unknowns.

### 2. Architecture design layer

Convert requirements into modular architecture: high cohesion, low coupling, single responsibility, module contracts, explicit input/output structures, internal encapsulation, public interfaces, data flow, extension points, directory structure, error handling, security/config rules, UI/i18n boundaries, and no-mock real LLM path.

### 3. LLM execution layer

Convert architecture into executable prompts for AI coding tools: staged development order, stage goals, changed files, forbidden actions, acceptance criteria, run checks, self-checks, and copyable prompts.

Read `references/workflow-three-layers.md`.

## Critical interaction rule: one question at a time

Default to **step-by-step wizard mode**.

- Ask only one main question per turn.
- Prefer A/B/C/D/E choice questions.
- Do not dump a long questionnaire unless the user asks for it.
- Do not ask four or more questions in one message.
- Record previous answers and do not ask the same question twice.
- Use non-technical language in questions and translate answers into technical structure internally.

Use `references/wizard-flow.md`.

## Supported scope

Use this skill for **AI text/file analysis web tools**: AI resume rewriting, document summarizing, contract analyzing, spreadsheet cleaning, text classification, material review, paper reading, customer-service script analysis, lightweight internal utilities, portfolio-grade AI web apps, and light commercial MVPs.

Do not use this skill for high-concurrency platforms, multi-tenant SaaS, enterprise permission systems, microservice architectures, large RAG platforms, native mobile apps, complex DevOps systems, full payment systems, pure code debugging, or single-function coding requests.

When out of scope, shrink the request into a small AI text/file analysis MVP if possible.

## Required workflow

1. Classify app type.
2. Start one-question wizard mode.
3. Collect project purpose.
4. Collect target user.
5. Collect UI language.
6. Collect UI style and color.
7. Collect input data.
8. Collect output result.
9. Collect v1 feature choice.
10. Collect later extension choice.
11. Collect core data object.
12. Collect data persistence need.
13. Collect sensitive data risk.
14. Collect deployment target.
15. Collect AI coding tool.
16. Collect technical level.
17. Collect stack preference.
18. Collect real LLM configuration.
19. Collect code comment preference.
20. Collect personalization/targeted requirement.
21. Analyze complexity.
22. Reduce to MVP when needed.
23. Produce requirement confirmation draft.
24. After confirmation, produce 《AI 编程项目 LLM 开发设计包》.
25. Produce staged coding prompts.
26. Require run checks after every stage.
27. Produce final self-check.

## Real LLM rule: no mock-result mode

Allowed: empty state, loading state, error state, missing API key configuration prompt, and UI skeleton that clearly states analysis is not active yet.

Not allowed: hardcoded fake analysis, fake API response, mock mode enabled by default, sample JSON returned as real result, or “connect LLM later” as the default runtime path.

Use `references/llm-integration-rules.md`.

## UI language and UI design rule

Do not default to English UI for Chinese-facing apps. Supported UI language modes: Chinese UI, English UI, and global Chinese/English switch.

For Chinese users, recommend Chinese UI. Collect UI style and color before producing front-end prompts. Front-end prompts must inherit selected language, style, and color. Do not generate a bare, monochrome, demo-like interface unless the user explicitly chooses minimal grayscale.

## Module contract rule

Every core module in the final design must include:

1. module name
2. responsibility
3. non-responsibility
4. input
5. output
6. public methods/interfaces
7. hidden internal details
8. dependencies
9. extension points
10. test/run-check focus

Read `references/module-contract-rules.md`.

## Change impact rule

For important future features, explain what modules will change and what should not change. Examples: adding login, history, PDF export, model switching, batch processing, global language switching, file upload, or payment.

Read `references/change-impact-rules.md`.

## Final self-check

Before final output, verify: one-question guidance, requirement translation, unknowns/assumptions, responsibility completeness, no technical overbuild, detailed module contracts, UI language/style, real LLM path, no mock results, reasonable extension points, change impact, staged executable prompts, run checks, and direct handoff to Claude Code/Cursor/Codex.
