import os

file_path = r"d:\个人项目\ai_assistant\api.py"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target1 = """    def close_app_completely(self):
        \"\"\"Terminate the process without re-entering pywebview's closing event.\"\"\"
        self._kill_comfyui()
        import os
        os._exit(0)"""

replacement1 = """    def close_app_completely(self):
        \"\"\"Terminate the process without re-entering pywebview's closing event.\"\"\"
        self._kill_comfyui()
        
        try:
            if getattr(self, '_pet_window', None):
                self._pet_window.destroy()
        except Exception:
            pass
            
        try:
            if getattr(self, '_float_window', None):
                self._float_window.destroy()
        except Exception:
            pass

        import os
        os._exit(0)"""

target2 = """        if not self._main_window_visible:
            import os
            os._exit(0)
        return "closed\""""

replacement2 = """        if not self._main_window_visible:
            self.close_app_completely()
        return "closed\""""

target3 = """    def exit_app(self):
        import os
        os._exit(0)"""

replacement3 = """    def exit_app(self):
        self.close_app_completely()"""

c = 0
if target1 in content:
    content = content.replace(target1, replacement1)
    c += 1
if target2 in content:
    content = content.replace(target2, replacement2)
    c += 1
if target3 in content:
    content = content.replace(target3, replacement3)
    c += 1

print(f"Replaced {c} targets.")
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
