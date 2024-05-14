from abc import ABC, abstractmethod

from .. geolocation import Coordinate, Address

class __IAPIClient(ABC):

    '''
    Интерфейс для клиентов API.
    '''

    def __init__(self, apikey: str):

        self._apikey = apikey 

    @property
    @abstractmethod
    def base_endpoint(self):
        pass
    

class IYandexAPIClient(__IAPIClient):

    '''
    Интерфейс для клиентов Yandex API
    '''


class I2GISAPIClient(__IAPIClient):
    
    '''
    Интерфейс для клиентов 2GIS API.
    '''

class INavitelAPICLient(__IAPIClient):

    '''
    Интерфейс для клиентов Navitel API
    '''

class IGeocoder(ABC):

    '''
    Интерфейс для клиентов геокодера.
    '''

    @abstractmethod
    def get_address(self):

        '''
        Получить адрес по координатам.
        '''

        pass

    @abstractmethod
    def get_coordinates(self):

        '''
        Получить координаты по адресу.
        '''

        pass

class ITSPSolver(ABC):

    @abstractmethod
    def solve_tsp(self):
        pass