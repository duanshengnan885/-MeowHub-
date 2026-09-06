# SRD — 星喵 (MeowHub) v2.x 项目全面规划

> Version: V0.1
> Date: 2026-09-06
> Author: ZCode（基于 v1.2.0 代码库全量调研自动生成）
> 调研基线：master@d41e619 + 工作区未提交改动（内置浏览器 / 深度思考滑块，约 256 行）

---

## 1. Customer（目标用户）

| 用户群 | 描述 | 核心诉求 |
|--------|------|---------|
| **主要：个人桌面重度用户** | 开发者 / 学生 / 效率玩家，Windows 10/11 为主，日常同时使用多个 AI 工具 | 一个常驻、本地优先、入口极低的 AI 工作站，替代「开浏览器→找网站→登录」的碎片流程 |
| **次要：开源社区用户** | 从 GitHub（duanshengnan885/-MeowHub-）克隆的尝鲜用户 | 拿到即能跑：依赖清晰、安装简单、不踩开发环境的坑 |
| **情感化需求用户** | 喜欢桌宠 / 萌系 UI 的轻量用户 | 宠物陪伴感 + 按需唤起的 AI 能力，而不是冷冰冰的 CLI |

> ⚠️ TBD — 待确认：是否考虑未来的付费 / 订阅场景（当前无变现设计，本规划按「个人开源项目 + 社区增长」假设展开）。

## 2. Job to be Done（核心任务）

用户希望在桌面上通过**一个常驻的、可爱的 AI 工作站**，随时完成多模型对话、让 AI 直接操控电脑（整理文件 / 跑脚本 / 浏览网页）、本地绘图和剪贴板处理，而不需要在多个工具和窗口之间切换。

## 3. Benefit（价值与收益）

### 3.1 客户价值和收益
- **单一入口**：Alt+Space 全局热键 0.5 秒唤起，覆盖对话、文件整理、终端、绘图四大高频场景
- **本地优先 = 隐私**：Ollama 本地模型 + ComfyUI 本地绘图，敏感数据可不离开本机
- **OS Agent 真实生产力**：AI 直接执行 PowerShell / Python / 文件操作，把「问 AI 怎么做」变成「让 AI 做完」
- **情感化体验**：桌宠 + 萌系 UI 降低工具的心理负担，长期使用黏性高于普通效率工具

### 3.2 业务价值和收益（个人开源项目口径）
- GitHub Star / Fork / Issue 增长（当前基线待确认，建议在 README 加 Star History 后建立月度记录）
- 可量化的社区健康度：克隆数、`MeowHub_Latest.exe` 下载量、issue 首响时长
- 作为个人作品集的核心项目，工程质量本身就是收益

### 3.3 品牌影响（品牌价值）
「会操控电脑的桌宠助手」是清晰的差异化定位；前提是**不能因稳定性 / 安全事故（如误删文件）砸掉口碑**——这是本规划把工程化放在第一期的原因。

## 4. Problem（现状问题清单）

以下问题全部来自对当前代码库的实际调研，按严重度排序。

### 4.1 🔴 安全与数据风险（最高优先级）
| # | 问题 | 证据位置 | 后果 |
|---|------|---------|------|
| P1 | API Key 明文存储在 `api_credentials.json`，且随目录分发风险 | `config.py` credentials 结构 | 密钥泄漏 |
| P2 | OS Agent `delete_item` 直接 `shutil.rmtree` / `os.remove` **物理删除，不进回收站** | `api.py:1431-1439` | AI 误判 → 用户数据不可恢复 |
| P3 | **权限分级是空壳**（2026-09-06 二次调研确认）：`agent_control_level` 仅在 `config.py:33/282` 与 `app.js:145/1428` 之间读写，**api.py 全文零引用**——v1.2.0 宣称的三级权限开关（询问/检测/完全控制）后端无任何强制执行；且 `run_powershell` 默认管理员权限（`run_as_admin=True`） | `api.py:1465-1466`、全仓 grep | 提示词注入即可无确认执行删除/写入/管理员命令；UI 给用户虚假安全感 |
| P4 | `read_file` 可读取任意本地文件，无路径边界 | `api.py:1440-1446` | 敏感文件内容进入第三方 API 上下文 |
| P5 | 会话历史全量存单个 `chat_sessions.json`，无原子写入 / 无备份轮转 | `config.py:load_all_configs/save_all_configs` | 崩溃或并发写 → 全部历史损坏 |

### 4.2 🔴 工程债（阻碍迭代速度）
| # | 问题 | 证据 |
|---|------|------|
| E1 | `api.py` 117KB / 约 2500 行 / 120+ 方法的上帝类：窗口管理、聊天、剪贴板、文件整理、ComfyUI、托盘、配置全部混在 `AppAPI` 一个类里 | `api.py` 全文 |
| E2 | 前端无构建体系：`app.js` 4762 行单文件、`style.css` 3274 行、`index.html` 724 行，全部手写全局作用域 | `ai_ui_assistant/` |
| E3 | **零测试**：全仓无任何 `test_*.py`；核心逻辑（配置合并、文件整理、OS 指令解析）改动只能靠手测 | find 结果 |
| E4 | **无依赖声明**：没有 `requirements.txt` / `pyproject.toml`，README 里靠手敲 `pip install` 列表 | 仓库根目录 |
| E5 | 日志靠 `print`，无 logging 体系、无滚动文件、无级别 | `api.py` 多处 print |
| E6 | 仓库卫生差：根目录残留 `fix_js.py` / `debug_js.log` / `float_lines.txt`，`scratch/` 7 个临时脚本，`scripts/` 堆了 26 个一次性 modify/patch 脚本 | 根目录、`scripts/`、`scratch/` |
| E7 | 工作区有 256 行未提交改动（内置浏览器 + 深度思考滑块），无提交信息、无验证记录 | `git diff --stat` |

### 4.3 🟡 功能短板（与标杆产品的差距）
| # | 短板 | 说明 |
|---|------|------|
| F1 | 无自动更新实现 | 配置里已有 `auto_update` / `update_notify` 字段，但没有任何更新检查 / 下载逻辑，属于「UI 承诺了但后端没做」 |
| F2 | 无长期记忆 | 对话历史只是存储，AI 无法跨会话记住用户偏好 / 项目上下文 |
| F3 | 无语音交互 | 无 STT 输入、无 TTS 播报，桌宠「会说话」是天然的匹配场景 |
| F4 | 无截图 / 屏幕理解 | OS Agent 看不到屏幕，只能靠文件操作盲操 |
| F5 | 工具调用是「提示词约定 JSON 字符串」而非原生 Function Calling | `execute_os_action(action_json_str)` 靠模型自觉输出合法 JSON，脆弱且无法流式确认 |
| F6 | 无会话搜索 | 历史多了以后找不回「上次那个答案」 |
| F7 | 无知识库（RAG） | 不能把本地文档喂给 AI 问答 |
| F8 | 无定时任务 | 「每天 9 点整理下载文件夹」这类场景做不了 |
| F9 | 新代码一致性回退：`dock-btn-browser` 又用回了原生 `prompt()`（v1.2.0 刚全量替换 alert→Toast） | `app.js` 未提交改动 |
| F10 | macOS 支持标记为实验性，无持续验证 | README |

## 5. Solution（解决方案方向）

### 5.1 Benchmark Analysis（标杆分析）

| 标杆 | 它做对了什么 | MeowHub 应借鉴 | 差异化守住点 |
|------|------------|---------------|-------------|
| **Cherry Studio / ChatBox** | 多 Provider 管理、模型库、知识库、助手预设 | Provider/模型数据结构、RAG 入口形态 | 它们是「聊天工具」，我们是「桌面 Agent + 桌宠」 |
| **Open Interpreter** | 结构化工具调用、确认机制、代码执行沙盒 | 原生 Function Calling + 危险操作二次确认 | 它是 CLI/无 GUI；我们有常驻 UI 和宠物人格 |
| **Raycast / PowerToys Run** | 全局热键 + Spotlight 指令面板 + 插件生态 | 快捷指令面板扩展性 | 同上，加上情感化层 |
| **桌面宠物类（Desktop Goose 等）** | 情感陪伴、桌面临场感 | 宠物状态与 AI 状态联动 | 它们没有 AI 大脑；我们的宠物「真的会干活」 |

**定位一句话**：桌面宠物形态的本地优先 AI Agent 工作站——Cherry Studio 的多模型能力 × Open Interpreter 的执行能力 × 桌宠的陪伴感。

### 5.2 Before/After Comparison（前后对比）

| 维度 | 现状（v1.2.0） | 目标（v2.x） |
|------|---------------|-------------|
| 数据安全 | Key 明文、删除物理不可恢复、历史单文件裸写 | keyring 加密、删除进回收站、SQLite + 原子写 + 自动备份 |
| 代码结构 | 1 个 2500 行上帝类 + 4762 行 JS | 按域拆分的 Python 包 + 模块化前端 |
| 质量保障 | 零测试、零 CI、手测 | 核心逻辑 pytest 覆盖 + GitHub Actions 每次提交自动跑 |
| 新人上手 | 无依赖清单，README 手敲 pip | `pip install -e .` 一条命令，PyInstaller 自动出包 |
| Agent 能力 | 提示词约定 JSON、盲操文件 | 原生 Function Calling + 屏幕理解 + 长期记忆 + 定时任务 |
| 迭代节奏 | 改一处怕崩全局（无回归保护） | 分层重构后各模块独立演进 |

### 5.3 Scope（In / Out）

| In Scope（本规划覆盖） | Out of Scope（明确不做） |
|----------------------|------------------------|
| 安全加固（密钥存储、删除确认、权限分级落地） | 多用户 / 云端同步账号体系 |
| 工程化重构（模块拆分、测试、CI、依赖管理） | 移动端 / Web 版 |
| OS Agent 升级（Function Calling、屏幕理解、定时任务） | 自训模型 / 微调 |
| 记忆系统（会话内摘要 + 跨会话长期记忆） | 商业化 / 付费墙 |
| 语音交互（STT/TTS） | macOS 一等公民支持（仅维持可用，不投入新特性） |
| 桌宠养成系统（与 AI 联动的状态机） | 插件市场（推迟到社区有真实需求后） |
| 自动更新真实实现 | |

### 5.4 Phasing（分期规划）⭐ 本项目核心章节

> 原则：**先固本（安全 + 工程化），再长能力（Agent + 记忆），最后做差异化（养成 + 语音）**。
> 每期周期按「个人业余开发」节奏估算，完成一期发一个 tag。

#### Phase 0 — v1.2.1 固本止损（约 1 周，工作量：小）
| 任务 | 说明 | 验收 |
|------|------|------|
| 提交或整理工作区 256 行改动 | 内置浏览器 / 深度思考滑块先收尾：`prompt()` 换成主题化输入框（修复 F9） | git status 干净，功能手测通过 |
| 仓库大扫除 | `fix_js.py`/`debug_js.log`/`float_lines.txt`/`scratch/` 删除；`scripts/` 26 个一次性脚本归档到 `scripts/archive/` | 根目录只剩必要文件 |
| 补 `requirements.txt`（或 `pyproject.toml`） | 锁定 pywebview / openai / psutil / pystray / pillow 及版本范围 | 新环境 `pip install -r requirements.txt && python main.py` 可跑 |
| 删除改回收站 | `delete_item` 改用 `send2trash`；删除前按 `agent_control_level` 弹确认（修复 P2） | AI 删除的文件可在回收站找回 |
| 权限空壳最小止损（决策点，见 plans/phase0_stability.md Task 4b） | `execute_os_action` 入口读 `agent_control_level`，`ask` 级别直接拒绝四类高危动作（delete/write/powershell/python）；完整分级留 Phase 1 | 默认配置下高危操作被拦截并提示去设置切换权限 |
| 配置写入原子化 + 自动备份 | `save_all_configs` 改「写临时文件→替换」，每次写前滚动备份上一版（缓解 P5） | kill -9 模拟后配置不损坏 |

#### Phase 1 — v1.3 工程化重构（约 2-3 周，工作量：中，**依赖 Phase 0**）
| 任务 | 说明 | 验收 |
|------|------|------|
| `api.py` 拆包 | 拆为 `meowhub/` 包：`chat.py`（对话/流式）、`agent.py`（OS 指令）、`files.py`（整理/沙盒）、`clipboard.py`、`drawing.py`（ComfyUI）、`windows.py`（窗口/托盘/热键适配）、`config_store.py`。`AppAPI` 保留为 pywebview 暴露面的薄壳，转发到各模块（对外 JS 接口零变化） | 前端零改动，功能全量回归通过 |
| API Key 加密 | Windows 用 `keyring`（DPAPI），Mac 用 Keychain；JSON 里只存 provider/base（修复 P1） | `api_credentials.json` 中不再出现明文 key |
| logging 体系 | 统一 `logging` + RotatingFileHandler 替代 print；OS Agent 每次执行落审计日志（谁/何时/什么命令） | `logs/` 产生滚动日志，含 Agent 审计线 |
| pytest 基础测试 | 优先覆盖：`config.py` 合并/迁移逻辑、`execute_os_action` 全 action 解析（含非法输入）、文件整理 plan 生成与回退 | `pytest` 全绿，覆盖率报告可出 |
| GitHub Actions CI | push 时跑 lint（ruff）+ pytest + PyInstaller 打包冒烟 | 每次提交有绿勾 |
| OS Agent 权限分级真落地 | `run_powershell` 不默认 admin；`ask` 级别下高危 action（删除/写文件/PowerShell）逐条弹确认（修复 P3） | 默认配置下高危操作必经用户确认 |

#### Phase 2 — v1.4 智能体进化（约 3-4 周，工作量：大，**依赖 Phase 1**）
| 任务 | 说明 | 验收 |
|------|------|------|
| 原生 Function Calling | DeepSeek/Kimi 均支持 tool calls；把 OS 动作注册为结构化工具，替代 JSON 字符串解析（修复 F5） | 工具调用成功率对比提示词方案有提升（记录两版各 20 次任务成功率） |
| 屏幕理解 | 截图热键 /「看看我的屏幕」→ 视觉模型（可用 Kimi/OpenAI 兼容 vision）分析后联动 OS Agent | 「帮我把屏幕上这个按钮关掉」类任务可完成 demo |
| 长期记忆 | 两层：会话自动摘要 + 跨会话用户画像/偏好，存本地 SQLite；设置里可查看/编辑/清空 | 「记住我喜欢用 PowerShell」跨会话生效 |
| 会话存储迁移 SQLite | sessions 从 JSON 迁到 SQLite + FTS5 全文搜索（修复 F6，根治 P5） | 旧 JSON 自动迁移；会话搜索 <200ms |
| 定时任务 | 内置调度器（APScheduler）：定时提醒、定时整理文件夹，由 Agent 执行 | 「每天 21:00 清理下载目录」可配置并执行 |
| 知识库 RAG（可选，时间盒 1 周） | 本地文档（md/pdf/txt）向量化（bge-small / chromadb），对话可 @知识库 | 3 篇文档场景下能正确引用出处 |

#### Phase 3 — v1.5+ 差异化体验（约 3-4 周，工作量：中，**依赖 Phase 2 的 Agent 状态总线**）
| 任务 | 说明 | 验收 |
|------|------|------|
| 桌宠养成系统 | 宠物状态机（心情/饥饿/亲密度）与使用行为联动：完成 Agent 任务加好感、长期不用会「睡觉」；宠物动画反映 AI 工作状态（思考/执行/完成） | 宠物状态可持久化，动画 ≥6 种状态 |
| 语音交互 | STT（本地 faster-whisper 或系统 API）+ TTS 播报（edge-tts，免费）| 按住热键说话可输入；可选朗读回复 |
| 自动更新实现 | 启动时查 GitHub Releases，下载差量提示安装（配已有 `auto_update` 配置项）（修复 F1） | 发一个测试 release，旧版本能收到升级提示 |
| 快捷指令面板增强 | Spotlight（Alt+Shift+Space）支持自定义指令 / 提示词直达 | 用户可自定义 ≥5 条指令 |

## 6. Success Metrics（成功指标）

| 指标类型 | 指标名称 | 目标值 |
|---------|---------|-------|
| 核心指标 | OS Agent 任务一次成功率（20 个标准任务集） | v1.2.0 基线 → v1.4 提升 20%+ |
| 核心指标 | 崩溃 / 数据损坏事故 | 0 起（回收站找回 + 备份可恢复） |
| 观测指标 | 新环境从 clone 到跑通耗时 | < 10 分钟（依赖清单 + 文档） |
| 观测指标 | pytest 覆盖率（核心模块 config/agent/files） | ≥ 60% |
| 观测指标 | GitHub Star 增长 | Phase 3 结束时较基线 +50%（基线待记录） |
| 观测指标 | `MeowHub_Latest.exe` 月下载量 | 建立统计后环比为正 |

## 7. Risks & Mitigation（风险评估）

| 风险类型 | 风险描述 | 应对措施 |
|---------|---------|---------|
| 技术风险 | **重构引入回归**：api.py 拆包动到 pywebview 暴露面，JS 接口多 | 拆包前先冻结接口清单（从 app.js 提取全部 `pywebview.api.*` 调用做契约测试）；对外签名零变化 |
| 技术风险 | Function Calling 在小模型 / Ollama 本地模型上不可用或质量差 | 保留提示词 JSON 通道作为降级路径，按模型能力自动切换 |
| 安全风险 | Agent 权限放大后提示词注入攻击面变大 | 危险操作白名单 + 逐条确认 + 审计日志；默认权限保持 `ask` |
| 时间风险 | 个人业余开发，Phase 2 工作量大易烂尾 | 每个任务时间盒化；RAG 等可选功能允许砍掉；每期结束必须发 tag 保持发布节奏 |
| 兼容风险 | SQLite / keyring 迁移伤及老用户数据 | 迁移前自动备份旧 JSON；提供回滚脚本 |

## 8. Feedback Loops（反馈闭环）

### 8.1 Stakeholders Feedback
- **关键利益相关者** — 项目作者（本人）+ GitHub issue 中的社区用户
- **跟踪和记录反馈** — 沿用 `docs/bugs_and_memory/YYYY-MM-DD.md` 现象→根因→修复→教训四段式（已有良好实践，保留）；社区反馈走 GitHub Issues + Discussions
- **反馈优先级排序** — 安全事故 > 数据丢失 > 高频路径 bug > 新功能

### 8.2 A/B Testing
> ⚠️ TBD — 桌面单机应用不适合传统 A/B；替代方案：Function Calling vs 提示词 JSON 用同一组 20 任务做离线对比评测（已写入 Phase 2 验收）。

### 8.3 Before/After Data
每期发版时记录：任务成功率、启动耗时、内存占用、exe 体积，写入 `docs/requirements/review-log.md` 附表。

## 9. Product Requirements（产品需求摘要）

1. **安全默认**：所有破坏性操作可撤销（回收站 / 回退），默认权限 `ask`，管理员权限必须显式开启
2. **本地优先**：记忆、历史、知识库全部本地存储；使用云模型时明确提示数据出境
3. **接口稳定**：pywebview JS API 是对外契约，重构期签名零变化
4. **渐进交付**：每个 Phase 独立可用、独立发版，任何时刻 master 可发布

## 10. UI/UX Requirements（设计需求摘要）

1. 延续 Soft-Cute 萌系语言，新功能（语音按钮 / 定时任务面板 / 记忆管理页）复用现有圆角 + 磨砂 + Toast 组件体系
2. **禁止原生弹窗**：所有新交互一律使用主题化 Toast / 模态框（把 F9 教训写入贡献规范）
3. 桌宠是差异化资产：所有新 Agent 能力必须有「宠物状态可视化」出口（执行任务时宠物有对应动画）
4. 深度思考滑块 / 权限开关这类「档位型」控件统一用滑块 + tooltip 模式（沿用 v1.2.0 模式）

---

## 附录 A：调研数据快照（2026-09-06）

- 代码规模：`api.py` 117KB/约2500行/120+方法；`app.js` 4762 行；`style.css` 3274 行；`index.html` 724 行
- 测试 / CI / 依赖声明：均无
- 仓库残留：根目录 3 个临时文件 + `scratch/`（7 文件）+ `scripts/`（26 个一次性脚本）
- git 历史：11 次提交，最新 d41e619（v1.2.0）
- 二次调研补充发现：`agent_control_level` 死配置（后端零执行）；psutil 已不再使用（README 安装命令过时）；无 requests 依赖（api.py 用 urllib）
- 已实现功能：多模型对话（DeepSeek/Kimi/Ollama/自定义）、深度思考分级、虚拟桌宠、剪贴板气泡+历史、智能文件整理（含回退）、PowerShell/CMD/Python 沙盒、OS Agent 九类动作、ComfyUI 本地绘图 + 云绘图、20+ 角色提示词库、多会话管理、双窗口+全局热键、托盘、开机自启、主题、系统监控、内置浏览器（未提交）
