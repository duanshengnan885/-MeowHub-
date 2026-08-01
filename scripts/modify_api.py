import sys

def modify_api():
    with open('api.py', 'r', encoding='utf-8') as f:
        content = f.read()

    target = '''                      if "256k" in m_id_lower or "k2.6" in m_id_lower or "k2.5" in m_id_lower:
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
                      elif model_type == "drawing":
                          context = "画图"
                          
                      name = m_id
                      if provider == "kimi":
                          if "k2.6" in m_id_lower:
                              name = "Kimi-K2.6 (思考旗舰)"
                          elif "k2.5" in m_id_lower:
                              name = "Kimi-K2.5 (思考智能体)"
                          elif "8k" in m_id_lower:
                              name = "Kimi-v1-8K (标准版)"
                          elif "32k" in m_id_lower:
                              name = "Kimi-v1-32K (长文本)"
                          elif "128k" in m_id_lower:
                              name = "Kimi-v1-128K (超长文本)"
                          elif "cogview" in m_id_lower:
                              name = "Kimi-CogView-3 (绘图)"
                      elif provider == "deepseek":
                          if "chat" in m_id_lower:
                              name = "DeepSeek-V3"
                          elif "reasoner" in m_id_lower:
                              name = "DeepSeek-R1"'''

    replacement = '''                      if "256k" in m_id_lower or "k2.6" in m_id_lower or "k2.5" in m_id_lower:
                          context = "256K"
                      elif "128k" in m_id_lower or "chat" in m_id_lower or "v4" in m_id_lower or "v3" in m_id_lower:
                          # DeepSeek chat/v4 is 128k
                          context = "128K"
                      elif "64k" in m_id_lower or "reasoner" in m_id_lower or "r1" in m_id_lower:
                          # DeepSeek reasoner is 64k output context
                          context = "64K"
                      elif "32k" in m_id_lower:
                          context = "32K"
                      elif "8k" in m_id_lower:
                          context = "8K"
                      elif provider == "deepseek" and context == "8K":
                          # DeepSeek fallback
                          context = "128K"
                      elif model_type == "drawing":
                          context = "画图"
                          
                      name = m_id
                      if provider == "kimi":
                          if "k2.6" in m_id_lower:
                              name = "Kimi-K2.6 (思考旗舰)"
                          elif "k2.5" in m_id_lower:
                              name = "Kimi-K2.5 (思考智能体)"
                          elif "8k" in m_id_lower:
                              name = "Kimi-v1-8K (标准版)"
                          elif "32k" in m_id_lower:
                              name = "Kimi-v1-32K (长文本)"
                          elif "128k" in m_id_lower:
                              name = "Kimi-v1-128K (超长文本)"
                          elif "cogview" in m_id_lower:
                              name = "Kimi-CogView-3 (绘图)"
                      elif provider == "deepseek":
                          if "v4" in m_id_lower:
                              name = "DeepSeek-V4"
                          elif "chat" in m_id_lower or "v3" in m_id_lower:
                              name = "DeepSeek-V3"
                          elif "reasoner" in m_id_lower or "r1" in m_id_lower:
                              name = "DeepSeek-R1"'''

    if target in content:
        content = content.replace(target, replacement)
        with open('api.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Success")
    else:
        print("Target not found. Let's check encoding or exact match.")

modify_api()
