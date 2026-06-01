# Design — super-skills 架构设计

## 1. 架构模式

采用**约定优于配置（Convention over Configuration）**的扁平文件架构。无构建步骤、无运行时服务，纯 Markdown/JSON 文件驱动的技能集合。

## 2. 目录结构

```
super-skills/                   # 项目根目录
├── .joycode/                   # IDE 持久化层
│   ├── memory/                 # 跨会话记忆文件
│   └── rules/                  # 项目级规则
├── docs/
│   └── spec/                   # SDD 文档
│       ├── spec.md             # 功能规格
│       ├── design.md           # 架构设计
│       └── tasks.md            # 任务清单
├── skills/                     # 自研技能集合根目录
│   └── <skill-name>/           # 单个技能（约定目录名 = 技能名）
│       ├── SKILL.md            # 技能核心定义（必须，含 frontmatter）
│       ├── README.md           # 技能说明文档
│       ├── CHANGELOG.md        # 版本变更记录
│       ├── LICENSE.txt         # 许可证
│       ├── evals/              # 评估用例
│       │   └── evals.json      # 评估定义（JSON 格式）
│       └── references/         # 参考资源
│           └── *.md            # 提示词模板等
└── useful/                     # 社区/第三方技能缓存（npx skills add 安装）
    └── <skill-name>/           # 第三方技能
        └── SKILL.md            # 技能定义
```

## 3. 技术选型

| 技术 | 用途 | 选择原因 |
|------|------|----------|
| Markdown | 技能定义与文档 | 人类可读，IDE 原生支持，AI 友好 |
| JSON | 评估用例 | 结构化数据，易于解析 |
| Git/GitHub | 版本管理与协作 | 行业标准，SSH 部署密钥已配置 |
| Python | 测试框架 | pytest 生态成熟 |

## 4. 数据流

```
用户输入触发词
    → IDE 扫描 skills/*/SKILL.md 和 useful/*/SKILL.md 的 frontmatter
    → 匹配 description 中的触发条件
    → 激活技能，加载 SKILL.md 正文指令
    → 按流程执行，产出文件到 docs/spec/
    → Git commit & push 到 GitHub
```

## 5. 关键设计决策

### 决策1：扁平文件而非数据库
- **选择**：纯文件结构，无数据库
- **Trade-off**：牺牲了查询性能，换来了零依赖、Git 原生版本控制、人类直接可读

### 决策2：SKILL.md frontmatter 作为技能元数据
- **选择**：YAML frontmatter（name/description/metadata）定义触发条件
- **Trade-off**：解析需 YAML 前置处理，但保持了与 Markdown 生态的兼容性

### 决策3：技能隔离而非共享
- **选择**：每个技能独立目录，各自含 evals/references/tests
- **Trade-off**：可能有重复资源，但保证了技能的独立性和可移植性

## 6. 部署方式

- **仓库**：`git@github.com:jcmissmeng/super-skills.git`
- **分支策略**：main 单分支，直接推送
- **无 CI/CD**：当前无自动化流水线
- **无容器/服务**：纯静态文件项目

## 7. 扩展点

- **新增技能**：在 `skills/` 下创建新目录即可，IDE 自动发现
- **技能间依赖**：SKILL.md 可声明依赖的其他技能（如 project-onboard 依赖 zoom-out）
- **评估扩展**：evals.json 可扩展评估维度和断言