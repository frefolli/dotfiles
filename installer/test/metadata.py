import unittest
import json
from ..src.metadata import Metadata

class TestMetadata(unittest.TestCase):
    def test_to_str(self):
        instance = Metadata("name", "author", "date")
        self.assertTrue(instance.to_str() == (
            "Metadata("
            "name = \"name\", " +
            "author = \"author\", " +
            "date = \"date\")"))

    def test_to_dict(self):
        instance = Metadata("name", "author", "date")
        self.assertTrue(instance.to_dict() == {
            "type": "metadata",
            "name": "name",
            "author": "author",
            "date": "date"
        })

    def test_to_json(self):
        instance = Metadata("name", "author", "date")
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))
