"""
CodeGenie Package Initialization
"""

# Import core functionalities for external usage
from .formatter import format_code
from .style_guide import generate_style_guide
from .plugin_loader import load_plugins

__all__ = [
    "format_code",
    "generate_style_guide",
    "load_plugins"
]
 
