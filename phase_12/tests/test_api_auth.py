import unittest

import json

import uuid

from urllib import request


class TestAPIAuth(unittest.TestCase):

    BASE_URL = "http://localhost:8000"

    # ---------- REGISTER ----------

    def test_register(self):

        username = str(uuid.uuid4())

        data = json.dumps({

            "username": username,

            "password": "123",

            "role": "admin"

        }).encode()

        req = request.Request(

            f"{self.BASE_URL}/register",

            data=data,

            method="POST",

            headers={
                "Content-Type":
                "application/json"
            }
        )

        response = request.urlopen(req)

        self.assertEqual(
            response.status,
            201
        )


if __name__ == "__main__":

    unittest.main()