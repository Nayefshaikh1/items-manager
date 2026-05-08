from db import get_connection


conn = get_connection()

cur = conn.cursor()

# ITEMS TABLE
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

# WORKFLOW HISTORY TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS workflow_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    item_id INTEGER NOT NULL,

    old_state TEXT NOT NULL,

    new_state TEXT NOT NULL,

    changed_at TEXT NOT NULL
)
""")

conn.commit()

cur.close()
conn.close()

print("Database setup complete.")