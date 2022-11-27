import unittest
import json
from ..src.command import Command

class TestCommand(unittest.TestCase):
    def test_to_str(self):
        instance = Command()
        self.assertTrue(instance.to_str() == "Command()")

    def test_to_dict(self):
        instance = Command()
        self.assertTrue(instance.to_dict() == {
            "type": "command"
        })

    def test_to_json(self):
        instance = Command()
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_run(self):
        instance = Command()
        instance.run()
