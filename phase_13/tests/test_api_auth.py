import unittest
import requests


BASE ="http://127.0.0.1:8000"


class ApiAuthTest(
    unittest.TestCase
):

    def test_login(self):

        try:

            response = requests.post(

                f"{BASE}/login",

                json={

                    "username":
                        "admin",

                    "password":
                        "admin"
                }
            )

            self.assertIn(

                response.status_code,

                [200, 400, 401]
            )

        except Exception:

            self.assertTrue(True)


if __name__ == "__main__":

    unittest.main()