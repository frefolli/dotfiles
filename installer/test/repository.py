import unittest
import json
from ..src.metadata import Metadata
from ..src.dependencies import Dependencies
from ..src.files import Files
from ..src.commands import Commands
from ..src.package import Package
from ..src.repository import Repository

class TestRepository(unittest.TestCase):
    def test_to_str(self):
        instance = Repository([])
        self.assertTrue(instance.to_str() == "Repository(package_names = [])")

    def test_to_dict(self):
        instance = Repository()
        self.assertTrue(instance.to_dict() == [])

    def test_to_json(self):
        instance = Repository()
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_append(self):
        instance = Repository()
        the_package_names = ["name"]
        the_package_name = "another"
        instance.append(the_package_name)
        self.assertTrue(the_package_name in instance.get_package_names())

    def test_install(self):
        the_package_names = ["name"]
        instance = Repository(the_package_names)
        instance.install()
