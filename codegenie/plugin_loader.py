import os
import importlib.util
from codegenie.plugin import CodeGeniePlugin

def load_plugins(plugin_directory):
    plugins = []
    for file_name in os.listdir(plugin_directory):
        if file_name.endswith(".py") and not file_name.startswith("__"):
            file_path = os.path.join(plugin_directory, file_name)
            module_name = file_name[:-3]
            
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (
                    isinstance(attr, type) and 
                    issubclass(attr, CodeGeniePlugin) and 
                    attr is not CodeGeniePlugin
                ):
                    plugins.append(attr(name=attr_name))
    return plugins
