# CodeGenie

CodeGenie is a simple yet powerful code style management and formatting tool for developers. It ensures consistent code style for Python projects and supports customizable style rules with plugins and automated workflows.

---

## Key Features

- **Code Formatting**: Enforces PEP 8 standards and supports custom style options (JSON-based settings).
- **Style Guide Generation**: Automatically generates Markdown-based style guides based on your style rules.
- **Plugin System**: Extend CodeGenie with custom plugins to handle unique formatting or linting needs.
- **CI/CD Integration**: Includes GitHub Actions workflows for automated testing and deployment.
- **Simple CLI Interface**: Easy-to-use commands for formatting and style guide generation.

---

## Installation

### Requirements

- Python 3.8 or higher

### Installation Steps

1. Clone CodeGenie:
   ```bash
   git clone https://github.com/smlee3845/codegenie.git
   cd codegenie
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. Code Formatting

Format Python files using your custom or default style settings:

```bash
python codegenie.py format <file_path> [--style <style_file_path>]
```

#### Examples:

```bash
python codegenie.py format tests/sample_code.py
python codegenie.py format tests/sample_code.py --style settings/custom_style.json
```

### 2. Style Guide Generation

Generate a Markdown style guide based on the current style settings:

```bash
python codegenie.py style-guide [--output <output_file>] [--style <style_file_path>]
```

#### Examples:

```bash
python codegenie.py style-guide
python codegenie.py style-guide --output my_style_guide.md
```

### 3. Plugin Support

To use a custom plugin, place your plugin files in the `plugins/` directory. CodeGenie will load and apply plugins automatically during formatting.

#### Plugin Example:

```python
from codegenie.plugin import CodeGeniePlugin

class MyCustomFormatter(CodeGeniePlugin):
    def process(self, code: str) -> str:
        # Custom processing logic here
        return code.replace("TODO", "FIXME")
```

---

## Default Style Settings

CodeGenie uses a JSON-based style configuration. Below is the default configuration (`settings/default_style.json`):

```json
{
  "indentation": 4,
  "line_length": 88,
  "string_quotes": "double",
  "trailing_commas": true
}
```

- **indentation**: Number of spaces for indentation.
- **line\_length**: Maximum allowed line length.
- **string\_quotes**: Use "double" or 'single' quotes for strings.
- **trailing\_commas**: Whether to add trailing commas in lists or dicts.

---

## Continuous Integration / Continuous Deployment (CI/CD)

CodeGenie includes a GitHub Actions workflow (`.github/workflows/ci_cd.yml`) for automated testing and deployment:

- **Automatic Testing**: Runs `pytest` on all test files.
- **Code Quality Checks**: Ensures all Python files adhere to CodeGenie's style rules.
- **Deployment Pipeline**: Prepares releases automatically.

To enable CI/CD, push your project to GitHub and include the provided workflow file.

---

## Contributing

CodeGenie is an open-source project, and contributions are welcome!

### Contribution Guidelines

1. *Fork the repository.*
2. *Create a new branch for your feature or bug fix.*
3. *Write tests and ensure all* tests pass.
4. Submit a pull request.

For more details, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

CodeGenie is distributed under the MIT License. Feel free to use, modify, and share it!

---

## Roadmap

Upcoming features for future versions:

- **Enhanced Plugin System**: Support for real-time linting and dynamic plugin loading.
- **Style Violation Reporting**: Highlight specific violations during formatting.
- **Community Templates**: Share and use style templates created by the community.
- **Integration with IDEs**: Provide plugins for popular IDEs like VSCode and PyCharm.

Stay tuned for updates!


