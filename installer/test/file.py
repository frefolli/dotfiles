import unittest
import json
from ..src.file import File

class TestFile(unittest.TestCase):
    def test_to_str(self):
        instance = File()
        self.assertTrue(instance.to_str() == "File()")

    def test_to_dict(self):
        instance = File()
        self.assertTrue(instance.to_dict() == {
            "type": "file"
        })

    def test_to_json(self):
        instance = File()
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_install(self):
        instance = File()
        instance.install()
