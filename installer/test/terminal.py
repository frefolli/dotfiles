import unittest
import tempfile
import os
from ..src.terminal import Terminal

class TestTerminal(unittest.TestCase):
    def test_move_file(self):
        the_dir = tempfile.TemporaryDirectory()
        terminal = Terminal()
        the_file = os.path.join(the_dir.name, "test_move_file_1")
        the_destination = os.path.join(the_dir.name, "test_move_file_2")
        try:
            terminal.touch_file(the_file)
            terminal.move_file(the_file, the_destination)
            terminal.delete_file(the_destination)
            self.assertTrue(False)
        except Exception:
            pass
        the_dir.cleanup()
    
    def test_copy_file(self):
        the_dir = tempfile.TemporaryDirectory()
        terminal = Terminal()
        the_file = os.path.join(the_dir.name, "test_copy_file_1")
        the_destination = os.path.join(the_dir.name, "test_copy_file_2")
        try:
            terminal.touch_file(the_file)
            terminal.copy_file(the_file, the_destination)
            terminal.delete_file(the_file)
            terminal.delete_file(the_destination)
            self.assertTrue(False)
        except Exception:
            pass
        the_dir.cleanup()
        
    def test_touch_delete_file(self):
        the_dir = tempfile.TemporaryDirectory()
        terminal = Terminal()
        the_file = os.path.join(the_dir.name, "test_touch_delete_file")
        try:
            terminal.touch_file(the_file)
            terminal.delete_file(the_file)
            self.assertTrue(False)
        except Exception:
            pass
        the_dir.cleanup()
        
    def test_create_delete_directory(self):
        the_dir = tempfile.TemporaryDirectory()
        terminal = Terminal()
        the_file = os.path.join(the_dir.name, "test_create_delete_directory")
        try:
            terminal.create_directory(the_file)
            terminal.delete_directory(the_file)
            self.assertTrue(False)
        except Exception:
            pass
        the_dir.cleanup()
