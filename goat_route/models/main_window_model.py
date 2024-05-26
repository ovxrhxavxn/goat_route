from .model_interface import IModel
from utilities.observer import Observer

class MainWindowModel(IModel):

    def __init__(self) -> None:

        super().__init__()

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):

        for observer in self._observers:
            
            observer.model_is_changed()