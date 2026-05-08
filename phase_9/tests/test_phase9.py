import unittest

from repository import ItemRepository
from service import ItemService


class TestPhase9(unittest.TestCase):

    def setUp(self):

        self.repo = ItemRepository()

        self.service = ItemService(
            self.repo
        )

    def test_create_item(self):

        item = self.service.create_item(
            "Task",
            "Details"
        )

        self.assertEqual(
            item.state,
            "draft"
        )

    def test_transition(self):

        item = self.service.create_item(
            "Task",
            "Details"
        )

        self.service.transition_item(
            item.id,
            "active"
        )

        updated = self.repo.find(item.id)

        self.assertEqual(
            updated.state,
            "active"
        )

    def test_invalid_transition(self):

        item = self.service.create_item(
            "Task",
            "Details"
        )

        with self.assertRaises(ValueError):

            self.service.transition_item(
                item.id,
                "completed"
            )


if __name__ == "__main__":
    unittest.main()