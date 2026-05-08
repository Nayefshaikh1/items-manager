from item import Item


class ItemService:

    def __init__(self, repository):

        self.repository = repository

    def create_item(
        self,
        title,
        details
    ):

        item = Item(
            item_id=None,
            title=title,
            details=details
        )

        return self.repository.create(item)

    def transition_item(
        self,
        item_id,
        new_state
    ):

        item = self.repository.find(item_id)

        if not item:
            raise ValueError("Item not found")

        history = item.transition_to(new_state)

        self.repository.update(item)

        self.repository.log_transition(
            item.id,
            history["old_state"],
            history["new_state"],
            history["changed_at"]
        )

        return item

    def list_items(self):

        return self.repository.list()

    def get_history(self, item_id):

        return self.repository.get_history(item_id)

    def workflow_summary(self):

        return self.repository.summary()