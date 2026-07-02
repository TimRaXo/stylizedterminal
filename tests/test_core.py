import io
import unittest
from contextlib import redirect_stdout

from stylizedterminal import StylizedStr, clear_screen


class TerminalUtilityTests(unittest.TestCase):
    def test_stylized_str_color_wraps_text(self) -> None:
        self.assertEqual(StylizedStr("hi").color("red"), "\033[31mhi\033[0m")

    def test_stylized_str_supports_background_and_text_styles(self) -> None:
        styled = StylizedStr("hi").background_color("blue").bold()
        self.assertEqual(styled, "\033[1m\033[44mhi\033[0m\033[0m")

    def test_ascii_art_renders_expected_lines(self) -> None:
        self.assertEqual(
            StylizedStr("A").ascii_art(),
            "  #    \n # #   \n#####  \n#   #  \n#   #  ",
        )

    def test_move_cursor(self) -> None:
        self.assertEqual(StylizedStr("hi").move_cursor("r", 2), "\033[2Chi")

    def test_clear_screen(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            clear_screen()
        self.assertEqual(buffer.getvalue(), "\033[2J\033[H")


if __name__ == "__main__":
    unittest.main()
