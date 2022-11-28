from .metadata_factory import MetadataFactory
from .files_factory import FilesFactory
from .commands_factory import CommandsFactory
from .dependencies_factory import DependenciesFactory
from .package import Package
import json

class PackageFactory:
    @staticmethod
    def from_location(location):
        with open(f"{location}/index.json", "r") as the_json_file:
            the_json_text = the_json_file.read()
            instance = PackageFactory.from_json(the_json_text)
            return instance

    @staticmethod
    def from_json(the_json_text):
        the_dict = json.loads(the_json_text)
        return PackageFactory.from_dict(the_dict)

    @staticmethod
    def from_dict(the_dict):
        return Package(
                metadata = MetadataFactory.from_dict(the_dict["metadata"]),
                dependencies = DependenciesFactory.from_dict(the_dict["dependencies"]),
                content = FilesFactory.from_dict(the_dict["content"]),
                post_install = CommandsFactory.from_dict(the_dict["post_install"]))
