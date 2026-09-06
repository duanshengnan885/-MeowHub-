# CLAUDE.md — 星喵 (MeowHub) 项目规则

本文档遵循 [docs/MASTER_RULES.md](file:///d:/个人项目/星喵%20(MeowHub)/docs/MASTER_RULES.md) 项目最高级规范。

## 项目身份
- 正式名称：星喵 (MeowHub)
- 代码代号：MeowHub
- 严禁称呼：AI Desktop Assistant 或 ai_assistant

## 核心准则
1. 最小改动原则：最小 Token 消耗 → 修正确 → 最小改动。严禁无序重构与擅动依赖。
2. 源码唯一真相源：当前工作区代码为唯一真相源，不回退，不导入 backup。
3. 需求与计划：3 步以上任务先理需求（`docs/requirements/`），开发前列计划（`docs/plans/`）。
4. 根因追踪与复盘：排查定位至根本原因，四段式（现象→根因→修复→教训）写入 `docs/bugs_and_memory/YYYY-MM-DD.md`。
5. 验证闭环：证据优先，必须附带实测命令与真实输出证据方可确认完成。
6. 文档体系：所有文档分类归入 `docs/` 下对应子目录。
