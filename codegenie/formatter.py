def format_code(file_path, style_path, check=False):
    """
    Format a Python file based on the given style configuration.

    Args:
        file_path (str): Path to the file to format.
        style_path (str): Path to the JSON style configuration file.
        check (bool): If True, only check if the file matches the style.

    Raises:
        FileNotFoundError: If the file or style configuration is not found.
        ValueError: If the JSON style configuration is invalid.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Error: File {file_path} does not exist.")

    try:
        with open(style_path, "r") as file:
            style = json.load(file)
    except json.JSONDecodeError:
        raise ValueError("Error: Invalid JSON in style configuration file.")

    # Build the Black formatting command
    black_command = ["black", file_path, f"--line-length={style['line_length']}"]
    if style.get("string_quotes") == "double":
        black_command.append("--skip-string-normalization")
    if style.get("trailing_commas"):
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

