# service.py

from item import Item

from logger_config import logger


class ItemService:

    def __init__(
        self,
        repository,
        auth
    ):

        # Database layer
        self.repository = repository

        # Authentication manager
        self.auth = auth

    # ==================================================
    # INTERNAL AUTHORIZATION HELPER
    # ==================================================

    def _authorize_item_access(
        self,
        item
    ):

        user = self.auth.current_user

        # Admin can access everything
        if user.is_admin():

            return

        # Normal users can access
        # only their own items
        if item.owner_id != user.id:

            raise PermissionError(
                "Access denied"
            )

    # ==================================================
    # AUTH SECTION
    # ==================================================

    def register(
        self,
        username,
        password,
        role="user"
    ):

        self.repository.create_user(
            username,
            password,
            role
        )

        logger.info(
            f"User registered: {username}"
        )

    def login(
        self,
        username,
        password
    ):

        user = (
            self.repository.find_user(
                username
            )
        )

        # Invalid credentials
        if (
            not user
            or user.password != password
        ):

            logger.warning(
                f"Failed login for {username}"
            )

            raise ValueError(
                "Invalid credentials"
            )

        # Generate token
        token = self.auth.login(user)

        logger.info(
            f"Login success: {username}"
        )

        return token

    # ==================================================
    # CREATE ITEM
    # ==================================================

    def create_item(
        self,
        title,
        details
    ):

        self.auth.require_login()

        user = self.auth.current_user

        # Create item object
        item = Item(
            item_id=None,
            title=title,
            details=details,
            owner_id=user.id
        )

        # Save item
        result = (
            self.repository.create_item(
                item
            )
        )

        logger.info(
            f"Item created "
            f"by {user.username}"
        )

        return result

    # ==================================================
    # READ SINGLE ITEM
    # ==================================================

    def get_item(
        self,
        item_id
    ):

        self.auth.require_login()

        item = (
            self.repository.find_item(
                item_id
            )
        )

        if not item:

            raise ValueError(
                "Item not found"
            )

        # Authorization check
        self._authorize_item_access(
            item
        )

        return item

    # ==================================================
    # READ ALL ITEMS
    # ==================================================

    def get_all_items(self):

        self.auth.require_login()

        user = self.auth.current_user

        items = (
            self.repository.find_all_items()
        )

        # Admin sees all items
        if user.is_admin():

            return items

        # Normal user sees own items
        return [

            item

            for item in items

            if item.owner_id == user.id
        ]

    # ==================================================
    # FILTER ITEMS BY STATE
    # ==================================================

    def get_items_by_state(
        self,
        state
    ):

        self.auth.require_login()

        user = self.auth.current_user

        items = (
            self.repository.find_items_by_state(
                state
            )
        )

        # Admin sees all
        if user.is_admin():

            return items

        # Normal user only own items
        return [

            item

            for item in items

            if item.owner_id == user.id
        ]

    # ==================================================
    # UPDATE ITEM
    # ==================================================

    def update_item(
        self,
        item_id,
        title,
        details
    ):

        self.auth.require_login()

        item = (
            self.repository.find_item(
                item_id
            )
        )

        if not item:

            logger.error(
                f"Update failed. "
                f"Item {item_id} not found"
            )

            raise ValueError(
                "Item not found"
            )

        # Authorization check
        self._authorize_item_access(
            item
        )

        # Update fields
        item.title = title

        item.details = details

        # Update timestamp
        item.touch()

        # Save item
        self.repository.update_item(
            item
        )

        logger.info(
            f"Item updated: {item_id}"
        )

        return item

    # ==================================================
    # WORKFLOW TRANSITION
    # ==================================================

    def transition_item(
        self,
        item_id,
        new_state
    ):

        self.auth.require_login()

        item = (
            self.repository.find_item(
                item_id
            )
        )

        if not item:

            logger.error(
                f"Workflow failed. "
                f"Item {item_id} not found"
            )

            raise ValueError(
                "Item not found"
            )

        # Authorization check
        self._authorize_item_access(
            item
        )

        # Change workflow state
        history = item.transition_to(
            new_state
        )

        # Update timestamp
        item.touch()

        # Save updated item
        self.repository.update_item(
            item
        )

        # Save workflow history
        self.repository.add_history(
            item.id,
            history["old_state"],
            history["new_state"],
            history["changed_at"]
        )

        logger.info(
            f"Workflow transition "
            f"{history['old_state']} "
            f"→ "
            f"{history['new_state']}"
        )

        return item

    # ==================================================
    # WORKFLOW HISTORY
    # ==================================================

    def get_history(
        self,
        item_id
    ):

        self.auth.require_login()

        item = (
            self.repository.find_item(
                item_id
            )
        )

        if not item:

            raise ValueError(
                "Item not found"
            )

        # Authorization check
        self._authorize_item_access(
            item
        )

        return (
            self.repository.get_history(
                item_id
            )
        )

    # ==================================================
    # WORKFLOW SUMMARY
    # ==================================================

    def workflow_summary(self):

        self.auth.require_login()

        user = self.auth.current_user

        items = (
            self.repository.find_all_items()
        )

        # Normal user sees own items only
        if not user.is_admin():

            items = [

                item

                for item in items

                if item.owner_id == user.id
            ]

        summary = {}

        for item in items:

            state = item.state

            if state not in summary:

                summary[state] = 0

            summary[state] += 1

        return summary

    # ==================================================
    # DELETE ITEM
    # ==================================================

    def delete_item(
        self,
        item_id
    ):

        self.auth.require_login()

        user = self.auth.current_user

        item = (
            self.repository.find_item(
                item_id
            )
        )

        if not item:

            raise ValueError(
                "Item not found"
            )

        # Admin can delete everything
        if user.is_admin():

            self.repository.delete_item(
                item_id
            )

            logger.info(
                f"Admin deleted item: {item_id}"
            )

            return

        # Normal user can delete own item
        if item.owner_id != user.id:

            logger.warning(
                f"Unauthorized delete "
                f"attempt by {user.username}"
            )

            raise PermissionError(
                "Access denied"
            )

        self.repository.delete_item(
            item_id
        )

        logger.info(
            f"User deleted own item: "
            f"{item_id}"
        )