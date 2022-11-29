"""
class CommandFactory
"""
from .command import Command
import json

class CommandFactory:
    @staticmethod
    def from_json(the_json_text):
        the_dict = json.loads(the_json_text)
        return CommandFactory.from_dict(the_dict)

    @staticmethod
    def from_dict(the_dict):
        return Command()
