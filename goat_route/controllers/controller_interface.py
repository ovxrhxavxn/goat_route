from abc import ABC, abstractmethod

from ..views.view_interface import IView
from ..models.model_interface import IModel

class IController(ABC):

    def __init__(self, view: IView, model: IModel) -> None:

        self._view = view
        self._model = model

    @abstractmethod
    def show_view(self):
        pass