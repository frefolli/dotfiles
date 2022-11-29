from .serializable import Serializable
from .terminal_factory import TerminalFactory

class File(Serializable):
    def __init__(self, file : str, destination : str):
        self._file = file
        self._destination = destination

    def get_file(self):
        return self._file

    def get_destination(self):
        return self._destination

    def to_str(self):
        return ("File(file = \"" +
                self._file + "\", destination = \"" +
                self._destination +"\")")

    def to_dict(self):
        return [ self._file, self._destination ]

    def install(self):
        terminal = TerminalFactory.get_terminal()
        terminal.copy_file(self._file, self._destination)
