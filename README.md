# Folder Synchronization Script README

## Description
The Folder Synchronization script is a Python program designed to synchronize the contents of two folders: an original folder and a replica folder. It ensures that the contents of the replica folder mirror those of the original folder, copying new or modified files from the original folder to the replica folder and removing any files from the replica folder that are not present in the original folder.

## Features
- Synchronizes files and directories between two specified folders.
- Logs synchronization actions, including file copies and removals, to a designated log file.
- Allows customization of synchronization intervals.

## Requirements
- Python 3.x
- No additional Python packages are required.


## Usage
To use the Folder Synchronization script, follow these steps:

1. **Clone the Repository**: Clone the repository containing the script to your local machine.

2. **Make sure you have an existeing folder created that will serve as "original_folder"**: Otherwise it will show logs that no folder was found, the others folders the script will create alone.

3. **Navigate to the Script Directory**: Open a terminal or command prompt and navigate to the directory containing the script (`sync_folder.py`).

4. **Run the Script**: Execute the script by running the following command:
    ```
    python sync_folder.py original_folder replica_folder log_file interval
    ```
    - `original_folder`: Path to the original folder to be synchronized.
    - `replica_folder`: Path to the replica folder where synchronized files will be copied.
    - `log_file`: Path to the log file where synchronization actions will be logged.
    - `interval`: Synchronization interval in seconds (the time delay between synchronization attempts).

## Example

...>...>sync_folder.py original_folder/path replica_folder/path sync_log.txt 60 


This command will synchronize the contents of "original_folder path" with "replica_folder path" , logging synchronization actions to sync_log.txt every 60 seconds(you can chose anytime you want).



