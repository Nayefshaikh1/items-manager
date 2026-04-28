import json
import os
from storage_base import StorageBase


class FileStorage(StorageBase):
    def __init__(self, file_path="data.json"):
        self.file_path = file_path

    def save_items(self, items):
        with open(self.file_path, "w") as f:
            json.dump(items, f)

    def load_items(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as f:
            return json.load(f)