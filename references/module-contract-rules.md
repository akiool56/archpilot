# Module Contract Rules

## Purpose

Module responsibility design is the core value of this skill.

## Required contract format

Every core module must include:

### Module: [module name]

**Responsibility**  
What this module owns.

**Non-responsibility**  
What this module must not do.

**Input**  
Data received by this module.

**Output**  
Data returned by this module.

**Public interface**  
Functions, methods, components, or API routes exposed to other modules.

**Hidden internals**  
Implementation details that should not leak outside this module.

**Dependencies**  
Other modules it may depend on.

**Extension points**  
Future features that can be added here without rewriting unrelated modules.

**Run/test focus**  
How to verify this module works.

## Required modules by default

For AI text/file analysis web tools, consider:

1. Page/AppShell
2. InputPanel
3. FileUpload/FileParser when file input exists
4. ValidationService
5. AnalysisOrchestrator
6. PromptBuilder
7. AIClient
8. ResultParser
9. ResultPanel
10. ExportService
11. ConfigService
12. ErrorPresenter
13. I18n/LanguageService when global switching is selected
14. StorageService when saving data is selected
15. HistoryService when history is selected or reserved

## Anti-patterns

Do not allow:

- `page.tsx` calling LLM provider directly
- UI component concatenating full prompt
- AI client returning hardcoded fake result
- export code inside result component
- file parser calling model directly
- one module owning input, prompt, AI call, parsing, rendering, and export
