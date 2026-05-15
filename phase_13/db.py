import sqlite3


# =========================
# DATABASE CONNECTION
# =========================

connection = sqlite3.connect(

    "database.db",

    check_same_thread=False,

    timeout=30
)


# =========================
# ENABLE WAL MODE
# =========================

connection.execute(

    "PRAGMA journal_mode=WAL;"
)


# =========================
# BETTER SQLITE PERFORMANCE
# =========================

connection.execute(

    "PRAGMA synchronous=NORMAL;"
)

connection.execute(

    "PRAGMA foreign_keys=ON;"
)


# =========================
# CURSOR
# =========================

cursor = connection.cursor()


# =========================
# COMMIT HELPER
# =========================

def commit():

    connection.commit()


# =========================
# CLOSE CONNECTION
# =========================

def close():

    connection.close()