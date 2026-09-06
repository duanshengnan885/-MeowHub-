import sys, os

with open('main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles
content = content.replace('title="MeowHub"', 'title="星喵 (MeowHub)"')
content = content.replace('pystray.Icon("MeowHub", image, "MeowHub", menu)', 'pystray.Icon("MeowHub", image, "星喵 (MeowHub)", menu)')
content = content.replace('MessageBoxW(0, msg, "MeowHub", 0)', 'MessageBoxW(0, msg, "星喵 (MeowHub)", 0)')

# Replace hwnd find
find_hwnd = '''hwnd = AppAPI._find_window_hwnd("星喵 (MeowHub)")
                    if not hwnd:
                        hwnd = AppAPI._find_window_hwnd("MeowHub")'''
content = content.replace('hwnd = AppAPI._find_window_hwnd("MeowHub")', find_hwnd)

# Add icon to webview
content = content.replace('min_size=(960, 600),', 'min_size=(960, 600),\n        icon="icon.ico",')

with open('main.py', 'w', encoding='utf-8') as f:
    f.write(content)

# Update spec
if os.path.exists('MeowHub.spec'):
    with open('MeowHub.spec', 'r', encoding='utf-8') as f:
        spec = f.read()
    import re
    if 'icon=' in spec:
        spec = re.sub(r'icon=[\'\"][^\'\"]*[\'\"]', "icon='icon.ico'", spec)
    else:
        spec = spec.replace('console=False,', "console=False,\n    icon='icon.ico',")
    with open('MeowHub.spec', 'w', encoding='utf-8') as f:
        f.write(spec)
    print('Spec updated')
print('main.py restored and icon added')
