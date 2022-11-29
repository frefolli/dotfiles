import unittest
import json
from ..src.file import File
from ..src.terminal_factory import TerminalFactory
import tempfile
import os

class TestFile(unittest.TestCase):
    def test_to_str(self):
        the_file = "file"
        the_destination = "destination"
        instance = File(file = the_file, destination = the_destination)
        self.assertTrue(instance.to_str() == ("File(" +
            "file = \"file\", "
            "destination = \"destination\"" + ")"))

    def test_to_dict(self):
        the_file = "file"
        the_destination = "destination"
        instance = File(file = the_file, destination = the_destination)
        self.assertTrue(instance.to_dict() == [instance.get_file(), instance.get_destination()])

    def test_to_json(self):
        the_file = "file"
        the_destination = "destination"
        instance = File(file = the_file, destination = the_destination)
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_install(self):
        the_directory = tempfile.TemporaryDirectory()
        the_file = os.path.join(the_directory.name, "file")
        the_destination = os.path.join(the_directory.name, "destination")
        terminal = TerminalFactory.get_terminal()
        terminal.touch_file(the_file)
        instance = File(the_file, the_destination)
        instance.install()
        terminal.delete_file(the_destination)
        the_directory.cleanup()
