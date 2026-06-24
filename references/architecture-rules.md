# Architecture Rules

Core rules: modular monolith, high cohesion, low coupling, explicit contracts, simple implementation, no fake enterprise complexity, no mock runtime analysis, real LLM path, UI language/style respected, stage run checks required.

Every core module must define input, output, public method, hidden internals, and extension points.

Reserve only likely future features: model switching, prompt templates, file parser expansion, export formats, history, login, batch jobs, i18n, analytics, admin dashboard.

Coding constraints: do not put business logic inside UI, do not build prompts inside page components, do not expose API keys, do not add login/payment/database unless confirmed, do not over-abstract, do not add unnecessary dependencies, do not proceed if run checks fail.
