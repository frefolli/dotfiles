"""
class FilesFactory
"""
from .file_factory import FileFactory
from .files import Files
import json

class FilesFactory:
    @staticmethod
    def from_json(the_json_text):
        the_dict = json.loads(the_json_text)
        return FilesFactory.from_dict(the_dict)

    @staticmethod
    def from_dict(the_dict):
        return Files(
            [ FileFactory.from_dict(the_file_dict) for the_file_dict in the_dict ]
        )
