import unittest
from ..src.terminal import Terminal

class TestTerminal(unittest.TestCase):
    def test_touch_file(self):
        terminal = Terminal()
        tmp_file = "tmp_file"
        terminal.touch_file(tmp_file)
        terminal.delete_file(tmp_file)

    def test_move_file(self):
        terminal = Terminal()
        tmp_file = "tmp_file"
        terminal.touch_file(tmp_file)
        terminal.move_file(tmp_file, tmp_file)
        terminal.delete_file(tmp_file)
    
    def test_copy_file(self):
        terminal = Terminal()
        tmp_file = "tmp_file"
        terminal.touch_file(tmp_file)
        terminal.copy_file(tmp_file, tmp_file)
        terminal.delete_file(tmp_file)

    def test_delete_file(self):
        terminal = Terminal()
        tmp_file = "tmp_file"
        terminal.touch_file(tmp_file)
        terminal.delete_file(tmp_file)
