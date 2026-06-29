import unittest

from textcanvas import greet
from textcanvas.core import move_cursor


class GreetTests(unittest.TestCase):
    def test_greet_defaults(self) -> None:
        self.assertEqual(greet(), "Hello, world!")

    def test_greet_custom_name(self) -> None:
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_move_cursor(self) -> None:
        self.assertEqual(move_cursor(2, 3), "\033[2;3H")


if __name__ == "__main__":
    unittest.main()
