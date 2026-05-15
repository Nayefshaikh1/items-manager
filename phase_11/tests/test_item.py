import unittest

from item import Item


class TestItem(unittest.TestCase):

    def test_item_creation(self):

        item = Item(
            None,
            "Learn Testing",
            "Phase 11",
            1
        )

        self.assertEqual(
            item.title,
            "Learn Testing"
        )

    def test_empty_title(self):

        with self.assertRaises(
            ValueError
        ):

            Item(
                None,
                "",
                "details",
                1
            )