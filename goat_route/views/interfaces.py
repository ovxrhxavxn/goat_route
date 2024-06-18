from abc import ABC, abstractmethod

from controllers.interfaces import IController
from models.interfaces import IModel

class IView(ABC):

    def __init__(self, controller: IController, model: IModel):

        self._controller = controller
        self._model = model

    @abstractmethod
    def show(self):
        pass