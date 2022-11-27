import json

class Serializable:
    def to_str(self):
        return "Serializable()"

    def to_dict(self):
        return {}

    def to_json(self):
        return json.dumps(self.to_dict())
