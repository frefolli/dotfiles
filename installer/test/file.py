import unittest
import json
from ..src.file import File
import tempfile

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
        the_file = tempfile.TemporaryFile()
        the_destination = tempfile.TemporaryFile()
        instance = File(the_file.name, the_destination.name)
        instance.install()
        the_file.close()
        the_destination.close()
