import unittest

from api.validation import (
    validate_item_payload
)


class TestValidation(unittest.TestCase):

    # ---------- MISSING TITLE ----------

    def test_missing_title(self):

        with self.assertRaises(
            ValueError
        ):

            validate_item_payload({})

    # ---------- INVALID TYPE ----------

    def test_invalid_title_type(self):

        with self.assertRaises(
            ValueError
        ):

            validate_item_payload(
                {
                    "title": 123
                }
            )


if __name__ == "__main__":

    unittest.main()