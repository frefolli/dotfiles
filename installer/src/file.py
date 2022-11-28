from .serializable import Serializable

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
        # TODO: stub
        pass
