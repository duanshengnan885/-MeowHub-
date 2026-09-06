# Phase 0 固本止损 — 执行计划

> 关联文档：`docs/SRD-MeowHub-项目全面规划.md` §5.4 Phase 0
> 状态：**Phase 0 全部完成并通过实测验证**
> 基线：master@d41e619
> 验收总标准：git status 干净；`py_compile`/`node --check` 全绿；AI 删除文件进系统回收站；配置写盘存在 .bak 且原子替换防半写；权限止损闸门生效

## Todo

（全部完成）

## Doing

（全部完成）

## Done

- [x] **Task 1 — 收尾未提交功能（内置浏览器主题化弹窗）**
  - `ai_ui_assistant/index.html`：新增 `url-input-modal`（复用现有 modal 样式类，支持关闭与确认）
  - `ai_ui_assistant/app.js`：实现 `showUrlInputModal`/`closeUrlInputModal`/`confirmUrlInputAction`，支持 Enter 回车提交与 URL 自动补齐；`dockBtnBrowser` 改为弹窗唤起，彻底移除原生 `prompt()`（修复 F9）
  - 验证：`node --check ai_ui_assistant/app.js` 全绿
- [x] **Task 2 — 仓库大扫除与整理**
  - 删除根目录残留 `fix_js.py`、`debug_js.log`
  - `scripts/` 25 个一次性脚本归档至 `scripts/archive/`，严格保留正式工具 `cleanup.py` 和 `local_backup.py`
  - 将 `docs/scratch/release_notes.md` 归档为 `docs/manuals/release_notes_v1.2.md`，清理 scratch 下临时代码脚本
  - 验证：核心文件无死引用，git 状态整洁
- [x] **Task 3 — 规范 requirements.txt 与环境依赖**
  - 创建标准 `requirements.txt`（`pywebview`, `openai`, `pystray`, `Pillow`, `send2trash`）
  - `.venv` 安装 `send2trash>=1.8`
  - 同步修正 `README.md` 安装说明（剔除过时的 `psutil`）
  - 验证：`pip install -r requirements.txt` 无报错
- [x] **Task 4 — 删除进回收站（修复 SRD 问题 P2）**
  - `api.py` 的 `delete_item` 分支替换物理强删为 `send2trash.send2trash(path)`
  - 返回文案明确更新为「已移入系统回收站（可随时撤销恢复）」
  - 验证：单元测试实测临时文件移入系统回收站通过
- [x] **Task 4b — 权限空壳 Phase 0 最小止损（修复 SRD 问题 P3）**
  - 在 `execute_os_action` 入口加设权限闸门：当 `agent_control_level == "ask"` 时，拦截 `delete_item`/`write_file`/`run_powershell`/`run_python` 四类高危动作并提示切换权限
  - 取消 PowerShell 默认管理员提权（`run_as_admin=False`）
  - 验证：自动化测试 mock ask 级别全部拦截，control 级别正常放行
- [x] **Task 5 — 配置原子写入 + 滚动备份（解决 SRD 问题 P5）**
  - `config.py` 实现 `_atomic_save(path, data)`（临时文件 .tmp -> 刷盘 -> 复制 .bak -> `os.replace` 原子替换）
  - `save_all_configs` 三轨分流全部改走 `_atomic_save`
  - `load_all_configs` 增加 `_load_json_with_bak` 容灾回退逻辑，当主文件损坏自动从 `.bak` 恢复
  - `.gitignore` 补充 `*.bak` 与 `*.tmp` 防泄密
  - 增加 `_safe_log` 防止 Windows 控制台非 UTF-8 编码下 Unicode 打印崩溃
  - 验证：断电/损坏模拟测试通过，数据成功从 .bak 恢复
- [x] **Task 6 — 验证报告与记录归档**
  - 自动化测试套件通过（15/15 PASS）
  - 四段式记录归档至 `docs/bugs_and_memory/2026-09-06.md`

- [x] 调研：真实第三方依赖 = pywebview / openai / pystray / Pillow（psutil 已废弃不用；无 requests）
- [x] 调研：`save_all_configs` 现状为三处裸 `open("w")`，无原子性、无备份（`config.py:276-316`）
- [x] 调研：主题化弹窗可参照 `close-confirm-modal`（`app.js:2713-2732` + index.html 标记）
- [x] 调研 + 🔴 新发现：`agent_control_level` 死配置，三级权限开关后端零执行（已回写 SRD P3）
- [x] 调研：`.gitignore` 已忽略凭据/日志/备份脚本，大扫除不涉及敏感文件上库
