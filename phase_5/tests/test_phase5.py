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
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def update(self, item):
        return item

    def delete(self, item_id):
        for i, item in enumerate(self.items):
            if item.id == item_id:
                return self.items.pop(i)
        return None


class TestPhase5(unittest.TestCase):

    def setUp(self):
        self.repo = FakeRepository()
        self.service = ItemService(self.repo)

    def test_create(self):
        item = self.service.create_item("Task", "D")
        self.assertEqual(item.id, 1)

    def test_update(self):
        self.service.create_item("Old", "D")
        updated = self.service.update_item(1, title="New")
        self.assertEqual(updated.title, "New")

    def test_delete(self):
        self.service.create_item("A", "a")
        self.service.delete_item(1)
        self.assertEqual(len(self.service.list_items()), 0)


if __name__ == "__main__":
    unittest.main()