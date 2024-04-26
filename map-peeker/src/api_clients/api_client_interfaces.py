from abc import ABC, abstractmethod

from .. geolocation import Coordinate

class IAPIClient(ABC):

    def __init__(self, apikey: str):
        self._apikey = apikey 

    @property
    @abstractmethod
    def base_url(self):
        pass       

class IGeocoder(ABC):

    @abstractmethod
    def get_address(self, coordinates: Coordinate):
        pass

    @abstractmethod
    def get_coordinates(self, address: str):
        pass