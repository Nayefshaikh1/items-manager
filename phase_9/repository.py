from item import Item
from db import get_connection


class ItemRepository:

    def create(self, item):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            INSERT INTO items
            (title, details, state, created_at)
            VALUES (?, ?, ?, ?)
        """, (
            item.title,
            item.details,
            item.state,
            item.created_at
        ))

        item.id = cur.lastrowid

        conn.commit()

        cur.close()
        conn.close()

        return item

    def find(self, item_id):

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
            row["state"],
            row["created_at"],
            row["updated_at"]
        )

    def list(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM items
            ORDER BY id
        """)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return [
            Item(
                row["id"],
                row["title"],
                row["details"],
                row["state"],
                row["created_at"],
                row["updated_at"]
            )
            for row in rows
        ]

    def update(self, item):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            UPDATE items
            SET state=?,
                updated_at=?
            WHERE id=?
        """, (
            item.state,
            item.updated_at,
            item.id
        ))

        conn.commit()

        cur.close()
        conn.close()

    def log_transition(
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
            (item_id, old_state, new_state, changed_at)
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

    def summary(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            SELECT state, COUNT(*) as total
            FROM items
            GROUP BY state
        """)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return {
            row["state"]: row["total"]
            for row in rows
        }