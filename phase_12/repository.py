from db import get_connection

from user import User

from item import Item


class Repository:

    # ---------- USERS ----------

    def create_user(
        self,
        username,
        password,
        role="user"
    ):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            INSERT INTO users
            (
                username,
                password,
                role
            )
            VALUES (?, ?, ?)
        """, (
            username,
            password,
            role
        ))

        conn.commit()

        cur.close()
        conn.close()

    def find_user(self, username):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM users
            WHERE username=?
        """, (username,))

        row = cur.fetchone()

        cur.close()
        conn.close()

        if not row:
            return None

        return User(
            row["id"],
            row["username"],
            row["password"],
            row["role"]
        )

    # ---------- ITEMS ----------

    def create_item(self, item):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            INSERT INTO items
            (
                title,
                details,
                state,
                owner_id,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            item.title,
            item.details,
            item.state,
            item.owner_id,
            item.created_at,
            item.updated_at
        ))

        item.id = cur.lastrowid

        conn.commit()

        cur.close()
        conn.close()

        return item

    def find_item(self, item_id):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM items
            WHERE id=?
        """, (item_id,))

        row = cur.fetchone()

        cur.close()
        conn.close()

        if not row:
            return None

        return Item(
            row["id"],
            row["title"],
            row["details"],
            row["owner_id"],
            row["state"],
            row["created_at"],
            row["updated_at"]
        )

    # ---------- LIST ALL ----------

    def find_all_items(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM items
        """)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return [

            Item(
                row["id"],
                row["title"],
                row["details"],
                row["owner_id"],
                row["state"],
                row["created_at"],
                row["updated_at"]
            )

            for row in rows
        ]

    # ---------- FILTER ----------

    def find_items_by_state(
        self,
        state
    ):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM items
            WHERE state=?
        """, (state,))

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return [

            Item(
                row["id"],
                row["title"],
                row["details"],
                row["owner_id"],
                row["state"],
                row["created_at"],
                row["updated_at"]
            )

            for row in rows
        ]

    # ---------- UPDATE ----------

    def update_item(self, item):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            UPDATE items
            SET
                title=?,
                details=?,
                state=?,
                updated_at=?
            WHERE id=?
        """, (
            item.title,
            item.details,
            item.state,
            item.updated_at,
            item.id
        ))

        conn.commit()

        cur.close()
        conn.close()

    # ---------- DELETE ----------

    def delete_item(self, item_id):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            DELETE FROM items
            WHERE id=?
        """, (item_id,))

        conn.commit()

        cur.close()
        conn.close()

    # ---------- WORKFLOW HISTORY ----------

    def add_history(
        self,
        item_id,
        old_state,
        new_state,
        changed_at
    ):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            INSERT INTO workflow_history
            (
                item_id,
                old_state,
                new_state,
                changed_at
            )
            VALUES (?, ?, ?, ?)
        """, (
            item_id,
            old_state,
            new_state,
            changed_at
        ))

        conn.commit()

        cur.close()
        conn.close()

    def get_history(self, item_id):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM workflow_history
            WHERE item_id=?
        """, (item_id,))

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return rows