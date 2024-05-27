from .interfaces import IModel

class MapWindowModel(IModel):
    
    def _init__(self) -> None:

        super().__init__()


    def notify_observers(self) -> None:

        for observer in self._observers:
            
            observer.model_is_changed()