import webbrowser

from ctkmvc.controller import Controller
from pathlib import WindowsPath

from resources.resource import Resource


class MainWindowController(Controller):
    
    def __init__(self, view_cls, model) -> None:

        super().__init__(view_cls, model)


    def generate_path(self, **args):
       
       self._model.generate_path(args)
            
       webbrowser.open(url=WindowsPath(Resource.MAP).resolve().as_uri())