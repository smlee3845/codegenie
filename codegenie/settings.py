"""
Default Style Settings Loader
"""
import json
import os

from utils.style_loader import load_style_config

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
    return load_style_config()
