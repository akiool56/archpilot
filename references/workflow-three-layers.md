# Three-Layer Workflow

## Layer 1: Requirement translation layer

Convert user language into structured requirements:

1. project definition
2. target user
3. core user workflow
4. input data
5. output result
6. v1 required features
7. excluded features
8. later extension features
9. core data objects
10. data persistence strategy
11. sensitive data risk
12. deployment target
13. UI language
14. UI style
15. AI coding tool
16. technical level
17. assumptions and unknowns

Do not ask for architecture terms. Ask in plain language and translate internally.

## Layer 2: Architecture design layer

Convert structured requirements into:

1. responsibility-complete app structure
2. high-cohesion modules
3. low-coupling data flow
4. detailed module contracts
5. public interfaces
6. hidden implementation boundaries
7. data structures
8. directory structure
9. real LLM integration path
10. UI/i18n boundaries
11. configuration and secret boundaries
12. extension points
13. change impact explanation

## Layer 3: LLM execution layer

Convert architecture into:

1. master project prompt
2. staged coding prompts
3. per-stage changed files
4. forbidden actions
5. acceptance criteria
6. run-check commands
7. stage completion report format
8. stop condition if checks fail
9. final refactor/self-check prompt
