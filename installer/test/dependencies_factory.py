from ..src.dependencies_factory import DependenciesFactory
import json
import unittest

class TestDependenciesFactory(unittest.TestCase):
    def test_from_json(self):
        the_json_text = """[]"""
        instance = DependenciesFactory.from_json(the_json_text)
 
    def test_from_dict(self):
        the_dict = []
        instance = DependenciesFactory.from_dict(the_dict)
