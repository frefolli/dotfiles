from .serializable import Serializable
from .package import Package

class Repository(Serializable):
    def __init__(self, package_names = None):
        if package_names == None:
            package_names = []
        self._package_names = package_names

    def append(self, package_name : str):
        self._package_names.append(package_name)

    def get_package_names(self):
        return self._package_names

    def to_str(self):
        return ("Repository(package_names = " +
                str(self._package_names)+")")

    def to_dict(self):
        return self._package_names

    def install(self):
        for package_name in self._package_names:
            # TODO: stub
            pass
