import os
import json
import subprocess

def format_code(file_path, style_config=None, check=False):
    """
    Format a file based on the given style configuration.

    Args:
        file_path (str): Path to the file to format.
        style_config (dict, optional): Dictionary of style configuration settings.
        check (bool): If True, only check if the file matches the style.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Error: File {file_path} does not exist.")

    if style_config is None:
        from utils.style_loader import load_style_config
        style_config = load_style_config()

    ext = os.path.splitext(file_path)[1]

    if ext == ".py":
        # Build the Black formatting command
        black_command = ["black", file_path, f"--line-length={style_config['line_length']}"]
        if style_config.get("string_quotes") == "double":
            black_command.append("--skip-string-normalization")
        if style_config.get("trailing_commas"):
            black_command.append("--target-version=py38")
        if check:
            black_command.append("--check")

        # Run the Black formatter
        try:
            subprocess.run(black_command, check=True)
            if check:
                print(f"File {file_path} matches the style.")
            else:
                print(f"File {file_path} formatted successfully.")
        except subprocess.CalledProcessError as e:
            if check:
                print(f"File {file_path} does not match the style.")
            else:
                print(f"Error while formatting file {file_path}: {e}")
    elif ext in [".js", ".ts"]:
        from engines.js_formatter import format_js
        format_js(file_path, style_config)
    else:
        print(f"Unsupported file type: {ext}")

