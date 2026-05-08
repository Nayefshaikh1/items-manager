from item import Item

class ItemService:
    def __init__(self, repository):
        self.repository = repository

    def create_item(self, title, details):
        try:
            item_id = self.repository.get_next_id()
            item = Item(item_id, title, details)
            self.repository.create(item)
            return item
        except ValueError:
            return None

    def list_items(self):
        return self.repository.list()

    def find_item(self, item_id):
        return self.repository.find(item_id)

    def update_item(self, item_id, title=None, details=None):
        item = self.repository.find(item_id)
        if not item:
            return None

        try:
            item.update(title, details)
            return self.repository.update(item)
        except ValueError:
            return None

    def delete_item(self, item_id):
        return self.repository.delete(item_id)