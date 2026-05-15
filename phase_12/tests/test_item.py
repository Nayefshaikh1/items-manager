import unittest

from item import Item


class TestItem(unittest.TestCase):

    # ---------- CREATE ITEM ----------

    def test_item_creation(self):

        item = Item(
            None,
            "Learn Testing",
            "Phase 12",
            1
        )

        self.assertEqual(
            item.title,
            "Learn Testing"
        )

    # ---------- EMPTY TITLE ----------

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

    # ---------- WORKFLOW ----------

    def test_transition(self):

        item = Item(
            None,
            "Task",
            "details",
            1
        )

        item.transition_to("active")

        self.assertEqual(
            item.state,
            "active"
        )


if __name__ == "__main__":

    unittest.main()