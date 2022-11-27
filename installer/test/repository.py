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
        self.assertTrue(instance.to_str() == "Repository(repository = [])")

    def test_to_dict(self):
        instance = Repository()
        self.assertTrue(instance.to_dict() == [])

    def test_to_json(self):
        instance = Repository()
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_append(self):
        instance = Repository()
        the_package = Package(
                Metadata("name", "author", "date", "version"),
                Dependencies(), Files(), Commands())
        instance.append(the_package)
        self.assertTrue(instance._repository == [the_package])

    def test_install(self):
        instance = Repository([
            Package(
                Metadata("name", "author", "date", "version"),
                Dependencies(), Files(), Commands())])
        instance.install()
