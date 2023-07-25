from pymysql import Connection
from pymysql.cursors import Cursor

def init_db_tables(db_connection: Connection, file_path: str) -> None:
    cursor: Cursor
    with db_connection.cursor() as cursor, open(file_path, "r") as sql_file:
        cursor.executemany(sql_file.read())
    db_connection.commit()