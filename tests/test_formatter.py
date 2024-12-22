import unittest
import json
import os
from codegenie.formatter import format_code

class TestFormatter(unittest.TestCase):
    def setUp(self):
        self.style_path = "settings/custom_style.json"
        self.file_path = "tests/sample_code.py"
        self.style_data = {
            "line_length": 100,
            "string_quotes": "double",
            "trailing_commas": True
        }
        self.sample_code = """def example_function(a, b):\n    return (a + b)\n"""

        os.makedirs("settings", exist_ok=True)
        os.makedirs("tests", exist_ok=True)
        with open(self.style_path, "w") as f:
            json.dump(self.style_data, f)
        with open(self.file_path, "w") as f:
            f.write(self.sample_code)

    def tearDown(self):
        if os.path.exists(self.style_path):
            os.remove(self.style_path)
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_format_code(self):
        format_code(self.file_path, style_config=self.style_data)
        with open(self.file_path, "r") as f:
            content = f.read()

        self.assertNotIn("return (a + b)", content)
        self.assertIn("return (a + b,)", content)

if __name__ == "__main__":
    unittest.main()
