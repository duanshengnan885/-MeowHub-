# 星喵 (MeowHub) — 全局最高执行规则与项目规范 (AGENTS.md)

> **最高权限指示**：本项目正式名称为「星喵 (MeowHub)」。全文规矩以 [docs/MASTER_RULES.md](file:///d:/个人项目/星喵%20(MeowHub)/docs/MASTER_RULES.md) 为唯一最高准则。AI Agent 在任何会话开始、代码修改、Bug 排查及验证前必须优先无条件遵从。

---

## 1. 项目核心身份
- **正式名称**：星喵 (MeowHub)
- **英文标识**：`MeowHub`（位于 `d:\个人项目\星喵 (MeowHub)`）
- **GitHub 仓库**：`duanshengnan885/-MeowHub-`
- **定位**：AI 驱动的桌面工作站助手，带虚拟宠物、多模型对话、智能文件整理、终端沙盒等功能。
- 🚫 **红线**：在所有对话、文档、注释、提交信息中，统一使用「星喵 (MeowHub)」，严禁使用 "AI Desktop Assistant" 或 "ai_assistant"。

---

## 2. 核心开发铁律 (Token Optimized)

### 核心优先级
1. **最小 Token 消耗 → 2. 修正确 → 3. 最小改动**。
当前源码为唯一真相源，严禁还原历史代码，禁止盲目回滚，禁止将外部 backup 拷入工作区。

### 改动边界
只修目标问题和必要配套改动。**严禁**：大范围重构、非目标目录重组、纯风格重写、无关优化、擅自修改依赖。

### 读文件规则
- 先定位相关文件（错误文件 → 上下游调用链 → 配置），再精准读取。严禁盲扫全仓。
- 只读执行路径上的必要文件，单次读取超 20 个需说明原因。
- 避开非代码目录：`build/`, `dist/`, `.venv/`, `.git/`, `__pycache__/`, `releases/`, `docs/scratch/`。

### 五大技能执行闭环
1. **需求梳理 (`requirement-writer`)**：复杂任务或新功能先梳理需求，规格落盘至 `docs/requirements/`。
2. **计划管理**：3 步以上复杂任务，先写 `docs/plans/<任务名>.md`，仅保留 `Todo / Doing / Done`，保证中断可续。
3. **测试先行 (`test-driven-development`)**：涉及核心逻辑与模型解析，遵循红-绿-重构循环。
4. **根因排查 (`systematic-debugging`)**：遇到 Bug 先找根因，禁止盲目试错（Symptom fixes are failure）。排查遵循完整调用链溯源。
5. **验证闭环 (`verification-before-completion`)**：声称“做完了”前必须跑验证命令拿真实控制台/UI证据，严禁假设。

### Bug 记录格式
每次 Bug 修复后，必须按四段式记录归档至 `docs/bugs_and_memory/YYYY-MM-DD.md`：
```
现象 → 根因 → 修复 → 教训
```
涉及全局性规则或经验时，同步写入 [docs/MASTER_RULES.md](file:///d:/个人项目/星喵%20(MeowHub)/docs/MASTER_RULES.md)。

---

## 3. 项目统一文档目录映射

所有文档与说明均统筹在 `docs/` 目录中：
- 👑 **最高级规范**：[docs/MASTER_RULES.md](file:///d:/个人项目/星喵%20(MeowHub)/docs/MASTER_RULES.md)
- 📋 **需求与规格**：`docs/requirements/`（SRD、PRD、评审记录）
- 📌 **执行计划**：`docs/plans/`（各阶段任务计划）
- 🩺 **Bug 记录与复盘**：`docs/bugs_and_memory/`（每日 YYYY-MM-DD.md）
- 📖 **平台使用说明**：`docs/manuals/`（Mac与双系统说明）
- 📝 **开发草稿与备忘**：`docs/scratch/`

---

## 4. 追踪与重试规范
- 网络/API 调用强制使用重试机制：`@retry(max_attempts=3, delay=1, backoff=2)` 指数退避 + jitter。
- `.token_tracker.json`：每 10 次调用写盘，失败不影响主流程。
- `.balance_snapshot.json`：每天首次锁定余额基线，差值算当日消耗。
- DeepSeek 缓存命中提示：`🎯 缓存: X/Y tokens (Z%)`。

---

## 5. 输出规范
只返回三项内容：
1. **改了哪些文件**（带 `file:///` 点击链接）；
2. **改了什么**（统一用标准 Markdown diff 格式，严禁全量输出长文件）；
3. **验证结果**（附真实测试命令与运行输出）。
