from .serializable import Serializable

class Dependency(Serializable):
    def __init__(self, package_name : str):
        self._package_name = package_name

    def get_package_name(self):
        return self._package_name

    def to_str(self):
        return ("Dependency(package_name = \"" +
                self._package_name + "\")")

    def to_dict(self):
        return self._package_name

    def install(self):
        # TODO: stub
        pass
