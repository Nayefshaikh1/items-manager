import json
import os

class JsonStorage:
    def __init__(self, file_path="data.json"):
        self.file_path = file_path

    def load(self):
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except:
            return []

    def save(self, items):
        with open(self.file_path, "w") as f:
            json.dump(items, f, indent=4)