import unittest
import json
from ..src.dependency import Dependency
from ..src.dependencies import Dependencies

class TestDependencies(unittest.TestCase):
    def test_to_str(self):
        instance = Dependencies([])
        self.assertTrue(instance.to_str() == "Dependencies(dependencies = [])")

    def test_to_dict(self):
        instance = Dependencies()
        self.assertTrue(instance.to_dict() == [])

    def test_to_json(self):
        instance = Dependencies()
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_append(self):
        instance = Dependencies()
        the_dependency = Dependency()
        instance.append(the_dependency)
        self.assertTrue(instance._dependencies == [the_dependency])

    def test_install(self):
        instance = Dependencies([Dependency()])
        instance.install()
