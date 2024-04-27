from abc import ABC, abstractmethod

from .. geolocation import Coordinate, Address

class IAPIClient(ABC):

    def __init__(self, apikey: str):
        self._apikey = apikey 

    @property
    @abstractmethod
    def base_url(self):
        pass   

class I2GISAPIClient(IAPIClient):

    _BASE_URL = 'http://routing.api.2gis.com/routing/7.0.0/global?'  

class IGeocoder(ABC):

    @abstractmethod
    def get_address(self, coordinates: Coordinate) -> Address:
        pass

    @abstractmethod
    def get_coordinates(self, address: Address) -> Coordinate:
        pass