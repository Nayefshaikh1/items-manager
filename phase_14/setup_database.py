from db import (
    connection,
    cursor
)


# =========================
# USERS TABLE
# =========================

cursor.execute("""

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    role TEXT NOT NULL
)

""")


# =========================
# ITEMS TABLE
# =========================

cursor.execute("""

CREATE TABLE IF NOT EXISTS items (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    details TEXT,

    state TEXT DEFAULT 'draft',

    owner_id INTEGER,

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
)

""")


# =========================
# WORKFLOW HISTORY
# =========================

cursor.execute("""

CREATE TABLE IF NOT EXISTS workflow_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    item_id INTEGER,

    old_state TEXT,

    new_state TEXT,

    changed_at TIMESTAMP
)

""")


# =========================
# SAVE
# =========================

connection.commit()

print(
    "\nDatabase setup completed.\n"
)