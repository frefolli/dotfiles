import unittest
import tempfile
import os
from ..src.terminal import Terminal

class TestTerminal(unittest.TestCase):
    def test_touch_file(self):
        the_dir = tempfile.TemporaryDirectory()
        terminal = Terminal()
        the_file = os.path.join(the_dir.name, "touch_file")
        try:
            terminal.touch_file(the_file)
            self.fail("should'nt be able to touch file")
        except Exception:
            pass
        the_dir.cleanup()

    def test_delete_file(self):
        the_dir = tempfile.TemporaryDirectory()
        terminal = Terminal()
        the_file = os.path.join(the_dir.name, "delete_file")
        try:
            terminal.delete_file(the_file)
            self.fail("should'nt be able to delete file")
        except Exception:
            pass
        the_dir.cleanup()

    def test_copy_file(self):
        the_dir = tempfile.TemporaryDirectory()
        terminal = Terminal()
        the_file = os.path.join(the_dir.name, "copy_file")
        the_destination = os.path.join(the_dir.name, "copy_destination")
        try:
            terminal.copy_file(the_file, the_destination)
            self.fail("should'nt be able to copy file")
        except Exception:
            pass
        the_dir.cleanup()

    def test_move_file(self):
        the_dir = tempfile.TemporaryDirectory()
        terminal = Terminal()
        the_file = os.path.join(the_dir.name, "move_file")
        the_destination = os.path.join(the_dir.name, "move_destination")
        try:
            terminal.move_file(the_file, the_destination)
            self.fail("should'nt be able to move file")
        except Exception:
            pass
        the_dir.cleanup()
    
    def test_create_directory(self):
        the_dir = tempfile.TemporaryDirectory()
        terminal = Terminal()
        the_directory = os.path.join(the_dir.name, "create_directory")
        try:
            terminal.create_directory(the_directory)
            self.fail("should'nt be able to create directory")
        except Exception:
            pass
        the_dir.cleanup()

    def test_delete_directory(self):
        the_dir = tempfile.TemporaryDirectory()
        terminal = Terminal()
        the_directory = os.path.join(the_dir.name, "delete_directory")
        try:
            terminal.delete_directory(the_directory)
            self.fail("should'nt be able to delete directory") 
        except Exception:
            pass
        the_dir.cleanup()
