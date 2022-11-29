from .serializable import Serializable
from .package import Package
from .package_factory import PackageFactory
from .package_not_found_exception import PackageNotFoundException
import os

class Repository(Serializable):
    def __init__(self, location = None,
                        package_names = None):
        if package_names == None:
            package_names = []
        if location == None:
            location = "./repository"
        self._location = location
        self._package_names = package_names
        self._packages = {}
        self._installed_packages = []

    def append(self, package_name : str):
        self._package_names.append(package_name)

    def remove(self, package_name : str):
        self._package_names.remove(package_name)

    def get_package_names(self):
        return self._package_names
    
    def _read_package(self, name : str):
        the_location = os.path.join(self.get_location(), name)
        self._packages[name] = PackageFactory.from_location(the_location)
    
    def get_package(self, name : str):
        if name not in self._package_names:
            raise PackageNotFoundException(name)
        if name not in self._packages:
            self._read_package(name)
        return self._packages[name]
    
    def get_location(self):
        return self._location

    def is_installed(self, package_name : str):
        return package_name in self._installed_packages

    def get_installed_packages(self):
        return self._installed_packages

    def to_str(self):
        return ("Repository(" + 
                "location = \"" + self._location + "\", " +
                "package_names = " + str(self._package_names) + ")")

    def to_dict(self):
        return self._package_names

    def install_packages(self, package_names = None):
        if package_names == None:
            package_names = []
        for package_name in package_names:
            self.install_package(package_name)

    def install_package(self, package_name : str):
        if not self.is_installed(package_name):
            the_package = self.get_package(package_name)
            the_package.install(self._location + "/" + package_name)
            self._installed_packages.append(package_name)
