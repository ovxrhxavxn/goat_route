from .controller_interface import IController
from ..views.main_window_view import MainWindowView

class MainWindowController(IController):
    
    def __init__(self, model) -> None:

        super().__init__(model)
        self._view = MainWindowView(self, model)

        self.show_view()
    
    def show_view(self) -> None:
        self._view.show()
