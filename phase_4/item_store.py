from item import Item

class ItemStore:
    def __init__(self, storage):
        self.storage = storage
        self.items = []
        self.next_id = 1

        self._load()

    #  LOAD 
    def _load(self):
        data = self.storage.load()
        self.items = [Item.from_dict(d) for d in data]

        if self.items:
            self.next_id = max(item.id for item in self.items) + 1

    #  SAVE 
    def _save(self):
        data = [item.to_dict() for item in self.items]
        self.storage.save(data)

    #  HELPER 
    def _find_index(self, item_id):
        for i, item in enumerate(self.items):
            if item.id == item_id:
                return i
        return -1

    # ---------- CRUD ----------
    def create(self, item):
        self.items.append(item)
        self._save()

    def list(self):
        return self.items

    def find(self, item_id):
        idx = self._find_index(item_id)
        return None if idx == -1 else self.items[idx]

    def delete(self, item_id):
        idx = self._find_index(item_id)
        if idx == -1:
            return None

        item = self.items.pop(idx)
        self._save()
        return item