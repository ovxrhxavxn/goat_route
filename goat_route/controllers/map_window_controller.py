from .controller_interface import IController

class MapWindowController(IController):

    def __init__(self, view, model) -> None:

        super().__init__(view, model)

        self.show_view()
    
    def show_view(self) -> None:
        self._view.show()