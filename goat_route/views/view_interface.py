from abc import ABC, abstractmethod

from ..controllers.controller_interface import IController
from ..models.model_interface import IModel

class IView(ABC):

    def __init__(self, ui, controller: IController, model: IModel):

        self._controller = controller
        self._model = model
        self._ui = ui

    @abstractmethod
    def show(self):
        pass