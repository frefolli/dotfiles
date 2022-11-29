"""
class Dependencies
"""
from .serializable import Serializable
from .dependency import Dependency

class Dependencies(Serializable):
    def __init__(self, dependencies = None):
        if dependencies == None:
            dependencies = []
        self._dependencies = dependencies

    def append(self, dependency : Dependency):
        self._dependencies.append(dependency)

    def to_str(self):
        return ("Dependencies(dependencies = " +
                    str([dependency.get_package_name() for dependency in self._dependencies])+ ")")

    def get_dependencies(self):
        return [dependency.get_package_name() for dependency in self._dependencies]

    def to_dict(self):
        return [dependency.to_dict() for dependency in self._dependencies]

    def install(self):
        for dependency in self._dependencies:
            dependency.install()
