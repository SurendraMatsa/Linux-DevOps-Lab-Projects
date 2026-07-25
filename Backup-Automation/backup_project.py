import os
import subprocess
import datetime
import sys

LOG_FILE = "/tmp/backup_execution.log"

if not os.path.exists(LOG_FILE):
    subprocess.run(['touch', 'LOG_FILE'], capture_output=True,  text=True, check=True)

def run_final_backup(source_dir, backup_dir):
    timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if not os.path.exists(source_dir):
        msg = f"[{log_timestamp}] ERROR: Source directory '{source_dir}' not found!\n"
        with open(LOG_FILE, "a") as f:
            f.write(msg)
        print(f"Error: {source_dir} does not exist!")
        return

    if not os.path.exists(backup_dir):
        print(f"Directory {backup_dir} not found. Creating it now...")
        os.makedirs(backup_dir)

    # 3. Target File Name Logic
    folder_name = os.path.basename(source_dir.strip('/'))
    archive_name = f"backup_{folder_name}_{timestamp_str}.tar.gz"
    final_backup_path = os.path.join(backup_dir, archive_name)

    print(f"Archiving {source_dir} into {final_backup_path}...")

    try:
        # 4. Running Linux tar command via Python Subprocess
        cmd = ['tar', '-czvf', final_backup_path, '-C', os.path.dirname(source_dir), folder_name]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # 5. Logging the Success
        success_msg = f"[{log_timestamp}] SUCCESS: Backup created successfully at {final_backup_path}\n"
        with open(LOG_FILE, "a") as f:
            f.write(success_msg)
            
        print("SUCCESS: Folder backed up and zipped perfectly!")
        print(f"Check logs at: {LOG_FILE}")

    except subprocess.CalledProcessError as e:
        # 6. Logging the Failure
        fail_msg = f"[{log_timestamp}] CRITICAL ERROR: Backup failed! Reason: {e.stderr}\n"
        with open(LOG_FILE, "a") as f:
            f.write(fail_msg)
        print("Critical: Backup generation failed. Check the execution log.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 final_backup_project.py <source_directory> <backup_destination_directory>")
        sys.exit(1)
        
    src = sys.argv[1]
    dest = sys.argv[2]
    
    run_final_backup(src, dest)