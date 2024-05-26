from abc import ABC, abstractmethod

from models.model_interface import IModel

class IController(ABC):

    def __init__(self, model: IModel) -> None:

        self._model = model

    @abstractmethod
    def _show_view(self):
        pass