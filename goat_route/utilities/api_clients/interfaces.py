from abc import ABC, abstractmethod

from utilities.mapping.geolocation import Coordinate, Address

class __IAPIClient(ABC):

    '''
    Интерфейс для клиентов API.
    '''

    def __init__(self, apikey: str):

        self._apikey = apikey 

    @property
    @abstractmethod
    def base_endpoint(self) -> str:
        pass


class IYandexAPIClient(__IAPIClient):

    '''
    Интерфейс для клиентов Yandex API
    '''


class IGeocoder(ABC):

    '''
    Интерфейс для клиентов геокодера.
    '''

    @abstractmethod
    def get_address(self, coordinates: Coordinate) -> Address:

        '''
        Получить адрес по координатам.
        '''

        pass

    @abstractmethod
    def get_coordinates(self, address: Address) -> Coordinate:

        '''
        Получить координаты по адресу.
        '''

        pass