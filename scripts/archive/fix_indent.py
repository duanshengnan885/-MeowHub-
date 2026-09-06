import sys

def fix_indentation():
    with open('api.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # The block from line 1258 to 1275 needs to have exactly 20 spaces of indentation (or whatever 'if "256k"' has).
    # "if 256k" has 20 spaces:
    # 12345678901234567890
    #                     if "256k"
    
    for i in range(1258, 1275):
        line = lines[i]
        # Strip leading whitespace and replace with 20 spaces
        stripped = line.lstrip()
        if stripped.startswith("elif") or stripped.startswith("context ="):
            # Check indentation: "elif" should be 20 spaces, "context =" should be 24 spaces
            if stripped.startswith("elif"):
                lines[i] = " " * 20 + stripped
            elif stripped.startswith("context ="):
                lines[i] = " " * 24 + stripped
                
    with open('api.py', 'w', encoding='utf-8') as f:
        f.writelines(lines)

fix_indentation()
