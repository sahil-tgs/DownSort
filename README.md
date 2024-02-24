# DownSort

## Description
DownSort is a Python automation script designed to help you organize your downloaded files by sorting them into folders based on their file types. It scans your download directory for new files and automatically moves them to their respective folders according to their file extensions.

## Why?
The motivation behind DownSort is to simplify file organization and improve efficiency by automating the process of sorting downloaded files. With DownSort, you no longer need to manually categorize files; it does the work for you, saving time and ensuring your files are neatly organized.

## Quick Start
1. Clone the DownSort repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies:
   ```bash
   pip install watchdog
4. Configure the project by editing the config.ini file to specify your download directory.
5. Run the main script:
    ```bash
    python src/main.py

## Usage
Once the script is running, it will continuously monitor your download directory for new files. When a new file is detected, DownSort will automatically move it to the appropriate folder based on its file type (e.g., PDF, JPG, MP3, etc.).

## Contributing
Although it is a very simple project, I would like to see how we can make this as close to a general tool or application, which is also cross platform and is better to interact with.

Feel free to add any PR, proposing to add features or fix any unknown issues.  