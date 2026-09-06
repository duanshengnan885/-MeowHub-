---
trigger: always_on
---

# 星喵 (MeowHub) — 项目最高级规矩与开发红线 (Always On)

> **最高权限指示**：所有开发、排查、测试、修改必须以 [docs/MASTER_RULES.md](file:///d:/个人项目/星喵%20(MeowHub)/docs/MASTER_RULES.md) 为唯一最高准则。

## 1. 身份与称谓红线
- 正式名称统一使用「星喵 (MeowHub)」，代码工程代号 `MeowHub`。
- 严禁使用 "AI Desktop Assistant" 或 "ai_assistant"。

## 2. 开发铁律 (Iron Laws)
1. **最小改动原则**：1. 最小 Token 消耗 → 2. 修正确 → 3. 最小改动。严禁大范围重构、目录重组、纯风格重写、无关优化、擅动依赖。
2. **唯一真相源**：当前工作区源码为唯一真相源，严禁盲目回滚、严禁将 backup 覆盖进工作区。
3. **需求与计划先行**：3 步以上复杂任务必须先梳理需求规格至 `docs/requirements/`，开发前编写 `docs/plans/<任务名>.md`（仅限 Todo/Doing/Done）。
4. **测试与 TDD**：红-绿-重构循环，无测试用例保护严禁重构核心。
5. **系统化根因排查**：遇到 Bug 严禁猜测试错（Symptom fixes are failure），必须遵循完整调用链定位根因。所有修复按四段式（现象→根因→修复→教训）归档至 `docs/bugs_and_memory/YYYY-MM-DD.md`。
6. **无铁证绝不言完成**：Evidence before assertions always。未跑真实命令并获取实际控制台/UI证据前，严禁宣称完成。

## 3. 文档归档映射
- 统一收纳在 `docs/`：
  - 最高规范：`docs/MASTER_RULES.md`
  - 需求与规格：`docs/requirements/`
  - 任务计划：`docs/plans/`
  - Bug 记录与复盘：`docs/bugs_and_memory/`
  - 使用说明：`docs/manuals/`
  - 临时备忘：`docs/scratch/`
