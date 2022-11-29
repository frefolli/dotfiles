"""
class DependenciesFactory
"""
from .dependency_factory import DependencyFactory
from .dependencies import Dependencies
import json

class DependenciesFactory:
    @staticmethod
    def from_json(the_json_text):
        the_dict = json.loads(the_json_text)
        return DependenciesFactory.from_dict(the_dict)

    @staticmethod
    def from_dict(the_dict):
        return Dependencies(
            [ DependencyFactory.from_dict(the_dependency_dict) for the_dependency_dict in the_dict ]
        )
