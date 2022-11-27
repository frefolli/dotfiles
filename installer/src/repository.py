from .serializable import Serializable
from .package import Package

class Repository(Serializable):
    def __init__(self, repository = None):
        if repository == None:
            repository = []
        self._repository = repository

    def append(self, package : Package):
        self._repository.append(package)

    def to_str(self):
        return ("Repository(repository = [" +
                ", ".join(
                    [package.to_str() for package in self._repository])
                +"])")

    def to_dict(self):
        return [package.to_dict() for package in self._repository]

    def install(self):
        for package in self._repository:
            package.install()
