import argparse
import json
import subprocess
import os
from utils.style_loader import load_style_config

def format_code(file_path, style_path, check=False):
    """
    Format or check the style of a Python file based on the given style configuration.
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: File {file_path} does not exist.")
        return
    
    # Load project-specific or default style config
    style_config = load_style_config()
    
    # Load style settings
    with open(style_path, 'r') as f:
        style = json.load(f)
    
    # Construct black arguments based on the settings
    black_command = ["black", file_path, f"--line-length={style['line_length']}"]
    if style.get("string_quotes") == "double":
        black_command.append("--skip-string-normalization")
    if style.get("trailing_commas"):
        black_command.append("--target-version=py38")
    if check:
        black_command.append("--check")

    # Execute black formatting or check
    result = subprocess.run(black_command)
    if check:
        if result.returncode == 0:
            print(f"{file_path} matches the style.")
        else:
            print(f"{file_path} does not match the style.")
    else:
        print(f"{file_path} formatted successfully.")

def generate_style_guide(output_path, style_path, example_code=None):
    """
    Generate a Markdown file describing the code style guide with additional rules.
    """
    with open(style_path, "r") as file:
        style = json.load(file)

    guide = "# Code Style Guide\n\n"
    guide += f"- **Indentation**: {style['indentation']} spaces\n"
    guide += f"- **Line length**: {style['line_length']} characters\n"
    guide += f"- **String quotes**: {'Double' if style['string_quotes'] == 'double' else 'Single'}\n"
    guide += f"- **Trailing commas**: {'Yes' if style['trailing_commas'] else 'No'}\n\n"
    guide += f"- **Variable Naming**: {style['variable_naming']}\n"
    guide += f"- **Function Documentation Style**: {style['function_documentation']}\n\n"

    if example_code:
        guide += "## Examples\n\n"
        for rule, example in style["examples"].items():
            guide += f"### {rule.replace('_', ' ').capitalize()}\n```python\n{example}\n```\n\n"

    with open(output_path, "w") as file:
        file.write(guide)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CodeGenie CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Format command
    format_parser = subparsers.add_parser("format")
    format_parser.add_argument("file", help="Path to the file to format")
    format_parser.add_argument("--style", default="settings/default_style.json", help="Path to style settings")
    format_parser.add_argument("--check", action="store_true", help="Only check if the file matches the style")

    # Style guide command
    guide_parser = subparsers.add_parser("style-guide")
    guide_parser.add_argument("--output", default="style_guide.md", help="Output path for the style guide")
    guide_parser.add_argument("--style", default="settings/default_style.json", help="Path to style settings")

    args = parser.parse_args()

    # Process commands
    if args.command == "format":
        format_code(args.file, args.style, args.check)
    elif args.command == "style-guide":
        generate_style_guide(args.output, args.style)

