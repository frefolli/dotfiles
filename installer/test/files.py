import unittest
import json
from ..src.file import File
from ..src.files import Files
import tempfile

class TestFiles(unittest.TestCase):
    def test_to_str(self):
        instance = Files([])
        self.assertTrue(instance.to_str() == "Files(files = [])")

    def test_to_dict(self):
        instance = Files()
        self.assertTrue(instance.to_dict() == [])

    def test_to_json(self):
        instance = Files()
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_append(self):
        instance = Files()
        the_file = File("file", "destination")
        instance.append(the_file)
        self.assertTrue(instance._files == [the_file])

    def test_install(self):
        the_file = tempfile.TemporaryFile()
        the_destination = tempfile.TemporaryFile()
        instance = Files([File(the_file, the_destination)])
        instance.install()
        the_file.close()
        the_destination.close()
