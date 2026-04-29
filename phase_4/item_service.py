from item import Item

class ItemService:
    def __init__(self, store):
        self.store = store

    def create_item(self, title, details):
        try:
            item_id = self.store.next_id
            item = Item(item_id, title, details)

            self.store.create(item)
            self.store.next_id += 1

            return item
        except ValueError:
            return None

    def list_items(self):
        return self.store.list()

    def find_item(self, item_id):
        return self.store.find(item_id)

    def update_item(self, item_id, title=None, details=None):
        item = self.store.find(item_id)
        if not item:
            return None

        try:
            item.update(title, details)
            self.store._save()
            return item
        except ValueError:
            return None

    def delete_item(self, item_id):
        return self.store.delete(item_id)