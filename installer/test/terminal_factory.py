from ..src.terminal_factory import TerminalFactory
import unittest
import os

class TestTerminalFactory(unittest.TestCase):
    def test_get_terminal(self):
        thrown_error = False
        try:
            TerminalFactory.get_terminal()
        except Exception:
            thrown_error = True
        self.assertFalse(thrown_error)

    def test_cant_get_terminal(self):
        the_os_name = os.name
        os.name = 'dummy'
        thrown_error = False
        try:
            TerminalFactory.get_terminal()
        except Exception:
            thrown_error = True
        os.name = the_os_name
        self.assertTrue(thrown_error)
