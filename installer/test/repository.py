import unittest
import json
from ..src.metadata import Metadata
from ..src.dependencies import Dependencies
from ..src.files import Files
from ..src.commands import Commands
from ..src.package import Package
from ..src.repository import Repository
from ..src.repository_factory import RepositoryFactory
import tempfile
from ..src.terminal_factory import TerminalFactory

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

    def test_install_some_packages(self):
        the_location = tempfile.TemporaryDirectory()
        with open(f"{the_location.name}/index.json", "w") as the_repository_index:
            the_repository_index.write("[ \"dummy\" ]")
        terminal = TerminalFactory.get_terminal()
        terminal.create_directory(f"{the_location.name}/dummy")
        with open(f"{the_location.name}/dummy/index.json", "w") as the_dummy_package_index:
            the_dummy_package_index.write("""
            {
                "metadata": {
                    "name": "dummy",
                    "author": "dummy",
                    "date": "dummy",
                    "version": "dummy"
                },
                "dependencies": [],
                "content": [],
                "post_install": []
            }
            """)
        instance = RepositoryFactory.from_location(the_location.name)
        instance.install_packages(["dummy"])
        the_installed_packages = instance.get_installed_packages()
        self.assertTrue(the_installed_packages == ["dummy"])
        the_location.cleanup()

    def test_install_no_packages(self):
        instance = Repository()
        instance.install_packages()
        the_installed_packages = instance.get_installed_packages()
        self.assertTrue(the_installed_packages == [])

    def test_get_package(self):
        the_package_name = "bash"
        instance = Repository(package_names = [the_package_name])
        self.assertTrue(the_package_name not in instance._packages)
        instance.get_package(the_package_name)
        self.assertTrue(the_package_name in instance._packages)

    def test_cant_get_package(self):
        the_package_name = "bash"
        instance = Repository(package_names = [])
        thrown_error = False
        try:
            instance.get_package(the_package_name)
        except Exception:
            thrown_error = True
        self.assertTrue(thrown_error)

    def test_location(self):
        the_location = "./repository"
        instance = RepositoryFactory.from_location(the_location)
        self.assertTrue(instance.get_location() == the_location)
