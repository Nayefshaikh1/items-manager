import unittest

from app_context import service


class PaginationTest(
    unittest.TestCase
):

    def test_pagination(self):

        items = service.get_items_paginated(

            1,

            5
        )

        self.assertLessEqual(

            len(items),

            5
        )


if __name__ == "__main__":

    unittest.main()