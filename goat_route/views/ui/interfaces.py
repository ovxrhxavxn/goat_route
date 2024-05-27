from abc import ABC, abstractmethod

from ..interfaces import IView

class IGUI(ABC):

    def set_owner_view(self, view: IView):

        self._owner = view

    @abstractmethod
    def init(self):
        pass