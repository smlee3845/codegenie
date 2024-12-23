"""
Plugin Base Class
"""
class CodeGeniePlugin:
    """
    Base class for CodeGenie plugins.
    """
    def __init__(self, name = None):
        self.name = name

    def run(self):
        return f"{self.name} plugin is running."
        
    def execute(self, *args, **kwargs):
        """
        Execute the plugin functionality. To be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the execute method.")
