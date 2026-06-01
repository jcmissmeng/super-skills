# Tasks — super-skills 任务清单

## 已完成 (done)

| ID | 任务 | 验收标准 | 完成时间 |
|----|------|----------|----------|
| T1 | 项目初始化与 Git 仓库创建 | GitHub 公开仓库可访问，main 分支有初始提交 | 2026-05-31 |
| T2 | 引入 project-onboard 技能 | skills/project-onboard/ 下文件完整，SKILL.md 可被 IDE 识别 | 2026-05-31 |
| T3 | SDD 文档逆向补全 | docs/spec/ 下 spec.md / design.md / tasks.md 齐全 | 2026-05-31 |

## 进行中 (in_progress)

| ID | 任务 | 验收标准 | 优先级 |
|----|------|----------|--------|
| T4 | 修复 project-onboard 测试配置 | conftest.py 不再引用不存在的 scripts/ 目录，tests 可正常运行 | P1 | 2026-05-31 |
| T5 | 补充项目根目录 .gitignore | 根目录有 .gitignore，排除 node_modules/.env 等 | P1 | 2026-05-31 |

## 待开发 (pending)

| ID | 任务 | 验收标准 | 优先级 | 来源 |
|----|------|----------|--------|------|
| T6 | 补充项目根目录 README.md | 包含项目定位、技能列表、使用方式说明 | P0 | 项目必备 | 2026-05-31 |
| T7 | 修复 project-onboard 缺失的 .gitignore | skills/project-onboard/.gitignore 存在且内容合理 | P2 | xcopy 遗漏 | 2026-05-31 |
| T8 | 完善 .joycode/memory 持久化记忆 | 建立用户偏好/项目上下文等记忆文件 | P3 | spec A3 |
| T9 | 完善 .joycode/rules 项目规则 | 定义代码规范、提交规范等规则文件 | P3 | spec A4 |
| T10 | 添加更多技能模块 | skills/ 下至少有 2 个技能目录，各有完整结构 | P2 | 项目扩展 | 2026-05-31 |
| T11 | 建立 CI/CD 流水线 | GitHub Actions 配置，自动检查技能结构完整性 | P3 | design 6 |