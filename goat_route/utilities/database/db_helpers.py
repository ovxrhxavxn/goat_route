import sqlite3
from interfaces import IDBHelper

class DBHelperSQLite(IDBHelper):

    def __init__(self, database_file):
        super().__init__(database_file)
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS addresses
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, address TEXT)''')

    def save_address(self, address):
        self.cursor.execute("INSERT INTO addresses (address) VALUES (?)", (address,))
        self.conn.commit()

    def get_addresses(self):
        self.cursor.execute("SELECT * FROM addresses")
        result = self.cursor.fetchall()
        return result if result else []
    
    def saves_address(self, address):
        if address.strip():
            self.cursor.execute("INSERT INTO addresses (address) VALUES (?)", (address,))
            self.conn.commit()

    def close(self):
        self.conn.close()