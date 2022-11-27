from .command_factory import CommandFactory
from .commands import Commands
import json

class CommandsFactory:
    @staticmethod
    def from_json(the_json_text):
        the_dict = json.loads(the_json_text)
        return CommandsFactory.from_dict(the_dict)

    @staticmethod
    def from_dict(the_dict):
        return Commands(
            [ CommandFactory.from_dict(the_command_dict) for the_command_dict in the_dict ]
        )
