import argparse
import json
import subprocess
import os
from utils.style_loader import load_style_config

def validate_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")

def format_code(file_path, style_path, check=False, log=False):
    validate_file(file_path)
    validate_file(style_path)

    style_config = load_style_config(style_path)
    black_command = ["black", file_path, f"--line-length={style_config.get('line_length', 88)}"]
    if style_config.get("string_quotes") == "double":
        black_command.append("--skip-string-normalization")
    if style_config.get("trailing_commas"):
        black_command.append("--target-version=py38")
    if check:
        black_command.append("--check")

    try:
        result = subprocess.run(black_command, check=True, text=True, capture_output=True)
        log_message = f"File {file_path} formatted successfully.\n" if not check else \
                      f"File {file_path} matches the style.\n"
        if result.returncode != 0:
            log_message = f"File {file_path} failed formatting check.\n"

        print(log_message)
        if log:
            with open("logs/format_log.txt", "a") as log_file:
                log_file.write(log_message)

    except subprocess.CalledProcessError as e:
        print(f"Error during formatting: {e}")


    if check:
        if result.returncode == 0:
            print(f"{file_path} matches the style.")
        else:
            print(f"{file_path} does not match the style.")
    else:
        print(f"{file_path} formatted successfully.")

def generate_style_guide(output_path, style_path, example_code=None):
    validate_file(style_path)

    with open(style_path, "r") as file:
        style = json.load(file)

    guide = "# Code Style Guide\n\n"
    guide += f"- **Indentation**: {style.get('indentation', 'Not specified')} spaces\n"
    guide += f"- **Line length**: {style.get('line_length', 88)} characters\n"
    guide += f"- **String quotes**: {'Double' if style.get('string_quotes') == 'double' else 'Single'}\n"
    guide += f"- **Trailing commas**: {'Yes' if style.get('trailing_commas') else 'No'}\n\n"
    guide += f"- **Variable Naming**: {style.get('variable_naming', 'Not specified')}\n"
    guide += f"- **Function Documentation Style**: {style.get('function_documentation', 'Not specified')}\n\n"

    if example_code:
        guide += "## Examples\n\n"
        for rule, example in style.get("examples", {}).items():
            guide += f"### {rule.replace('_', ' ').capitalize()}\n```python\n{example}\n```\n\n"

    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_path, "w") as file:
        file.write(guide)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CodeGenie CLI")
    subparsers = parser.add_subparsers(dest="command")

    format_parser = subparsers.add_parser("format")
    format_parser.add_argument("file", help="Path to the file to format")
    format_parser.add_argument("--style", default="settings/default_style.json", help="Path to style settings")
    format_parser.add_argument("--check", action="store_true", help="Only check if the file matches the style")

    guide_parser = subparsers.add_parser("style-guide")
    guide_parser.add_argument("--output", default="style_guide.md", help="Output path for the style guide")
    guide_parser.add_argument("--style", default="settings/default_style.json", help="Path to style settings")

    args = parser.parse_args()

    validate_file(args.style)

    if args.command == "format":
        format_code(args.file, args.style, args.check)
    elif args.command == "style-guide":
        generate_style_guide(args.output, args.style)

