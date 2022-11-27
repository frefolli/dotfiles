from .package_factory import PackageFactory
from .repository import Repository
import json

class RepositoryFactory:
    @staticmethod
    def from_json(the_json_text):
        the_dict = json.loads(the_json_text)
        return RepositoryFactory.from_dict(the_dict)

    @staticmethod
    def from_dict(the_dict):
        return Repository(
            [ PackageFactory.from_dict(the_package_dict) for the_package_dict in the_dict ]
        )
