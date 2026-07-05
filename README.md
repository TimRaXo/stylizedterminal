# stylizedterminal

stylizedterminal is a lightweight Python package for adding terminal styling to text using ANSI escape codes. It provides helpers for colors, background colors, bold/italic/underline/strikethrough text, cursor movement, screen clearing, and simple ASCII art.

## Installation

Install the package from PyPI:

### Linux/Macos

```bash
python3 -m pip install stylizedterminal
```

### Windows
```cmd
py -m pip install stylizedterminal
```

### Importing the package

```python
import stylizedterminal
```

## Usage

### Text colors

```python
from stylizedterminal import StylizedStr

print(StylizedStr("Hello, World!").color("red"))
```

### Background colors

```python
from stylizedterminal import StylizedStr

print(StylizedStr("Hello, World!").background_color("blue"))
```

### You can also use RGB
```python 
from stylizedterminal import StylizedStr

print(StylizedStr("Hello, World!").color_rgb(255, 255, 0))
print(StylizedStr("Hello, World!").background_color_rgb(255, 255, 0))
```

### Text styles

```python
from stylizedterminal import StylizedStr

print(StylizedStr("Hello, World!").bold())
print(StylizedStr("Hello, World!").italic())
print(StylizedStr("Hello, World!").underline())
print(StylizedStr("Hello, World!").strikethrough())
```

### Cursor movement and screen clearing

```python
from stylizedterminal import StylizedStr, clear_screen

print(StylizedStr("Hello, World!").move_cursor(r, 5)) # The first parameter is the direction, the second parameter is how much you want to move the cursor.
clear_screen()
```

### ASCII art

```python
from stylizedterminal import StylizedStr

print(StylizedStr("Hello, World!").ascii_art())
```

### Chaining
You can chain multiple functions together like this:

```python
from stylizedstr import StylizedStr

print(StylizedStr("Hello, World!").ascii_art().color("red")) # Make sure to call the ASCII function first if you want to chain ASCII with different styles.
```

## Development

If you want to work on the package locally:

```bash
git clone https://github.com/TimRaXo/stylizedterminal.git
cd stylizedterminal
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

## Project structure

- `src/stylizedterminal/` contains the package source code
- `tests/` contains the test suite
- `pyproject.toml` defines packaging metadata
