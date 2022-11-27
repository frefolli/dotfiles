from .serializable import Serializable

class Dependency(Serializable):
    def to_str(self):
        return ("Dependency()")

    def to_dict(self):
        return {
            "type": "dependency",
        }

    def install(self):
        # TODO: stub
        pass
