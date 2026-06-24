# Staged Coding Prompt Template

## Stage [number] prompt

Current stage goal: [Only this stage's goal]

Project background: [Short project description]

Tech stack: [stack]

AI coding tool: [Claude Code / Cursor / Codex / Windsurf / Trae]

UI language rule: [selected language rule]

UI style rule: [selected UI style and color rule]

Architecture rule: Use responsibility-complete but not technically complex architecture. Keep modules high-cohesion and low-coupling. Do not mix UI, prompt construction, LLM provider calls, result parsing, and export logic in one file.

Module contract rule: Any created core module must have a clear responsibility, non-responsibility, input, output, public interface, hidden internals, dependencies, and extension points.

Real LLM integration rule: Use a real LLM integration path. Do not implement mock mode, hardcoded fake responses, fake API responses, or sample analysis data. If API credentials are not configured, return a clear configuration error and ask for the required environment variables. Empty/loading/error states are allowed; fake analysis results are not allowed.

Need to complete:
1. [task]

Files to create or modify:
1. [file]

Do not do:
1. Do not implement unconfirmed features.
2. Do not add login, payment, admin dashboard, database, or permissions unless this stage explicitly requires it.
3. Do not put business logic inside UI components.
4. Do not build prompts inside page components.
5. Do not expose API keys in frontend code for deployable apps.
6. Do not introduce unnecessary dependencies.
7. Do not create mock runtime analysis results.
8. Do not default to English UI if Chinese UI was selected.
9. Do not generate a bare, unstyled interface.
10. Do not proceed to the next stage if run checks fail.

Acceptance criteria:
1. [criterion]

Run check requirement:

Next.js:
```bash
npm run build
npm run lint
npm run dev
```

Python/FastAPI:
```bash
python -m compileall .
pytest
uvicorn app.main:app --reload
```

Streamlit:
```bash
streamlit run app.py
```

Run check report:

### Run check result
Commands executed:
1. [command]
Result: [passed/failed]
Errors: [error or none]
Fixes applied: [fix or none]
Current stage status: Ready for next stage / Not ready, needs fix
