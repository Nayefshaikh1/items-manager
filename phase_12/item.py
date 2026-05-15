# item.py

from datetime import datetime


class Item:

    def __init__(
        self,
        item_id,
        title,
        details,
        owner_id,
        state="draft",
        created_at=None,
        updated_at=None
    ):

        self.id = item_id

        self.title = title

        self.details = details

        self.owner_id = owner_id

        self.state = state

        self.created_at = (
            created_at
            or datetime.now().isoformat()
        )

        self.updated_at = updated_at

    # ---------- UPDATE TIMESTAMP ----------

    def touch(self):

        self.updated_at = (
            datetime.now().isoformat()
        )

    # ---------- WORKFLOW ----------

    def transition_to(
        self,
        new_state
    ):

        old_state = self.state

        self.state = new_state

        self.touch()

        return {

            "old_state": old_state,

            "new_state": new_state,

            "changed_at": self.updated_at
        }

    # ---------- STRING ----------

    def __str__(self):

        return (
            f"Item("
            f"id={self.id}, "
            f"title={self.title}, "
            f"state={self.state}"
            f")"
        )