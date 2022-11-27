import unittest
import json
from ..src.command import Command
from ..src.commands import Commands

class TestCommands(unittest.TestCase):
    def test_to_str(self):
        instance = Commands([])
        self.assertTrue(instance.to_str() == "Commands(commands = [])")

    def test_to_dict(self):
        instance = Commands()
        self.assertTrue(instance.to_dict() == {
            "type": "commands",
            "commands": []
        })

    def test_to_json(self):
        instance = Commands()
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_append(self):
        instance = Commands()
        the_command = Command()
        instance.append(the_command)
        self.assertTrue(instance._commands == [the_command])

    def test_run(self):
        instance = Commands([Command()])
        instance.run()
