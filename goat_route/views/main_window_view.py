from .view_interface import IView
from utilities.observer import Observer
from .ui.gui_interface import IGUI

class MainWindowView(IView, Observer):

    def __init__(self, gui: IGUI, controller, model):

        super().__init__(controller, model)

        self._gui = gui
        self._model.add_observer(self)
        
    def show(self):
        self._gui.init()

    def model_is_changed(self):
        pass

