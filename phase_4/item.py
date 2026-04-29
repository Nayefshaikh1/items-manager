class Item:
    def __init__(self, item_id, title, details):
        self._validate_id(item_id)
        self._validate_title(title)
        self._validate_details(details)

        self.id = item_id
        self.title = title
        self.details = details

    # ---------- VALIDATION ----------
    def _validate_id(self, item_id):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Invalid id")

    def _validate_title(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Invalid title")

    def _validate_details(self, details):
        if not isinstance(details, str):
            raise ValueError("Invalid details")

    # ---------- BEHAVIOR ----------
    def update(self, title=None, details=None):
        if title is not None:
            self._validate_title(title)
            self.title = title

        if details is not None:
            self._validate_details(details)
            self.details = details

    # ---------- DISPLAY ----------
    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Details: {self.details}"

    def __repr__(self):
        return self.__str__()

    # ---------- CONVERSION ----------
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "details": self.details
        }

    @staticmethod
    def from_dict(data):
        return Item(data["id"], data["title"], data["details"])