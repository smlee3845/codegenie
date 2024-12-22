import subprocess

def format_js(file_path, style_config):
    """
    Format JavaScript/TypeScript files using Prettier.

    Args:
        file_path (str): Path to the JS/TS file.
        style_config (dict): JavaScript-specific style configuration.
    """
    command = ["prettier", "--write", file_path]
    subprocess.run(command, check=True)
