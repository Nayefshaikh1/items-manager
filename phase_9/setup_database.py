from db import get_connection


conn = get_connection()

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS items (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    details TEXT,

    state TEXT NOT NULL,

    created_at TEXT NOT NULL,

    updated_at TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS workflow_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    item_id INTEGER,

    old_state TEXT,

    new_state TEXT,

    changed_at TEXT
)
""")

conn.commit()

cur.close()
conn.close()

print("Database ready.")