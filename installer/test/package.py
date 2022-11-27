import unittest
import json
from ..src.metadata import Metadata
from ..src.files import Files
from ..src.commands import Commands
from ..src.package import Package

class TestPackage(unittest.TestCase):
    def test_to_str(self):
        instance = Package(
                Metadata("name", "author", "date"),
                Files(), Commands())
        self.assertTrue(instance.to_str() == (
            "Package(" + 
            "metadata = " + instance._metadata.to_str() + ", " + 
            "content = " + instance._content.to_str() + ", " +
            "post_install = " + instance._post_install.to_str() + ")"))

    def test_to_dict(self):
        instance = Package(
                Metadata("name", "author", "date"),
                Files(), Commands())
        self.assertTrue(instance.to_dict() == {
            "type": "package",
            "metadata": instance._metadata.to_dict(),
            "content": instance._content.to_dict(),
            "post_install": instance._post_install.to_dict()
        })

    def test_to_json(self):
        instance = Package(
                Metadata("name", "author", "date"), 
                Files(), Commands())
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))