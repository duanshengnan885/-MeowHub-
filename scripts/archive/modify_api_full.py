import sys

def modify_api():
    with open('api.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert _coerce_bool
    if "_coerce_bool" not in content:
        target1 = "    _pet_hwnd = None"
        replacement1 = '''    _pet_hwnd = None

    @staticmethod
    def _coerce_bool(val):
        if isinstance(val, str):
            return val.lower() in ('true', '1', 'yes')
        return bool(val)'''
        content = content.replace(target1, replacement1)

    # 2. Apply deepseek fix
    target2 = '''                    if "256k" in m_id_lower or "k2.6" in m_id_lower or "k2.5" in m_id_lower:
                        context = "256K"
                    elif "128k" in m_id_lower or "chat" in m_id_lower:
                        # DeepSeek chat is 128k
                        context = "128K"
                    elif "64k" in m_id_lower or "reasoner" in m_id_lower:
                        # DeepSeek reasoner is 64k output context
                        context = "64K"
                    elif "32k" in m_id_lower:
                        context = "32K"
                    elif "8k" in m_id_lower:
                        context = "8K"
                    elif model_type == "drawing":'''

    replacement2 = '''                    if "256k" in m_id_lower or "k2.6" in m_id_lower or "k2.5" in m_id_lower:
                        context = "256K"
                    elif "128k" in m_id_lower or "chat" in m_id_lower or "v4" in m_id_lower or "v3" in m_id_lower:
                        context = "128K"
                    elif "64k" in m_id_lower or "reasoner" in m_id_lower or "r1" in m_id_lower:
                        context = "64K"
                    elif "32k" in m_id_lower:
                        context = "32K"
                    elif "8k" in m_id_lower:
                        context = "8K"
                    elif provider == "deepseek" and context == "8K":
                        context = "128K"
                    elif model_type == "drawing":'''

    target3 = '''                    elif provider == "deepseek":
                        if "chat" in m_id_lower:
                            name = "DeepSeek-V3"
                        elif "reasoner" in m_id_lower:
                            name = "DeepSeek-R1"'''

    replacement3 = '''                    elif provider == "deepseek":
                        if "v4" in m_id_lower:
                            name = "DeepSeek-V4"
                        elif "chat" in m_id_lower or "v3" in m_id_lower:
                            name = "DeepSeek-V3"
                        elif "reasoner" in m_id_lower or "r1" in m_id_lower:
                            name = "DeepSeek-R1"'''

    content = content.replace(target2, replacement2)
    content = content.replace(target3, replacement3)

    with open('api.py', 'w', encoding='utf-8') as f:
        f.write(content)

modify_api()
