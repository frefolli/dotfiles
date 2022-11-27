import unittest
import json
from ..src.dependency import Dependency

class TestDependency(unittest.TestCase):
    def test_to_str(self):
        instance = Dependency()
        self.assertTrue(instance.to_str() == "Dependency()")

    def test_to_dict(self):
        instance = Dependency()
        self.assertTrue(instance.to_dict() == {})

    def test_to_json(self):
        instance = Dependency()
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_install(self):
        instance = Dependency()
        instance.install()
