from .serializable import Serializable

class Metadata(Serializable):
    def __init__(self, name : str, author : str, date : str):
        self._name = name
        self._author = author
        self._date = date

    def to_str(self):
        return ("Metadata(" +
                "name = \"" + self._name + "\", " +
                "author = \"" + self._author + "\", " +
                "date = \"" + self._date + "\")")

    def to_dict(self):
        return {
            "type": "metadata",
            "name": self._name,
            "author": self._author,
            "date": self._date
        }
