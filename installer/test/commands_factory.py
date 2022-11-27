from ..src.commands_factory import CommandsFactory
import json
import unittest

class TestCommandsFactory(unittest.TestCase):
    def test_from_json(self):
        the_json_text = """[]"""
        instance = CommandsFactory.from_json(the_json_text)
        self.assertTrue(the_json_text == instance.to_json())
 
    def test_from_dict(self):
        the_dict = []
        instance = CommandsFactory.from_dict(the_dict)
        self.assertTrue(the_dict == instance.to_dict())
