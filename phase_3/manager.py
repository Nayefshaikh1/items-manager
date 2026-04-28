from item import build_item
from file_storage import FileStorage


class ItemsManager:
    def __init__(self, storage=None):
        self.storage = storage if storage else FileStorage()
        self.items = self.storage.load_items()
        self.next_id = self._get_next_id()

    #  Helper methods

    def _get_next_id(self):
        if not self.items:
            return 1
        return max(item["id"] for item in self.items) + 1

    def _is_valid_title(self, title):
        return isinstance(title, str) and title.strip() != ""

    def _find_index(self, id):
        for i, item in enumerate(self.items):
            if item["id"] == id:
                return i
        return -1

    def _save(self):
        self.storage.save_items(self.items)

    # CRUD methods

    def create_item(self, title, details):
        if not self._is_valid_title(title):
            return None

        item = build_item(self.next_id, title, details)
        self.items.append(item)
        self.next_id += 1
        self._save()
        return item

    def list_items(self):
        return self.items

    def find_item(self, id):
        index = self._find_index(id)
        if index == -1:
            return None
        return self.items[index]

    def update_item(self, id, title, details):
        index = self._find_index(id)
        if index == -1:
            return None

        if title:
            self.items[index]["title"] = title
        if details is not None:
            self.items[index]["details"] = details

        self._save()
        return self.items[index]

    def delete_item(self, id):
        index = self._find_index(id)
        if index == -1:
            return None

        item = self.items.pop(index)
        self._save()
        return item


if __name__ == "__main__":
    manager = ItemsManager()
    manager.create_item("Hello", "World")
    manager.create_item("Another", "Item")  
    print(manager.list_items())