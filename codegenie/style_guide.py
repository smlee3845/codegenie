def generate_style_guide(output_path, style_config):
    """
    Generate a Markdown file describing the code style guide.

    Args:
        output_path (str): Path to save the generated style guide.
        style_config (dict): Dictionary of style configuration settings.

    Raises:
        ValueError: If the style configuration is invalid.
    """
    guide = (
        "# Code Style Guide\n\n"
        f"- **Indentation**: {style_config['indentation']} spaces\n"
        f"- **Line length**: {style_config['line_length']} characters\n"
        f"- **String quotes**: {'Double' if style_config['string_quotes'] == 'double' else 'Single'}\n"
        f"- **Trailing commas**: {'Yes' if style_config['trailing_commas'] else 'No'}\n"
    )

    try:
        with open(output_path, "w") as file:
            file.write(guide)
        print(f"Style guide written to {output_path}")
    except IOError as e:
        print(f"Error: Unable to write style guide: {e}")
