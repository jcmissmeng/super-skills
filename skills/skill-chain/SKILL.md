---
name: skill-chain
description: "通过指令调用预定义的技能链，按场景自动编排多个技能的协同执行顺序。Use when: (1) 用户要开发新功能/从零开始, (2) 用户要安装新技能, (3) 用户要排查Bug/调试, (4) 用户要做架构审查, (5) 用户要接手/理解已有项目, (6) 用户说'技能链'/'skill chain'/'按流程执行'/'帮我从头到尾', (7) 用户描述了一个需要多个技能协作的复杂场景。在任何需要多技能协作时主动建议使用。"
metadata:
  version: 1.0.0
---

# Skill Chain — 技能链调用

## 概述

根据用户场景，按预定义的技能链编排多个技能的执行顺序。每个技能链定义了从输入到产出的完整协作流程。

## 核心规则：技能优先级

技能链中标注的技能是推荐流程。实际执行时，如果存在功能相同的技能，按以下优先级选择：

1. **已安装的技能** > 未安装的技能（检查 skills/ 目录下是否存在对应 SKILL.md）
2. **推荐使用的技能** > 备选技能（技能链中 `/` 分隔的，左侧为推荐，右侧为备选）
3. **项目级技能** > 用户级技能

### 功能等价映射

以下技能功能相近，执行时按优先级选择：

| 功能 | 优先使用 | 备选 |
|------|----------|------|
| 需求对齐/深度提问 | grill-with-docs（如已安装） | superpowers 中的 brainstorm |
| 调试/排查 Bug | diagnose（如已安装） | superpowers 中的 debug 流程 |
| 代码审查 | review（如已安装） | superpowers 中的 review 流程 |
| 浏览器自动化 | playwright-cli（官方更完整） | agent-browser（更轻量） |
| 前端实现 | frontend-design | ui-ux-pro-max 的实现部分 |
| 全流程开发 | superpowers | mattpocock 子技能组合 |

## 技能链定义

### 链1：从零开发新功能

**触发指令**：`/chain feature` 或 "我要开发新功能" / "从零开发"

```
1. office-hours → 产品验证：真的有需求吗？最小切入口？
2. grill-with-docs / superpowers → 需求对齐：范围？约束？
3. superpowers → 脑暴 + 计划：2-3 方案 → 逐任务计划
4. ui-ux-pro-max → UI/UX 设计：页面设计、状态处理
5. frontend-design → 前端实现：代码产出
6. tdd / superpowers:tdd → 测试驱动：红→绿→重构
7. playwright-cli → E2E 测试：流程自动化验证
8. review → 代码审查：标准 + 规范
9. self-improvement → 经验记录
```

### 链2：安装新技能

**触发指令**：`/chain install` 或 "安装新技能" / "找个技能"

```
1. find-skills → 搜索：npx skills find <关键词>
2. skill-vetter → 审查：来源→代码→权限→风险
3. find-skills → 安装：npx skills add <skill-name>
```

### 链3：Bug 排查与修复

**触发指令**：`/chain debug` 或 "排查Bug" / "调试" / "报错了"

```
1. diagnose → 科学化调试：复现→最小化→假设→验证→修复→回归
2. zoom-out → 理解上下文：问题链路全景图
3. self-improvement → 记录经验：bug 原因和修复方式
```

### 链4：架构审查

**触发指令**：`/chain review` 或 "检查架构" / "架构审查"

```
1. zoom-out → 全局模块映射
2. improve-codebase-architecture → 耦合度分析→深化重构机会
3. request-refactor-plan → 详细重构计划（可选）
```

### 链5：接手已有项目

**触发指令**：`/chain onboard` 或 "理解项目" / "梳理项目" / "接手项目"

```
1. project-onboard → 三阶段九步骤
   - 阶段一：zoom-out + 深度探索 + 领域语言
   - 阶段二：SDD逆向补全（spec.md + design.md + tasks.md）
   - 阶段三：架构改进 + 文档验证
2. self-improvement → 记录理解要点
```

## 执行策略

- 每个技能的输出作为下一个技能的输入上下文
- 如果链中某个技能不可用（未安装），按"功能等价映射"选择备选
- 如果连备选也不可用，跳过该步骤并告知用户
- 用户可随时中断链，要求只执行某几步
- 每步执行前简要说明即将做什么，执行后总结产出

## 指令速查

| 指令 | 场景 |
|------|------|
| `/chain feature` | 从零开发新功能 |
| `/chain install` | 安装新技能 |
| `/chain debug` | Bug 排查修复 |
| `/chain review` | 架构审查 |
| `/chain onboard` | 接手已有项目 |

详见 [references/chains-detail.md](references/chains-detail.md) 了解每个技能链的详细步骤说明。