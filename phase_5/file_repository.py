from item_repository import ItemRepository
from item import Item

class FileItemRepository(ItemRepository):
    def __init__(self, storage):
        self.storage = storage
        self.items = []
        self._load()

    def _load(self):
        data = self.storage.load()
        self.items = [Item.from_dict(d) for d in data]

    def _save(self):
        data = [item.to_dict() for item in self.items]
        self.storage.save(data)

    def get_next_id(self):
        if not self.items:
            return 1
        return max(item.id for item in self.items) + 1

    def create(self, item):
        self.items.append(item)
        self._save()

    def list(self):
        return self.items

    def find(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def update(self, item):
        self._save()
        return item

    def delete(self, item_id):
        for i, item in enumerate(self.items):
            if item.id == item_id:
                removed = self.items.pop(i)
                self._save()
                return removed
        return None