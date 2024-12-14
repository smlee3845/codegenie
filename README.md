# CodeGenie

CodeGenie is a simple yet powerful tool for managing and formatting code styles, designed specifically for developers. It ensures consistent Python code styles and automates formatting based on user-defined rules.

---

## Key Features
- **Code Formatting**: Adheres to PEP 8 standards with support for customizable style options (JSON).
- **Style Guide Generation**: Automatically generates a Markdown style guide based on defined rules.
- **Simple CLI Interface**: Easily format and generate guides using commands like `codegenie format` and `codegenie style-guide`.

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
   pip install black
   ```

---

## Usage
### 1. Code Formatting
```bash
python codegenie.py format <file_path> [--style <style_file_path>]
```
- Formats the specified Python file according to the provided style settings.
- The default style settings file is `settings/default_style.json`.

#### Examples
```bash
python codegenie.py format tests/sample_code.py
python codegenie.py format tests/sample_code.py --style settings/custom_style.json
```

---

### 2. Style Guide Generation
```bash
python codegenie.py style-guide [--output <output_file_path>] [--style <style_file_path>]
```
- Generates a Markdown style guide based on the current style settings.
- The default output file is `style_guide.md`.

#### Examples
```bash
python codegenie.py style-guide
python codegenie.py style-guide --output my_style_guide.md
```

---

## Default Style Settings
CodeGenie uses a JSON file for style configurations. Below is an example of the default settings file (`settings/default_style.json`):
```json
{
  "indentation": 4,
  "line_length": 88,
  "string_quotes": "double",
  "trailing_commas": true
}
```

- **indentation**: Number of spaces for indentation.
- **line_length**: Maximum allowed line length.
- **string_quotes**: Type of quotes to use for strings ("double" or "single").
- **trailing_commas**: Whether to include trailing commas after the last item.

---

## Contributing
CodeGenie is an open-source project, and contributions are welcome!

### How to Contribute
1. Check existing issues or open a new one.
2. Fork the repository to make your changes.
3. Submit a Pull Request with your updates.

---

## License
CodeGenie is distributed under the MIT License. Feel free to use and contribute!

