# codegenie/utils/style_loader.py
import json
import os

def load_style_config(style_path):
    if not os.path.exists(style_path):
        raise FileNotFoundError(f"Style configuration file {style_path} not found.")
    with open(style_path, "r") as file:
        return json.load(file)
