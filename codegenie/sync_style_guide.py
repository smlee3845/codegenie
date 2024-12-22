import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from style_guide import generate_style_guide

class StyleGuideSyncHandler(FileSystemEventHandler):
    """
    Handler for file system events to sync the style guide.
    """
    def __init__(self, style_path, output_path, example_code):
        self.style_path = style_path
        self.output_path = output_path
        self.example_code = example_code

    def on_modified(self, event):
        if event.src_path == self.style_path:
            print(f"Detected changes in {self.style_path}. Regenerating style guide...")
            generate_style_guide(self.output_path, self.style_path, self.example_code)

def watch_style_file(style_path, output_path, example_code=None):
    """
    Watch the style configuration file for changes and regenerate the style guide.
    """
    event_handler = StyleGuideSyncHandler(style_path, output_path, example_code)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(style_path), recursive=False)
    observer.start()

    print(f"Watching {style_path} for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
