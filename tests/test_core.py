import io
import unittest
from contextlib import redirect_stdout

from stylizedterminal import StylizedStr, clear_screen


class TerminalUtilityTests(unittest.TestCase):
    def test_stylized_str_color_wraps_text(self) -> None:
        self.assertEqual(StylizedStr("test").color("red"), "\033[31mtest\033[0m")

    def test_stylized_str_supports_background_and_text_styles(self) -> None:
        styled = StylizedStr("test").background_color("blue").bold()
        self.assertEqual(styled, "\033[1m\033[44mtest\033[0m\033[0m")

    def test_italic(self) -> None:
        self.assertEqual(StylizedStr("test").italic(),"\033[3mtest\033[0m",)

    def test_underline(self) -> None:
        self.assertEqual(StylizedStr("test").underline(),"\033[4mtest\033[0m",)
    
    def test_strikethrough(self) -> None:
        self.assertEqual(StylizedStr("hi").strikethrough(),"\033[9mhi\033[0m",)

    def test_ascii_art_renders_expected_lines(self) -> None:
        self.assertEqual(
            StylizedStr("A").ascii_art(),
            "  #    \n # #   \n#####  \n#   #  \n#   #  ",
        )
    
    def test_ascii_art_unknown_character_renders_blank_space(self) -> None:
        self.assertEqual(
            StylizedStr("🙂").ascii_art(),
            "       \n       \n       \n       \n       ",
        )

    def test_move_cursor(self) -> None:
        self.assertEqual(StylizedStr("test").move_cursor("r", 2), "\033[2Ctest")

    def test_clear_screen(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            clear_screen()
        self.assertEqual(buffer.getvalue(), "\033[2J\033[H")
    
    def test_move_cursor_invalid_direction(self) -> None:
        with self.assertRaises(ValueError):
            StylizedStr("test").move_cursor("x", 2)
    
    def test_invalid_text_color_defaults_to_reset(self) -> None:
        self.assertEqual(
            StylizedStr("test").color("orange"),
            "\033[0mtest\033[0m",
        )
    
    def test_invalid_background_color_defaults_to_reset(self) -> None:
        self.assertEqual(
            StylizedStr("test").background_color("orange"),
            "\033[0mtest\033[0m",
        )


if __name__ == "__main__":
    unittest.main()
