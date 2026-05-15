from item import Item


class ItemService:

    def __init__(
        self,
        repository,
        auth
    ):

        self.repository = repository

        self.auth = auth

    # USERS

    def register(
        self,
        username,
        password,
        role="user"
    ):

        existing = (
            self.repository.find_user(
                username
            )
        )

        if existing:

            raise ValueError(
                "Username already exists"
            )

        self.repository.create_user(
            username,
            password,
            role
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

            raise ValueError(
                "Invalid credentials"
            )

        self.auth.login(user)

    def forgot_password(
        self,
        username,
        new_password
    ):

        user = (
            self.repository.find_user(
                username
            )
        )

        if not user:

            raise ValueError(
                "User not found"
            )

        self.repository.reset_password(
            username,
            new_password
        )

    def logout(self):

        self.auth.logout()

    # ITEMS

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

        return self.repository.create_item(
            item
        )

    def list_my_items(self):

        self.auth.require_login()

        user = self.auth.current_user

        items = (
            self.repository.list_items()
        )

        if user.is_admin():

            return items

        return [
            item for item in items
            if item.owner_id == user.id
        ]

    def filter_items(self, state):

        self.auth.require_login()

        user = self.auth.current_user

        items = (
            self.repository.filter_by_state(
                state
            )
        )

        if user.is_admin():

            return items

        return [
            item for item in items
            if item.owner_id == user.id
        ]

    def get_history(self, item_id):

        self.auth.require_login()

        return self.repository.get_history(
            item_id
        )

    def workflow_summary(self):

        self.auth.require_login()

        return (
            self.repository.workflow_summary()
        )

    def update_item(
        self,
        item_id,
        title,
        details
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

        if (
            item.owner_id != user.id
            and not user.is_admin()
        ):

            raise PermissionError(
                "Access denied"
            )

        item.title = title

        item.details = details

        self.repository.update_item(item)

    def delete_item(self, item_id):

        self.auth.require_login()

        user = self.auth.current_user

        if not user.is_admin():

            raise PermissionError(
                "Only admin can delete"
            )

        self.repository.delete_item(item_id)

    def transition_item(
        self,
        item_id,
        new_state
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

        if (
            item.owner_id != user.id
            and not user.is_admin()
        ):

            raise PermissionError(
                "Access denied"
            )

        history = item.transition_to(
            new_state
        )

        self.repository.update_item(item)

        self.repository.log_history(
            item.id,
            history["old_state"],
            history["new_state"],
            history["changed_at"]
        )