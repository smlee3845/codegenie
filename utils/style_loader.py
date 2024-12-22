import os
import json

def load_style_config():
    """
    Load the style configuration from the project directory or fallback to default.
    """
    project_config = "project_style.json"
    default_config = "settings/default_style.json"
    
    if os.path.isfile(project_config):
        with open(project_config, "r") as file:
            return json.load(file)
    elif os.path.isfile(default_config):
        with open(default_config, "r") as file:
            return json.load(file)
    else:
        raise FileNotFoundError("No style configuration file found.")
