from ..src.file_factory import FileFactory
import json
import unittest

class TestFileFactory(unittest.TestCase):
    def test_from_dict(self):
        the_dict = [".file", "~/.file"]
        instance = FileFactory.from_dict(the_dict)
        self.assertTrue(the_dict == instance.to_dict())

    def test_from_json(self):
        the_json_text = "[\".file\", \"~/.file\"]"
        instance = FileFactory.from_json(the_json_text)
        self.assertTrue(the_json_text == instance.to_json())
