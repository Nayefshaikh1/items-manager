from item import Item

class FileRepository:
    def __init__(self, storage):
        self.storage = storage
        self.items = []
        self._load()

    def _load(self):
        data = self.storage.load()
        self.items = [Item.from_dict(d) for d in data]

    def _save(self):
        self.storage.save([i.to_dict() for i in self.items])

    def get_next_id(self):
        return max([i.id for i in self.items], default=0) + 1

    def create(self, item):
        self.items.append(item)
        self._save()

    def list(self):
        return self.items

    def find(self, item_id):
        return next((i for i in self.items if i.id == item_id), None)

    def update(self, item):
        self._save()
        return item

    def delete(self, item_id):
        self.items = [i for i in self.items if i.id != item_id]
        self._save()