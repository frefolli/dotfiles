from .serializable import Serializable

class File(Serializable):
    def to_str(self):
        return ("File()")

    def to_dict(self):
        return {}

    def install(self):
        # TODO: stub
        pass
