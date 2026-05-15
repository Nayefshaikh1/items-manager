import unittest

from workflow import (
    ALLOWED_TRANSITIONS
)


class WorkflowTest(
    unittest.TestCase
):

    def test_draft_transition(self):

        self.assertIn(

            "active",

            ALLOWED_TRANSITIONS[
                "draft"
            ]
        )


    def test_completed_transition(self):

        self.assertIn(

            "active",

            ALLOWED_TRANSITIONS[
                "completed"
            ]
        )


if __name__ == "__main__":

    unittest.main()