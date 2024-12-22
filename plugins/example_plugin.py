from codegenie.plugin import CodeGeniePlugin

class ExamplePlugin(CodeGeniePlugin):
    """
    A sample plugin that demonstrates extending CodeGenie functionality.
    """
    def execute(self, *args, **kwargs):
        print(f"{self.name}: Example plugin executed successfully!")
        print("Arguments received:", args, kwargs)
