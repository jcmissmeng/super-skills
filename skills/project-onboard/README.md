# Skill Name: project-onboard

## Overview

系统化理解已有/半成品项目的技能。通过三阶段九步骤流程（探索理解 → 结构化文档化 → 架构优化），逆向梳理项目架构、功能、业务、部署等信息，产出 `docs/spec/` 下的 spec.md / design.md / tasks.md，并提供开发过程中持续更新文档的提示词模板。

## Features

* 三阶段九步骤完整流程：鸟瞰全局 → 深度探索 → 领域语言 → SDD初始化 → spec逆向 → design逆向 → tasks梳理 → 架构改进 → 验证理解
* 逆向文档化：从已有代码反向产出 docs/spec/spec.md（做什么）、docs/spec/design.md（怎么做）、docs/spec/tasks.md（还差什么）
* 持续文档更新模板：加功能、改Bug、重构、改配置、发版前全场景覆盖
* 文档一致性审计：定期检查文档与代码实现对齐

## Prerequisites & Setup

* 依赖技能：`zoom-out`、`ubiquitous-language`、`creating-sdd-directory`、`managing-spec-document`、`managing-design-document`、`managing-tasks-document`、`improve-codebase-architecture`、`grill-with-docs`
* 项目需已有代码基础（非空项目）

## Trigger Prompts & User Scenarios

- **Scenario 1: 接手已有项目**
  - User Prompt: "帮我理解这个项目" / "梳理项目架构"
  - Expected: 执行三阶段完整流程
- **Scenario 2: 补全文档**
  - User Prompt: "项目缺文档，帮我补全" / "逆向写spec和design"
  - Expected: 执行阶段二SDD逆向补全
- **Scenario 3: 持续更新文档**
  - User Prompt: "功能开发完了，更新文档" / "重构完了，更新design"
  - Expected: 按场景选择对应更新模板
- **Scenario 4: 发版前检查**
  - User Prompt: "发版前检查文档一致性"
  - Expected: 执行全量对齐检查

## Input & Output Specification

**Inputs**: 项目代码库（已有代码）

**Outputs**: 
- `docs/spec/spec.md` — 功能规格（做什么）
- `docs/spec/design.md` — 架构设计（怎么做）
- `docs/spec/tasks.md` — 任务清单（还差什么）
- `UBIQUITOUS_LANGUAGE.md` — 领域术语表

## Limitations & Known Issues

- 大型项目可能需要分模块多次执行深度探索
- 逆向文档化的准确度依赖代码质量和命名规范
- 架构改进建议需人工评估后再实施

## License

This project is licensed, please see the [LICENSE](LICENSE.txt) file for details.
