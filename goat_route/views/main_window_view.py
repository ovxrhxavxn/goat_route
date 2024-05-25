from .view_interface import IView
from ..utilities.observer import Observer
from .gui.main_window_gui import MainWindowGUI

class MainWindowView(IView, Observer):

    def __init__(self, controller, model):

        super().__init__(controller, model)
        self._gui = MainWindowGUI()

        self._model.add_observer(self)
        

    def show(self):
        self._gui.mainloop()

    def model_is_changed(self):
        pass

