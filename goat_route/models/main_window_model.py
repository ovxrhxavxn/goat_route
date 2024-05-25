from .model_interface import IModel

class MainWindowModel(IModel):

    def ___init__(self) -> None:

        super()._init__()

    def notify_observers(self):

        for observer in self._observers:
            
            observer.model_is_changed()