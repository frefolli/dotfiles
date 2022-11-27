from .file import File
import json

class FileFactory:
    @staticmethod
    def from_json(the_json_text):
        the_dict = json.loads(the_json_text)
        return FileFactory.from_dict(the_dict)

    @staticmethod
    def from_dict(the_dict):
        return File()
