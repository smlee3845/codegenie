import argparse
import json
import subprocess
import os

def format_code(file_path, style_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: File {file_path} does not exist.")
        return

    # Load style settings
    with open(style_path, 'r') as f:
        style = json.load(f)
    
    # Construct black arguments based on the settings
    black_command = ["black", file_path, f"--line-length={style['line_length']}"]
    if style.get("string_quotes") == "double":
        black_command.append("--skip-string-normalization")
    if style.get("trailing_commas"):
        black_command.append("--target-version=py38")

    # Execute black formatting
    subprocess.run(black_command)

def generate_style_guide(output_path, style_path):
    # Load style settings
    with open(style_path, 'r') as f:
        style = json.load(f)
    
    # Generate Markdown content
    guide = "# Code Style Guide\n\n"
    guide += f"- **Indentation**: {style['indentation']} spaces\n"
    guide += f"- **Line length**: {style['line_length']} characters\n"
    guide += f"- **String quotes**: {'Double' if style['string_quotes'] == 'double' else 'Single'}\n"
    guide += f"- **Trailing commas**: {'Yes' if style['trailing_commas'] else 'No'}\n"

    # Write to output file
    with open(output_path, 'w') as f:
        f.write(guide)
    print(f"Style guide written to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CodeGenie CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Format command
    format_parser = subparsers.add_parser("format")
    format_parser.add_argument("file", help="Path to the file to format")
    format_parser.add_argument("--style", default="settings/default_style.json", help="Path to style settings")
    format_parser.add_argument("--check", action="store_true", help="Only check if the file matches the style")
    if args.command == "format":
     format_code(args.file, args.style, args.check)
    
    # Style guide command
    guide_parser = subparsers.add_parser("style-guide")
    guide_parser.add_argument("--output", default="style_guide.md", help="Output path for the style guide")
    guide_parser.add_argument("--style", default="settings/default_style.json", help="Path to style settings")
    
    args = parser.parse_args()
    if args.command == "format":
        format_code(args.file, args.style)
    elif args.command == "style-guide":
        generate_style_guide(args.output, args.style)


if args.command == "format":
    format_code(args.file, args.style, args.check)
