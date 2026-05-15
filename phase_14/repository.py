# repository.py

from db import (
    connection,
    cursor
)

from item import Item

from user import User


class Repository:

    # =========================
    # USERS
    # =========================

    def create_user(

        self,
        username,
        password,
        role
    ):

        cursor.execute(

            """

            INSERT INTO users (

                username,
                password,
                role

            )

            VALUES (?, ?, ?)

            """,

            (
                username,
                password,
                role
            )
        )

        connection.commit()


    def find_user(
        self,
        username
    ):

        cursor.execute(

            """

            SELECT *

            FROM users

            WHERE username = ?

            """,

            (username,)
        )

        row = cursor.fetchone()

        if not row:

            return None

        return User(

            row[0],
            row[1],
            row[2],
            row[3]
        )


    # =========================
    # CREATE ITEM
    # =========================

    def create_item(
        self,
        item
    ):

        cursor.execute(

            """

            INSERT INTO items (

                title,
                details,
                state,
                owner_id

            )

            VALUES (?, ?, ?, ?)

            """,

            (
                item.title,
                item.details,
                item.state,
                item.owner_id
            )
        )

        connection.commit()

        item.id = cursor.lastrowid

        return item


    # =========================
    # FIND ITEM
    # =========================

    def find_item(
        self,
        item_id
    ):

        cursor.execute(

            """

            SELECT *

            FROM items

            WHERE id = ?

            """,

            (item_id,)
        )

        row = cursor.fetchone()

        if not row:

            return None

        item = Item(

            item_id=row[0],

            title=row[1],

            details=row[2],

            owner_id=row[4]
        )

        item.state = row[3]

        return item


    # =========================
    # FIND ALL ITEMS
    # =========================

    def find_all_items(self):

        cursor.execute(

            """

            SELECT *

            FROM items

            ORDER BY id DESC

            """
        )

        rows = cursor.fetchall()

        items = []

        for row in rows:

            item = Item(

                item_id=row[0],

                title=row[1],

                details=row[2],

                owner_id=row[4]
            )

            item.state = row[3]

            items.append(item)

        return items


    # =========================
    # FILTER BY STATE
    # =========================

    def find_items_by_state(
        self,
        state
    ):

        cursor.execute(

            """

            SELECT *

            FROM items

            WHERE state = ?

            ORDER BY id DESC

            """,

            (state,)
        )

        rows = cursor.fetchall()

        items = []

        for row in rows:

            item = Item(

                item_id=row[0],

                title=row[1],

                details=row[2],

                owner_id=row[4]
            )

            item.state = row[3]

            items.append(item)

        return items


    # =========================
    # PAGINATED ITEMS
    # =========================

    def find_items_paginated(

        self,
        page,
        limit,
        state=None
    ):

        offset = (
            page - 1
        ) * limit

        if state:

            cursor.execute(

                """

                SELECT *

                FROM items

                WHERE state = ?

                ORDER BY id DESC

                LIMIT ? OFFSET ?

                """,

                (
                    state,
                    limit,
                    offset
                )
            )

        else:

            cursor.execute(

                """

                SELECT *

                FROM items

                ORDER BY id DESC

                LIMIT ? OFFSET ?

                """,

                (
                    limit,
                    offset
                )
            )

        rows = cursor.fetchall()

        items = []

        for row in rows:

            item = Item(

                item_id=row[0],

                title=row[1],

                details=row[2],

                owner_id=row[4]
            )

            item.state = row[3]

            items.append(item)

        return items


    # =========================
    # UPDATE ITEM
    # =========================

    def update_item(
        self,
        item
    ):

        cursor.execute(

            """

            UPDATE items

            SET

                title = ?,
                details = ?,
                state = ?

            WHERE id = ?

            """,

            (
                item.title,
                item.details,
                item.state,
                item.id
            )
        )

        connection.commit()


    # =========================
    # DELETE ITEM
    # =========================

    def delete_item(
        self,
        item_id
    ):

        cursor.execute(

            """

            DELETE FROM items

            WHERE id = ?

            """,

            (item_id,)
        )

        connection.commit()


    # =========================
    # WORKFLOW HISTORY
    # =========================

    def add_history(

        self,
        item_id,
        old_state,
        new_state,
        changed_at
    ):

        cursor.execute(

            """

            INSERT INTO workflow_history (

                item_id,
                old_state,
                new_state,
                changed_at

            )

            VALUES (?, ?, ?, ?)

            """,

            (
                item_id,
                old_state,
                new_state,
                changed_at
            )
        )

        connection.commit()


    # =========================
    # GET HISTORY
    # =========================

    def get_history(
        self,
        item_id
    ):

        cursor.execute(

            """

            SELECT

                old_state,
                new_state,
                changed_at

            FROM workflow_history

            WHERE item_id = ?

            ORDER BY id DESC

            """,

            (item_id,)
        )

        rows = cursor.fetchall()

        history = []

        for row in rows:

            history.append({

                "old_state":
                    row[0],

                "new_state":
                    row[1],

                "changed_at":
                    row[2]
            })

        return history


    # =========================
    # SUMMARY
    # =========================

    def workflow_summary(self):

        cursor.execute(

            """

            SELECT

                state,
                COUNT(*)

            FROM items

            GROUP BY state

            """
        )

        rows = cursor.fetchall()

        summary = {}

        for row in rows:

            summary[row[0]] = row[1]

        return summary

    # =========================
    # HEALTH CHECK
    # =========================

    def check_health(self):
        try:
            cursor.execute("SELECT 1")
            cursor.fetchone()
            return True
        except Exception:
            return False