import unittest
import json
from ..src.dependency import Dependency

class TestDependency(unittest.TestCase):
    def test_to_str(self):
        the_dependency_name = "dependency"
        instance = Dependency(the_dependency_name)
        self.assertTrue(instance.to_str() == "Dependency(" +
                        "package_name = \"" +
                        the_dependency_name + "\")")

    def test_to_dict(self):
        the_dependency_name = "dependency"
        instance = Dependency(the_dependency_name)
        self.assertTrue(instance.to_dict() == the_dependency_name)

    def test_to_json(self):
        the_dependency_name = "dependency"
        instance = Dependency(the_dependency_name)
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))

    def test_install(self):
        the_dependency_name = "dependency"
        instance = Dependency(the_dependency_name)
        instance.install()
