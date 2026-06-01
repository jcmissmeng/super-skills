# super-skills

Agent 技能集合，用于存放和管理多个 AI Agent 技能模块。

## 项目结构

```
super-skills/
├── docs/spec/          # SDD 文档（spec.md / design.md / tasks.md）
├── skills/             # 自研技能集合
│   └── <skill-name>/   # 单个技能
│       ├── SKILL.md    # 技能核心定义（必须）
│       ├── README.md   # 技能说明
│       ├── CHANGELOG.md
│       ├── LICENSE.txt
│       ├── evals/      # 评估用例
│       └── references/ # 参考资源
├── useful/             # 社区/第三方技能缓存
│   └── <skill-name>/   # 通过 npx skills add 安装的技能
└── .joycode/           # IDE 持久化层
```

## 已有技能

| 技能 | 版本 | 说明 |
|------|------|------|
| [project-onboard](skills/project-onboard/) | 1.1.0 | 系统化理解已有/半成品项目，逆向产出 spec/design/tasks 文档 |
| [skill-chain](skills/skill-chain/) | 1.0.0 | 通过指令调用预定义技能链，按场景编排多技能协同执行 |

## 使用方式

在 IDE 中输入技能触发词即可自动激活，例如：

- "梳理项目" / "理解项目" → 激活 project-onboard
- "补全文档" / "更新文档" → 激活 project-onboard
- `/chain feature` / "从零开发" → 激活 skill-chain
- `/chain debug` / "排查Bug" → 激活 skill-chain

## 添加新技能

1. 在 `skills/` 下创建新目录（kebab-case 命名）
2. 编写 `SKILL.md`（含 YAML frontmatter：name / description / metadata）
3. 添加 `evals/evals.json` 评估用例
4. 添加 `references/` 参考资源（可选）

## 许可证

[Apache 2.0](LICENSE.txt)