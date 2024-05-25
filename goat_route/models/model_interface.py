from abc import ABC, abstractmethod

from ..utilities.observer import Observer

class IModel(ABC):

    def _init__(self):

        self._observers: list[Observer] = []

    @abstractmethod
    def notify_observers(self):
        pass