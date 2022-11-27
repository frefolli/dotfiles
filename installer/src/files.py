from .serializable import Serializable
from .file import File

class Files(Serializable):
    def __init__(self, files = None):
        if files == None:
            files = []
        self._files = []

    def append(self, file : File):
        self._files.append(file)

    def to_str(self):
        return ("Files(files = [" +
                ", ".join(
                    [file.to_str() for file in self._files])
                +"])")

    def to_dict(self):
        return {
            "type": "files",
            "files": [file.to_dict() for file in self._files]
        }