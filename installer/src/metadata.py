"""
class Metadata
"""
from .serializable import Serializable

class Metadata(Serializable):
    def __init__(self, name : str, author : str, date : str, version : str):
        self._name = name
        self._author = author
        self._date = date
        self._version = version

    def get_name(self):
        return self._name

    def get_author(self):
        return self._author

    def get_date(self):
        return self._date

    def get_version(self):
        return self._version

    def to_str(self):
        return ("Metadata(" +
                "name = \"" + self.get_name() + "\", " +
                "author = \"" + self.get_author() + "\", " +
                "date = \"" + self.get_date() + "\", " + 
                "version = \"" + self.get_version() + "\")")

    def to_dict(self):
        return {
            "name": self.get_name(),
            "author": self.get_author(),
            "date": self.get_date(),
            "version": self.get_version()
        }
