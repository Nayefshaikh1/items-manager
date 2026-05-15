from db import get_connection


conn = get_connection()

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    role TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS items (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    details TEXT,

    state TEXT NOT NULL,

    owner_id INTEGER NOT NULL,

    created_at TEXT NOT NULL,

    updated_at TEXT
)
""")

conn.commit()

cur.close()
conn.close()

print("Database ready.")