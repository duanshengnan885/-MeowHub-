import os

file_path = r'd:\个人项目\星喵 (MeowHub)\ai_ui_assistant\app.js'
with open(file_path, 'r', encoding='utf-8', errors='surrogateescape') as f:
    content = f.read()

# Replace 1
old_1 = """            const activeAutostart = config.autostart || "disabled";
            const autostartEl = document.getElementById('config-autostart');
            if (autostartEl) autostartEl.value = activeAutostart;
        });"""
new_1 = """            const activeAutostart = config.autostart || "disabled";
            const autostartEl = document.getElementById('config-autostart');
            if (autostartEl) autostartEl.value = activeAutostart;

            const petEnabled = config.desktop_pet_enabled !== undefined ? config.desktop_pet_enabled : false;
            const petEnabledEl = document.getElementById('config-desktop-pet-enabled');
            if (petEnabledEl) petEnabledEl.value = petEnabled ? "true" : "false";

            const petOnTop = config.pet_on_top !== undefined ? config.pet_on_top : true;
            const petOnTopEl = document.getElementById('config-pet-on-top');
            if (petOnTopEl) petOnTopEl.value = petOnTop ? "true" : "false";
        });"""
if old_1 in content:
    content = content.replace(old_1, new_1)
    print('Replaced old_1')
else:
    print('Failed to find old_1')

# Replace 2 (it appears twice in the file, so replacing it will update both saveSettings and saveSettingsSilent)
old_2 = """        floating_dialogue_width: parseInt(document.getElementById('config-floating-dialogue-width').value) || 380,
        floating_dialogue_max_width: 800,
        custom_scripts: window.customScripts || [],"""
new_2 = """        floating_dialogue_width: parseInt(document.getElementById('config-floating-dialogue-width').value) || 380,
        floating_dialogue_max_width: 800,
        desktop_pet_enabled: (document.getElementById('config-desktop-pet-enabled') || {}).value === 'true',
        pet_on_top: (document.getElementById('config-pet-on-top') || {}).value === 'true',
        custom_scripts: window.customScripts || [],"""
if old_2 in content:
    content = content.replace(old_2, new_2)
    print('Replaced old_2')
else:
    print('Failed to find old_2')

with open(file_path, 'w', encoding='utf-8', errors='surrogateescape') as f:
    f.write(content)

print('Success')
