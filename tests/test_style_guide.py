import unittest
import os
import json
from codegenie.style_guide import generate_style_guide

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

if __name__ == "__main__":
    unittest.main()

