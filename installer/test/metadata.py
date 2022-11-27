import unittest
import json
from ..src.metadata import Metadata

class TestMetadata(unittest.TestCase):
    def test_to_str(self):
        instance = Metadata("name", "author", "date", "version")
        self.assertTrue(instance.to_str() == (
            "Metadata("
            "name = \"name\", " +
            "author = \"author\", " +
            "date = \"date\", " +
            "version = \"version\")"))

    def test_to_dict(self):
        instance = Metadata("name", "author", "date", "version")
        self.assertTrue(instance.to_dict() == {
            "name": "name",
            "author": "author",
            "date": "date",
            "version": "version"
        })

    def test_to_json(self):
        instance = Metadata("name", "author", "date", "version")
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_gets(self):
        instance = Metadata("name", "author", "date", "version")
        self.assertTrue(instance.get_name() == "name")
        self.assertTrue(instance.get_author() == "author")
        self.assertTrue(instance.get_date() == "date")
        self.assertTrue(instance.get_version() == "version")
 
