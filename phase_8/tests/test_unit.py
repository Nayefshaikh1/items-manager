import unittest

from item import Item


class TestWorkflowUnit(unittest.TestCase):

    def test_default_state(self):

        item = Item(
            None,
            "A",
            "a"
        )

        self.assertEqual(
            item.state,
            "draft"
        )

    def test_valid_transition(self):

        item = Item(
            None,
            "A",
            "a"
        )

        item.transition_to("active")

        self.assertEqual(
            item.state,
            "active"
        )

    def test_invalid_transition(self):

        item = Item(
            None,
            "A",
            "a"
        )

        with self.assertRaises(ValueError):

            item.transition_to("completed")


if __name__ == "__main__":
    unittest.main()