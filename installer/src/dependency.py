from .serializable import Serializable

class Dependency(Serializable):
    def to_str(self):
        return ("Dependency()")

    def to_dict(self):
        return {}

    def install(self):
        # TODO: stub
        pass
