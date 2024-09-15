import webbrowser
import multiprocessing
from pathlib import WindowsPath

from ctkmvc.controller import Controller

from resources.resource import Resource


class MainWindowController(Controller):
    
    def __init__(self, view_cls, model) -> None:

        super().__init__(view_cls, model)

    
    def generate_path(self, **kwargs):
       
        process = multiprocessing.Process(target=self._model.generate_path, kwargs=kwargs)

        process.start()

        # if not process.is_alive():

        #     webbrowser.open(url=WindowsPath(Resource.MAP).resolve().as_uri())