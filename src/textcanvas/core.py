COLORS_TEXT = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
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

class CanvasStr(str):
    def color(self, color='reset'):
        color_code = COLORS_TEXT.get(color.lower(), COLORS_TEXT['reset'])
        return CanvasStr(f"{color_code}{self}{COLORS_TEXT['reset']}")

    def background_color(self, color='reset'):
        color_code = COLORS_BACKGROUND.get(color.lower(), COLORS_BACKGROUND['reset'])
        return CanvasStr(f"{color_code}{self}{COLORS_BACKGROUND['reset']}")      

          