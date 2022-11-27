from .serializable import Serializable

class Command(Serializable):
    def to_str(self):
        return ("Command()")

    def to_dict(self):
        return {
            "type": "command",
        }

    def run(self):
        # this is a template method
        pass
