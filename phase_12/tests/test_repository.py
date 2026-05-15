import unittest

from repository import Repository

from item import Item


class TestRepository(unittest.TestCase):

    def setUp(self):

        self.repo = Repository()

    # ---------- CREATE + FIND ----------

    def test_create_and_find_item(self):

        item = Item(
            None,
            "Repo Test",
            "details",
            1
        )

        created = (
            self.repo.create_item(item)
        )

        found = (
            self.repo.find_item(
                created.id
            )
        )

        self.assertEqual(
            found.title,
            "Repo Test"
        )

    # ---------- LIST ----------

    def test_find_all_items(self):

        items = (
            self.repo.find_all_items()
        )

        self.assertIsInstance(
            items,
            list
        )


if __name__ == "__main__":

    unittest.main()