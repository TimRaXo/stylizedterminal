COLORS_TEXT = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m",
}

COLORS_BACKGROUND = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "white": "\033[47m",
    "reset": "\033[0m",
}

TERMINAL_CODES = {
    "r": "C",
    "l": "D",
    "u": "A",
    "d": "B",
}

class StylizedStr(str):
    def color(self, color='reset'):
        color_code = COLORS_TEXT.get(color.lower(), COLORS_TEXT['reset'])
        return StylizedStr(f"{color_code}{self}{COLORS_TEXT['reset']}")

    def background_color(self, color="reset"):
        color_code = COLORS_BACKGROUND.get(color.lower(), COLORS_BACKGROUND["reset"])
        return StylizedStr(f"{color_code}{self}{COLORS_BACKGROUND['reset']}")
    def move_cursor(self, direction, steps):
        direction_code = TERMINAL_CODES.get(direction.lower())
        if direction_code is None:
            raise ValueError(f"Invalid direction: {direction}. Use 'r', 'l', 'u', or 'd'.")
        return StylizedStr(f"\033[{steps}{direction_code}{self}")


def clear_screen():
    print("\033[2J\033[H", end="")



