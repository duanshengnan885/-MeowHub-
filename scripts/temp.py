with open('api.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'elif provider == "deepseek":' in line:
        for j in range(i-5, i+20):
            if j < len(lines):
                print(f"{j+1}: {lines[j].rstrip()}")
        break
