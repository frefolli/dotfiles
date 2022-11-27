from ..src.file_factory import FileFactory
import json
import unittest

class TestFileFactory(unittest.TestCase):
    def test_from_json(self):
        the_json_text = """{}"""
        instance = FileFactory.from_json(the_json_text)
 
    def test_from_dict(self):
        the_dict = {}
        instance = FileFactory.from_dict(the_dict)
