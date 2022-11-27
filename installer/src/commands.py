from .serializable import Serializable
from .command import Command

class Commands(Serializable):
    def __init__(self, commands = None):
        if commands == None:
            commands = []
        self._commands = []

    def append(self, command : Command):
        self._commands.append(command)

    def to_str(self):
        return ("Commands(commands = [" +
                ", ".join(
                    [command.to_str() for command in self._commands])
                +"])")

    def to_dict(self):
        return {
            "type": "commands",
            "commands": [command.to_dict() for command in self._commands]
        }