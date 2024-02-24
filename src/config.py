import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def get_download_directory(self):
        return self.config.get('Settings', 'download_directory')