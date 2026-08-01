import re

with open('api.py', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(
    r'(\s+if "256k" in m_id_lower or "k2\.6" in m_id_lower or "k2\.5" in m_id_lower:\s+context = "256K"\s+)'
    r'(elif "128k" in m_id_lower or "chat" in m_id_lower:\s+# DeepSeek chat is 128k\s+context = "128K"\s+)'
    r'(elif "64k" in m_id_lower or "reasoner" in m_id_lower:\s+# DeepSeek reasoner is 64k output context\s+context = "64K"\s+)'
    r'(elif "32k" in m_id_lower:\s+context = "32K"\s+)'
    r'(elif "8k" in m_id_lower:\s+context = "8K"\s+)'
    r'(elif model_type == "drawing":\s+context = ".*?画图.*?"\s+)', re.DOTALL)

replacement = r'''\1elif "128k" in m_id_lower or "chat" in m_id_lower or "v4" in m_id_lower or "v3" in m_id_lower:
                          context = "128K"
                      elif "64k" in m_id_lower or "reasoner" in m_id_lower or "r1" in m_id_lower:
                          context = "64K"
                      elif "32k" in m_id_lower:
                          context = "32K"
                      elif "8k" in m_id_lower:
                          context = "8K"
                      elif provider == "deepseek" and context == "8K":
                          context = "128K"
                      \6'''

content = pattern.sub(replacement, content)

pattern2 = re.compile(
    r'(elif provider == "deepseek":\s+)'
    r'(if "chat" in m_id_lower:\s+name = "DeepSeek-V3"\s+)'
    r'(elif "reasoner" in m_id_lower:\s+name = "DeepSeek-R1")', re.DOTALL)

replacement2 = r'''\1if "v4" in m_id_lower:
                              name = "DeepSeek-V4"
                          elif "chat" in m_id_lower or "v3" in m_id_lower:
                              name = "DeepSeek-V3"
                          elif "reasoner" in m_id_lower or "r1" in m_id_lower:
                              name = "DeepSeek-R1"'''

content = pattern2.sub(replacement2, content)

with open('api.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
