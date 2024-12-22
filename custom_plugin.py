from codegenie.plugin import CodeGeniePlugin

class CustomPlugin(CodeGeniePlugin):
    """
    A user-defined plugin for demonstrating custom behavior.
    """
    def execute(self, *args, **kwargs):
        print(f"{self.name}: Custom plugin executed with arguments:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")
