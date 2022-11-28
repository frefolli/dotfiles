import unittest
import json
from ..src.metadata import Metadata
from ..src.dependencies import Dependencies
from ..src.files import Files
from ..src.commands import Commands
from ..src.package import Package
from ..src.repository import Repository
from ..src.repository_factory import RepositoryFactory

class TestRepository(unittest.TestCase):
    def test_to_str(self):
        instance = Repository(package_names = [])
        self.assertTrue(instance.to_str() == "Repository(location = \"./repository\", package_names = [])")

    def test_to_dict(self):
        instance = Repository()
        self.assertTrue(instance.to_dict() == [])

    def test_to_json(self):
        instance = Repository()
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_append(self):
        the_package_names = ["name"]
        the_package_name = "another"
        instance = Repository(package_names = the_package_names)
        instance.append(the_package_name)
        self.assertTrue(the_package_name in instance.get_package_names())

    def test_remove(self):
        the_package_name = "name"
        instance = Repository(package_names = [the_package_name])
        instance.remove(the_package_name)
        self.assertTrue(the_package_name not in instance.get_package_names())

    def test_install(self):
        the_package_names = ["name"]
        instance = Repository(package_names = the_package_names)
        instance.install()

    def test_get_package(self):
        the_package_name = "bash"
        instance = Repository(package_names = [the_package_name])
        self.assertTrue(the_package_name not in instance._packages)
        instance.get_package(the_package_name)
        self.assertTrue(the_package_name in instance._packages)

    def test_cant_get_package(self):
        the_package_name = "bash"
        instance = Repository(package_names = [])
        try:
            instance.get_package(the_package_name)
        except:
            return
        self.fail("shouldn't exists in names")

    def test_location(self):
        the_location = "./repository"
        instance = RepositoryFactory.from_location(the_location)
        self.assertTrue(instance.get_location() == the_location)
