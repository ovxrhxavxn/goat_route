from .interfaces import IController
from views.map_window_view import MapWindowView

class MapWindowController(IController):

    def __init__(self, model) -> None:

        super().__init__(model)
        self._view = MapWindowView(self, model)

        self._show_view()
    
    def _show_view(self) -> None:
        self._view.show()