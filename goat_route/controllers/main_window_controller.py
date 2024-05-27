import webbrowser

from pathlib import WindowsPath

from .interfaces import IController
from views.main_window_view import MainWindowView
from views.ui.interfaces import IGUI
from models.interfaces import IModel
from utilities.observer import GUIObserver

class MainWindowController(IController, GUIObserver):
    
    def __init__(self, view_gui: IGUI, model: IModel) -> None:

        super().__init__(model)

        self._view = MainWindowView(view_gui, self, model)

        view_gui.set_owner_view(self._view)

        view_gui.add_observer(self)

        self._show_view()

    def handle_event(self, event_name, **args):
        
        if event_name == 'generate_path':

            self.handle_generate_path(args)
            
    
    def handle_generate_path(self, args):

        self._model.generate_path(args)

        webbrowser.open_new_tab(url=WindowsPath('goat_route\\views\\ui\\resources\\map.html').resolve().as_uri())


    def _show_view(self) -> None:
        self._view.show()