import subprocess

def test_cli_format():
    result = subprocess.run(
        ["python", "codegenie.py", "format", "tests/sample_code.py"],
        capture_output=True, text=True
    )
    assert "Formatting completed" in result.stdout

def test_cli_style_guide():
    result = subprocess.run(
        ["python", "codegenie.py", "style-guide", "--output", "style_guide.md"],
        capture_output=True, text=True
    )
    assert "Style guide generated" in result.stdout
 
