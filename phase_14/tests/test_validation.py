import unittest

from api.validation import (
    validate_item_payload
)


class ValidationTest(
    unittest.TestCase
):

    def test_valid_payload(self):

        payload = {

            "title": "Hello",

            "details": "World"
        }

        validate_item_payload(
            payload
        )


if __name__ == "__main__":

    unittest.main()