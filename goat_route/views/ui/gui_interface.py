from abc import ABC, abstractmethod

class IGUI(ABC):

    @abstractmethod
    def init(self):
        pass