# scripts/local_backup.py
import os
import shutil
from datetime import datetime

def do_backup():
    try:
        # 获取项目根目录 (该脚本存放在 scripts 目录下)
        project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        project_name = os.path.basename(project_dir)
        backup_root = rf"F:\{project_name}_Backups"
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        backup_dest = os.path.join(backup_root, f"{project_name}_{timestamp}")
        
        print(f"[Backup] 正在将项目 {project_name} 备份到: {backup_root} ...")
        os.makedirs(backup_root, exist_ok=True)
        shutil.copytree(
            project_dir, backup_dest,
            ignore=shutil.ignore_patterns(
                "__pycache__", "*.pyc", ".venv", "build", "dist", ".git", "node_modules",
                "api_credentials.json", "chat_sessions.json", "app_config.json",
                "memory", "releases", "*.log", ".token_tracker.json", ".balance_snapshot.json"
            ),
            dirs_exist_ok=True
        )
        print(f"[Backup] 项目已成功备份至: {backup_dest}")
        
        # Keep only the last 10 backups
        existing_backups = []
        for d in os.listdir(backup_root):
            if d.startswith(f"{project_name}_"):
                full_path = os.path.join(backup_root, d)
                if os.path.isdir(full_path):
                    existing_backups.append(full_path)
        existing_backups.sort()
        if len(existing_backups) > 10:
            for old_backup in existing_backups[:-10]:
                try:
                    shutil.rmtree(old_backup)
                    print(f"[Backup] Deleted old backup: {old_backup}")
                except Exception as ex:
                    print(f"[Backup] Warning: Failed to delete old backup {old_backup}: {ex}")
    except Exception as e:
        print(f"[Backup] Warning: Failed to backup: {e}")

if __name__ == "__main__":
    do_backup()
