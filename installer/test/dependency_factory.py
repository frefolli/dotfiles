from ..src.dependency_factory import DependencyFactory
import json
import unittest

class TestDependencyFactory(unittest.TestCase):
    def test_from_json(self):
        the_json_text = """{}"""
        instance = DependencyFactory.from_json(the_json_text)
 
    def test_from_dict(self):
        the_dict = {}
        instance = DependencyFactory.from_dict(the_dict)

    def test_dict(self):
        the_dict = {}
        instance = DependencyFactory.from_dict(the_dict)
        self.assertTrue(the_dict == instance.to_dict())

    def test_json(self):
        the_json_text = """{}"""
        instance = DependencyFactory.from_json(the_json_text)
        self.assertTrue(the_json_text == instance.to_json())
