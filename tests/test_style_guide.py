import unittest
import json
import os
from codegenie.style_guide import generate_style_guide

class TestStyleGuide(unittest.TestCase):
    def setUp(self):
        self.style_path = "settings/custom_style.json"
        self.output_path = "tests/output_style_guide.md"
        self.style_data = {
            "indentation": 4,
            "line_length": 100,
            "string_quotes": "single",
            "trailing_commas": True
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
        generate_style_guide(self.output_path, self.style_path)
        self.assertTrue(os.path.exists(self.output_path))

        with open(self.output_path, "r") as f:
            content = f.read()

        self.assertIn("# Code Style Guide", content)
        self.assertIn("Indentation: 4 spaces", content)
        self.assertIn("Line length: 100 characters", content)
        self.assertIn("String quotes: Single", content)
        self.assertIn("Trailing commas: Yes", content)
        

if __name__ == "__main__":
    unittest.main()
