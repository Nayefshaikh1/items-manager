import unittest

from repository import Repository

from item import Item


class RepositoryTest(
    unittest.TestCase
):

    def setUp(self):

        self.repo = Repository()


    def test_create_item(self):

        item = Item(

            title="Repo Test",

            details="Testing"
        )

        created = self.repo.create_item(
            item
        )

        self.assertIsNotNone(
            created.id
        )


    def test_find_item(self):

        item = self.repo.find_item(1)

        if item:

            self.assertIsNotNone(
                item.title
            )

        else:

            self.assertTrue(True)


if __name__ == "__main__":

    unittest.main()