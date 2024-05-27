from abc import ABC, abstractmethod

class IDBHelper(ABC):

    @abstractmethod
    def create_table(self):
        pass