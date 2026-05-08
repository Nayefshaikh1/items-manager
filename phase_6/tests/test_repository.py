import unittest
import os
from storage import JsonStorage
from file_repository import FileRepository
from item import Item


class TestRepository(unittest.TestCase):

    def setUp(self):
        self.file = "test_data.json"
        self.storage = JsonStorage(self.file)
        self.repo = FileRepository(self.storage)

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    # ✅ CREATE + PERSIST
    def test_create_persists_data(self):
        item = Item(1, "Task", "Details")
        self.repo.create(item)

        new_repo = FileRepository(self.storage)
        items = new_repo.list()

        self.assertEqual(len(items), 1)

    # ✅ FIND
    def test_find_item(self):
        item = Item(1, "Task", "Details")
        self.repo.create(item)

        found = self.repo.find(1)
        self.assertIsNotNone(found)

    # ✅ UPDATE
    def test_update_persists_updated_at(self):
        item = Item(1, "Task", "Details")
        self.repo.create(item)

        item.update(title="New")
        self.repo.update(item)

        new_repo = FileRepository(self.storage)
        updated = new_repo.find(1)

        self.assertEqual(updated.title, "New")
        self.assertIsNotNone(updated.updated_at)

    # ✅ DELETE
    def test_delete_removes_item(self):
        item = Item(1, "Task", "Details")
        self.repo.create(item)

        self.repo.delete(1)

        self.assertEqual(len(self.repo.list()), 0)


if __name__ == "__main__":
    unittest.main()