import unittest
from item_store import ItemStore
from item_service import ItemService
from storage import JsonStorage
import os


class TestPhase4(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_data.json"
        self.storage = JsonStorage(self.test_file)
        self.store = ItemStore(self.storage)
        self.service = ItemService(self.store)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create(self):
        item = self.service.create_item("Task", "Details")
        self.assertIsNotNone(item)
        self.assertEqual(item.id, 1)

    def test_list(self):
        self.service.create_item("A", "a")
        self.service.create_item("B", "b")
        self.assertEqual(len(self.service.list_items()), 2)

    def test_find(self):
        self.service.create_item("Task", "D")
        item = self.service.find_item(1)
        self.assertEqual(item.title, "Task")

    def test_update(self):
        self.service.create_item("Old", "D")
        updated = self.service.update_item(1, title="New")
        self.assertEqual(updated.title, "New")

    def test_delete(self):
        self.service.create_item("A", "a")
        self.service.delete_item(1)
        self.assertEqual(len(self.service.list_items()), 0)

    def test_persistence(self):
        self.service.create_item("Persist", "Data")

        new_store = ItemStore(self.storage)
        new_service = ItemService(new_store)

        items = new_service.list_items()
        self.assertEqual(len(items), 1)


if __name__ == "__main__":
    unittest.main()