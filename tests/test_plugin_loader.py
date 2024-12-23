import unittest
import os
from codegenie.plugin_loader import load_plugins
from codegenie.plugin import CodeGeniePlugin

class TestPluginLoader(unittest.TestCase):
    def setUp(self):
     self.plugin_dir = "tests/test_plugins"
     os.makedirs(self.plugin_dir, exist_ok=True)
     with open(f"{self.plugin_dir}/sample_plugin.py", "w") as f:
        f.write(
            """
from codegenie.plugin import CodeGeniePlugin

class SamplePlugin(CodeGeniePlugin):
    def __init__(self, name=None):
        super().__init__(name=name)
"""
        )


    def tearDown(self):
     if os.path.exists(self.plugin_dir):
        for root, dirs, files in os.walk(self.plugin_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(self.plugin_dir)

    def test_plugin_loader(self):
        plugins = load_plugins(self.plugin_dir)
        self.assertEqual(len(plugins), 1)  

class SamplePlugin(CodeGeniePlugin):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def execute(self, code):
        return code  

if __name__ == "__main__":
    unittest.main()
