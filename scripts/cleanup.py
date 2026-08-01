import sys

# 1. Modify app.js
with open('ai_ui_assistant/app.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Remove setInterval
js_content = js_content.replace('setInterval(updateSystemStatsInPopover, 3500);', '// setInterval(updateSystemStatsInPopover, 3500);')
# Remove event listener
js_content = js_content.replace("document.getElementById('dock-status-orb').addEventListener('click', toggleStatusPopover);", "// dock-status-orb removed")

with open('ai_ui_assistant/app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)


# 2. Modify api.py (We can just let it exist or rename it, but deleting the interval is enough to stop polling. Let's delete the function to be clean)
with open('api.py', 'r', encoding='utf-8') as f:
    api_content = f.read()

func_start = api_content.find('    def get_system_stats(self):')
if func_start != -1:
    func_end = api_content.find('    def minimize_to_tray(self):', func_start)
    if func_end != -1:
        api_content = api_content[:func_start] + api_content[func_end:]
        with open('api.py', 'w', encoding='utf-8') as f:
            f.write(api_content)
        print("api.py get_system_stats removed.")

print("Finished cleanup")
