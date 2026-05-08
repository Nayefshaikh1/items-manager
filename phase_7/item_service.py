from item import Item


class ItemService:

    def __init__(self, repository):
        self.repository = repository

    def create_item(self, title, details):

        item = Item(
            item_id=None,
            title=title,
            details=details
        )

        return self.repository.create(item)

    def list_items(self):
        return self.repository.list()

    def find_item(self, item_id):
        return self.repository.find(item_id)

    def update_item(
        self,
        item_id,
        title=None,
        details=None
    ):

        item = self.repository.find(item_id)

        if not item:
            return None

        item.update(title, details)

        return self.repository.update(item)

    def delete_item(self, item_id):
        self.repository.delete(item_id)