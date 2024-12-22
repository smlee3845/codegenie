def generate_style_guide(output_path, style_path):
    """
    Generate a Markdown file describing the code style guide.

    Args:
        output_path (str): Path to save the generated style guide.
        style_path (str): Path to the JSON style configuration file.

    Raises:
        FileNotFoundError: If the style configuration file is not found.
        ValueError: If the JSON style configuration is invalid.
    """
    try:
        with open(style_path, "r") as file:
            style = json.load(file)
    except json.JSONDecodeError:
        raise ValueError("Error: Invalid JSON in style configuration file.")

    guide = (
        "# Code Style Guide\n\n"
        f"- **Indentation**: {style['indentation']} spaces\n"
        f"- **Line length**: {style['line_length']} characters\n"
        f"- **String quotes**: {'Double' if style['string_quotes'] == 'double' else 'Single'}\n"
        f"- **Trailing commas**: {'Yes' if style['trailing_commas'] else 'No'}\n"
    )

    try:
        with open(output_path, "w") as file:
            file.write(guide)
        print(f"Style guide written to {output_path}")
    except IOError as e:
        print(f"Error: Unable to write style guide: {e}")
 
