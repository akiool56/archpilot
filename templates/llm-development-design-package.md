# 《AI 编程项目 LLM 开发设计包》

## 1. 项目定位

[把用户人话需求转成准确项目定义]

## 2. 需求理解与合理假设

### 用户明确说了什么
1. [fact]

### 用户没说清楚什么
1. [unknown]

### 当前合理假设
1. [assumption]

### 假设对架构的影响
1. [impact]

## 3. MVP 功能边界

### 第一版必须做
1. [feature]

### 第二版再做
1. [feature]

### 暂时不做
1. [feature]

## 4. 用户流程

1. [step]
2. [step]
3. [step]

## 5. 界面语言与 UI 设计规范

### 界面语言
[Chinese / English / global switch]

### UI 风格
[style]

### 主色调
[color]

### 页面结构
1. [header]
2. [input area]
3. [result area]
4. [action area]
5. [empty/loading/error states]

## 6. 责任完整但不过度复杂的架构说明

### 已覆盖的应用责任
1. 页面/UI 层
2. 用户输入层
3. 校验层
4. 业务流程编排层
5. Prompt 管理层
6. 真实 LLM 调用层
7. 结果解析层
8. 数据结构层
9. 文件处理层
10. 结果展示层
11. 导出/复制层
12. 错误处理层
13. 配置管理层
14. UI 语言/风格层
15. 后续扩展接口层
16. 试运行与验证层

### 明确不引入的复杂设计
1. 微服务
2. 消息队列
3. 复杂 DDD
4. 多租户权限
5. 企业 SSO
6. 完整支付系统
7. 插件市场
8. 无用抽象基类

### 架构原则
使用模块化单体：一个项目仓库，一个应用，内部模块边界清晰。

## 7. 推荐技术栈

### 主方案
[stack]

### 选择原因
1. [reason]

### 备选方案
[fallback]

## 8. 模块职责设计

Every module must use this exact format.

### Module: [module name]

**Responsibility**
1. [what it owns]

**Non-responsibility**
1. [what it must not do]

**Input**
1. [input]

**Output**
1. [output]

**Public interface**
1. [method/interface]

**Hidden internals**
1. [internal detail]

**Dependencies**
1. [dependency]

**Extension points**
1. [future extension]

**Run/test focus**
1. [how to verify]

## 9. 数据结构设计

### [TypeName]
Fields:
1. [field]: [meaning]

Used by:
1. [module]

## 10. 接口与扩展点设计

### 第一版实现
1. [interface]

### 后续预留
1. [interface]

### 预留但不实现的原因
1. [reason]

## 11. 后续功能变更影响说明

### 如果未来增加 [feature]

需要改：
1. [module]

不应该改：
1. [module]

需要新增/扩展的数据结构：
1. [type]

当前预留接口：
1. [interface]

## 12. 目录结构

```text
project-name/
├── app/
├── components/
├── lib/
│   ├── aiClient.ts
│   ├── promptBuilder.ts
│   ├── resultParser.ts
│   ├── exportService.ts
│   ├── validators.ts
│   ├── config.ts
│   └── i18n.ts
├── types/
├── prompts/
└── docs/
```

## 13. 分阶段开发顺序

For each phase:

### Phase [n]: [name]
目标：[goal]
修改文件：[file]
不要做：[forbidden]
验收标准：[criterion]
试运行：[command]

## 14. 给 LLM 编程工具的提示词

Include master prompt, staged prompts, and final self-check prompt.

Use `templates/stage-prompt.md`.

## 15. 架构与代码自检清单

1. 是否高内聚？
2. 是否低耦合？
3. 是否每个模块都有明确输入/输出？
4. 是否存在一个文件做太多事？
5. 是否把 Prompt 拼接写进页面？
6. 是否把 API Key 暴露到前端？
7. 是否引入无用依赖？
8. 是否有 Mock 假结果？
9. 是否保留合理扩展点？
10. 是否没有过度设计？
11. 是否每阶段能试运行？
12. 是否能直接交给 LLM 分阶段开发？
