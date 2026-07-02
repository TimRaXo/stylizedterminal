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

print(StylizedStr("Hello").color("red"))
print(StylizedStr("Hello").color("green"))
```

### Background colors

```python
from stylizedterminal import StylizedStr

print(StylizedStr("Hello").background_color("blue"))
```

### Text styles

```python
from stylizedterminal import StylizedStr

print(StylizedStr("Hello").bold())
print(StylizedStr("Hello").italic())
print(StylizedStr("Hello").underline())
print(StylizedStr("Hello").strikethrough())
```

### Cursor movement and screen clearing

```python
from stylizedterminal import StylizedStr, clear_screen

print(StylizedStr("Hello").move_cursor(r, 5)) # The first parameter is the direction, the second parameter is by how much.
clear_screen()
```

### ASCII art

```python
from stylizedterminal import StylizedStr

print(StylizedStr("HELLO").ascii_art()) # if you also want to make it something else for example a different color you will have to call the ascii_art() function first, else it will get confused and print the color code in the ascii.
```

## Development

If you want to work on the package locally:

```bash
git clone <your-repo-url>
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
