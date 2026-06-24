# Run Check Policy

Every implementation stage must be run or checked before moving to the next stage.

Report commands executed, pass/fail, errors, fixes, and ready/not ready.

Next.js: `npm run build`, `npm run lint`, `npm run dev`. If lint unavailable, at least build.

Python/FastAPI: `python -m compileall .`, `pytest`, `uvicorn app.main:app --reload`.

Streamlit: `streamlit run app.py`.

If API key is missing, report clearly and do not fake success.
