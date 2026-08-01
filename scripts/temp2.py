with open('api.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'name = "DeepSeek-V3"' in line:
        for j in range(i-30, i+15):
            if j < len(lines):
                print(f"{j+1}: {lines[j].rstrip()}")
        break
