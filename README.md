# README.md

## CodeGenie

CodeGenie is a robust, extensible, and developer-friendly code style management and formatting tool. Designed for Python and JavaScript developers, it enforces consistent code styles, generates style guides, and supports customizable rules with plugin functionality.

---

## Key Features

- **Code Formatting**: Automatically formats Python and JavaScript/TypeScript files according to style rules.
- **Style Guide Generation**: Creates Markdown-based style guides from your configuration.
- **Plugin System**: Extend functionality with custom plugins for unique formatting and linting requirements.
- **CI/CD Integration**: Includes workflows for automated testing and formatting checks.
- **Simple CLI Interface**: Command-line tools for formatting and generating style guides.

---

## Installation

### Requirements

- Python 3.8 or higher

### Installation Steps

1. Clone the CodeGenie repository:
   ```bash
   git clone https://github.com/your-repo/codegenie.git
   cd codegenie
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Activate on Windows
   .\venv\Scripts\activate
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

---

## Usage

### 1. Code Formatting

Use CodeGenie to format files or check their compliance with style rules.

#### Format Files:
```bash
python codegenie.py format <file_path> [--style <style_file_path>]
```

#### Examples:
```bash
python codegenie.py format my_script.py
python codegenie.py format my_script.py --style settings/custom_style.json
```

#### Check Style Compliance:
```bash
python codegenie.py format <file_path> --check
```

### 2. Generate a Style Guide

Generate a Markdown file detailing the current style rules.
```bash
python codegenie.py style-guide [--output <output_file>] [--style <style_file_path>]
```

#### Examples:
```bash
python codegenie.py style-guide
python codegenie.py style-guide --output style_guide.md
```

### 3. Plugin Integration

To use custom plugins, place them in the `plugins/` directory. CodeGenie will automatically load plugins at runtime.

#### Plugin Example:
```python
from codegenie.plugin import CodeGeniePlugin

class MyCustomPlugin(CodeGeniePlugin):
    def process(self, code: str) -> str:
        return code.replace("TODO", "FIXME")
```

---

## Default Style Settings

The default style configuration (`settings/default_style.json`) includes:

```json
{
  "indentation": 4,
  "line_length": 88,
  "string_quotes": "double",
  "trailing_commas": true
}
```

### Explanation:

- **indentation**: Number of spaces for indentation.
- **line_length**: Maximum allowed line length.
- **string_quotes**: Preferred quotes for strings (double or single).
- **trailing_commas**: Include trailing commas in multi-line structures.

---

## CI/CD Integration

CodeGenie includes GitHub Actions workflows for automation:

1. **`ci.yml`**: Checks code formatting on pull requests.
2. **`cd.yml`**: Runs tests and prepares releases on merges to `main`.

To enable these workflows, copy the YAML files from `.github/workflows/` into your project.

---

## Contributing

CodeGenie is open-source and welcomes contributions!

### Contribution Steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Write tests for your changes.
4. Run all tests to ensure they pass.
5. Submit a pull request.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

## License

CodeGenie is licensed under the MIT License. See the LICENSE file for more details.

---

## Roadmap

Planned features for future releases:

- Enhanced real-time linting with dynamic plugin loading.
- Advanced violation reporting with detailed suggestions.
- Community-shared style templates.
- IDE plugins for VSCode and PyCharm.

Stay updated with our latest releases and features!



