import unittest
import os
from codegenie.plugin_loader import load_plugins

class TestPluginLoader(unittest.TestCase):
    def setUp(self):
        self.plugin_dir = "tests/test_plugins"
        os.makedirs(self.plugin_dir, exist_ok=True)
        with open(f"{self.plugin_dir}/sample_plugin.py", "w") as f:
            f.write(
                """
from codegenie.plugin import CodeGeniePlugin

class SamplePlugin(CodeGeniePlugin):
    def __init__(self):
        super().__init__("SamplePlugin")
                """
            )

    def tearDown(self):
     if os.path.exists(self.plugin_dir):
        for file in os.listdir(self.plugin_dir):
            file_path = os.path.join(self.plugin_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):  # __pycache__ 같은 디렉토리 제거
                os.rmdir(file_path)
        os.rmdir(self.plugin_dir)


    def test_plugin_loader(self):
        plugins = load_plugins(self.plugin_dir)
        self.assertEqual(len(plugins), 1)  

if __name__ == "__main__":
    unittest.main()
