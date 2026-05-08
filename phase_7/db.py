import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="items_db",
        user="postgres",
        password="nayef1",
        host="localhost",
        port="5432"
    )