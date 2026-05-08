from datetime import datetime

class Item:
    def __init__(self, item_id, title, details, created_at=None, updated_at=None):
        self._validate(item_id, title, details, created_at, updated_at)

        self.id = item_id
        self.title = title
        self.details = details
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at

    # ---------- VALIDATION ----------
    def _validate(self, item_id, title, details, created_at, updated_at):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Invalid id")

        if not isinstance(title, str) or not title.strip():
            raise ValueError("Invalid title")

        if not isinstance(details, str):
            raise ValueError("Invalid details")

        if created_at and not isinstance(created_at, datetime):
            raise ValueError("Invalid created_at")

        if updated_at and not isinstance(updated_at, datetime):
            raise ValueError("Invalid updated_at")

    # ---------- BEHAVIOR ----------
    def update(self, title=None, details=None):
        changed = False

        if title is not None:
            if not title.strip():
                raise ValueError("Invalid title")
            self.title = title
            changed = True

        if details is not None:
            if not isinstance(details, str):
                raise ValueError("Invalid details")
            self.details = details
            changed = True

        if changed:
            self.updated_at = datetime.now()

    # ---------- DISPLAY ----------
    def __str__(self):
        return (
            f"ID: {self.id}, Title: {self.title}, Details: {self.details}, "
            f"CreatedAt: {self.created_at}, UpdatedAt: {self.updated_at}"
        )

    # ---------- CONVERSION ----------
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "details": self.details,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

    @staticmethod
    def from_dict(data):
        from datetime import datetime

        return Item(
            data["id"],
            data["title"],
            data["details"],
            datetime.fromisoformat(data["created_at"]),
            datetime.fromisoformat(data["updated_at"]) if data["updated_at"] else None
        )