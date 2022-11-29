"""
class Files
"""
from .serializable import Serializable
from .file import File

class Files(Serializable):
    def __init__(self, files = None):
        if files == None:
            files = []
        self._files = files

    def append(self, file : File):
        self._files.append(file)

    def to_str(self):
        return ("Files(files = [" +
                ", ".join(
                    [file.to_str() for file in self._files])
                +"])")

    def to_dict(self):
        return [file.to_dict() for file in self._files]

    def install(self, location):
        for file in self._files:
            file.install(location)
