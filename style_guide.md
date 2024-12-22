# CodeGenie Style Guide

This style guide defines the coding conventions and rules enforced by **CodeGenie**. It ensures consistent and clean Python code across projects.

---

## 1. Indentation
- Use **4 spaces** for indentation.
- Tabs are not allowed.

### Example:
```python
def example_function():
    print("Hello, World!")
```

---

## 2. Line Length
- Maximum line length is **88 characters**.
- Lines exceeding this limit should be wrapped.

### Example:
```python
# Correct
def sample_function():
    print("This is a properly formatted line that stays within 88 characters.")

# Incorrect
def sample_function(): print("This line is too long and exceeds the maximum character limit set.")
```

---

## 3. String Quotes
- Use **double quotes** (`"`) for strings.
- Single quotes (`'`) are only allowed when escaping is necessary.

### Example:
```python
# Correct
message = "This is a string with double quotes."

# Incorrect
message = 'This is a string with single quotes.'

# Escaping example
message = 'This string includes a double quote: "Example"'
```

---

## 4. Trailing Commas
- Always include trailing commas in multi-line structures (lists, dictionaries, tuples).

### Example:
```python
# Correct
my_list = [
    "item1",
    "item2",
    "item3",
]

# Incorrect
my_list = [
    "item1",
    "item2",
    "item3"
]
```

---

## 5. Function Definitions
- Use **def** with proper spacing and a single blank line before each function.
- Avoid inline function definitions.

### Example:
```python
# Correct
def greet(name):
    return f"Hello, {name}!"

# Incorrect
def greet(name): return f"Hello, {name}!"
```

---

## 6. Naming Conventions
- Use **snake_case** for variables and function names.
- Use **PascalCase** for class names.
- Constants should be written in **UPPERCASE**.

### Example:
```python
# Correct
my_variable = 10

class MyClass:
    pass

PI = 3.14

# Incorrect
myVariable = 10
class my_class:
    pass
pi = 3.14
```

---

## 7. Blank Lines
- Use **two blank lines** between top-level definitions (e.g., functions or classes).
- Use **one blank line** inside functions to separate logical sections.

### Example:
```python
# Correct
class MyClass:
    pass


def first_function():
    print("First")


def second_function():
    print("Second")

# Incorrect
class MyClass:
    pass
def first_function():
    print("First")
def second_function():
    print("Second")
```

---

## 8. Imports
- Group imports into three sections:
  1. **Standard library imports**
  2. **Third-party imports**
  3. **Local application imports**
- Each section should be separated by a blank line.

### Example:
```python
# Correct
import os
import sys

from flask import Flask

from my_project import my_module

# Incorrect
import os, sys
from my_project import my_module
import Flask
```

---

## 9. Comments
- Write **meaningful comments** to describe the purpose of the code.
- Use `#` for inline comments and avoid unnecessary comments.

### Example:
```python
# Correct
# Calculate the sum of two numbers
def add(a, b):
    return a + b

# Incorrect
# Add function
def add(a, b):
    return a + b  # This line adds two numbers
```

---

## 10. Additional Rules
- No unused imports or variables.
- Avoid deep nesting; refactor code if needed.
- Use `is` for `None` comparisons instead of `==`.

### Example:
```python
# Correct
if variable is None:
    print("Variable is None")

# Incorrect
if variable == None:
    print("Variable is None")
```

---

## Summary
By adhering to this style guide, you ensure consistent, readable, and maintainable Python code. Use **CodeGenie** to automatically apply these rules to your codebase!

