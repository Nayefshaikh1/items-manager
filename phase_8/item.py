from datetime import datetime

from workflow import (
    WORKFLOW_STATES,
    DEFAULT_STATE,
    ALLOWED_TRANSITIONS
)


class Item:

    def __init__(
        self,
        item_id,
        title,
        details,
        state=DEFAULT_STATE,
        created_at=None,
        updated_at=None
    ):

        if state not in WORKFLOW_STATES:
            raise ValueError("Invalid workflow state")

        self.id = item_id
        self.title = title
        self.details = details
        self.state = state

        self.created_at = (
            created_at or str(datetime.now())
        )

        self.updated_at = updated_at

    def transition_to(self, new_state):

        if new_state not in WORKFLOW_STATES:
            raise ValueError("Invalid target state")

        allowed = ALLOWED_TRANSITIONS[self.state]

        if new_state not in allowed:
            raise ValueError(
                f"Cannot move from "
                f"{self.state} to {new_state}"
            )

        old_state = self.state

        self.state = new_state

        self.updated_at = str(datetime.now())

        return {
            "old_state": old_state,
            "new_state": new_state,
            "changed_at": self.updated_at
        }

    def __str__(self):

        return (
            f"ID={self.id}, "
            f"Title={self.title}, "
            f"State={self.state}"
        )