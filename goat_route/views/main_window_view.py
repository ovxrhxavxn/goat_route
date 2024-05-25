from .view_interface import IView
from ..utilities.observer import Observer

class MainWindowView(IView, Observer):

    def __init__(self, ui, controller, model):

        super().__init__(ui, controller, model)

    def show(self):
        pass

    def model_is_changed(self):
        pass