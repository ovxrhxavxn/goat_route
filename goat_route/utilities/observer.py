from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def model_is_changed(self):
        pass