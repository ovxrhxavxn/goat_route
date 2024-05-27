from abc import ABC, abstractmethod

class ModelObserver(ABC):

    @abstractmethod
    def model_is_changed(self):
        pass


class GUIObserver(ABC):

    @abstractmethod
    def handle_event(self, event_name, **args):
        pass


class IObservable(ABC):

    @abstractmethod
    def add_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify_observers(self):
        pass