import cx_Oracle

conn = None  # Connection to Oracle


def connect(username, password, dsn):
    global conn
    if conn is None:
        connection = cx_Oracle.connect(
            user=username,
            password=password,
            dsn=dsn
        )
        conn = connection


def getCursor():
    global conn
    if conn is not None:
        return conn.cursor()
    return None
