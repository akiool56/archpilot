# Real LLM Integration Rules

Do not use default mock-result mode.

Not allowed: hardcoded fake analysis, fake API route pretending to be model output, sample JSON returned as real output, “LLM later” as default runtime behavior, random result generation, mock mode enabled by default.

Allowed: empty state, loading state, error state, missing API key message, UI skeleton with no fake results, schema examples clearly labeled as examples.

Default deployable config: server-side env vars like `MODEL_PROVIDER`, `MODEL_NAME`, `MODEL_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`. Frontend calls backend. Backend calls provider. Do not expose deployable keys in frontend.
