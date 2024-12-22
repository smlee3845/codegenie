from codegenie.plugin import CodeGeniePlugin

class Plugin(CodeGeniePlugin):
    def process(self, code: str) -> str:
        return "# Processed by Example Plugin\n" + code
 
