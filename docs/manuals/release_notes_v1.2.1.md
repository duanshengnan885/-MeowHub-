# 星喵 (MeowHub) v1.2.1 更新日志 (Phase 0 固本止损与数据安全)

### 🛡️ 安全加固与物理防毁 (P2 & P3)
- **回收站删除**：OS Agent 本地文件/目录删除操作全面接入 `send2trash` 系统回收站机制，彻底消除了物理粉碎删除带来的误删物理毁损风险，误删文件可随时通过系统回收站还原。
- **权限止损闸门**：当权限级别处于「💬 询问」状态时，后端主动拦截 `delete_item`、`write_file`、`run_powershell`、`run_python` 四类高危动作，并引导用户按需提权；PowerShell 终端执行默认关闭管理员提权模式 (`run_as_admin=False`)。

### 💾 存储原子化与配置容灾 (P5)
- **原子写盘与备份**：三轨配置文件（`app_config.json`、`api_credentials.json`、`chat_sessions.json`）写盘全面升级为「.tmp 写入 + 刷盘 + .bak 滚动备份 + os.replace 原子替换」机制，杜绝断电或写中断导致配置损坏或半写。
- **容灾自动恢复**：配置载入层增加容灾回退能力，若主文件发生损坏或解析异常，自动从 `.bak` 备份文件中无缝恢复。
- **编码健壮性**：增加控制台安全打印保护函数 `_safe_log`，彻底根除 Windows GBK 环境下 Unicode 字符引发的 `UnicodeEncodeError`。

### 🎨 体验一致性与去原生化 (F9)
- **主题化模态窗**：彻底移除内置浏览器入口的原生浏览器 `prompt()` 弹窗，替换为星喵 Soft-Cute 萌系毛玻璃风格的 `url-input-modal`，支持 Enter 回车提交、Escape 取消与 URL 协议前缀智能补全。

### 🧹 工程规范与仓库整理
- **依赖清单确立**：新增 `requirements.txt` 标准依赖清单，剔除全仓已不使用的 `psutil`，正式确立 `send2trash>=1.8` 依赖。
- **仓库大扫除**：清理根目录残留的临时脚本与日志，将 25 个一次性历史脚本统一归档至 `scripts/archive/`。
