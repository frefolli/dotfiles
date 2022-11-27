from .metadata import Metadata
import json

class MetadataFactory:
    @staticmethod
    def from_json(the_json_text):
        the_dict = json.loads(the_json_text)
        return MetadataFactory.from_dict(the_dict)

    @staticmethod
    def from_dict(the_dict):
        return Metadata(
            name = the_dict["name"], author = the_dict["author"],
            date = the_dict["date"], version = the_dict["version"])
