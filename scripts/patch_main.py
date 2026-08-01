import os

file_path = r"d:\个人项目\ai_assistant\main.py"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """        # 若主界面当前处于隐藏状态，说明主程序已被隐藏关闭，此处隐藏悬浮窗应导致彻底退出
        if not getattr(api, "_main_window_visible", True):
            import os
            os._exit(0)
        return False
    float_window.events.closing += on_float_closing"""

replacement = """        # 若主界面当前处于隐藏状态，说明主程序已被隐藏关闭，此处隐藏悬浮窗应导致彻底退出
        if not getattr(api, "_main_window_visible", True):
            api.close_app_completely()
        return False
    float_window.events.closing += on_float_closing"""

if target in content:
    content = content.replace(target, replacement)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
