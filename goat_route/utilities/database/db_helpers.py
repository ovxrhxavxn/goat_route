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
        if address.strip():
            try:
                self.cursor.execute("INSERT INTO addresses (address) VALUES (?)", (address,))
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Ошибка при сохранении адреса: {e}")

    def get_addresses(self):
        try:
            self.cursor.execute("SELECT * FROM addresses")
            result = self.cursor.fetchall()
            return result if result else []
        except sqlite3.Error as e:
            print(f"Ошибка при получении адресов: {e}")
            return []

    def print_addresses(self):
        addresses = self.get_addresses()
        for address in addresses:
            print(f"ID: {address[0]}, Address: {address[1]}")

    def close(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Ошибка при закрытии соединения: {e}")

    def __del__(self):
        self.close()

# Создаем экземпляр класса DBHelperSQLite
db_helper = DBHelperSQLite('addresses.db')

# Сохраняем адреса
db_helper.save_address('Улица Пушкина, дом Колотушкина')
db_helper.save_address('Проспект Ленина, 123')

# Выводим содержимое базы данных
db_helper.print_addresses()