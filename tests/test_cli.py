import subprocess
import os

def test_cli_format():
    result = subprocess.run(
        ["python", "codegenie.py", "format", "tests/sample_code.py"],
        capture_output=True, text=True
    )
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
    assert result.returncode == 0, "CLI returned an error."
    assert "formatted successfully" in result.stdout, "Formatting output mismatch."

def test_cli_style_guide():
    result = subprocess.run(
        ["python", "codegenie.py", "style-guide", "--output", "style_guide.md"],
        capture_output=True, text=True
    )
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
    assert result.returncode == 0, "CLI returned an error."
    assert os.path.exists("style_guide.md"), "Style guide was not generated."
