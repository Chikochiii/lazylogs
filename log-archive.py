#!/usr/bin/env python3
"""
===============================================
   My LazyLogs:D v1.0
   Author  : Chikochi
   GitHub  : Chikochiii/log-archive
   Description : Tool to archive & clean logs
                 for lazy people like me :3
===============================================
"""

import os
import sys
import shutil
import tarfile
import datetime

# === Configuration ===
ARCHIVE_DIR = "archives"
LOG_FILE = "archive.log"
DRY_RUN = False

# === Helper Functions ===
def log_message(msg: str):
    """Print message to console and save to archive.log"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

# === Archive logs ===
def create_archive(log_dir: str):
    """Create tar.gz archive from the log directory"""
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(ARCHIVE_DIR, archive_name)

    if DRY_RUN:
        log_message(f"[DRY RUN] Would create archive {archive_path}")
    else:
        with tarfile.open(archive_path, "w:gz") as tar:
            tar.add(log_dir, arcname=os.path.basename(log_dir))
        log_message(f"Archived logs from {log_dir} -> {archive_path}")

# === Delete old logs ===
def delete_old_logs(log_dir: str, keep_days: int):
    """Delete logs older than keep_days"""
    now = datetime.datetime.now()
    for root, _, files in os.walk(log_dir):
        for file in files:
            file_path = os.path.join(root, file)
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if (now - mtime).days > keep_days:
                if DRY_RUN:
                    log_message(f"[DRY RUN] Would delete log: {file_path}")
                else:
                    os.remove(file_path)
                    log_message(f"Deleted old log: {file_path}")


def delete_old_archives(keep_days: int):
    """Delete archives older than keep_days"""
    if not os.path.exists(ARCHIVE_DIR):
        return
    now = datetime.datetime.now()
    for file in os.listdir(ARCHIVE_DIR):
        file_path = os.path.join(ARCHIVE_DIR, file)
        if os.path.isfile(file_path):
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if (now - mtime).days > keep_days:
                if DRY_RUN:
                    log_message(f"[DRY RUN] Would delete archive: {file_path}")
                else:
                    os.remove(file_path)
                    log_message(f"Deleted old archive: {file_path}")

# Two options: non-interactive or interactive
# === Non-Interactive Mode ===
def run_non_interactive(args):
    # Extra option: --dry-run
    """Run with command line arguments"""
    global DRY_RUN
    if len(args) < 3:
        print("Usage: python log_archive.py <log_dir> <keep_logs_days> <keep_archives_days> [--dry-run]")
        sys.exit(1)

    log_dir = args[0]
    keep_logs_days = int(args[1])
    keep_archives_days = int(args[2])

    if len(args) == 4 and args[3] == "--dry-run":
        DRY_RUN = True
        log_message("DRY RUN mode enabled")

    if not os.path.isdir(log_dir):
        log_message(f"[ERROR] Invalid log directory: {log_dir}")
        sys.exit(1)

    create_archive(log_dir)
    delete_old_logs(log_dir, keep_logs_days)
    delete_old_archives(keep_archives_days)

# === Interactive Mode ===
def run_interactive():
    """Run in interactive mode with menu"""
    global DRY_RUN
    log_dir = ""
    keep_logs_days = 7
    keep_archives_days = 30

    while True:
        print("\n=== My Log Archive Tool ===")
        print("1. Set log directory")
        print("2. Set how many days to keep logs")
        print("3. Set how many days to keep archives")
        print("4. Run archive process")
        print("5. Enable/Disable DRY RUN mode")
        print("6. Exit")

        choice = input("Choose an option [1-6]: ")

        if choice == "1":
            log_dir = input(f"Enter log directory [{log_dir or '/var/log'}]: ") or (log_dir or "/var/log")
            if not os.path.isdir(log_dir):
                log_message("[ERROR] Log directory does not exist.")
                log_dir = ""
            else:
                log_message(f"Log directory set to {log_dir}")

        elif choice == "2":
            keep_logs_days = int(input(f"Keep logs for how many days [{keep_logs_days}]: ") or keep_logs_days)
            log_message(f"Logs older than {keep_logs_days} days will be deleted.")

        elif choice == "3":
            keep_archives_days = int(input(f"Keep archives for how many days [{keep_archives_days}]: ") or keep_archives_days)
            log_message(f"Archives older than {keep_archives_days} days will be deleted.")

        elif choice == "4":
            if not log_dir:
                log_message("[ERROR] Please set log directory first.")
            else:
                create_archive(log_dir)
                delete_old_logs(log_dir, keep_logs_days)
                delete_old_archives(keep_archives_days)
                log_message("Archive process completed.")

        elif choice == "5":
            DRY_RUN = not DRY_RUN
            log_message(f"DRY RUN mode {'enabled' if DRY_RUN else 'disabled'}.")

        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_non_interactive(sys.argv[1:])
    else:
        run_interactive()
