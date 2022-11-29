from ..src.terminal_factory import TerminalFactory
import unittest
import os

class TestTerminalFactory(unittest.TestCase):
    def test_get_terminal(self):
        try:
            TerminalFactory.get_terminal()
        except Exception:
            self.fail("should be able to get terminal")

    def test_cant_get_terminal(self):
        the_os_name = os.name
        os.name = 'dummy'
        try:
            TerminalFactory.get_terminal()
            self.fail("should not be able to get terminal")
        except Exception:
            pass
        os.name = the_os_name
