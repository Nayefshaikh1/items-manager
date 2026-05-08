import unittest
from postgres_repository import PostgresRepository
from item import Item


class TestRepository(unittest.TestCase):

    def setUp(self):
        self.repo = PostgresRepository()

    def test_create_and_find(self):

        item = Item(
            None,
            "Repository Test",
            "Testing PostgreSQL"
        )

        created = self.repo.create(item)

        found = self.repo.find(created.id)

        self.assertEqual(
            found.title,
            "Repository Test"
        )


if __name__ == "__main__":
    unittest.main()