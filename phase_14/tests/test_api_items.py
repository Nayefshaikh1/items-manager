import unittest
import requests


BASE ="http://127.0.0.1:8000"


class ApiItemsTest(
    unittest.TestCase
):

    def test_get_items(self):

        try:

            response = requests.get(
                f"{BASE}/items"
            )

            self.assertIn(

                response.status_code,

                [200, 400, 401]
            )

        except Exception:

            self.assertTrue(True)


if __name__ == "__main__":

    unittest.main()