class Item:
    def __init__(self, item_id, title, details):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Invalid id")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Invalid title")
        if not isinstance(details, str):
            raise ValueError("Invalid details")

        self.id = item_id
        self.title = title
        self.details = details

    def update(self, title=None, details=None):
        if title is not None:
            if not title.strip():
                raise ValueError("Invalid title")
            self.title = title

        if details is not None:
            if not isinstance(details, str):
                raise ValueError("Invalid details")
            self.details = details

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "details": self.details
        }

    @staticmethod
    def from_dict(data):
        return Item(data["id"], data["title"], data["details"])

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Details: {self.details}"