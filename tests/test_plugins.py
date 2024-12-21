from codegenie.plugin_loader import load_plugins
from codegenie.plugin import CodeGeniePlugin

class DummyPlugin(CodeGeniePlugin):
    def process(self, code: str) -> str:
        return "# Test Plugin\n" + code

def test_plugin_loader():
    plugins = load_plugins("tests/test_plugins")
    assert len(plugins) == 1
    assert isinstance(plugins[0], CodeGeniePlugin)

def test_plugin_execution():
    plugin = DummyPlugin()
    input_code = "print('Hello, World!')"
    output_code = plugin.process(input_code)
    assert output_code == "# Test Plugin\nprint('Hello, World!')"
