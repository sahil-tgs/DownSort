from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Monitor:
    def __init__(self, directory, sorter=None):
        self.directory = directory
        self.sorter = sorter
        self.observer = Observer()

    def start(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_created = self.on_created
        self.observer.schedule(event_handler, self.directory, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()

    def on_created(self, event):
        if self.sorter:
            self.sorter.sort_files(self.directory)
