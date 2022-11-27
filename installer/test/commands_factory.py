from ..src.commands_factory import CommandsFactory
import json
import unittest

class TestCommandsFactory(unittest.TestCase):
    def test_from_json(self):
        the_json_text = """[]"""
        instance = CommandsFactory.from_json(the_json_text)
 
    def test_from_dict(self):
        the_dict = []
        instance = CommandsFactory.from_dict(the_dict)
