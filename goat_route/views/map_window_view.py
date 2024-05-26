from .view_interface import IView
# from .ui.gui import MapWindowUI
from utilities.observer import Observer

class MapWindowView(IView, Observer):

    def __init__(self, controller, model):

        super().__init__(controller, model)

        # self._gui = MapWindowGUI()
        self._model.add_observer(self)

    def show(self):
        # self._gui.init()
        pass

    def model_is_changed(self):
        pass