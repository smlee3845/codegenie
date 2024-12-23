import os
from codegenie.plugin_loader import load_plugins
from codegenie.plugin import CodeGeniePlugin

class DummyPlugin(CodeGeniePlugin):
    def process(self, code: str) -> str:
        return "# Test Plugin\n" + code

def setUpModule():
    """Setup test environment."""
    plugin_dir = "tests/test_plugins"
    os.makedirs(plugin_dir, exist_ok=True)
    with open(f"{plugin_dir}/dummy_plugin.py", "w") as f:
        f.write(
            """
from codegenie.plugin import CodeGeniePlugin

class DummyPlugin(CodeGeniePlugin):
    def __init__(self, name=None):
        super().__init__(name=name)
"""
        )

def tearDownModule():
    """Clean up test environment."""
    plugin_dir = "tests/test_plugins"
    if os.path.exists(plugin_dir):
        for root, dirs, files in os.walk(plugin_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(plugin_dir)

def test_plugin_loader():
    plugins = load_plugins("tests/test_plugins")
    assert len(plugins) == 1
    assert isinstance(plugins[0], CodeGeniePlugin)

def test_plugin_execution():
    plugin = DummyPlugin()
    input_code = "print('Hello, World!')"
    output_code = plugin.process(input_code)
    assert output_code == "# Test Plugin\nprint('Hello, World!')"

