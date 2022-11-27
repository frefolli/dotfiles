from ..src.metadata_factory import MetadataFactory
import json
import unittest

class TestMetadataFactory(unittest.TestCase):
    def test_from_json(self):
        the_json_text = """
        {
            \"name\": \"name\",
            \"author\": \"author\",
            \"date\": \"date\",
            \"version\": \"version\"
        }
        """
        instance = MetadataFactory.from_json(the_json_text)
        self.assertTrue(instance.get_name() == "name")
        self.assertTrue(instance.get_author() == "author")
        self.assertTrue(instance.get_date() == "date")
        self.assertTrue(instance.get_version() == "version")
 
    def test_from_dict(self):
        the_dict = {
            "name": "name",
            "author": "author",
            "date": "date",
            "version": "version"
        }
        instance = MetadataFactory.from_dict(the_dict)
        self.assertTrue(instance.get_name() == "name")
        self.assertTrue(instance.get_author() == "author")
        self.assertTrue(instance.get_date() == "date")
        self.assertTrue(instance.get_version() == "version")
