import sys

with open('main.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    new_lines.append(line)
    if 'if sys.platform == "win32":' in line:
        # Check if the next few lines contain 'try:' and 'hwnd = None'
        if i + 3 < len(lines) and 'try:' in lines[i+1] and 'hwnd = None' in lines[i+2]:
            # This is one of our target blocks
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(f"{indent}    user32 = ctypes.windll.user32\n")

# Now, we also need to remove or comment out the 'user32 = ctypes.windll.user32' inside 'if not hwnd:' to avoid redundancy, though it's not strictly necessary if we declare it above.
# Actually, the error was because user32 was used later.
content = "".join(new_lines)
with open('main.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("main.py updated.")
