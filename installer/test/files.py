import unittest
import json
from ..src.file import File
from ..src.files import Files

class TestFiles(unittest.TestCase):
    def test_to_str(self):
        instance = Files([])
        self.assertTrue(instance.to_str() == "Files(files = [])")

    def test_to_dict(self):
        instance = Files()
        self.assertTrue(instance.to_dict() == {
            "type": "files",
            "files": []
        })

    def test_to_json(self):
        instance = Files()
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_append(self):
        instance = Files()
        the_file = File()
        instance.append(the_file)
        self.assertTrue(instance._files == [the_file])

    def test_install(self):
        instance = Files([File()])
        instance.install()
