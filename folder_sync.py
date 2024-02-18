import os
import shutil
import time
import argparse
from datetime import datetime


def sync_folder(original_folder, replica_folder, log_file):
    # Checking if the folder exist
    if not os.path.exists(original_folder):
        print(f"Source folder '{original_folder}' does not exist.")
        return

    # If source folder exist but the replicza one don't this block of code will create it
    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)

    # Synchronize original and replica folders
    for root, dirs, files in os.walk(original_folder):
        relative_path = os.path.relpath(root, original_folder)
        replica_path = os.path.join(replica_folder, relative_path)

        # Synchronize original and replica directories
        for directory in dirs:
            replica_dir = os.path.join(replica_path, directory)

            if not os.path.exists(replica_dir):
                os.makedirs(replica_dir)

        # Synchronize original and replica files
        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_path, file)

            if not os.path.exists(replica_file) or \
                    os.stat(source_file).st_mtime > os.stat(replica_file).st_mtime:
                shutil.copy2(source_file, replica_file)
                log_action(log_file, f"Copied: {source_file} to {replica_file}")

    # Delete files in replica that are not in originall
    for root, dirs, files in os.walk(replica_folder):
        relative_path = os.path.relpath(root, replica_folder)
        source_path = os.path.join(original_folder, relative_path)

        for file in files:
            replica_file = os.path.join(root, file)
            source_file = os.path.join(source_path, file)

            if not os.path.exists(source_file):
                os.remove(replica_file)
                log_action(log_file, f"Removed: {replica_file}")


def log_action(log_file, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"
    with open(log_file, "a") as f:
        f.write(log_message + '\n')
    print(log_message)


def main():
    parser = argparse.ArgumentParser(description="Folder Synchronization Program")
    parser.add_argument("original_folder", type=str, help="Path to original folder")
    parser.add_argument("replica_folder", type=str, help="Path to replica folder")
    parser.add_argument("log_file", type=str, help="Path to log file")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    args = parser.parse_args()

    print("Starting folder synchronization...")
    print(f"Original Folder: {args.original_folder}")
    print(f"Replica Folder: {args.replica_folder}")
    print(f"Log File: {args.log_file}")
    print(f"Synchronization Interval: {args.interval} seconds\n")

    while True:
        sync_folder(args.original_folder, args.replica_folder, args.log_file)
        time.sleep(args.interval)


if __name__ == "__main__":
    main()

