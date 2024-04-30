from abc import ABC, abstractmethod

from .. geolocation import Coordinate, Address

class IAPIClient(ABC):

    '''
    Интерфейс для клиентов API
    '''

    def __init__(self, apikey: str):
        self._apikey = apikey 

    @property
    @abstractmethod
    def base_url(self):

        '''
        Базовый URL для запросов
        '''
        pass   

class I2GISAPIClient(IAPIClient):
    
    '''
    Интерфейс для клиентов 2GIS API 
    '''

    _BASE_URL = 'http://routing.api.2gis.com/routing/7.0.0/global?'  

class IGeocoder(ABC):

    '''
    Интерфейс для клиентов геокодера
    '''

    @abstractmethod
    def get_address(self, coordinates: Coordinate) -> Address:

        '''
        Получить адрес по координатам
        '''

        pass

    @abstractmethod
    def get_coordinates(self, address: Address) -> Coordinate:

        '''
        Получить координаты по адресу
        '''

        pass