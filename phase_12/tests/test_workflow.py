import unittest

from item import Item


class TestWorkflow(unittest.TestCase):

    # ---------- VALID ----------

    def test_valid_transition(self):

        item = Item(
            None,
            "Task",
            "details",
            1
        )

        item.transition_to(
            "active"
        )

        self.assertEqual(
            item.state,
            "active"
        )

    # ---------- INVALID ----------

    def test_invalid_transition(self):

        item = Item(
            None,
            "Task",
            "details",
            1
        )

        with self.assertRaises(
            ValueError
        ):

            item.transition_to(
                "completed"
            )


if __name__ == "__main__":

    unittest.main()