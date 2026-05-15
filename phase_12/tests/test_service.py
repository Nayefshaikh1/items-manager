import unittest

import uuid

from repository import Repository

from auth import AuthManager

from service import ItemService


class TestService(unittest.TestCase):

    def setUp(self):

        self.repo = Repository()

        self.auth = AuthManager()

        self.service = ItemService(
            self.repo,
            self.auth
        )

        self.username = (
            str(uuid.uuid4())
        )

        self.service.register(
            self.username,
            "123",
            "admin"
        )

    # ---------- LOGIN ----------

    def test_login(self):

        token = self.service.login(
            self.username,
            "123"
        )

        self.assertIsNotNone(
            token
        )

    # ---------- CREATE ITEM ----------

    def test_create_item(self):

        self.service.login(
            self.username,
            "123"
        )

        item = (
            self.service.create_item(
                "Learn APIs",
                "Phase 12"
            )
        )

        self.assertEqual(
            item.title,
            "Learn APIs"
        )

    # ---------- GET ITEMS ----------

    def test_get_all_items(self):

        self.service.login(
            self.username,
            "123"
        )

        items = (
            self.service.get_all_items()
        )

        self.assertIsInstance(
            items,
            list
        )


if __name__ == "__main__":

    unittest.main()