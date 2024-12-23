import unittest
import os
import json
from codegenie.style_guide import generate_style_guide
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class TestStyleGuide(unittest.TestCase):
    def setUp(self):
        self.style_path = "settings/custom_style.json"
        self.output_path = "tests/output_style_guide.md"
        self.style_data = {
            "indentation": 4,
            "line_length": 88,
            "string_quotes": "single",
            "trailing_commas": False
        }
        os.makedirs("settings", exist_ok=True)
        os.makedirs("tests", exist_ok=True)
        with open(self.style_path, "w") as f:
            json.dump(self.style_data, f)

    def tearDown(self):
        if os.path.exists(self.style_path):
            os.remove(self.style_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_generate_style_guide(self):
        with open(self.style_path, "r") as f:
            style_config = json.load(f)
        generate_style_guide(self.output_path, style_config)
        self.assertTrue(os.path.exists(self.output_path))

class StyleGuideSyncHandler(FileSystemEventHandler):
    def __init__(self, style_path, output_path, example_code=None):
        self.style_path = style_path
        self.output_path = output_path
        self.example_code = example_code

    def on_modified(self, event):
        if event.src_path == self.style_path:
            print(f"Detected changes in {event.src_path}. Regenerating style guide...")
            generate_style_guide(self.output_path, self.style_path, self.example_code)
            log_dir = "logs"
            os.makedirs(log_dir, exist_ok=True)  # Ensure logs directory exists
            with open(f"{log_dir}/format_log.txt", "a") as log_file:
                log_file.write(f"Style Guide regenerated: {event.src_path}\n")

if __name__ == "__main__":
    unittest.main()
