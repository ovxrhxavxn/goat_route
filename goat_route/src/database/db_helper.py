import sqlite3

from .. geolocation import Address

class DBHelperSQLite:

    def __init__(self):
        self._conn = None

    @property
    def conn(self):
        if not self._conn:
            self.connect()
        return self._conn

    def connect(self):
        try:
            self._conn = sqlite3.connect(self.db_file)
        except sqlite3.Error as e:
            print(e)

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS addresses (
                    id INTEGER PRIMARY KEY,
                    address TEXT NOT NULL
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def insert_address(self, address: Address) -> int:
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO addresses (address) VALUES (?)", (address))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(e)

    def close_connection(self):
        if self._conn:
            self._conn.close()