import unittest

from app_context import service


class ServiceTest(
    unittest.TestCase
):

    def test_create_item(self):

        item = service.create_item(

            "Service Test",

            "Testing"
        )

        self.assertEqual(
            item.title,
            "Service Test"
        )


    def test_get_all_items(self):

        items = service.get_all_items()

        self.assertIsInstance(
            items,
            list
        )


if __name__ == "__main__":

    unittest.main()