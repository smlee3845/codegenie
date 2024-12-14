# CodeGenie Style Guide

This style guide outlines the coding standards and conventions followed by CodeGenie. It provides developers with clear and consistent rules to ensure high-quality and maintainable Python code. Use this guide alongside CodeGenie’s automated tools to streamline your workflow.

---

## **General Formatting Rules**
### **Indentation**
- Use **4 spaces** per indentation level.
- Do not use tabs for indentation.

### **Line Length**
- Limit all lines to a maximum of **88 characters**.
- Break lines that exceed this limit using Python’s recommended line continuation rules.

### **Blank Lines**
- Separate top-level function and class definitions with **2 blank lines**.
- Use **1 blank line** between methods inside a class.
- Surround logical sections of code within a function with blank lines.

### **Trailing Whitespace**
- Remove any trailing whitespace at the end of lines.

---

## **Strings**
### **Quotes**
- Use **double quotes (")** for all string literals.
  - Example:
    ```python
    message = "Hello, World!"
    ```

### **Multiline Strings**
- Use triple double-quotes (`"""`) for multiline strings.
  - Example:
    ```python
    def example():
        """
        This is a multiline string example.
        """
        pass
    ```

---

## **Imports**
### **Ordering**
- Organize imports into three sections:
  1. Standard library imports
  2. Third-party library imports
  3. Local application/library imports
- Use a blank line to separate each section.

### **Import Rules**
- Avoid wildcard imports (`from module import *`).
- Group imports from the same module into a single line where possible.
  - Example:
    ```python
    from os import path, system
    ```

---

## **Naming Conventions**
### **Variables and Functions**
- Use `snake_case` for variable and function names.
  - Example:
    ```python
    def calculate_area(radius):
        return 3.14 * radius ** 2
    ```

### **Classes**
- Use `PascalCase` for class names.
  - Example:
    ```python
    class DataProcessor:
        pass
    ```

### **Constants**
- Use `UPPER_SNAKE_CASE` for constants.
  - Example:
    ```python
    MAX_CONNECTIONS = 10
    ```

---

## **Comments**
### **Inline Comments**
- Use inline comments sparingly and only when the code’s purpose is not obvious.
  - Example:
    ```python
    x = x + 1  # Increment x by 1
    ```

### **Block Comments**
- Use block comments to describe more complex logic or processes.
  - Example:
    ```python
    # This function calculates the area of a circle.
    # It uses the formula: area = pi * radius^2
    def calculate_area(radius):
        return 3.14 * radius ** 2
    ```

### **Docstrings**
- Write docstrings for all public modules, functions, classes, and methods.
- Use triple double-quotes for docstrings.
  - Example:
    ```python
    def example_function():
        """
        This is an example function.
        It doesn’t do anything meaningful.
        """
        pass
    ```

---

## **Best Practices**
### **Error Handling**
- Use specific exceptions when possible instead of generic `Exception`.
  - Example:
    ```python
    try:
        value = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    ```

### **Type Annotations**
- Use type annotations for function signatures to improve code clarity.
  - Example:
    ```python
    def add_numbers(a: int, b: int) -> int:
        return a + b
    ```

---

## **Automated Tools**
- Use CodeGenie to automatically format your code according to this style guide.
  - Example:
    ```bash
    python codegenie.py format <file_path>
    ```
- Generate a customized style guide:
  - Example:
    ```bash
    python codegenie.py style-guide --style <style_file_path>
    ```

---

Adhering to this style guide ensures that your code remains clean, readable, and maintainable for all contributors. Happy coding!

