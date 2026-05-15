# service.py

from datetime import datetime

from item import Item

from workflow import (
    DEFAULT_STATE,
    ALLOWED_TRANSITIONS
)


class ItemService:

    def __init__(
        self,
        repo,
        auth
    ):

        self.repo = repo

        self.auth = auth


    # =========================
    # REGISTER
    # =========================

    def register(

        self,
        username,
        password,
        role="user"
    ):

        existing_user = (
            self.repo.find_user(
                username
            )
        )

        if existing_user:

            raise Exception(
                "User already exists"
            )

        self.repo.create_user(

            username,
            password,
            role
        )


    # =========================
    # LOGIN
    # =========================

    def login(
        self,
        username,
        password
    ):

        user = self.repo.find_user(
            username
        )

        if not user:

            raise Exception(
                "Invalid username"
            )

        if user.password != password:

            raise Exception(
                "Invalid password"
            )

        token = self.auth.generate_token(
            username
        )

        return token


    # =========================
    # CREATE ITEM
    # =========================

    def create_item(

        self,
        title,
        details="",
        owner_id=None
    ):

        item = Item(

            title=title,

            details=details,

            owner_id=owner_id
        )

        item.state = DEFAULT_STATE

        return self.repo.create_item(
            item
        )


    # =========================
    # GET ITEM
    # =========================

    def get_item(
        self,
        item_id
    ):

        item = self.repo.find_item(
            item_id
        )

        if not item:

            raise Exception(
                "Item not found"
            )

        return item


    # =========================
    # GET ALL ITEMS
    # =========================

    def get_all_items(self):

        return self.repo.find_all_items()


    # =========================
    # FILTER ITEMS
    # =========================

    def get_items_by_state(
        self,
        state
    ):

        return self.repo.find_items_by_state(
            state
        )


    # =========================
    # PAGINATED ITEMS
    # =========================

    def get_items_paginated(

        self,
        page,
        limit,
        state=None
    ):

        return self.repo.find_items_paginated(

            page,
            limit,
            state
        )


    # =========================
    # UPDATE ITEM
    # =========================

    def update_item(

        self,
        item_id,
        title,
        details
    ):

        item = self.get_item(
            item_id
        )

        item.title = title

        item.details = details

        self.repo.update_item(
            item
        )

        return item


    # =========================
    # DELETE ITEM
    # =========================

    def delete_item(
        self,
        item_id
    ):

        item = self.get_item(
            item_id
        )

        self.repo.delete_item(
            item.id
        )


    # =========================
    # CHANGE STATE
    # =========================

    def change_state(

        self,
        item_id,
        new_state
    ):

        item = self.get_item(
            item_id
        )

        current_state = item.state

        allowed = (
            ALLOWED_TRANSITIONS.get(
                current_state,
                set()
            )
        )

        if new_state not in allowed:

            raise Exception(
                f"Cannot move from "
                f"{current_state} "
                f"to {new_state}"
            )

        item.state = new_state

        self.repo.update_item(
            item
        )

        self.repo.add_history(

            item.id,

            current_state,

            new_state,

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        return item


    # =========================
    # GET HISTORY
    # =========================

    def get_history(
        self,
        item_id
    ):

        return self.repo.get_history(
            item_id
        )


    # =========================
    # SUMMARY
    # =========================

    def workflow_summary(self):

        return self.repo.workflow_summary()