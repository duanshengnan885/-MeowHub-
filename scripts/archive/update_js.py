import sys, re

sys.stdout.reconfigure(encoding='utf-8')
with open('ai_ui_assistant/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 3.2 Hardware Ring Important
content = content.replace('el.style.stroke = strokeColor;', "el.style.setProperty('stroke', strokeColor, 'important');")

# 3.4 AI Personas Injection
persona_code = '''
const AI_PERSONAS = {
    'deepseek': { icon: '🐳', accent: '#1d4ed8' },
    'kimi': { icon: '🌙', accent: '#3b82f6' },
    'gpt': { icon: '🌿', accent: '#10a37f' },
    'ollama': { icon: '🦙', accent: '#f43f5e' },
    'default': { icon: '🐾', accent: '#fb7185' }
};
function getModelPersona() {
    const activeModelId = document.getElementById('config-active-model').value.toLowerCase();
    const provider = document.getElementById('config-provider').value.toLowerCase();
    const key = Object.keys(AI_PERSONAS).find(k => activeModelId.includes(k) || provider.includes(k)) || 'default';
    return AI_PERSONAS[key];
}
'''
if 'const AI_PERSONAS =' not in content:
    content = content.replace('function createAssistantBubble() {', persona_code + '\nfunction createAssistantBubble() {')

bubble_replacement = '''function createAssistantBubble() {
    const persona = getModelPersona();
    const container = document.getElementById('chat-container');
    const wrap = document.createElement('div'); wrap.className = "bubble-wrap";
    wrap.innerHTML = `<div class="avatar ai" style="background:${persona.accent};">${persona.icon}</div><div class="bubble-content" style="width: 100%;"><div id="active-reasoning-box"><details open><summary id="active-reasoning-summary">🐾 星喵思考中...</summary><div id="active-reasoning-content" style="white-space: pre-wrap;"></div></details></div><div id="active-body-content"><div class="typing-indicator"><span></span><span></span><span></span></div></div></div>`;
    container.appendChild(wrap); scrollToBottom(true); return wrap;
}'''
content = re.sub(r'function createAssistantBubble\(\) \{.*?(?=function getActiveModelType)', bubble_replacement + '\n\n', content, flags=re.DOTALL)

# 3.3 Auto-titling hook in sendMessage
auto_title_code = '''
function autoTitleWorker(sessId, firstMsg) {
    if (!window.pywebview || !window.pywebview.api) return;
    const prompt = `你是一个极简主义的标题提取器。请将以下用户的发言浓缩为一个 3 到 6 个字的精炼标题。禁止使用任何标点符号、解释性语句或前缀。直接输出内容即可。用户发言：${firstMsg}`;
    window.pywebview.api.silent_llm_request(prompt).then(title => {
        if (title) {
            const session = window.sessions.find(s => s.id === sessId);
            if (session) {
                session.title = title.trim();
                renderSessionList();
                saveSettingsSilent();
            }
        }
    }).catch(e => console.log('Auto title failed:', e));
}
'''
if 'function autoTitleWorker' not in content:
    content = content + '\n' + auto_title_code

if 'if (activeSession.history.length === 1 && activeSession.title.includes("新会话"))' not in content:
    hook = '''    if (activeSession.history.length === 1 && activeSession.title.includes("新会话")) {
        autoTitleWorker(activeSession.id, text);
    }'''
    # We inject this right after history.push in handleFloatUserMessage/appendUserBubble
    content = content.replace('if (activeSession) { activeSession.history.push({ role: "user", content: text }); saveSettingsSilent(); }', 
    'if (activeSession) { activeSession.history.push({ role: "user", content: text }); saveSettingsSilent();\n' + hook + '\n    }')

with open('ai_ui_assistant/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Success')
