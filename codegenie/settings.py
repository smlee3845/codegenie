"""
Default Style Settings Loader
"""
import json
import os

def load_default_style(style_path):
    """
    Load the default style settings from a JSON file.

    Args:
        style_path (str): Path to the JSON style configuration file.

    Returns:
        dict: Dictionary containing style settings.

    Raises:
        FileNotFoundError: If the style configuration file is not found.
        ValueError: If the JSON style configuration is invalid.
    """
    if not os.path.isfile(style_path):
        raise FileNotFoundError(f"Error: Default style configuration file {style_path} not found.")

    try:
        with open(style_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise ValueError("Error: Invalid JSON in default style configuration file.")

