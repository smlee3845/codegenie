import subprocess

def format_python(file_path, style_config):
    """
    Format Python files using Black.

    Args:
        file_path (str): Path to the Python file.
        style_config (dict): Python-specific style configuration.
    """
    command = ["black", file_path]
    if "line_length" in style_config:
        command.append(f"--line-length={style_config['line_length']}")
    subprocess.run(command, check=True)
