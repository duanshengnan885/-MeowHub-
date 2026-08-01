import sys

def rewrite_model_parsing():
    with open('api.py', 'r', encoding='utf-8') as f:
        content = f.read()

    target = '''                    model_type = "chat"
                    context = "8K"
                    
                    if "drawing" in m_id_lower or "dall-e" in m_id_lower or "cogview" in m_id_lower:
                        model_type = "drawing"
                        context = "画图"
                    elif "reasoner" in m_id_lower or "r1" in m_id_lower or "thinking" in m_id_lower or "k2.6" in m_id_lower or "k2.5" in m_id_lower:
                        model_type = "reasoning"
                        
                    if "256k" in m_id_lower or "k2.6" in m_id_lower or "k2.5" in m_id_lower:
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

    replacement = '''                    model_type = "chat"
                    context = None
                    
                    if "drawing" in m_id_lower or "dall-e" in m_id_lower or "cogview" in m_id_lower or "midjourney" in m_id_lower:
                        model_type = "drawing"
                        context = "画图"
                    elif "reasoner" in m_id_lower or "r1" in m_id_lower or "thinking" in m_id_lower or "k2.6" in m_id_lower or "k2.5" in m_id_lower or "o1" in m_id_lower or "o3" in m_id_lower:
                        model_type = "reasoning"
                        
                    import re
                    match_k = re.search(r'(\d+)k', m_id_lower)
                    if match_k and not context:
                        context = f"{match_k.group(1)}K"
                        
                    if not context:
                        if "claude-3" in m_id_lower:
                            context = "200K"
                        elif "gemini-1.5" in m_id_lower or "gemini-pro" in m_id_lower or "gemini-2" in m_id_lower:
                            context = "1024K"
                        elif "deepseek" in m_id_lower or "qwen" in m_id_lower or "yi" in m_id_lower or provider == "deepseek":
                            if "reasoner" in m_id_lower or "r1" in m_id_lower:
                                context = "64K"
                            else:
                                context = "128K"
                        elif "k2.6" in m_id_lower or "k2.5" in m_id_lower:
                            context = "256K"
                        elif model_type == "drawing":
                            context = "画图"
                        else:
                            context = "128K" # Global fallback for modern LLMs
                            
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
                    else:
                        if "deepseek" in name.lower() or provider == "deepseek":
                            name = re.sub(r'(?i)deepseek', 'DeepSeek', name)
                            name = re.sub(r'(?i)\b(v3|v4|r1|v2)\b', lambda m: m.group(1).upper(), name)
                            name = re.sub(r'(?i)\bpro\b', 'Pro', name)'''

    if target in content:
        content = content.replace(target, replacement)
        with open('api.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Success")
    else:
        print("Target not found. Will dump exact text.")
        
rewrite_model_parsing()
