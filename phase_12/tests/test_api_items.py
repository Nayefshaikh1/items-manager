import unittest

import json

import uuid

from urllib import request


class TestAPIItems(unittest.TestCase):

    BASE_URL = "http://localhost:8000"

    def setUp(self):

        username = str(uuid.uuid4())

        register_data = json.dumps({

            "username": username,

            "password": "123",

            "role": "admin"

        }).encode()

        register_req = request.Request(

            f"{self.BASE_URL}/register",

            data=register_data,

            method="POST",

            headers={
                "Content-Type":
                "application/json"
            }
        )

        request.urlopen(register_req)

        login_data = json.dumps({

            "username": username,

            "password": "123"

        }).encode()

        login_req = request.Request(

            f"{self.BASE_URL}/login",

            data=login_data,

            method="POST",

            headers={
                "Content-Type":
                "application/json"
            }
        )

        response = request.urlopen(
            login_req
        )

        body = json.loads(
            response.read().decode()
        )

        self.token = (
            body["data"]["token"]
        )

    # ---------- CREATE ITEM ----------

    def test_create_item(self):

        data = json.dumps({

            "title": "Learn APIs",

            "details": "Phase 12"

        }).encode()

        req = request.Request(

            f"{self.BASE_URL}/items",

            data=data,

            method="POST",

            headers={

                "Content-Type":
                "application/json",

                "Authorization":
                f"Bearer {self.token}"
            }
        )

        response = request.urlopen(req)

        self.assertEqual(
            response.status,
            201
        )


if __name__ == "__main__":

    unittest.main()