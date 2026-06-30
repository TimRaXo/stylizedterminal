COLORS_TEXT = {               # ANSI escape codes for text colors
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

COLORS_BACKGROUND = {        # ANSI escape codes for background colors
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

TERMINAL_CODES = {            # Direction codes for moving the cursor
    "r": "C",
    "l": "D",
    "u": "A",
    "d": "B",
}

class StylizedStr(str):                                                                # A subclass of str that adds methods for styling text in the terminal
    def color(self, color='reset'):                                                    # Method to wrap the string in ANSI escape codes for text color                                
        color_code = COLORS_TEXT.get(color.lower(), COLORS_TEXT['reset'])
        return StylizedStr(f"{color_code}{self}{COLORS_TEXT['reset']}")

    def background_color(self, color="reset"):                                         # Method to wrap the string in ANSI escape codes for background color
        color_code = COLORS_BACKGROUND.get(color.lower(), COLORS_BACKGROUND["reset"])
        return StylizedStr(f"{color_code}{self}{COLORS_BACKGROUND['reset']}")
    def move_cursor(self, direction, steps):                                           # Method to move the cursor in the terminal in a specified direction by a specified number of steps
        direction_code = TERMINAL_CODES.get(direction.lower())
        if direction_code is None:
            raise ValueError(f"Invalid direction: {direction}. Use 'r', 'l', 'u', or 'd'.")
        return StylizedStr(f"\033[{steps}{direction_code}{self}")
    def bold(self):                                                                    # Method to make the string bold in the terminal
        return StylizedStr(f"\033[1m{self}\033[0m")
    def italic(self):                                                                  # Method to make the string italic in the terminal
        return StylizedStr(f"\033[3m{self}\033[0m")
    def underline(self):                                                               # Method to underline the string in the terminal
        return StylizedStr(f"\033[4m{self}\033[0m")
    def strikethrough(self):                                                           # Method to strike through the string in the terminal
        return StylizedStr(f"\033[9m{self}\033[0m")


def clear_screen(): # Function to clear the terminal screen and move the cursor to the top-left corner
    print("\033[2J\033[H", end="")