import sys

def fix_indentation():
    with open('api.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the "elif provider == "deepseek":" part
    for i, line in enumerate(lines):
        if 'elif provider == "deepseek":' in line:
            start_idx = i + 1
            # We want:
            #                         if "v4" in m_id_lower:
            #                             name = "DeepSeek-V4"
            #                         elif "chat" in m_id_lower or "v3" in m_id_lower:
            #                             name = "DeepSeek-V3"
            #                         elif "reasoner" in m_id_lower or "r1" in m_id_lower:
            #                             name = "DeepSeek-R1"
            
            lines[start_idx] = "                        if \"v4\" in m_id_lower:\n"
            lines[start_idx+1] = "                            name = \"DeepSeek-V4\"\n"
            lines[start_idx+2] = "                        elif \"chat\" in m_id_lower or \"v3\" in m_id_lower:\n"
            lines[start_idx+3] = "                            name = \"DeepSeek-V3\"\n"
            lines[start_idx+4] = "                        elif \"reasoner\" in m_id_lower or \"r1\" in m_id_lower:\n"
            lines[start_idx+5] = "                            name = \"DeepSeek-R1\"\n"
            break
            
    with open('api.py', 'w', encoding='utf-8') as f:
        f.writelines(lines)

fix_indentation()
