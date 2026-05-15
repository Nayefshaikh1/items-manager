import unittest

from repository import Repository
from auth import AuthManager
from service import ItemService


class TestPhase10(unittest.TestCase):

    def setUp(self):

        self.repo = Repository()

        self.auth = AuthManager()

        self.service = ItemService(
            self.repo,
            self.auth
        )

    def test_register_and_login(self):

        self.service.register(
            "nayef",
            "123"
        )

        self.service.login(
            "nayef",
            "123"
        )

        self.assertEqual(
            self.auth.current_user.username,
            "nayef"
        )

    def test_create_item(self):

        self.service.register(
            "nayef",
            "123"
        )

        self.service.login(
            "nayef",
            "123"
        )

        item = self.service.create_item(
            "Learn Security",
            "Phase 10"
        )

        self.assertEqual(
            item.title,
            "Learn Security"
        )

    def test_admin_delete(self):

        self.service.register(
            "admin",
            "123",
            "admin"
        )

        self.service.login(
            "admin",
            "123"
        )

        item = self.service.create_item(
            "Task",
            "Details"
        )

        self.service.delete_item(
            item.id
        )

        result = self.repo.find_item(
            item.id
        )

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()