from .interfaces import IView
from utilities.observer import ModelObserver
from .ui.interfaces import IGUI
from controllers.interfaces import IController
from models.interfaces import IModel

class MainWindowView(IView, ModelObserver):

    def __init__(self, gui: IGUI, controller: IController, model: IModel):

        super().__init__(controller, model)

        self._gui = gui
        self._model.add_observer(self)

    def show(self):
        self._gui.init()

    def model_is_changed(self):
        pass