import json
import os

def generate_style_guide(output_path, style_path, example_code=None):
    """
    Generate a Markdown file describing the code style guide.

    Args:
        output_path (str): Path to save the generated style guide.
        style_path (str): Path to the JSON style configuration file.
        example_code (dict): Optional dictionary containing examples for each style rule.

    Raises:
        FileNotFoundError: If the style configuration file is not found.
        ValueError: If the JSON style configuration is invalid.
    """
    if not os.path.isfile(style_path):
        raise FileNotFoundError(f"Error: Style configuration file {style_path} not found.")

    try:
        with open(style_path, "r") as file:
            style = json.load(file)
    except json.JSONDecodeError:
        raise ValueError("Error: Invalid JSON in style configuration file.")

    guide = "# Code Style Guide\n\n"
    guide += f"- **Indentation**: {style['indentation']} spaces\n"
    guide += f"- **Line length**: {style['line_length']} characters\n"
    guide += f"- **String quotes**: {'Double' if style['string_quotes'] == 'double' else 'Single'}\n"
    guide += f"- **Trailing commas**: {'Yes' if style['trailing_commas'] else 'No'}\n\n"

    if example_code:
        guide += "## Examples\n\n"
        for rule, example in example_code.items():
            guide += f"### {rule.capitalize()}\n```python\n{example}\n```\n\n"

    try:
        with open(output_path, "w") as file:
            file.write(guide)
        print(f"Style guide written to {output_path}")
    except IOError as e:
        print(f"Error: Unable to write style guide: {e}")
