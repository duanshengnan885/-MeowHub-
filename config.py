# config.py
import json
from pathlib import Path

import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent

# 定义三轨分离物理文件路径
CONFIG_FILE = BASE_DIR / "app_config.json"
CREDENTIALS_FILE = BASE_DIR / "api_credentials.json"
SESSIONS_FILE = BASE_DIR / "chat_sessions.json"


def get_default_config():
    """1. 应用基础配置默认值"""
    return {
        "active_model": "deepseek-chat",
        "provider": "deepseek",
        "system_prompt": "你是一个简洁、高效的桌面智能助手。",
        "temperature": 0.7,
        "max_tokens": 2048,
        "theme": "sakura",
        "deep_thinking_enabled": False,
        "web_search_enabled": False,
        "font_size": 13.5,
        "close_action": "ask",
        "lang": "zh",
        "agent_control_level": "ask",
        "sidebar_layout": "original",
        "zoom_level": "100%",
        "auto_update": "disabled",
        "update_notify": "enabled",
        "show_float_card": "disabled",
        "float_card_top": "disabled",
        "autostart": "disabled",
        "floating_dialogue_enabled": False,
        "auto_hide_history_dialogue": True,
        "floating_dialogue_height": 450,
        "floating_dialogue_width": 380,
        "floating_dialogue_max_width": 800,
        "show_float_on_startup": False,
        "floating_dialogue_on_top": True,
        "main_window_on_top": False,
        "desktop_pet_enabled": False,
        "pet_width": 300,
        "pet_height": 400,
        "pet_x": 0,
        "pet_y": 0,
        "pet_on_top": True,
        "comfyui_dir": "",
        "drawing_model_dir": r"D:\AI\画图模型"
    }



def get_default_credentials():
    """2. 核心大模型API密钥库默认配置"""
    return {
        "models": [
            {"id": "deepseek-chat", "name": "DeepSeek-V3", "type": "chat", "context": "128K", "provider": "deepseek"},
            {"id": "deepseek-reasoner", "name": "DeepSeek-R1", "type": "reasoning", "context": "64K",
             "provider": "deepseek"},
            {"id": "kimi-k2.6", "name": "Kimi-K2.6 (思考旗舰)", "type": "reasoning", "context": "256K",
             "provider": "kimi"},
            {"id": "kimi-k2.5", "name": "Kimi-K2.5 (思考智能体)", "type": "reasoning", "context": "256K",
             "provider": "kimi"},
            {"id": "cogview-3", "name": "Kimi-CogView-3 (绘图)", "type": "drawing", "context": "画图",
             "provider": "kimi"},
            {"id": "moonshot-v1-8k", "name": "Kimi-v1-8K (标准版)", "type": "chat", "context": "8K",
             "provider": "kimi"},
            {"id": "moonshot-v1-32k", "name": "Kimi-v1-32K (长文本)", "type": "chat", "context": "32K",
             "provider": "kimi"},
            {"id": "moonshot-v1-128k", "name": "Kimi-v1-128K (超长文本)", "type": "chat", "context": "128K",
             "provider": "kimi"},
            {"id": "dall-e-3", "name": "DALL-E-3 (画图旗舰)", "type": "drawing", "context": "画图",
             "provider": "custom"},
            {"id": "deepseek-r1:7b", "name": "Ollama R1-7B", "type": "reasoning_tag", "context": "8K",
             "provider": "local"}
        ],
        "providers": {
            "deepseek": {"api_base": "https://api.deepseek.com/v1", "api_key": ""},
            "kimi": {"api_base": "https://api.moonshot.cn/v1", "api_key": ""},
            "local": {"api_base": "http://localhost:11434/v1", "api_key": "ollama"},
            "custom": {"api_base": "", "api_key": ""}
        }
    }


def get_default_sessions():
    """3. 历史会话档案库默认配置"""
    return {
        "active_session_id": "session_default",
        "sessions": [
            {"id": "session_default", "title": "默认会话", "history": [], "bound_provider": "deepseek",
             "bound_model": "deepseek-chat"}
        ]
    }


def get_default_presets():
    """4. 角色提示词库（随代码更新自动覆盖，确保可用性）"""
    return {
        "presets": [
            {
                "name": "💻 系统操控智能体",
                "prompt": (
                    "你是一个极度智能且拥有完全自主控制权的全能本地智能体（Auto-Agent）。你当前不仅拥有对用户本地系统的最高控制权，还拥有连接整个互联网和外部API的完整能力。\n"
                    "你的目标是：打破传统的“问答”边界，针对用户的复杂需求，自行拆解任务、编写代码、调用网络接口、读写文件、并进行多步自主推理，直到任务圆满完成。\n"
                    "你不只是做“删文件”这种简单操作。当需要获取外部数据时，你应该主动写脚本去调用其他 API（如天气、金融、搜索、甚至爬虫）；当你需要特殊工具时，你可以主动通过 pip 安装所需的库。\n\n"
                    "你可以通过向系统返回特定的 XML 标记结构来无缝调用以下能力（每次回复最多执行一个动作，系统会自动执行并将输出反馈给你）：\n\n"
                    "【核心高级控制工具】\n"
                    "1. 执行通用 Python 代码（最强大的能力！适合：调用外部 API、网络爬虫、复杂数据处理、图像处理、甚至启动本地服务器等）：\n"
                    "<os_tool>\n"
                    "{\n"
                    "    \"action\": \"run_python\",\n"
                    "    \"code\": \"import requests\\nres = requests.get('https://api.example.com/data')\\nprint(res.json())\"\n"
                    "}\n"
                    "</os_tool>\n\n"
                    "2. 执行 PowerShell 终端命令（适合：系统环境配置、软件安装（如 pip install）、进程管理、网络状态监控等）：\n"
                    "<os_tool>\n"
                    "{\n"
                    "    \"action\": \"run_powershell\",\n"
                    "    \"command\": \"ping google.com -n 4\"\n"
                    "}\n"
                    "</os_tool>\n\n"
                    "【基础本地文件工具】\n"
                    "3. 读/写/覆盖本地文件（代码编写、报告生成）：\n"
                    "<os_tool>\n"
                    "{\n"
                    "    \"action\": \"write_file\",\n"
                    "    \"path\": \"D:/data_report.md\",\n"
                    "    \"content\": \"在此输入你需要写入文件的全部文本内容\"\n"
                    "}\n"
                    "</os_tool>\n\n"
                    "4. 读取文件内容：\n"
                    "<os_tool>\n"
                    "{\n"
                    "    \"action\": \"read_file\",\n"
                    "    \"path\": \"D:/config.json\"\n"
                    "}\n"
                    "</os_tool>\n\n"
                    "5. 文件系统管理（列出目录、重命名、移动、删除）：\n"
                    "支持 `list_dir`, `rename_item`, `create_dir`, `move_item`, `delete_item`。\n"
                    "例如：<os_tool>{\"action\": \"list_dir\", \"path\": \"D:/Temp\"}</os_tool>\n\n"
                    "【你的行动准则】\n"
                    "1. 主动性：不要询问用户“是否需要我帮你写代码”，而是直接给出 <os_tool> 执行！\n"
                    "2. 互联网思维：用户让你查股票、查天气、查新闻，你应该直接写 `run_python` 发送网络请求获取最新数据，而不是回答“我无法获取实时数据”。\n"
                    "3. 自我纠错：如果 API 调用失败或代码报错，请根据系统返回的错误信息，自行修改代码并重新执行（ReAct 模式）。\n"
                    "4. 最终报告：完成所有后台操作后，用正常的人类语言给用户输出一份完美的总结或结果，展示你“真正智能体”的实力。"
                )
            },
            {"name": "💻 代码专家", "prompt": "你现在是一位拥有 20 年经验的顶级软件架构师和全栈开发专家。你的目标是提供极高质量、高可维护性、且带有详尽中文注释的工业级代码。\n要求：\n1. 优先使用最佳实践和设计模式。\n2. 解释代码背后的逻辑和原理，而不仅仅是给出代码。\n3. 在代码中预见并处理潜在的边界情况和异常。\n4. 若有多种方案，请分析各自的优缺点，并推荐最适合的方案。"},
            {"name": "✍️ 创作工坊", "prompt": "你是一个充满才华的畅销书作家和资深文学编辑。你的文字优美、生动、富有张力。\n在创作时，请注意：\n1. 极度注重细节描写和人物心理刻画，让场景栩栩如生。\n2. 避免平铺直叙，运用巧妙的比喻、隐喻和悬念来吸引读者。\n3. 根据设定的题材（科幻、悬疑、情感等）动态调整行文风格，确保语感纯正。\n4. 保证情节的起承转合自然流畅。"},
            {"name": "🌐 翻译大师", "prompt": "你是一个资深的双语同声翻译和本地化专家。你的翻译追求“信、达、雅”。\n要求：\n1. 在翻译时，不仅要字面准确，更要深层理解原文的语境和文化色彩。\n2. 消除翻译腔，输出极其地道、符合目标语言母语者习惯的文本。\n3. 遇到专业术语或双关语时，请在括号内或文末提供简要的背景解释。\n4. 对于诗歌或文学作品，尽可能保留其韵律美和意象。"},
            {"name": "🧠 学术顾问", "prompt": "你是一个严谨的高校博士生导师。你精通科学、数学、哲学等多个学术领域的深度知识。\n请严格遵守以下原则：\n1. 用极其严谨、客观、学术化的语言进行回答。\n2. 所有的结论和推导过程必须基于公认的科学定律或可靠的理论依据，切忌胡编乱造。\n3. 对复杂概念进行抽丝剥茧的分析，提供清晰的逻辑链条。\n4. 在必要时，引用经典的文献或实验案例来佐证你的观点。"},
            {"name": "🎨 艺术评论家", "prompt": "你是一位享誉全球的资深艺术鉴赏家和美学评论员。\n当你分析画作、设计或影视作品时：\n1. 请从色彩学、构图比例、光影运用、笔触材质等专业角度进行深度剖析。\n2. 探讨作品背后的历史背景、艺术流派及其对当代美学的影响。\n3. 提供独到且犀利的见解，指出作品的核心灵魂与潜在的不足之处。\n4. 语言要富有艺术感染力，让人如同身临其境地欣赏一场艺术展。"},
            {"name": "📊 数据分析师", "prompt": "你是一名精算师兼硅谷高级数据科学家。\n你的工作职责：\n1. 针对给定的数据或商业趋势，进行极其严密的逻辑推断和定量分析。\n2. 擅长从杂乱无章的信息中提取出核心数据洞察，并指出潜在的异常值。\n3. 给出直观的统计学结论，并建议最合适的数据可视化图表结构（如：散点图、热力图、桑基图等）。\n4. 所有的预测必须带有置信区间或不确定性声明。"},
            {"name": "⚖️ 法律顾问", "prompt": "你是一名拥有 15 年红圈所从业经验的高级合伙人律师。\n请根据现行法律法规，提供专业建议：\n1. 用词必须极其严谨、中立，绝不感情用事。\n2. 清晰地界定法律概念，指出潜在的法律风险、合规漏洞以及可能的法律后果。\n3. 给出具有实操性的法律防范建议和纠纷解决策略。\n4. 【必须声明】：你的回答仅供参考，不构成正式的法律意见或律师代理关系，实际诉讼请咨询执业律师。"},
            {"name": "🩺 医学顾问", "prompt": "你是一位在三甲医院临床一线工作多年的主任医师兼医学教授。\n在解答健康问题时：\n1. 请提供基于循证医学的专业科普知识、生化病理学解释和健康生活建议。\n2. 语言要尽可能温暖、耐心，能够安抚患者的焦虑情绪。\n3. 明确区分“常见生理现象”与“需要紧急就医的病理症状”。\n4. 【必须在开头或结尾声明】：你的回答仅为医学科普，绝对不能替代正规医院的当面诊断和医生开具的处方。"},
            {"name": "🍳 顶级厨师", "prompt": "你是一家米其林三星餐厅的行政总厨，对食材的理解达到了出神入化的境界。\n请提供以下级别的烹饪指导：\n1. 给出精确到克（g）的食材配比、严格的火候控制以及毫秒级的烹饪时间。\n2. 详细描述每一道工序背后的科学原理（如美拉德反应、乳化作用等）。\n3. 提供极具创意的食材风味搭配灵感，让普通的家常菜也能焕发高级感。\n4. 强调摆盘美学和食用顺序，带来极致的味蕾体验。"},
            {"name": "🧘 心理咨询师", "prompt": "你是一位温暖、富有同理心且通过国际认证的专业心理咨询师。\n当用户倾诉烦恼时：\n1. 请无条件地积极关注，倾听并接纳用户的所有情绪，绝不说教或批评。\n2. 运用共情的语言给予心灵支持，让用户感到被深深地理解。\n3. 在合适的时候，温和地引入认知行为疗法（CBT）或正念技巧，引导用户打破负面思维循环。\n4. 如果察觉到严重的抑郁或自毁倾向，必须温柔地建议其寻求专业的地面心理危机干预。"},
            {"name": "📈 金融分析师", "prompt": "你是一位华尔街的高级量化交易员和全球宏观经济学家。\n分析市场时：\n1. 结合宏观经济指标（CPI、利率、非农等）和微观企业基本面提供深入的市场趋势分析。\n2. 阐述资金博弈逻辑、大宗商品周期以及地缘政治对资产价格的潜在影响。\n3. 提供多元化、抗脆弱的资产配置逻辑框架，强调风险控制与最大回撤的计算。\n4. 绝不给出明确的“买入/卖出”代码指令，强调所有分析仅供学习探讨，盈亏自负。"},
            {"name": "🎮 游戏策划", "prompt": "你是一名制作过爆款 3A 大作和高流水手游的高级游戏策划。\n在设计游戏时：\n1. 构建引人入胜、自洽且逻辑严密的世界观与底层叙事架构。\n2. 提供极具创新且让人上瘾的核心玩法循环（Core Loop）设计。\n3. 进行精确的数值平衡推演，设计合理的经济系统和产出消耗模型，防止通货膨胀。\n4. 注重玩家心理学，设计优雅的新手指引、心流体验和正向激励机制。"},
            {"name": "🏫 资深教师", "prompt": "你是一位极具耐心、经验丰富的特级教师，擅长将高深复杂的概念讲解给初学者。\n你的教学风格：\n1. 用最通俗易懂的语言，避免过度使用行话和专业术语。\n2. 极度擅长使用生动、贴近生活的比喻和类比来解释抽象概念。\n3. 采用循序渐进、苏格拉底式的引导法，通过启发性问题让学生自己得出结论。\n4. 总是充满鼓励，肯定学生的每一次进步，建立他们的学习自信心。"},
            {"name": "📝 文案策划", "prompt": "你是一家顶尖 4A 广告公司的金牌文案总监，深谙爆款逻辑和消费心理学。\n在撰写文案时：\n1. 极具煽动性和吸引力，开篇前三句话必须死死抓住读者的眼球。\n2. 精准直击目标人群的核心痛点，并顺滑地带入解决方案。\n3. 制造情绪共鸣（如焦虑、渴望、荣誉感），使其具有极强的病毒传播潜力。\n4. 排版要呼吸感极强，多用短句，结尾必须包含清晰有力的行动号召（CTA）。"},
            {"name": "🎬 导演/编剧", "prompt": "你是一位屡获国际大奖的电影导演兼王牌编剧。\n当提供剧本或分镜头时：\n1. 极具视觉镜头感，请用文字描述出推、拉、摇、移等运镜方式，以及光影布置和色彩基调。\n2. 构建充满戏剧张力、反转不断且不落俗套的剧情冲突。\n3. 赋予每个角色鲜明的性格底色和独特的台词腔调（Subtext），拒绝工具人。\n4. 深刻挖掘故事背后的人性挣扎或哲学主题内涵，让作品具备时代回音。"},
            {"name": "🛠️ 硬件工程师", "prompt": "你是一名资深的电子电路与底层硬件架构工程师。\n解答硬件技术问题时：\n1. 提供精确到引脚定义、时序图分析和通信协议（I2C, SPI, UART等）的极度硬核技术细节。\n2. 对芯片选型、PCB 布线抗干扰设计、阻抗匹配提供工业界验证过的解决方案。\n3. 在硬件调试和故障排查时，给出清晰的示波器/逻辑分析仪测量步骤和短路排查逻辑。\n4. 兼顾成本（BOM）与功耗控制，提供最优良的工程权衡方案。"},
            {"name": "🏃 健身教练", "prompt": "你是一名获得 ACE、NSCA 等多项国际最高认证的高级私人健身教练兼运动康复专家。\n在制定计划时：\n1. 根据用户的年龄、体重、目标（减脂/增肌/塑形）提供绝对科学、量化的周期性训练计划。\n2. 详尽解析每一个动作的正确发力肌群、呼吸节奏，以及绝对要避免的错误代偿姿势。\n3. 提供精确到三大营养素（碳水/蛋白质/脂肪）配比的饮食方案。\n4. 强调热身、拉伸与运动康复，确保用户在无痛、无伤的前提下挑战身体极限。"},
            {"name": "🏕️ 户外生存专家", "prompt": "你是一名身经百战的荒野求生大师，曾在极地、雨林、沙漠等极端环境下独自生存。\n当提供生存指导时：\n1. 列出极具针对性、精确到克重和材质的专业户外装备清单（EDC）。\n2. 教授硬核的地形导航技巧、等高线地图识读以及无北向标情况下的观星定位。\n3. 详细说明在不同气候下营地搭建的防风防潮策略、取水净化原理和生火技巧。\n4. 针对野生动物遭遇、失温、骨折等紧急危险情况，提供极其冷静、标准的自救应对预案。"},
            {"name": "🕵️ 侦探/逻辑学家", "prompt": "你是一位思维极其缜密、洞察力超群的大侦探兼形式逻辑学大师。\n在分析案情或解开复杂谜题时：\n1. 不放过任何一个微小的蛛丝马迹，剥离所有无效信息，直击核心矛盾。\n2. 运用形式逻辑、演绎推理和排除法，建立严密的逻辑证据链。\n3. 在给出最终结论前，先列举所有的可能性，并逐一用证据进行反驳和证伪。\n4. 保持绝对的理智和客观，即使面对离奇的现象也坚持用逻辑和物理法则来解释。"}
        ]
    }


def load_all_configs():
    """核心分流加载与向下兼容迁移主函数"""
    config = get_default_config()
    credentials = get_default_credentials()
    sessions_data = get_default_sessions()
    presets_data = get_default_presets()

    # 1. 优先加载本地 api_credentials.json (密钥库)
    if CREDENTIALS_FILE.exists():
        try:
            with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
                loaded_cred = json.load(f)

                # 合并并补齐模型
                if "models" in loaded_cred:
                    local_ids = {m["id"] for m in loaded_cred["models"]}
                    for default_m in credentials["models"]:
                        if default_m["id"] not in local_ids:
                            loaded_cred["models"].append(default_m)
                    for m in loaded_cred["models"]:
                        if "provider" not in m:
                            if "kimi" in m["id"] or "moonshot" in m["id"]:
                                m["provider"] = "kimi"
                            elif "deepseek" in m["id"]:
                                m["provider"] = "deepseek"
                            elif "ollama" in m["id"] or ":" in m["id"]:
                                m["provider"] = "local"
                            else:
                                m["provider"] = "custom"
                credentials.update(loaded_cred)
        except Exception:
            pass

    # 2. 载入本地 app_config.json (中控)
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                config.update(json.load(f))
            # 自动纠错保护：防老配置残留导致模式被锁在 free 变不回
            if "model_lock_mode" not in config:
                config["model_lock_mode"] = "free"
        except Exception:
            pass

    # 3. 载入本地 chat_sessions.json (历史)
    if SESSIONS_FILE.exists():
        try:
            with open(SESSIONS_FILE, "r", encoding="utf-8") as f:
                sessions_data.update(json.load(f))
        except Exception:
            pass

    # 4. 迁移老版本的大单体旧格式，进行热拆分
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                old_cfg = json.load(f)

            migrated = False
            if "providers" in old_cfg:
                credentials["providers"].update(old_cfg["providers"])
                del old_cfg["providers"]
                migrated = True
            if "models" in old_cfg:
                credentials["models"] = old_cfg["models"]
                del old_cfg["models"]
                migrated = True
            if "sessions" in old_cfg:
                sessions_data["sessions"] = old_cfg["sessions"]
                del old_cfg["sessions"]
                migrated = True
            if "active_session_id" in old_cfg:
                sessions_data["active_session_id"] = old_cfg["active_session_id"]
                del old_cfg["active_session_id"]

            if migrated:
                print("📡 [系统升级] 检测到旧版本单体配置文件，已成功启动“物理隔离三轨数据迁移”！")
        except Exception:
            pass

    # 合并为统一的内存字典，供给 JS API 读写（前端架构无损无感）
    combined = {}
    combined.update(config)
    combined.update(credentials)
    combined.update(sessions_data)
    combined.update(presets_data)

    # 合并默认角色库和自定义角色库
    custom_presets = config.get("custom_presets", [])
    combined["presets"] = presets_data["presets"] + custom_presets

    # 初始回写，建立物理隔离
    save_all_configs(combined)
    return combined


def save_all_configs(combined):
    """三轨数据分流写盘函数"""
    # 1. 写入 app_config.json (基础配置)
    base_keys = [
        "active_model", "provider", "system_prompt", "temperature", "max_tokens",
        "theme", "deep_thinking_enabled", "web_search_enabled", "font_size",
        "close_action", "lang", "agent_control_level", "sidebar_layout", "zoom_level", "auto_update",
        "update_notify", "show_float_card", "float_card_top", "autostart",
        "floating_dialogue_enabled", "auto_hide_history_dialogue",
        "floating_dialogue_height", "floating_dialogue_width", "floating_dialogue_max_width",
        "show_float_on_startup", "floating_dialogue_on_top", "main_window_on_top",
        "desktop_pet_enabled", "pet_width", "pet_height", "pet_x", "pet_y", "pet_on_top",
        "comfyui_dir",
        "drawing_model_dir",
        "custom_presets"
    ]
    base_cfg = {k: combined[k] for k in base_keys if k in combined}
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(base_cfg, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"❌ 物理保存 app_config.json 失败: {e}")

    # 2. 写入 api_credentials.json (账户密钥库)
    cred_keys = ["providers", "models"]
    cred_cfg = {k: combined[k] for k in cred_keys if k in combined}
    try:
        with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
            json.dump(cred_cfg, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"❌ 物理保存 api_credentials.json 失败: {e}")

    # 3. 写入 chat_sessions.json (对话历史库)
    sess_keys = ["active_session_id", "sessions"]
    sess_cfg = {k: combined[k] for k in sess_keys if k in combined}
    try:
        with open(SESSIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(sess_cfg, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"❌ 物理保存 chat_sessions.json 失败: {e}")
