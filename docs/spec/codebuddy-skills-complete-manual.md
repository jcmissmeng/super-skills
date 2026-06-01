# CodeBuddy IDE 技能完整使用手册

> **文档说明**：本文档详细介绍 `skills/` 目录下所有技能的用途、使用方法和触发方式。
> **更新时间**：2026-05-31
> **适用版本**：CodeBuddy CN
> **技能总数**：12 个技能集（含 mattpocock 下的 28 个子技能）

---

## 目录

1. [技能分类概览](#1-技能分类概览)
2. [浏览器自动化类](#2-浏览器自动化类)
   - 2.1 [agent-browser — Agent Browser](#21-agent-browser)
   - 2.2 [playwright-cli — Playwright CLI](#22-playwright-cli)
3. [设计开发类](#3-设计开发类)
   - 3.1 [frontend-design — 前端界面设计](#31-frontend-design)
   - 3.2 [ui-ux-pro-max — UI/UX 设计智能](#32-ui-ux-pro-max)
4. [产品规划类](#4-产品规划类)
   - 4.1 [office-hours — 产品思维办公室](#41-office-hours)
5. [开发工作流类](#5-开发工作流类)
   - 5.1 [superpowers — 规范优先开发工作流](#51-superpowers)
   - 5.2 [mattpocock — Matt Pocock 编码技能集](#52-mattpocock)
6. [项目理解与文档类](#6-项目理解与文档类)
   - 6.1 [project-onboard — 项目系统化理解与文档维护](#61-project-onboard)
7. [技能编排类](#7-技能编排类)
   - 7.1 [skill-chain — 技能链调用](#71-skill-chain)
8. [技能管理类](#8-技能管理类)
   - 8.1 [find-skills — 技能发现与安装](#81-find-skills)
   - 8.2 [skill-vetter — 技能安全审查](#82-skill-vetter)
   - 8.3 [self-improvement — 持续改进代理](#83-self-improvement)
9. [技能协同使用](#9-技能协同使用)
10. [常见问题](#10-常见问题)

---

## 1. 技能分类概览

`skills/` 目录下共 **12 个技能集**，按功能领域分为六大类：

| 类别 | 技能 | 版本 | 核心领域 |
|:------|:-----|:-----|:---------|
| **浏览器自动化** | agent-browser | 0.2.0 | 无头浏览器操作 |
| | playwright-cli | 1.0.0 | 官方 Playwright 自动化 |
| **设计开发** | frontend-design | 1.0.0 | 前端界面设计 |
| | ui-ux-pro-max | 0.1.0 | UI/UX 设计智能 |
| **产品规划** | office-hours | 1.0.0 | 产品思维/需求分析 |
| **开发工作流** | superpowers | 1.0.0 | 规范优先 TDD 开发 |
| | mattpocock | — | 28 个编码子技能 |
| **项目理解与文档** | project-onboard | 1.0.0 | 项目系统化理解/文档维护 |
| **技能编排** | skill-chain | 1.0.0 | 技能链调用/多技能协同 |
| **技能管理** | find-skills | 0.1.0 | 发现与安装技能 |
| | skill-vetter | 1.0.0 | 技能安全审查 |
| | self-improvement | 3.0.21 | 持续改进/经验记录 |

### 完整技能树

```
skills/
├── 📂 agent-browser/              → Agent Browser (浏览器自动化)
├── 📂 find-skills/                → 技能市场搜索引擎
├── 📂 frontend-design/            → 高质量前端界面设计
├── 📂 mattpocock/                 → Matt Pocock 28 个编码子技能
│   ├── caveman/                   → 极简对话模式
│   ├── design-an-interface/       → 接口设计
│   ├── diagnose/                  → 科学化调试
│   ├── edit-article/              → 编辑文章
│   ├── git-guardrails-claude-code/ → Git 安全防护
│   ├── grill-me/                  → 需求深问
│   ├── grill-with-docs/           → 文档对对齐
│   ├── handoff/                   → 会话交接
│   ├── improve-codebase-architecture/ → 架构优化
│   ├── migrate-to-shoehorn/       → 迁移到 Shoehorn
│   ├── obsidian-vault/            → Obsidian 知识库
│   ├── prototype/                 → 快速原型
│   ├── qa/                        → 质量保证
│   ├── request-refactor-plan/     → 重构计划
│   ├── review/                    → 代码审查
│   ├── scaffold-exercises/        → 练习题生成
│   ├── setup-matt-pocock-skills/  → 技能初始化配置
│   ├── setup-pre-commit/          → Pre-commit 配置
│   ├── skill-creator/             → 技能创建器
│   ├── tdd/                       → 测试驱动开发
│   ├── to-issues/                 → 需求转 Issue
│   ├── to-prd/                    → 需求转 PRD
│   ├── triage/                    → Issue 分拣
│   ├── ubiquitous-language/       → 统一领域语言
│   ├── write-a-skill/             → 编写技能
│   ├── writing-beats/             → 写作节拍
│   ├── writing-fragments/         → 写作片段
│   ├── writing-shape/             → 写作结构
│   └── zoom-out/                  → 宏观视角
├── 📂 office-hours/               → YC 式产品思维
├── 📂 project-onboard/            → 项目系统化理解与文档维护
├── 📂 skill-chain/                → 技能链调用/多技能协同
├── 📂 playwright-cli-openclaw/    → Playwright 自动化
├── 📂 self-improving-agent/       → 持续改进代理
├── 📂 skill-vetter/               → 技能安全审查
├── 📂 superpowers/                → 规范优先工作流
└── 📂 ui-ux-pro-max/              → UI/UX 设计智能
```

---

## 2. 浏览器自动化类

### 2.1 agent-browser

**技能名称**：Agent Browser
**版本**：v0.2.0
**技能类型**：社区插件技能

#### 用途

基于 Rust 的快速无头浏览器自动化 CLI 工具（带 Node.js 回退方案），使 AI 代理能够通过结构化命令导航网页、点击、输入和截图。底层使用 [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)。

#### 使用方法

**安装步骤**：
```bash
# 推荐方式：npm 安装
npm install -g agent-browser
agent-browser install
agent-browser install --with-deps

# 从源码安装
git clone https://github.com/vercel-labs/agent-browser
cd agent-browser && pnpm install
```

**核心命令**：
| 类别 | 命令 | 说明 |
|:-----|:-----|:-----|
| 导航 | `agent-browser open <url>` | 打开网页 |
| 截图 | `agent-browser snapshot -i` | 页面快照（含交互元素索引） |
| 点击 | `agent-browser click @ref` | 按索引点击元素 |
| 输入 | `agent-browser fill @ref "text"` | 填写输入框 |
| 提取 | `agent-browser get text/html/value @ref` | 提取内容 |
| 等待 | `agent-browser wait <ms>` | 等待毫秒 |
| 截图 | `agent-browser screenshot` | 页面截图 |
| PDF | `agent-browser pdf` | 生成 PDF |
| 脚本 | `agent-browser eval "js code"` | 执行 JavaScript |

**完整功能**：导航、截图、点击/输入/键入交互、信息提取（text/html/value）、状态检查、截图 & PDF、视频录制、等待、鼠标控制、语义定位器（find）、浏览器设置、Cookie & Storage、网络拦截、标签页 & 窗口、框架、对话框、JavaScript eval、状态管理（save/load）、多浏览器并行会话。

**标准工作流**：`open url → snapshot -i → click/fill @ref → snapshot → ...`

#### 触发方式

自动触发，当用户的请求涉及以下场景时：
- 自动化网页交互
- 从页面提取结构化数据
- 程序化填写表单
- 测试 Web UI

**触发关键词示例**：

| 场景 | 示例语句 |
|:-----|:---------|
| 打开网页 | "打开 https://example.com"、"访问这个网站" |
| 截图 | "给这个网页截图" |
| 填写表单 | "在登录表单中输入用户名密码" |
| 提取内容 | "提取网页的所有文章标题" |

---

### 2.2 playwright-cli

**技能名称**：Playwright CLI Automation
**版本**：v1.0.0
**技能类型**：社区插件技能

#### 用途

微软官方 Playwright CLI 网页自动化工具，支持 Chromium、Firefox、WebKit 三大主流浏览器的无头/有头自动化操作，包括页面导航、元素交互、截图、录制、测试等功能。

#### 使用方法

**安装步骤**：
```bash
# 安装 Playwright CLI
npm install -g @playwright/test
# 或
pip install playwright

# 安装浏览器
playwright install
# 仅安装特定浏览器
playwright install chromium firefox

# 安装系统依赖（Linux）
playwright install-deps
```

**核心命令**：
| 类别 | 命令 | 说明 |
|:-----|:-----|:-----|
| 打开页面 | `playwright open <url>` | 打开网页（有头模式） |
| 截图 | `playwright screenshot <url>` | 网页截图 |
| 生成 PDF | `playwright pdf <url>` | 生成 PDF |
| 录制 | `playwright codegen <url> --output script.py` | 录制用户操作为脚本 |
| 测试 | `playwright test` | 运行 E2E 测试 |
| 有头测试 | `playwright test --headed` | 可见模式运行测试 |
| 调试 | `playwright test --debug` | 调试模式 |
| 查看浏览器 | `playwright list-browsers` | 查看已安装浏览器 |

**最佳实践**：
- 优先使用无头模式（默认）
- 复杂操作用 `codegen` 录制
- 添加 `--slowmo` 防反爬
- 保存登录状态以复用

#### 触发方式

自动触发，当用户的请求涉及以下场景时：

| 场景 | 示例语句 |
|:-----|:---------|
| 网页自动化 | "帮我自动登录这个网站" |
| 浏览器操作 | "用浏览器打开这个页面" |
| E2E 测试 | "测试登录功能是否正常" |
| 截图 | "给这个网页截全页图" |
| 录制操作 | "录制用户登录的操作流程" |
| 数据提取 | "提取这个网页的所有链接" |

---

## 3. 设计开发类

### 3.1 frontend-design

**技能名称**：Frontend Design
**版本**：v1.0.0
**技能类型**：社区插件技能

#### 用途

创建独特的、生产级前端界面，具有高设计质量。核心目标是**避免通用 AI 美学**（"AI slop"），生成有创意、精致、令人难忘的前端代码。

#### 使用方法

**设计思考流程**（在写任何代码之前）：
1. **理解目的**：这个界面解决什么问题？谁使用？
2. **选择美学方向**：从以下风格中大胆选择 —
   - **极简/极繁**、**复古未来**、**有机自然**
   - **奢华精致**、**玩趣/玩具**、**编辑杂志风**
   - **粗野主义/原生态**、**装饰艺术/几何**
   - **柔和粉彩**、**工业实用** 等
3. **技术约束**：确认框架（React/Vue/HTML）、性能要求、可访问性标准
4. **差异化**：什么会让这个界面让人过目不忘？

**代码实现原则**：
- **排版**：选择独特有趣的字体，**禁止**使用 Arial / Inter / Roboto 等通用字体
- **色彩 & 主题**：用 CSS 变量保持一致性，主导色 + 锐利强调色
- **动效**：CSS 优先的动画和微交互
- **空间构成**：不对称、重叠、对角线流动、打破网格
- **背景 & 细节**：渐变网格、噪点纹理、几何图案、分层透明度

**核心禁忌**：永远不要使用通用 AI 美学（白底 + 紫色渐变 + Inter 字体 + 千篇一律的卡片布局）

#### 触发方式

自动触发，当用户请求以下内容时：

| 场景 | 示例语句 |
|:-----|:---------|
| 创建组件 | "创建一个登录表单组件" |
| 构建页面 | "帮我做一个产品展示页面" |
| 创建应用 | "创建一个待办事项应用" |
| 美化界面 | "美化这个表格界面" |
| 改进 UI | "让这个页面更有设计感" |

---

### 3.2 ui-ux-pro-max

**技能名称**：UI/UX Pro Max
**版本**：v0.1.0
**技能类型**：社区插件技能

#### 用途

UI/UX 设计智能和实现指导，用于构建精致的界面。内置 **100+ 条推理规则**、**67 种 UI 风格**、多技术栈设计数据（React / Vue / Next.js / Svelte / Tailwind / Flutter / SwiftUI 等），覆盖从 UI 概念到设计系统到代码实现的完整流程。

#### 使用方法

**四步工作流**：

**第 1 步 — Triage（分诊）**：仅问必要问题
- 目标平台：Web / iOS / Android / Desktop
- 技术栈：React / Vue / Svelte / CSS / Tailwind / 组件库
- 目标和约束：转化率、速度、品牌调性、无障碍等级（WCAG AA?）
- 现有资源：截图、Figma、仓库、URL、用户旅程

**第 2 步 — 生成交付物**（按需选择）：
- **UI 概念 + 布局**：视觉方向、网格、排版、色彩系统、关键页面
- **UX 流程**：用户旅程、关键路径、错误/空/加载状态、边界情况
- **设计系统**：Token（颜色/排版/间距/圆角/阴影）、组件规则、可访问性说明
- **实现计划**：精确到文件级别的编辑、组件分解、验收标准

**第 3 步 — 使用打包数据**：从 `skills/ui-ux-pro-max/assets/data/` 读取调色板、模式、启发式规则

**第 4 步 — 可选脚本**：
```bash
python3 skills/ui-ux-pro-max/scripts/design_system.py --help
```

**输出标准**：
- ASCII-only token 系统
- 含间距/类型/颜色 token
- 2-3 种字体配对选项
- 组件状态覆盖（hover/active/disabled/focus）

**当用户说"全部都要"**：按 design → UX → code → design system 顺序依次交付。

#### 触发方式

自动触发，当用户请求以下内容时：

| 场景 | 示例语句 |
|:-----|:---------|
| UI 设计 | "设计一个用户管理页面的 UI" |
| UX 流程 | "帮我规划用户注册的用户旅程" |
| 设计系统 | "为项目创建一套设计系统 tokens" |
| 组件规范 | "定义按钮组件的所有状态和样式" |
| 可访问性 | "让这个页面达到 WCAG AA 标准" |
| 前端代码审查 | "审查这个页面是否符合设计规范" |
| 全面设计 | "全部都要，从设计到代码到设计系统" |

---

## 4. 产品规划类

### 4.1 office-hours

**技能名称**：Office Hours（产品思维办公室）
**版本**：v1.0.0
**技能类型**：社区插件技能

#### 用途

YC 式产品思维办公室。用第一性原理拆解产品想法，通过"六问逼问法"验证需求真伪，挑战前提假设，生成多种实现方案。

**硬性规则：不写代码、不搭项目、不实现任何功能。唯一输出是设计文档。**

#### 使用方法

**六阶段流程**：

**Phase 1 — 理解上下文**
询问目标类型（单选）：
- 创业项目（正经做公司）→ Startup 模式（2A）
- 内部项目（公司内推动）→ Startup 模式（适配版）
- Hackathon / Demo → Builder 模式（2B）
- 开源 / 研究 → Builder 模式
- 学习 / 练手 → Builder 模式
- 纯兴趣 / 玩 → Builder 模式

**Phase 2A — Startup 模式：六问逼问法**

逐个提问，等待每次回答：
| 问题 | 核心要点 |
|:-----|:---------|
| Q1: 需求真实性 | 用户真的需要这个吗？现在用什么替代方案？ |
| Q2: 现状替代方案 | 没有你产品的人现在是怎么解决问题的？ |
| Q3: 极度具体的用户 | 谁是最迫切需要这个的第一个用户？ |
| Q4: 最窄切入口 | 如果只能做一件事，是什么？ |
| Q5: 观察与意外 | 观察用户后发现的最意外的事是什么？ |
| Q6: 未来适配性 | 半年后最可能需要适配什么？ |

**Phase 2B — Builder 模式**
设计伙伴角色，适用于 Hackathon / 学习 / 开源场景，注重执行而非商业模式验证。

**Phase 3 — 前提挑战**
列出所有隐含假设，逐条确认真伪。

**Phase 4 — 方案生成**
生成 2-3 个不同路径：
- 最小可行版（MVP）
- 理想架构版
- 创意/非直觉方案

**Phase 5 — 设计文档**
按模板输出完整设计文档，包含：
- 问题定义、目标用户、核心价值主张
- 解决方案描述、技术路线
- 风险和假设、成功指标

**Phase 6 — 收尾**
观察反射 + 下一步推荐

#### 触发方式

自动触发 + **主动建议**，当用户表达以下意图时：

| 场景 | 示例语句 |
|:-----|:---------|
| 产品想法讨论 | "帮我想想这个点子" |
| 需求验证 | "这个值不值得做" |
| 头脑风暴 | "brainstorm 一下新功能" |
| 产品规划 | "帮我做产品规划" |
| 需求分析 | "帮我分析一下这个需求" |
| 思路梳理 | "帮我理清思路" |

**重要提醒**：在任何代码实现之前，AI 应主动建议使用本技能。这是最核心的产品验证工具。

---

## 5. 开发工作流类

### 5.1 superpowers

**技能名称**：Superpowers Dev Workflow
**版本**：v1.0.0
**技能类型**：社区插件技能

#### 用途

规范优先、TDD、子代理驱动的软件开发工作流。改编自 [obra/superpowers](https://github.com/obra/superpowers)，**是强制性工作流而非建议**。

#### 使用方法

**五阶段流水线**：

```
Idea → Brainstorm → Plan → Subagent-Driven Build (TDD) → Code Review → Finish Branch
```

**Phase 1 — 头脑风暴（Brainstorm）**
- 探索项目上下文
- 逐个提问，等待回答
- 提出 2-3 个方案，含权衡分析
- 逐节展示设计
- 写设计文档，提交到仓库
- **硬性门禁**：设计批准前不写代码

**Phase 2 — 写计划（Plan）**
- 详细到逐个任务的实现计划
- 每个任务预估 2-5 分钟：写测试 → 看失败 → 实现 → 看通过 → 提交

**Phase 3 — 子代理驱动开发（Subagent-Driven Build）**
- 每个任务派出三个子代理：
  - **实现者** — 写代码
  - **规范审查** — 检查是否符合设计
  - **代码质量审查** — 检查代码质量
- TDD 强制执行（红 → 绿 → 重构）

**Phase 4 — 系统调试（Systematic Debugging）**
- 四阶段调试流程：
  1. 根因调查
  2. 模式分析
  3. 假设 + 测试
  4. 修复 + 验证
- **硬性门禁**：没有根因调查就不修复

**Phase 5 — 完成分支（Finish Branch）**
- 验证所有测试通过
- 确定基础分支
- 提供 4 个选项：本地合并 / 推送 PR / 保留 / 丢弃

#### 触发方式

自动触发，当用户表达以下意图时：

| 场景 | 示例语句 |
|:-----|:---------|
| 构建新功能 | "帮我开发商品搜索功能" |
| 调试 Bug | "登录后偶尔闪退，帮我排查" |
| 测试失败 | "这个测试失败了，帮我修" |
| 开始构建 | "let's build"、"开始做吧" |
| 请求规划 | "help me plan"、"帮我规划一下" |
| 添加功能 | "I want to add X"、"我想加一个..." |
| 功能报错 | "this is broken"、"这个坏了" |
| 完成分支 | "这个功能做完了，合并吧" |

**不适用场景**（不要触发）：单行修复、阅读代码、非代码任务。

---

### 5.2 mattpocock

**技能名称**：Matt Pocock Skills
**版本**：—
**技能类型**：社区技能集（28 个子技能）

#### 用途

Matt Pocock 的 AI 编码技能集，由知名 TypeScript 专家和教育者创建。包含 **28 个**针对真实工程开发的 AI 智能体技能，覆盖需求对齐、测试驱动开发、调试排障、架构优化等全流程。

#### 子技能完整列表

##### 5.2.1 需求与规划类

| 子技能 | 用途 | 触发方式 | 核心流程 |
|:-------|:-----|:---------|:---------|
| **grill-with-docs** | 结合项目文档深度对齐需求 | "我要开发..."、"需求对不齐" | 深度提问 → 生成 CONTEXT.md → 生成 ADR → 确保对齐 |
| **grill-me** | 无文档场景的深度提问 | "帮我严格审查这个设计" | 逐个向下遍历决策树，直到共享理解 |
| **to-prd** | 将对话上下文转为 PRD 文档 | "生成 PRD" | 综合已有理解，直接生成 PRD（不额外访谈） |
| **to-issues** | 将计划拆解为独立可领取的 Issue | "把需求拆成 Issue" | 垂直切片（tracer bullet）方式拆分 |
| **ubiquitous-language** | 提取领域语言词汇表 | "定义领域术语"、"建词汇表" | 从对话中抽取术语，消除歧义，保存 UBIQUITOUS_LANGUAGE.md |

##### 5.2.2 开发与实现类

| 子技能 | 用途 | 触发方式 | 核心流程 |
|:-------|:-----|:---------|:---------|
| **tdd** | 测试驱动开发（红-绿-重构） | "用 TDD 实现"、"先写测试" | 红（写失败测试）→ 绿（最小实现）→ 重构 |
| **prototype** | 快速原型探索 | "做个原型试试"、"探索几个设计" | 构建可丢弃的原型，用于验证数据模型或 UI 方向 |
| **design-an-interface** | 设计接口（Design It Twice） | "设计 API"、"设计模块接口" | 生成多个截然不同的设计方案进行对比 |
| **scaffold-exercises** | 创建练习目录结构 | "生成练习题" | 按规范创建含题目、解答、说明的练习结构 |

##### 5.2.3 调试与排障类

| 子技能 | 用途 | 触发方式 | 核心流程 |
|:-------|:-----|:---------|:---------|
| **diagnose** | 科学化调试 | "帮我排查这个 bug"、"调试" | 复现 → 最小化 → 假设 → 埋点 → 修复 → 回归 |
| **zoom-out** | 宏观理解代码 | "这段代码我不熟悉" | 上升到抽象层，给出模块全景图 |

##### 5.2.4 代码质量类

| 子技能 | 用途 | 触发方式 | 核心流程 |
|:-------|:-----|:---------|:---------|
| **review** | 双轴代码审查 | "帮我审查代码"、"review since X" | 并行子代理：标准审查 + 规范审查 |
| **qa** | 交互式质量保证 | "QA session"、"我要报 bug" | 对话式提 issue，自动探索代码上下文中创建 |
| **improve-codebase-architecture** | 架构优化扫描 | "优化架构"、"重构机会" | 识别耦合、职责不清、重复代码，提出深化重构 |
| **request-refactor-plan** | 重构计划生成 | "规划重构"、"重构 RFC" | 用户访谈 → 详细计划 → 小步提交策略 |

##### 5.2.5 效率与人效类

| 子技能 | 用途 | 触发方式 | 核心流程 |
|:-------|:-----|:---------|:---------|
| **caveman** | 极简对话模式 | "caveman mode"、"少废话" | 削减 ~75% token，仅保留技术实质 |
| **handoff** | 会话交接文档 | "交接给下一个 agent" | 生成摘要 + 关键决策 + 待办事项 + 建议技能 |
| **triage** | Issue 分拣 | "整理 Issue"、"分类问题" | 状态机驱动的分拣角色流程 |

##### 5.2.6 配置与管理类

| 子技能 | 用途 | 触发方式 | 核心流程 |
|:-------|:-----|:---------|:---------|
| **setup-matt-pocock-skills** | 首次初始化配置 | 首次使用技能集时 | 设置 Issue 跟踪器、分类标签、文档路径 |
| **setup-pre-commit** | 配置 Pre-commit 钩子 | "配置 git 钩子" | 设置代码提交前的自动化检查 |
| **git-guardrails-claude-code** | Git 安全防护 | 自动执行 | 阻止危险的 git 命令（如 force push） |

##### 5.2.7 技能创建类

| 子技能 | 用途 | 触发方式 | 核心流程 |
|:-------|:-----|:---------|:---------|
| **skill-creator** | 创建自定义技能 | "创建技能"、"写个技能" | 含初始化/打包/验证的完整工具链 |
| **write-a-skill** | 编写技能文件 | "写个新 skill" | 渐进式披露结构 + 打包资源 |

##### 5.2.8 内容与写作类

| 子技能 | 用途 | 触发方式 |
|:-------|:-----|:---------|
| **edit-article** | 编辑技术文章 | 编辑/审查文章时 |
| **writing-beats** | 写作节拍/节奏控制 | 写作需要节奏感时 |
| **writing-fragments** | 写作片段生成 | 需要补齐内容片段时 |
| **writing-shape** | 写作结构/形态 | 需要调整文章结构时 |

##### 5.2.9 其他类

| 子技能 | 用途 | 触发方式 |
|:-------|:-----|:---------|
| **obsidian-vault** | Obsidian 知识库管理 | "管理 Obsidian" |
| **migrate-to-shoehorn** | 迁移到 Shoehorn 框架 | 需要使用 Shoehorn 时 |

#### 关键注意事项

1. **首次使用必须初始化**：运行 `/setup-matt-pocock-skills` 完成配置
2. **按需使用**：不需要使用所有子技能，根据场景选择
3. **协同使用**：可与 superpowers、scm-b2b-dev 等其他技能协同

#### 推荐工作流链

```
新功能开发：
  /grill-with-docs → /to-prd → /to-issues → /tdd → /improve-codebase-architecture

Bug 排查：
  /diagnose → /zoom-out

代码审查：
  /review → /request-refactor-plan（如需重构）
```

---

## 6. 项目理解与文档类

### 6.1 project-onboard

**技能名称**：Project Onboard（项目系统化理解与文档维护）
**版本**：v1.0.0
**技能类型**：自定义技能

#### 用途

系统化理解已有/半成品项目，逆向梳理架构、功能、业务、部署等信息并结构化文档化（SDD），同时提供开发过程中持续更新文档的提示词模板。**在任何代码实现之前主动建议使用。**

#### 使用方法

**三阶段九步骤完整流程**：

**阶段一：探索理解**

| 步骤 | 操作 | 提示词 |
|:-----|:-----|:-------|
| 1 | 鸟瞰全局 | "请帮我 zoom-out，从高层视角理解这个项目的整体架构、模块划分、核心依赖关系和业务流程。" |
| 2 | 深度探索 | "请深度探索这个项目，我需要了解：1.目录结构及各模块职责 2.核心模块间的调用关系和数据流 3.配置/环境变量的体系及消费链路 4.入口文件的启动编排逻辑 5.对外接口完整清单 6.第三方依赖及其用途" |
| 3 | 提炼领域语言 | "请提取这个项目的领域术语表（ubiquitous-language），覆盖：业务概念、技术概念、模块概念，消除命名歧义，建立统一术语。" |

**阶段二：结构化文档化（SDD逆向补全）**

| 步骤 | 操作 | 提示词 |
|:-----|:-----|:-------|
| 4 | 初始化SDD目录 | "请用 creating-sdd-directory 为当前项目初始化SDD目录结构。项目描述：[一句话描述项目是什么、用什么技术、解决什么问题、面向谁]" |
| 5 | 逆向写 spec.md | "请基于现有代码逆向梳理 spec.md，覆盖：1.功能清单 2.业务规则 3.用户场景 4.约束条件 5.配置项说明 6.接口契约" |
| 6 | 逆向写 design.md | "请基于现有代码逆向梳理 design.md，覆盖：1.架构模式 2.目录结构 3.技术选型 4.数据流 5.关键设计决策 6.部署方式 7.扩展点" |
| 7 | 写 tasks.md | "请基于 spec.md 和 design.md 梳理 tasks.md：1.已完成(done) 2.半成品(in_progress) 3.待开发(pending) 4.按优先级排列+验收标准" |

**阶段三：架构优化**

| 步骤 | 操作 | 提示词 |
|:-----|:-----|:-------|
| 8 | 架构改进 | "请分析这个项目的架构改进机会：1.模块间耦合度 2.重复逻辑 3.配置灵活性 4.错误处理 5.测试覆盖 6.性能/安全" |
| 9 | 验证理解 | "请用 grill-with-docs 验证 spec.md 和 design.md 的准确性：对照实际代码，质疑文档中可能的错误或遗漏，确保文档与代码实现一致。" |

**执行策略**：
- 步骤1-3 可一次性并行发出
- 步骤4 必须先执行，步骤5-7 依赖SDD目录
- 步骤5-6 可并行，spec和design互不依赖
- 步骤8-9 依赖阶段二的产出，需串行

#### 开发中持续更新文档

| 场景 | 更新文档 | 原则 |
|:-----|:---------|:-----|
| 加功能 | spec + design + tasks + README | 先更新再实现 |
| 改Bug | spec(规则) + design(容错) | 仅当暴露规格遗漏时 |
| 重构 | design(必) + spec(仅行为变) | 架构变必更新design |
| 改配置 | design(部署) + spec(约束) + README | 用户可见必更新README |
| 发版 | 全量对齐检查 | 文档即合约 |

**持续更新提示词示例**：

| 场景 | 提示词 |
|:-----|:-------|
| 功能开发前 | "我要开发 [功能描述]，请先检查 spec.md 和 design.md 中相关内容，确认是否需要更新规格或设计文档后再开始实现。" |
| 功能开发后 | "[功能]已实现，请更新：1.spec.md 2.design.md 3.tasks.md 4.README.md" |
| Bug修复后 | "[Bug描述]已修复，请检查是否需要更新：1.spec.md 2.design.md 3.tasks.md" |
| 重构后 | "[重构内容]已完成，请更新：1.design.md 2.spec.md(仅行为变) 3.tasks.md" |
| 发版前 | "即将发布版本，请全面检查文档一致性：spec↔功能 design↔架构 tasks↔进度 README↔用户信息" |

#### 触发方式

自动触发 + **主动建议**，当用户表达以下意图时：

| 场景 | 示例语句 |
|:-----|:---------|
| 接手已有项目 | "理解项目"、"梳理项目"、"项目接管" |
| 补量文档 | "补全文档"、"逆向写spec和design" |
| 持续更新 | "功能开发完了，更新文档"、"重构完了，更新design" |
| 发版检查 | "发版前检查文档一致性" |
| 定期审计 | "审计文档一致性" |

**重要提醒**：在任何代码实现之前，AI 应主动建议使用本技能进行项目理解。

---

## 7. 技能编排类

### 7.1 skill-chain

**技能名称**：Skill Chain
**版本**：v1.0.0
**技能类型**：项目自研技能

#### 用途

通过指令调用预定义的技能链，按场景自动编排多个技能的协同执行顺序。每个技能链定义了从输入到产出的完整协作流程，并内置技能优先级规则：功能相同的技能，优先使用已安装或推荐使用的。

#### 五条技能链

| 指令 | 场景 | 技能链流程 |
|:------|:-----|:-----------|
| `/chain feature` | 从零开发新功能 | office-hours → grill-with-docs → superpowers → ui-ux-pro-max → frontend-design → tdd → playwright-cli → review → self-improvement |
| `/chain install` | 安装新技能 | find-skills → skill-vetter → find-skills |
| `/chain debug` | Bug 排查修复 | diagnose → zoom-out → self-improvement |
| `/chain review` | 架构审查 | zoom-out → improve-codebase-architecture → request-refactor-plan |
| `/chain onboard` | 接手已有项目 | project-onboard → self-improvement |

#### 链修饰符

修饰符可叠加在任何链指令后，改变链的执行风格而非流程步骤：

| 修饰符 | 说明 | 示例 |
|:--------|:------|:------|
| `--caveman` | 极简对话模式，减少约 75% token | `/chain feature --caveman` |

#### 技能优先级规则

1. **已安装的技能** > 未安装的技能（检查 skills/ 目录下是否存在对应 SKILL.md）
2. **推荐使用的技能** > 备选技能（技能链中 `/` 分隔的，左侧为推荐，右侧为备选）
3. **项目级技能** > 用户级技能

功能等价映射：

| 功能 | 优先使用 | 备选 |
|:------|:----------|:------|
| 需求对齐/深度提问 | grill-with-docs | superpowers 中的 brainstorm |
| 调试/排查 Bug | diagnose | superpowers 中的 debug 流程 |
| 代码审查 | review | superpowers 中的 review 流程 |
| 浏览器自动化 | playwright-cli | agent-browser |
| 前端实现 | frontend-design | ui-ux-pro-max 的实现部分 |
| 全流程开发 | superpowers | mattpocock 子技能组合 |

#### 触发方式

| 场景 | 示例语句 |
|:-----|:---------|
| 开发新功能 | "我要开发商品搜索功能" / `/chain feature` |
| 安装新技能 | "安装一个 PDF 处理技能" / `/chain install` |
| 排查 Bug | "支付回调偶尔重复处理" / `/chain debug` |
| 架构审查 | "检查一下项目架构质量" / `/chain review` |
| 接手项目 | "帮我理解这个项目" / `/chain onboard` |
| 多技能协作 | 用户描述了需要多个技能协作的复杂场景 |

---

## 8. 技能管理类

### 8.1 find-skills

**技能名称**：Find Skills
**版本**：v0.1.0
**技能类型**：社区插件技能

#### 用途

帮助用户发现和安装来自开放 agent 技能生态系统的技能。本质上是"技能市场的搜索引擎"，通过 `npx skills` CLI 搜索和安装社区技能包。

#### 使用方法

**技能管理命令**：
```bash
# 搜索技能（交互式或按关键词）
npx skills find [query]

# 安装技能
npx skills add <package>

# 检查技能更新
npx skills check

# 更新所有已安装技能
npx skills update
```

**四步工作流程**：
1. **理解用户需求**：用户想做什么？
2. **搜索技能**：使用 `npx skills find` 搜索匹配
3. **展示选项**：列出找到的技能及其功能和安装方式
4. **提供安装**：引导安装并说明使用方式

**技能市场**：[https://skills.sh/](https://skills.sh/)（浏览所有可用技能）

#### 触发方式

自动触发，当用户表达以下意图时：

| 场景 | 示例语句 |
|:-----|:---------|
| 询问方法 | "how do I do X"（可能已有现成技能） |
| 查找技能 | "find a skill for X"、"有没有处理 Excel 的技能？" |
| 能力询问 | "is there a skill that can..."、"你能做 X 吗？" |
| 扩展能力 | "有没有更好的方法来做..." |
| 特定领域帮助 | 用户提到需要设计、测试、部署等特定领域帮助 |

---

### 8.2 skill-vetter

**技能名称**：Skill Vetter
**版本**：v1.0.0
**技能类型**：社区插件技能

#### 用途

面向 AI agent 的安全优先技能审查工具。在安装任何技能之前使用，检查红旗标志、权限范围、可疑模式。

**核心原则：没有审查，绝不安装。有疑问就不装。**

#### 使用方法

**四步审查协议**：

**第 1 步 — 来源检查**
需回答的问题：
- [ ] 技能来自哪里？
- [ ] 作者是否可信/知名？
- [ ] 有多少下载量/星数？
- [ ] 最后更新时间？
- [ ] 是否有其他 agent 的评价？

**第 2 步 — 代码审查（强制）**
读取技能的所有文件，逐一检查以下红旗标志：
- ❌ `curl`/`wget` 到未知 URL
- ❌ 发送数据到外部服务器
- ❌ 请求凭证/Token/API 密钥
- ❌ 读取 `~/.ssh` 等敏感目录
- ❌ `base64` 解码执行
- ❌ `eval`/`exec` 外部输入
- ❌ 修改系统文件（`/etc/hosts`、`~/.bashrc`）
- ❌ 安装未列出的软件包
- ❌ 混淆/加密代码
- ❌ 请求 `sudo` 权限

**第 3 步 — 权限范围**
确认：读/写什么文件？执行什么命令？需要网络访问吗？

**第 4 步 — 风险分类**
| 级别 | 颜色 | 含义 |
|:-----|:-----|:-----|
| **LOW** | 🟢 | 安全，可以安装 |
| **MEDIUM** | 🟡 | 有注意事项，需在理解后决定 |
| **HIGH** | 🔴 | 有重大风险，强烈建议不安装 |
| **EXTREME** | ⛔ | 禁止安装 |

**输出**：标准化的审查报告。

#### 触发方式

自动触发，当用户表达以下意图时（AI 应主动建议）：

| 场景 | 示例语句 |
|:-----|:---------|
| 安装来自 ClawdHub 的技能 | "安装这个技能" |
| 运行来自 GitHub 的技能 | "试试 git clone 来的这个 skill" |
| 评估其他 agent 分享的技能 | "这是别人分享的技能，帮我看看" |
| 被要求安装未知代码 | 任何时候安装技能前 |

---

### 8.3 self-improvement

**技能名称**：Self-Improving Agent
**版本**：v3.0.21
**技能类型**：社区插件技能

#### 用途

捕获学习、错误和修正以实现持续改进。将经验记录到结构化 markdown 文件中，供后续编码 agent 处理并提升为项目记忆。支持学习提升机制和技能提取功能。

#### 使用方法

**初始化**（首次使用）：
```bash
mkdir -p .learnings
# 自动创建三个文件：
# .learnings/LEARNINGS.md      - 学习记录
# .learnings/ERRORS.md         - 错误记录
# .learnings/FEATURE_REQUESTS.md - 功能请求
```

**三种记录类型**：

**1. 学习条目（LEARNINGS.md）**
| 类别 | 说明 |
|:-----|:-----|
| correction | AI 被纠正的记录 |
| insight | 新发现的洞察 |
| knowledge_gap | 知识盲区 |
| best_practice | 最佳实践 |

条目格式：结构化 ID（LRN-YYYYMMDD-XXX）+ 优先级 + 状态 + 区域 + 详细描述

**2. 错误条目（ERRORS.md）**
记录命令失败和集成错误，含错误信息和上下文。

**3. 功能请求条目（FEATURE_REQUESTS.md）**
记录用户请求的不存在功能。

**提升机制**：
- 将广泛适用的学习提升到 `CLAUDE.md` / `AGENTS.md` / `.github/copilot-instructions.md`
- 重复模式检测：搜索已有条目 → 链接 → 升级优先级 → 考虑系统修复
- 技能提取：当学习足够有价值时，用 `extract-skill.sh` 提取为独立技能

**Hook 集成（可选）**：
自动在每次提示后提醒记录学习，检测命令错误。详见 `hooks/` 目录。

**重要安全规则**：不要记录 secrets、tokens、私钥、环境变量或完整源文件，除非用户明确要求。

#### 触发方式

自动触发，当发生以下情况时：

| 场景 | 触发事件 |
|:-----|:---------|
| 命令失败 | 命令或操作意外失败 |
| 用户纠正 | 用户说 "No, that's wrong..."、"Actually..." |
| 能力缺失 | 用户请求不存在的能力 |
| 外部失败 | 外部 API 或工具失败 |
| 知识过时 | AI 意识到知识过时或不正确 |
| 更好方法 | 发现更优的重复性任务处理方式 |
| 重大任务前 | 任务前自动回顾已有学习记录 |

---

## 9. 技能协同使用

### 9.1 典型协同场景

#### 场景 1：从零开发新功能

```
用户："我要开发商品搜索功能"

触发技能链：
1. office-hours（产品验证）
   → 真的有需求吗？最小切入口是什么？
2. superpowers / mattpocock:grill-with-docs（需求对齐）
   → 搜索范围？分词？排序？CONTEXT.md
3. superpowers（脑暴 + 计划）
   → 2-3 个方案 → 逐任务计划
4. ui-ux-pro-max（UI/UX 设计）
   → 搜索页面设计 → 搜索结果卡片 → 空/加载/错误状态
5. frontend-design（前端实现）
   → 独特美学的搜索页面代码
6. superpowers:tdd（测试驱动实现）
   → 红 → 绿 → 重构循环（单元测试/集成测试）
7. playwright-cli（E2E 自动化测试）
   → 浏览器自动化：搜索流程 E2E 测试、表单交互、截图验证
8. mattpocock:review（代码审查）
   → 标准审查 + 规范审查
9. self-improvement（经验记录）
   → 记录开发中的学习要点
```

#### 场景 2：安装新技能

```
用户："安装一个 PDF 处理技能"

触发技能链：
1. find-skills（搜索）
   → npx skills find pdf → 找到 pdf skill
2. skill-vetter（审查）
   → 来源检查 → 代码审查 → 权限范围 → 风险分类
3. find-skills（安装）
   → npx skills add <skill-name>
```

#### 场景 3：Bug 排查与修复

```
用户："支付回调偶尔重复处理"

触发技能链：
1. mattpocock:diagnose（科学化调试）
   → 复现 → 最小化 → 假设 → 验证 → 修复 → 回归
2. mattpocock:zoom-out（理解上下文）
   → 支付回调链路全景图
3. self-improvement（记录经验）
   → 记录 bug 原因和修复方式
```

#### 场景 4：架构审查

```
用户："检查一下项目架构质量"

触发技能链：
1. mattpocock:zoom-out
   → 全局模块映射
2. mattpocock:improve-codebase-architecture
   → 耦合度分析 → 深化重构机会
3. mattpocock:request-refactor-plan
   → 详细重构计划（可选）
```

#### 场景 5：接手已有项目

```
用户："帮我理解这个项目" / "梳理项目架构"

触发技能链：
1. project-onboard（三阶段九步骤）
   → 阶段一：zoom-out + 深度探索 + 领域语言
   → 阶段二：SDD逆向补全（spec.md + design.md + tasks.md）
   → 阶段三：架构改进 + 文档验证
2. self-improvement（记录理解要点）
   → 记录项目关键决策和架构特点
```

### 9.2 技能选择指南

| 你想做什么 | 推荐技能 | 说明 |
|:-----------|:---------|:-----|
| 验证产品想法 | office-hours | 写代码之前先确认方向 |
| 从零开发功能 | superpowers | 完整开发流水线 |
| 理解已有项目 | project-onboard | 三阶段九步骤系统化梳理 |
| 补量项目文档 | project-onboard | 逆向补全spec/design/tasks |
| 持续更新文档 | project-onboard | 加功能/改Bug/重构/发版全场景 |
| 需求不清晰 | mattpocock:grill-with-docs | 深度提问对齐 |
| 快速原型 | mattpocock:prototype | 可丢弃的探索代码 |
| 写高质量代码 | mattpocock:tdd | 测试驱动开发 |
| 前端界面设计 | frontend-design | 独特美学的 UI |
| UI/UX 全流程 | ui-ux-pro-max | 从设计到代码到系统 |
| 调试困难 Bug | mattpocock:diagnose | 科学化调试流程 |
| 代码审查 | mattpocock:review | 双轴并行审查 |
| 浏览器自动化 | agent-browser / playwright-cli | 两个工具互补 |
| 安装新技能 | find-skills → skill-vetter | 先搜索再审查后安装 |
| 精简对话 | mattpocock:caveman | 减少 75% token |
| 技能链/多技能协作 | skill-chain | 按场景编排技能链，指令触发 |
| 记录经验 | self-improvement | 持续改进 |

---

## 10. 常见问题

### Q1：如何查看当前已安装的技能？

查看 `skills/` 目录即可看到所有已安装的技能。也可通过锁文件查看：
```json
// skills/.skills_store_lock.json
```

或在对话中询问："显示已安装的技能"。

---

### Q2：如何安装新技能？

1. **使用 find-skills 搜索**：说"帮我找处理 Excel 的技能"
2. **AI 自动审查**：skill-vetter 自动触发安全审查
3. **确认安装**：通过审查后，AI 使用 `npx skills add` 安装
4. **手动安装**：`npx skills add <package>`

---

### Q3：技能冲突怎么办？

不同技能有不同触发条件和适用场景，大部分情况下互补而非冲突：

- **agent-browser vs playwright-cli**：都是浏览器自动化，前者更轻量快速（Rust），后者是微软官方工具（功能更完整）
- **frontend-design vs ui-ux-pro-max**：前者专注代码实现美学，后者覆盖从设计到系统的完整流程
- **superpowers vs mattpocock**：前者是强制性全流程工作流，后者是可组合的工具集

---

### Q4：如何禁用某个技能？

在 CodeBuddy IDE 中：
1. 点击左侧边栏的"技能"图标
2. 找到要禁用的技能
3. 点击"禁用"按钮

---

### Q5：技能不触发怎么办？

1. **检查技能是否存在**：确认 `skills/` 目录下有对应的 SKILL.md
2. **使用正确的触发语**：参考各技能的触发方式章节
3. **明确指定技能**：直接说出技能名，如"用 office-hours 帮我分析这个想法"或使用链指令 `/chain feature`
4. **检查 SKILL.md**：确认 `read_when` 或 `description` 中的触发条件

---

### Q6：self-improvement 的记录放哪里？

所有记录存放在项目根目录的 `.learnings/` 下：
- `.learnings/LEARNINGS.md` — 学习记录
- `.learnings/ERRORS.md` — 错误记录
- `.learnings/FEATURE_REQUESTS.md` — 功能请求

这些文件建议加入 `.gitignore`（含领域特定知识），或加入版本控制（通用开发经验）。

---

## 参考资料

- CodeBuddy 官网：https://www.codebuddy.ai
- CodeBuddy 文档：https://www.codebuddy.ai/docs
- 技能市场：https://skills.sh/
- 上游 superpowers：https://github.com/obra/superpowers
- 上游 agent-browser：https://github.com/vercel-labs/agent-browser

---

## 更新日志

| 日期 | 版本 | 更新内容 |
|:-----|:-----|:---------|
| 2026-05-30 | 2.1 | 新增 project-onboard 技能（项目系统化理解与文档维护），技能总数更新为 11 |
| 2026-05-28 | 2.0 | 重写全手册，覆盖 `skills/` 下全部 10 个技能集（含 mattpocock 28 个子技能） |
| 2026-05-12 | 1.0 | 初始版本，含 14 个内置技能的说明 |

---

**文档结束**

> 如有问题或建议，请在 GitHub Issues 中反馈。
