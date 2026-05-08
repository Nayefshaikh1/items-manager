from datetime import datetime


class Item:

    def __init__(
        self,
        item_id,
        title,
        details,
        created_at=None,
        updated_at=None
    ):
        self.id = item_id
        self.title = title
        self.details = details
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at

    def update(self, title=None, details=None):

        if title:
            self.title = title

        if details:
            self.details = details

        self.updated_at = datetime.now()

    def __str__(self):
        return (
            f"ID={self.id}, "
            f"Title={self.title}, "
            f"Details={self.details}"
        )