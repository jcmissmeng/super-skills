# Spec — super-skills 功能规格

## 1. 功能清单

### 核心功能

| ID | 功能 | 说明 | 状态 |
|----|------|------|------|
| F1 | 技能托管 | 以 `skills/<skill-name>/` 目录结构托管多个 Agent 技能模块 | done |
| F2 | 技能定义 | 每个技能通过 SKILL.md 定义触发条件、流程和指令 | done |
| F3 | 技能评估 | 每个技能通过 evals/ 目录存放评估用例，验证技能触发和输出正确性 | done |
| F4 | 技能参考资源 | 每个技能通过 references/ 目录存放提示词模板等参考资源 | done |
| F5 | 版本管理 | Git 管理代码版本，推送至 GitHub 公开仓库 | done |
| F6 | 技能链调用 | 通过 skill-chain 技能按场景编排多技能协同执行 | done |

### 辅助功能

| ID | 功能 | 说明 | 状态 |
|----|------|------|------|
| A1 | 技能变更记录 | 每个技能通过 CHANGELOG.md 记录版本变更 | done |
| A2 | 技能测试 | 每个技能通过 tests/ 目录存放测试配置 | done |
| A3 | 持久化记忆 | 通过 .joycode/memory/ 跨会话记忆 | pending |
| A4 | 项目规则 | 通过 .joycode/rules/ 定义项目级规则 | pending |

## 2. 业务规则

- 每个技能必须包含 `SKILL.md` 作为核心定义文件
- 技能目录命名采用 kebab-case（如 `project-onboard`）
- 技能版本遵循语义化版本（Semantic Versioning）
- 技能许可证统一为 Apache 2.0

## 3. 用户场景

### 场景1：使用现有技能
- 用户在 IDE 中输入触发词 → 技能自动激活 → 按流程执行

### 场景2：添加新技能
- 用户在 `skills/` 下创建新目录 → 编写 SKILL.md → 添加 evals/references/tests → 推送至 GitHub

### 场景3：技能迭代
- 修改技能文件 → 更新 CHANGELOG.md → 提交推送

## 4. 约束条件

- 技能目录内不可包含嵌套的 .git 仓库
- 技能文件编码统一为 UTF-8
- 项目无后端服务，纯文件结构
- 无 npm/pip 等包管理依赖

## 5. 配置项说明

当前无外部配置文件，所有配置通过文件结构隐式约定。

## 6. 接口契约

- **Git 接口**：`git@github.com:jcmissmeng/super-skills.git`，main 分支
- **技能注册**：通过 IDE 的 skill 列表自动发现 `skills/*/SKILL.md`