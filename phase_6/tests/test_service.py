import unittest
from item_service import ItemService
from item import Item


class FakeRepository:
    def __init__(self):
        self.items = []

    def get_next_id(self):
        return len(self.items) + 1

    def create(self, item):
        self.items.append(item)

    def list(self):
        return self.items

    def find(self, item_id):
        return next((i for i in self.items if i.id == item_id), None)

    def update(self, item):
        return item

    def delete(self, item_id):
        for i, item in enumerate(self.items):
            if item.id == item_id:
                return self.items.pop(i)
        return None


class TestItemService(unittest.TestCase):

    def setUp(self):
        self.repo = FakeRepository()
        self.service = ItemService(self.repo)

    # ✅ CREATE
    def test_create_item_sets_created_at(self):
        item = self.service.create_item("Task", "Details")

        self.assertIsNotNone(item)
        self.assertIsNotNone(item.created_at)
        self.assertIsNone(item.updated_at)

    # ✅ INVALID CREATE
    def test_create_invalid_title(self):
        item = self.service.create_item("", "Details")
        self.assertIsNone(item)

    # ✅ UPDATE
    def test_update_sets_updated_at(self):
        item = self.service.create_item("Task", "Details")

        updated = self.service.update_item(item.id, title="New Title")

        self.assertIsNotNone(updated.updated_at)
        self.assertEqual(updated.title, "New Title")

    # ✅ FIND
    def test_find_item(self):
        self.service.create_item("A", "a")
        item = self.service.find_item(1)

        self.assertIsNotNone(item)

    # ✅ DELETE
    def test_delete_item(self):
        self.service.create_item("A", "a")
        self.service.delete_item(1)

        self.assertEqual(len(self.service.list_items()), 0)


if __name__ == "__main__":
    unittest.main()