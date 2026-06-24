# ArchPilot（架构领航）

**中文 | [English](#archpilot-architecture-pilot)**

> **架构第一行，别让它变成你未来三个月重构的第一行。**

ArchPilot（架构领航）是一个面向 **AI 编程新手** 的 **引导型 LLM 可执行架构设计 Skill**。它不会替你写完全部代码然后离开，而是像一位耐心的架构导师，从第一句话开始，带你一起 **规划边界、拆解模块、建立契约、逐步迭代**——让你少走弯路、少花 token、少在「当初要是这样设计就好了」里后悔。

---

## ✨ 为什么选 ArchPilot？

### 🧭 1. 先规划，再写码

大多数项目不是写不出来，而是一开始就没想清楚。ArchPilot 把 **架构规划** 放在第一位：先理解需求、识别角色、拆分职责，再进入实现。让代码的每一行都有处可归。

### 🦮 2. 引导型交互，不是命令型生成

你不是在对一个黑箱许愿。ArchPilot 使用 **一问一答的引导式对话**，每次只给你一个 A/B/C/D/E 选择题，解释「为什么这样选」，并让你确认、调整、学习。适合正在建立工程直觉的新手开发者。

### 🌱 3. 为新手开发者设计

不需要十年架构经验，也能做出干净的项目。术语会解释，选择会给理由，复杂决策会被拆成可理解的小步骤。成长从第一次动手就开始了。

### 💰 4. 显著节省 token

通过清晰的三层机制（需求翻译层 → 架构设计层 → LLM 执行层）、固定的输入模板和模块级输出结构，ArchPilot 避免了反复生成整份代码、反复返工的浪费。花在刀刃上，而不是花在「再来一遍」上。

### 🏗️ 5. 一个优秀的初始架构，胜过十次后期重构

初始架构决定了你未来要还多少技术债。ArchPilot 强调 **「一开始就把骨架搭对」**：边界清晰、依赖明确、扩展有位置。项目越小，越值得认真设计。

### 📦 6. 独立封装模块

每个功能都被设计为 **可独立理解、独立修改、独立测试** 的模块。模块有入口、有出口、有契约。最终设计包里的每个模块都会写明：负责什么、不负责什么、输入、输出、公开接口、隐藏细节、依赖、扩展点、测试重点。

### 🔗 7. 高内聚、低耦合

ArchPilot 遵循并教授模块化设计的基本原则：相关的东西放在一起，不相关的东西通过稳定接口交互。改一处，不必翻十处。同时坚持 **「责任完整，不是技术复杂」**，覆盖真实应用所需职责，但默认不引入微服务、消息队列、复杂 DDD、多租户等企业级复杂度。

### 🔄 8. 迭代式引导

不是一次性画一张天书架构图就结束了。ArchPilot 支持 **多轮、增量、可回退** 的迭代流程：新增需求？回到规划层，分析变更影响，再落地修改。

---

## 🚀 适合谁？

- 刚入门 LLM 应用开发，想写出「像样」项目的新手
- 想培养架构思维、而不只是调 prompt 的开发者
- 讨厌重复返工、希望一开始就走在正道上的效率党
- 需要带领团队或新人统一开发语言的 Tech Lead

---

## 🛠️ 一句话定位

**ArchPilot = 你的第一个 AI 项目的正确启动方式。**

---

## 📦 安装方式

ArchPilot 是一个 Claude / Cursor 等 AI 编程工具可识别的 Skill 包。安装方式非常简单：

### 项目级安装（推荐）

将本仓库复制到你的项目目录下：

```text
your-project/.claude/skills/archpilot/
```

### 用户级安装

复制到用户目录，所有项目都能调用：

```text
~/.claude/skills/archpilot/
```

> **注意**：最终结构必须是 `~/.claude/skills/archpilot/SKILL.md`，`SKILL.md` 必须直接位于 `archpilot` 目录下，不要多套一层版本目录。

### 验证安装

进入 Skill 目录后运行：

```bash
python scripts/validate_skill.py
```

看到以下提示即表示安装成功：

```text
OK: skill package structure is valid.
```

---

## 🎯 调用方式

安装完成后，在 Claude / Cursor 等支持 Skill 调用的 AI 编程工具中，使用以下任意一种方式启动 ArchPilot：

### 推荐调用（最完整）

```text
请使用 archpilot skill。我想做一个 AI 简历改写工具。请按一步一步选择的方式，引导我确定需求、MVP、中文界面、UI风格、复杂度、模块职责、接口预留、真实 LLM 配置和分阶段编码方案。
```

### 快捷调用

```text
/archpilot 我想做一个 AI 简历改写工具。
```

或：

```text
请使用 ArchPilot（架构领航）skill。我想做一个 AI 简历改写工具。
```

### 预期行为

- 一次只问你一个选择题，像向导一样循序渐进；
- 自动把你的自然语言需求翻译成结构化需求；
- 分析复杂度，必要时帮你把范围缩小到 MVP；
- 生成一份需要你确认的需求确认草案；
- 确认后，产出 **《AI 编程项目 LLM 开发设计包》**；
- 每个模块都包含详细职责契约、接口边界、扩展点、变更影响；
- 输出可直接交给 Claude Code、Cursor、Codex、Windsurf、Trae 等 AI 编程工具分阶段执行。

---

## 📦 仓库内容

- `SKILL.md` — Skill 使用入口与核心流程
- `docs/` — 安装、命名规范、使用指南
- `references/` — 架构规则、模块契约、复杂度评估、变更影响分析等决策参考
- `templates/` — 确认草案、阶段提示、LLM 开发设计包模板
- `examples/` — 真实场景示例（合同分析器、文档摘要器、简历改写器等）
- `scripts/validate_skill.py` — Skill 结构校验脚本
- `tests/smoke-test-prompts.md` — 冒烟测试提示

---

## 📣 我们的信念

> 好的代码不是生成出来的，是**想清楚后，一步一步建出来的**。
>
> ArchPilot 陪你完成第一步，也陪你走好每一步。

---

# ArchPilot (Architecture Pilot)

**[中文](#archpilot架构领航) | English**

> **Get the architecture right from the first line, so you don't spend the next three months refactoring it.**

ArchPilot is a **guided, LLM-executable architecture design Skill** for **AI-coding beginners**. It won't write all your code and disappear. Instead, it acts like a patient architecture mentor: starting from your very first sentence, it helps you **define boundaries, break down modules, establish contracts, and iterate step by step**—so you take fewer detours, waste fewer tokens, and avoid the regret of "if only I had designed it this way from the start."

---

## ✨ Why ArchPilot?

### 🧭 1. Plan First, Code Second

Most projects don't fail because they can't be built—they fail because no one thought them through at the start. ArchPilot puts **architecture planning** first: understand requirements, identify roles, split responsibilities, then implement. Every line of code has a clear home.

### 🦮 2. Guided, Not Command-Based

You're not throwing wishes into a black box. ArchPilot uses **one-question-at-a-time guided conversations**, usually A/B/C/D/E choices, explaining *why* each choice matters and letting you confirm, adjust, and learn. Perfect for beginners building engineering intuition.

### 🌱 3. Built for Beginner Developers

You don't need ten years of architecture experience to build a clean project. Jargon is explained, choices come with reasons, and complex decisions are broken into small, understandable steps. Growth starts with your first hands-on attempt.

### 💰 4. Saves Tokens Significantly

Through a clear three-layer mechanism (Requirement Translation → Architecture Design → LLM Execution), fixed input templates, and module-level output structure, ArchPilot avoids repeatedly generating full codebases and repeatedly fixing them. Spend tokens where they matter, not on "let's try again."

### 🏗️ 5. A Great Initial Architecture Beats Ten Late Refactors

Your initial architecture determines how much technical debt you'll pay later. ArchPilot emphasizes **"get the skeleton right from the start"**: clear boundaries, explicit dependencies, and reserved extension points. The smaller the project, the more it deserves careful design.

### 📦 6. Independently Encapsulated Modules

Every feature is designed as a module that can be **understood, modified, and tested independently**. Each module has an entry, an exit, and a contract. In the final design package, every module specifies: responsibility, non-responsibility, input, output, public interface, hidden internals, dependencies, extension points, and test focus.

### 🔗 7. High Cohesion, Low Coupling

ArchPilot follows and teaches core modular design principles: related things stay together; unrelated things interact through stable interfaces. Change one place without touching ten others. At the same time, it sticks to **"responsibility complete, not technically complex"**—covering everything a real app needs without defaulting to microservices, message queues, complex DDD, multi-tenancy, or enterprise-level overengineering.

### 🔄 8. Iterative Guidance

It's not a one-time architecture diagram you never look at again. ArchPilot supports **multi-round, incremental, reversible** iteration: new requirement? Go back to the planning layer, analyze the impact, then implement the change.

---

## 🚀 Who Is It For?

- Beginners entering LLM app development who want to build projects that look "real"
- Developers who want to grow architectural thinking, not just prompt-tuning skills
- Efficiency seekers who hate rework and want to start on the right path
- Tech Leads who need a shared language for onboarding teams or newcomers

---

## 🛠️ One-Line Positioning

**ArchPilot = the right way to start your first AI project.**

---

## 📦 Installation

ArchPilot is a Skill package recognized by AI coding tools such as Claude / Cursor. Installation is simple:

### Project-Level Installation (Recommended)

Copy this repository into your project directory:

```text
your-project/.claude/skills/archpilot/
```

### User-Level Installation

Copy it to your user directory so all projects can access it:

```text
~/.claude/skills/archpilot/
```

> **Note**: The final structure must be `~/.claude/skills/archpilot/SKILL.md`. `SKILL.md` must sit **directly** under the `archpilot` directory—do not add an extra version folder layer.

### Validate Installation

Enter the Skill directory and run:

```bash
python scripts/validate_skill.py
```

A successful installation shows:

```text
OK: skill package structure is valid.
```

---

## 🎯 How to Invoke

After installation, start ArchPilot in Claude / Cursor or any Skill-supported AI coding tool using any of the following:

### Recommended Invocation (Most Complete)

```text
请使用 archpilot skill。我想做一个 AI 简历改写工具。请按一步一步选择的方式，引导我确定需求、MVP、中文界面、UI风格、复杂度、模块职责、接口预留、真实 LLM 配置和分阶段编码方案。
```

### Quick Invocation

```text
/archpilot 我想做一个 AI 简历改写工具。
```

Or:

```text
请使用 ArchPilot（架构领航）skill。我想做一个 AI 简历改写工具。
```

### Expected Behavior

- Asks one multiple-choice question at a time, like a wizard;
- Translates your natural-language idea into structured requirements;
- Analyzes complexity and narrows the scope to MVP when needed;
- Produces a requirement confirmation draft for your approval;
- After confirmation, outputs the **《AI 编程项目 LLM 开发设计包》** (LLM Development Design Package);
- Every module includes detailed responsibility contracts, interface boundaries, extension points, and change-impact analysis;
- Output can be handed directly to Claude Code, Cursor, Codex, Windsurf, Trae, or similar AI coding tools for staged execution.

---

## 📦 Repository Contents

- `SKILL.md` — Skill entry point and core workflow
- `docs/` — Installation, naming conventions, and usage guides
- `references/` — Architecture rules, module contracts, complexity rubrics, change-impact analysis, and other decision references
- `templates/` — Confirmation drafts, stage prompts, and LLM development design package templates
- `examples/` — Real-world examples (contract analyzer, document summarizer, resume rewriter, etc.)
- `scripts/validate_skill.py` — Skill structure validation script
- `tests/smoke-test-prompts.md` — Smoke-test prompts

---

## 📣 Our Belief

> Great code isn't generated—it's **built step by step, after thinking it through**.
>
> ArchPilot walks with you through the first step, and every step after.
