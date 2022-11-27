import unittest
import json
from ..src.serializable import Serializable

class TestSerializable(unittest.TestCase):
    def test_to_str(self):
        instance = Serializable()
        self.assertTrue(instance.to_str() == "Serializable()")

    def test_to_dict(self):
        instance = Serializable()
        self.assertTrue(instance.to_dict() == {})

    def test_to_json(self):
        instance = Serializable()
        self.assertTrue(instance.to_json() == json.dumps(instance.to_dict()))
