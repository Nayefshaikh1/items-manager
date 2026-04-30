import unittest
import os
from storage import JsonStorage
from file_repository import FileItemRepository
from item import Item


class TestRepository(unittest.TestCase):

    def setUp(self):
        self.file = "test_data.json"
        self.storage = JsonStorage(self.file)
        self.repo = FileItemRepository(self.storage)

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_persistence(self):
        item = Item(1, "Persist", "Data")
        self.repo.create(item)

        # Reload repository
        new_repo = FileItemRepository(self.storage)
        items = new_repo.list()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, "Persist")

    def test_delete(self):
        item = Item(1, "A", "a")
        self.repo.create(item)
        self.repo.delete(1)

        self.assertEqual(len(self.repo.list()), 0)