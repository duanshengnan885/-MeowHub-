import os
def search_dir(d, terms):
    for root, dirs, files in os.walk(d):
        for file in files:
            if file.endswith(('.html', '.js', '.py')):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        for i, line in enumerate(f):
                            for term in terms:
                                if term in line:
                                    print(f"{filepath}:{i+1}: {line.strip()}")
                except Exception:
                    pass

search_dir('.', ['系统状态', '实时看版', '系统实时看板', '系统实时看', '看板'])
