from style_guide import generate_style_guide
from sync_style_guide import watch_style_file

if __name__ == "__main__":
    style_path = "settings/default_style.json"
    output_path = "style_guide.md"
    example_code = {
        "indentation": "def example():\n    pass",
        "line_length": "# This is a very long comment exceeding the line limit...",
        "string_quotes": 'name = "John"',
        "trailing_commas": "items = [1, 2, 3,]"
    }

    # Generate the initial style guide
    generate_style_guide(output_path, style_path, example_code)

    # Start watching the style file for changes
    watch_style_file(style_path, output_path, example_code)
