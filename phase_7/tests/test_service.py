import unittest
from item_service import ItemService
from item import Item


class FakeRepository:

    def __init__(self):
        self.items = []
        self.next_id = 1

    def create(self, item):

        item.id = self.next_id
        self.next_id += 1

        self.items.append(item)

        return item

    def find(self, item_id):

        for item in self.items:
            if item.id == item_id:
                return item

        return None

    def list(self):
        return self.items

    def update(self, item):
        return item

    def delete(self, item_id):

        self.items = [
            i for i in self.items
            if i.id != item_id
        ]


class TestService(unittest.TestCase):

    def setUp(self):

        self.repo = FakeRepository()

        self.service = ItemService(self.repo)

    def test_create(self):

        item = self.service.create_item("A", "a")

        self.assertEqual(item.id, 1)

    def test_update(self):

        item = self.service.create_item("A", "a")

        updated = self.service.update_item(
            item.id,
            title="New"
        )

        self.assertEqual(updated.title, "New")

    def test_delete(self):

        item = self.service.create_item("A", "a")

        self.service.delete_item(item.id)

        self.assertEqual(
            len(self.service.list_items()),
            0
        )


if __name__ == "__main__":
    unittest.main()