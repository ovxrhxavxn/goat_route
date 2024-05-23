from ..views.map_window_view import MapWindowView

class mapWindowController:
    
    def __init__(self, model):

        self._model = model
        self._view = MapWindowView()