# ArchPilot Smoke Test Prompts

# Smoke Test Prompts

## Test 1
```text
请使用 archpilot skill。我想做一个 AI 简历改写工具。
```
Expected: classify internally and ask only one question.

## Test 2
```text
请使用 archpilot skill。我想做一个合同风险分析工具，第一版要简单但架构别乱。
```
Expected: final design includes 责任完整但不过度复杂的架构说明.

## Test 3
```text
请使用 archpilot skill。生成最终设计包时，每个模块都要写清楚职责、非职责、输入、输出和接口。
```
Expected: every module uses detailed contract format.

## Test 4
```text
请使用 archpilot skill。我想做给中国用户用的 AI 文档总结网站。
```
Expected: recommend Chinese UI and collect UI style/color.

## Test 5
```text
请使用 archpilot skill。分阶段编码提示词不要 Mock，每阶段都要试运行。
```
Expected: real LLM path, no mock, run commands and report format.
