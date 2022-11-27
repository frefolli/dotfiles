from .dependency import Dependency
import json

class DependencyFactory:
    @staticmethod
    def from_json(the_json_text):
        the_dict = json.loads(the_json_text)
        return DependencyFactory.from_dict(the_dict)

    @staticmethod
    def from_dict(the_dict):
        return Dependency()
