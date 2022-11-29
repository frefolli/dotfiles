import unittest
import tempfile
import os
from ..src.linux_terminal import LinuxTerminal

class TestLinuxTerminal(unittest.TestCase):
    def test_move_file(self):
        the_dir = tempfile.TemporaryDirectory()
        linux_terminal = LinuxTerminal()
        the_file = os.path.join(the_dir.name, "test_move_file_1")
        the_destination = os.path.join(the_dir.name, "test_move_file_2")
        linux_terminal.touch_file(the_file)
        linux_terminal.move_file(the_file, the_destination)
        linux_terminal.delete_file(the_destination)
        the_dir.cleanup()
    
    def test_copy_file(self):
        the_dir = tempfile.TemporaryDirectory()
        linux_terminal = LinuxTerminal()
        the_file = os.path.join(the_dir.name, "test_copy_file_1")
        the_destination = os.path.join(the_dir.name, "test_copy_file_2")
        linux_terminal.touch_file(the_file)
        linux_terminal.copy_file(the_file, the_destination)
        linux_terminal.delete_file(the_file)
        linux_terminal.delete_file(the_destination)
        the_dir.cleanup()
        
    def test_touch_delete_file(self):
        the_dir = tempfile.TemporaryDirectory()
        linux_terminal = LinuxTerminal()
        the_file = os.path.join(the_dir.name, "test_touch_delete_file")
        linux_terminal.touch_file(the_file)
        linux_terminal.delete_file(the_file)
        the_dir.cleanup()
        
    def test_create_delete_directory(self):
        the_dir = tempfile.TemporaryDirectory()
        linux_terminal = LinuxTerminal()
        the_file = os.path.join(the_dir.name, "test_create_delete_directory")
        linux_terminal.create_directory(the_file)
        linux_terminal.delete_directory(the_file)
        the_dir.cleanup()

    def test_fail_touch_file(self):
        the_dir = tempfile.TemporaryDirectory()
        linux_terminal = LinuxTerminal()
        try:
            linux_terminal.touch_file(f"{the_dir.name}/null/file")
            self.assertTrue(False)
        except Exception:
            pass
        the_dir.cleanup()

    def test_fail_delete_file(self):
        the_dir = tempfile.TemporaryDirectory()
        linux_terminal = LinuxTerminal()
        try:
            linux_terminal.delete_file(f"{the_dir.name}/null/file")
            self.assertTrue(False)
        except Exception:
            pass
        the_dir.cleanup()

    def test_fail_copy_file(self):
        the_dir = tempfile.TemporaryDirectory()
        linux_terminal = LinuxTerminal()
        try:
            linux_terminal.copy_file(f"{the_dir.name}/null/file {the_dir.name}/null2/file")
            self.assertTrue(False)
        except Exception:
            pass
        the_dir.cleanup()

    def test_fail_move_file(self):
        the_dir = tempfile.TemporaryDirectory()
        linux_terminal = LinuxTerminal()
        try:
            linux_terminal.move_file(f"{the_dir.name}/null/file {the_dir.name}/null2/file")
            self.assertTrue(False)
        except Exception:
            pass
        the_dir.cleanup()


    def test_fail_create_directory(self):
        the_dir = tempfile.TemporaryDirectory()
        linux_terminal = LinuxTerminal()
        try:
            linux_terminal.create_directory(f"{the_dir.name}/null/directory")
            self.assertTrue(False)
        except Exception:
            pass
        the_dir.cleanup()

    def test_fail_delete_directory(self):
        the_dir = tempfile.TemporaryDirectory()
        linux_terminal = LinuxTerminal()
        try:
            linux_terminal.delete_directory(f"{the_dir.name}/null/directory")
            self.assertTrue(False)
        except Exception:
            pass
        the_dir.cleanup()

