from ..src.files_factory import FilesFactory
import json
import unittest

class TestFilesFactory(unittest.TestCase):
    def test_from_json(self):
        the_json_text = """[]"""
        instance = FilesFactory.from_json(the_json_text)
 
    def test_from_dict(self):
        the_dict = []
        instance = FilesFactory.from_dict(the_dict)
