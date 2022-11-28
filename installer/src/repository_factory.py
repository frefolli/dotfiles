from .package_factory import PackageFactory
from .repository import Repository
import json

class RepositoryFactory:
    @staticmethod
    def from_location(location):
        with open(f"{location}/index.json", "r") as the_json_file:
            the_json_text = the_json_file.read()
            instance = RepositoryFactory.from_json(the_json_text)
            instance._location = location
            return instance

    @staticmethod
    def from_json(the_json_text):
        the_dict = json.loads(the_json_text)
        return RepositoryFactory.from_dict(the_dict)

    @staticmethod
    def from_dict(the_dict):
        return Repository(package_names = the_dict)
