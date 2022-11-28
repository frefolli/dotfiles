from ..src.metadata import Metadata
from ..src.dependencies import Dependencies
from ..src.files import Files
from ..src.commands import Commands
from ..src.package_factory import PackageFactory
import json
import unittest

class TestPackageFactory(unittest.TestCase):
    def test_from_location(self):
        the_name = "bash"
        the_location = f"./repository/{the_name}"
        instance = PackageFactory.from_location(the_location)
        self.assertTrue(the_name == instance.get_metadata().get_name())

    def test_from_json(self):
        metadata = Metadata("name", "author", "date", "version")
        dependencies = Dependencies([])
        content = Files([])
        post_install = Commands([])
        the_json_text = """
        {
            \"metadata\": """ + metadata.to_json() + """,
            \"dependencies\": """ + dependencies.to_json() + """,
            \"content\": """ + content.to_json() + """,
            \"post_install\": """ + post_install.to_json() + """
        }
        """
        instance = PackageFactory.from_json(the_json_text)
        self.assertTrue(instance.get_metadata().to_json() == metadata.to_json())
        self.assertTrue(instance.get_dependencies().to_json() == dependencies.to_json())
        self.assertTrue(instance.get_content().to_json() == content.to_json())
        self.assertTrue(instance.get_post_install().to_json() == post_install.to_json())
 
    def test_from_dict(self):
        metadata = Metadata("name", "author", "date", "version")
        dependencies = Dependencies([])
        content = Files([])
        post_install = Commands([])
        the_dict = {
                "metadata": metadata.to_dict(),
                "dependencies": dependencies.to_dict(),
                "content": content.to_dict(),
                "post_install": post_install.to_dict()
        }
        instance = PackageFactory.from_dict(the_dict)
        self.assertTrue(instance.get_metadata().to_dict() == metadata.to_dict())
        self.assertTrue(instance.get_dependencies().to_dict() == dependencies.to_dict())
        self.assertTrue(instance.get_content().to_dict() == content.to_dict())
        self.assertTrue(instance.get_post_install().to_dict() == post_install.to_dict())
