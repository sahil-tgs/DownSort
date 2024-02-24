import os
import shutil

class Sorter:
    def sort_files(self, download_directory):
        # Get list of files in the download directory
        files = os.listdir(download_directory)

        # Iterate through files and sort based on extension
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(download_directory, file)

            # Ignore directories
            if os.path.isdir(file_path):
                continue

            # Extract file extension
            _, extension = os.path.splitext(file)

            # Skip if the file has no extension
            if not extension:
                continue

            # Remove the leading dot from the extension
            extension = extension[1:].lower()

            # Create a directory for the extension if it doesn't exist
            if not os.path.exists(os.path.join(download_directory, extension)):
                os.makedirs(os.path.join(download_directory, extension))

            # Move the file to the directory corresponding to its extension
            shutil.move(file_path, os.path.join(download_directory, extension, file))
