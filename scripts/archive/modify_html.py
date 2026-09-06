import sys

with open('ai_ui_assistant/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '<div id="dock-status-orb" class="status-orb idle" title="系统硬件负荷监视" style="margin: 0 auto; width: 12px; height: 12px; cursor: pointer;"></div>'
replacement = '<div id="dock-status-orb" class="status-orb idle" title="戳戳星喵~" style="margin: 0 auto; width: 22px; height: 22px; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 13px; user-select: none; transition: transform 0.2s;">🐾</div>'

if target in content:
    content = content.replace(target, replacement)
    with open('ai_ui_assistant/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated successfully.")
else:
    print("Target not found in index.html!")
    # Try a looser match
    import re
    new_content = re.sub(r'<div id="dock-status-orb"[^>]+>.*?</div>', replacement, content, flags=re.DOTALL)
    if new_content != content:
        with open('ai_ui_assistant/index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("index.html updated with regex.")
