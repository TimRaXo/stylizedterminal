import io
import unittest
from contextlib import redirect_stdout

from stylizedterminal import CanvasStr, clear_screen, move_cursor


class TerminalUtilityTests(unittest.TestCase):
    def test_canvas_color_wraps_text(self) -> None:
        self.assertEqual(CanvasStr("hi").color("red"), "\033[31mhi\033[0m")

    def test_move_cursor(self) -> None:
        self.assertEqual(move_cursor(2, 3), "\033[2;3H")

    def test_clear_screen(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            clear_screen()
        self.assertEqual(buffer.getvalue(), "\033[2J\033[H")


if __name__ == "__main__":
    unittest.main()
