import sys

def fix_indentation():
    with open('api.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # The elif provider == "deepseek": is at line 1287.
    # The if "v4" in m_id_lower: is at 1288 (24 spaces).
    
    lines[1289] = "                            name = \"DeepSeek-V4\"\n"
    lines[1290] = "                        elif \"chat\" in m_id_lower or \"v3\" in m_id_lower:\n"
    lines[1291] = "                            name = \"DeepSeek-V3\"\n"
    lines[1292] = "                        elif \"reasoner\" in m_id_lower or \"r1\" in m_id_lower:\n"
    lines[1293] = "                            name = \"DeepSeek-R1\"\n"
            
    with open('api.py', 'w', encoding='utf-8') as f:
        f.writelines(lines)

fix_indentation()
