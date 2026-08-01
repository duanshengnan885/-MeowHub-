import sys
with open('ai_ui_assistant/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

bad_string = "floatEl.style.transform = \translate(px, -px) scale(1.3);"
new_string = "floatEl.style.transform = `translate(${Math.random() * 40 - 20}px, -${Math.random() * 40 + 50}px) scale(1.3)`;"

if bad_string in content:
    content = content.replace(bad_string, new_string)
else:
    # try regex because of the weird backtick and tab
    import re
    content = re.sub(r'floatEl\.style\.transform = .*?;', new_string, content)

with open('ai_ui_assistant/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("app.js fixed")
