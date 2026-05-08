from item_repository import ItemRepository
from item import Item
from db import get_connection


class PostgresRepository(ItemRepository):

    def create(self, item):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO items
            (title, details, created_at, updated_at)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (
            item.title,
            item.details,
            item.created_at,
            item.updated_at
        ))

        item.id = cur.fetchone()[0]

        conn.commit()

        cur.close()
        conn.close()

        return item

    def find(self, item_id):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id,
                title,
                details,
                created_at,
                updated_at
            FROM items
            WHERE id = %s
        """, (item_id,))

        row = cur.fetchone()

        cur.close()
        conn.close()

        if not row:
            return None

        return Item(*row)

    def list(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id,
                title,
                details,
                created_at,
                updated_at
            FROM items
            ORDER BY id
        """)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return [Item(*row) for row in rows]

    def update(self, item):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE items
            SET title = %s,
                details = %s,
                updated_at = %s
            WHERE id = %s
        """, (
            item.title,
            item.details,
            item.updated_at,
            item.id
        ))

        conn.commit()

        cur.close()
        conn.close()

        return item

    def delete(self, item_id):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM items
            WHERE id = %s
        """, (item_id,))

        conn.commit()

        cur.close()
        conn.close()