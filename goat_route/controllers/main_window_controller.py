from .controller_interface import IController
from views.main_window_view import MainWindowView
from views.ui.gui_interface import IGUI

class MainWindowController(IController):
    
    def __init__(self, view_gui: IGUI, model) -> None:

        super().__init__(model)

        self._view = MainWindowView(self, view_gui, model)

        self._show_view()
    
    def _show_view(self) -> None:
        self._view.show()
