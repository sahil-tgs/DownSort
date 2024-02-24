import os
from config import Config
from monitor import Monitor
from sorter import Sorter

def main():
    # Load configuration
    config = Config()
    download_directory = config.get_download_directory()

    # Create an instance of the Sorter class
    sorter = Sorter()

    # Start monitoring with the Sorter instance
    monitor = Monitor(download_directory, sorter)
    monitor.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        monitor.stop()

if __name__ == "__main__":
    main()
