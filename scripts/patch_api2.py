import os

file_path = r"d:\个人项目\星喵 (MeowHub)\api.py"
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith("    def close_app_completely(self):"):
        if "os._exit(0)" in lines[i+4]:
            lines[i+3] = ""
            lines[i+4] = """        try:
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
        os._exit(0)\n"""
            
    if line.startswith("        if not self._main_window_visible:"):
        if "import os" in lines[i+1] and "os._exit(0)" in lines[i+2]:
            lines[i+1] = "            self.close_app_completely()\n"
            lines[i+2] = ""
            
    if line.startswith("    def exit_app(self):"):
        if "import os" in lines[i+1] and "os._exit(0)" in lines[i+2]:
            lines[i+1] = "        self.close_app_completely()\n"
            lines[i+2] = ""

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("api.py patched successfully")
