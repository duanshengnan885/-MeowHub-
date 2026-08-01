# 星喵 (MeowHub)

> **项目正式名称：星喵 (MeowHub)**

AI 驱动的桌面工作站助手，基于 Python + WebView 构建。支持多模型对话、桌面虚拟宠物互动、智能文件整理、剪贴板气泡、终端沙盒、会话管理等。

## ✨ 功能

### 🐾 桌面虚拟宠物 (全新功能)
- 桌面常驻的可爱虚拟小宠物（透明背景）
- 支持鼠标拖拽移动位置
- 宠物状态指示（思考中、开心等微动画）
- 右键菜单支持快速隐藏或退出
- 全局唤醒交互核心

### 🤖 多模型对话
- 支持 **DeepSeek**、**Kimi**、**Ollama 本地模型**、**自定义 OpenAI 兼容接口**
- 深度思考模式（Reasoning）切换
- 流式输出，Markdown 渲染
- 对话历史管理，多会话切换

### 📋 剪贴板气泡
- 复制文本时自动弹出 AI 气泡
- 一键发送到对话窗口处理
- 智能过滤，只响应有意义的文本

### 🗂️ 智能文件整理
- 选择文件夹，AI 分析文件并生成整理方案
- 自动归类、移动文件到子目录
- 支持回退操作

### 💻 终端沙盒
- 集成 PowerShell / CMD 终端
- 在 AI 对话中直接执行命令
- 命令输出实时回显

### 🪟 全新可爱风双窗口
- **全新萌系 UI**：圆角、高斯模糊、软糖配色与顺滑微动画
- **主窗口**：完整功能面板，聊天与设置中心
- **悬浮窗**：精简紧凑，始终置顶的快捷对话输入框
- 全局快捷键呼出：`Alt+Space`（快速唤醒/隐藏）/ `Alt+Shift+Space`（Spotlight 快捷指令）

### 🔧 其他
- 系统托盘常驻，匹配统一风格图标，右键菜单快速操作
- 全新的透明磨砂质感界面
- 系统状态监控（CPU/内存/网络/Ollama）
- 一键导出会话
- 开机自启（可选）
- 单实例锁，防止重复启动

## 🚀 快速开始

### 环境要求
- Python 3.12+
- Windows 10/11（主开发平台）
- macOS（实验性支持）

### 安装运行

```bash
# 克隆仓库
git clone https://github.com/duanshengnan885/-MeowHub-.git
cd 星喵(MeowHub)

# 创建虚拟环境
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS

# 安装依赖
pip install openai webview pyperclip pyinstaller Pillow pystray

# 启动
python main.py
```

Windows 用户也可直接双击 `run_win.bat`，macOS 双击 `run_mac.command`。

### 打包为 EXE

```bash
pyinstaller MeowHub.spec
```
输出在 `dist/MeowHub/` 目录。

## ⚙️ 配置

启动后点击左下角 ⚙️ 进入设置：

| 配置项 | 说明 |
|--------|------|
| API 密钥 | DeepSeek / Kimi / 自定义 API Key |
| 模型选择 | 对话模型 / 推理模型 / 绘图模型 |
| 终端 | 系统默认 / PowerShell / CMD |
| 主题 | 萌系亮色 / 质感暗色 |
| 快捷键 | Alt+Space / Alt+Shift+Space |
| 宠物设置 | 尺寸大小、透明度、固定位置 |
| 开机自启 | 启用/禁用 |

配置文件存储在 `api_credentials.json`、`app_config.json`、`chat_sessions.json`（均不上传 Git）。

## 📁 项目结构

```
星喵(MeowHub)/
├── main.py              # 入口：WebView 窗口、宠物窗口、托盘、全局热键
├── api.py               # 后端 API：聊天、剪贴板、文件整理、终端
├── config.py            # 配置管理：模型、凭据、会话预设
├── scripts/             # 开发遗留与工具脚本
├── ai_ui_assistant/
│   ├── index.html       # 主窗口前端界面
│   ├── pet.html         # 桌面宠物前端界面
│   ├── float.html       # 悬浮窗前端界面
│   ├── app.js           # 主程序与动画逻辑
│   └── style.css        # 全新萌系/磨砂主题样式
├── MeowHub.spec         # PyInstaller 打包配置
├── run_win.bat          # Windows 快速一键启动
└── run_mac.command      # macOS 快速一键启动
```

## 📝 更新日志

### v1.1.0 (全新可爱风 UI 与宠物升级版)
- ✨ **全新功能**：加入桌面虚拟宠物，支持拖拽交互与状态动画展示
- 🎨 **UI 视觉重构**：全面更新为 "Soft-Cute" 萌系风格，加入圆角、磨砂玻璃效果及大量微交互动画
- 🐛 **修复与优化**：修复了窗口退出导致进程残留的严重 Bug，优化了托盘和宠物应用的生命周期管理
- ⚡ **体验提升**：移除了后台轮询导致卡顿的剪贴板逻辑，改为被动事件监听
- 🧹 **项目清理**：整理根目录，移动所有临时测试脚本到 `scripts/`，删除废弃文件

### v1.0.0
- 多模型对话（DeepSeek / Kimi / Ollama / 自定义）
- 剪贴板气泡智能检测
- AI 智能文件整理
- PowerShell 终端沙盒
- 双窗口模式 + 全局热键
- 系统托盘 + 开机自启
- 暗色/亮色主题
- 会话管理 + 一键导出
- 系统状态监控面板
