import unittest

from auth import AuthManager


class AuthTest(
    unittest.TestCase
):

    def setUp(self):

        self.auth = AuthManager()


    def test_generate_token(self):

        token = self.auth.generate_token(
            "nayef"
        )

        self.assertIsNotNone(
            token
        )


if __name__ == "__main__":

    unittest.main()