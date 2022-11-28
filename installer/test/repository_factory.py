from ..src.repository_factory import RepositoryFactory
import json
import unittest

class TestRepositoryFactory(unittest.TestCase):
    def test_from_location(self):
        the_location = "./repository"
        instance = RepositoryFactory.from_location(the_location)
        self.assertTrue(the_location == instance.get_location())

    def test_from_dict(self):
        the_dict = []
        instance = RepositoryFactory.from_dict(the_dict)
        self.assertTrue(the_dict == instance.to_dict())

    def test_from_json(self):
        the_json_text = """[]"""
        instance = RepositoryFactory.from_json(the_json_text)
        self.assertTrue(the_json_text == instance.to_json())
