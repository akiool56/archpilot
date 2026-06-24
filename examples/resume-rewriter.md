# Example: AI Resume Rewriter

Input: 我想做一个 AI 简历改写工具。

Correct first response: classify internally as AI resume rewriting / JD matching tool, then ask only one question:

这个项目主要用途是什么？

A. 自己练手，先跑通核心功能  
B. 作品集项目，要能展示给别人看  
C. 接单/交付项目，需要稳定和可维护  
D. 商业化 MVP，后续可能加登录、支付、历史记录  
E. 内部工具，给团队或公司内部使用  

Architecture highlights: page/UI, ResumeInput, JdInput, ValidationService, PromptBuilder, AIClient, ResultParser, ResultPanel, ExportService, ConfigService, ErrorPresenter, extension points.

Do not include login/payment/admin/microservices/database in v1 unless confirmed.
