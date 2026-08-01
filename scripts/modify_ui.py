import sys

def remove_dashboards():
    with open('ai_ui_assistant/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove status-popover
    start_popover = content.find('<div id="status-popover" class="status-popover" style="display: none;">')
    if start_popover != -1:
        end_popover = content.find('            <div id="dock-status-orb"', start_popover)
        if end_popover != -1:
            content = content[:start_popover] + content[end_popover:]

    # 2. Remove system-monitor-card in session-drawer
    start_monitor = content.find('        <!-- 系统硬件状态看板 -->')
    if start_monitor != -1:
        end_monitor = content.find('        <div class="session-stats">', start_monitor)
        if end_monitor != -1:
            content = content[:start_monitor] + content[end_monitor:]

    with open('ai_ui_assistant/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("HTML modifications applied.")

remove_dashboards()
