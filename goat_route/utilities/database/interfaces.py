import sqlite3
from abc import ABC, abstractmethod

class IDBHelper(ABC):
    def __init__(self, database_file):
        self.database_file = database_file
        self.conn = None
        self.cursor = None

    @abstractmethod
    def create_table(self):
        """Абстрактный метод для создания таблицы в базе данных."""
        pass

    @abstractmethod
    def save_address(self, address: str):
        """Абстрактный метод для сохранения адреса в базе данных."""
        pass

    @abstractmethod
    def get_addresses(self):
        """Абстрактный метод для получения всех адресов из базы данных."""
        pass

    def close(self):
        """Метод для закрытия соединения с базой данных."""
        if self.conn:
            self.conn.close()

    def connect(self):
        """Метод для подключения к базе данных."""
        self.conn = sqlite3.connect(self.database_file)
        self.cursor = self.conn.cursor()