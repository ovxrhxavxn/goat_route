from ..views.main_window_view import MainWindowView

class MainWindowController:

    def __init__(self, model):

        self._model = model
        self._view = MainWindowView()
