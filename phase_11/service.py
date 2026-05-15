from item import Item

from logger_config import logger


class ItemService:

    def __init__(
        self,
        repository,
        auth
    ):

        self.repository = repository

        self.auth = auth

    # ---------- AUTH ----------

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

    # ---------- CREATE ----------

    def create_item(
        self,
        title,
        details
    ):

        self.auth.require_login()

        user = self.auth.current_user

        item = Item(
            item_id=None,
            title=title,
            details=details,
            owner_id=user.id
        )

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

    # ---------- READ ----------

    def get_item(self, item_id):

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

        return item

    def get_all_items(self):

        self.auth.require_login()

        return (
            self.repository.find_all_items()
        )

    def get_items_by_state(
        self,
        state
    ):

        self.auth.require_login()

        return (
            self.repository.find_items_by_state(
                state
            )
        )

    # ---------- UPDATE ----------

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

        item.title = title

        item.details = details

        self.repository.update_item(item)

        logger.info(
            f"Item updated: {item_id}"
        )

        return item

    # ---------- WORKFLOW ----------

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

        history = item.transition_to(
            new_state
        )

        self.repository.update_item(item)

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

    # ---------- DELETE ----------

    def delete_item(self, item_id):

        self.auth.require_login()

        user = self.auth.current_user

        if not user.is_admin():

            logger.warning(
                f"Unauthorized delete "
                f"attempt by {user.username}"
            )

            raise PermissionError(
                "Only admin can delete"
            )

        self.repository.delete_item(item_id)

        logger.info(
            f"Item deleted: {item_id}"
        )