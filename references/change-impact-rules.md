# Change Impact Rules

The final design package must include **后续功能变更影响说明**.

For each likely future feature, state:

1. what modules will change
2. what modules should not change
3. what interfaces should be extended
4. what data structures may be added
5. why current v1 design can support it

## Common future features

### Login

Will change: AuthService/UserService, StorageService, API route middleware.  
Should not change: PromptBuilder, AIClient core call logic, ResultParser, ExportService core logic.  
Reserved interfaces: `getCurrentUser()`, `userId?: string`, `saveUserHistory(userId, result)`.

### History

Will change: StorageService, HistoryService, ResultPanel history entry point.  
Should not change: PromptBuilder, AIClient, FileParser.  
Reserved interfaces: `saveAnalysisRecord(record)`, `listAnalysisRecords(filter)`.

### PDF/DOCX export

Will change: ExportService, export format UI controls.  
Should not change: AIClient, PromptBuilder, ResultParser core schema unless export requires extra fields.  
Reserved interfaces: `exportAsMarkdown(result)`, `exportAsPdf(result)`, `exportAsDocx(result)`.

### Model switching

Will change: ConfigService, AIClient provider adapter, optional UI selector.  
Should not change: page layout, PromptBuilder domain logic, ResultPanel if schema remains same.  
Reserved interfaces: `ModelProvider`, `ModelConfig`, `callModel(provider, request)`.

### Batch processing

Will change: AnalysisOrchestrator, queue/batch handler, progress UI, result aggregation.  
Should not change: single-item PromptBuilder, single-item ResultParser, AIClient provider interface.  
Reserved interfaces: `analyzeOne(input)`, `analyzeBatch(inputs)`, `BatchResult`.
