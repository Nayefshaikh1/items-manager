import unittest

from repository import ItemRepository
from service import ItemService


class TestWorkflowIntegration(unittest.TestCase):

    def setUp(self):

        self.repo = ItemRepository()

        self.service = ItemService(
            self.repo
        )

    def test_create_item_default_state(self):

        item = self.service.create_item(
            "Task",
            "Details"
        )

        saved = self.repo.find(item.id)

        self.assertEqual(
            saved.state,
            "draft"
        )

    def test_transition_persisted(self):

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

    def test_history_logged(self):

        item = self.service.create_item(
            "Task",
            "Details"
        )

        self.service.transition_item(
            item.id,
            "active"
        )

        history = self.repo.get_history(
            item.id
        )

        self.assertEqual(
            len(history),
            1
        )


if __name__ == "__main__":
    unittest.main()