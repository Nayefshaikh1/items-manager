import unittest

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

        try:

            self.service.register(
                "admin",
                "123",
                "admin"
            )

        except:
            pass

    def test_login(self):

        self.service.login(
            "admin",
            "123"
        )

        self.assertEqual(
            self.auth.current_user.username,
            "admin"
        )