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
        return ("Dependencies(dependencies = [" +
                ", ".join(
                    [dependency.to_str() for dependency in self._dependencies])
                +"])")

    def to_dict(self):
        return [dependency.to_dict() for dependency in self._dependencies]

    def install(self):
        for dependency in self._dependencies:
            dependency.install()
