from requests import Session

from . api_client_interfaces import IGeocoder, IAPIClient
from .. geolocation import Address, Coordinate

class StaticAPIClient(IAPIClient):

    _BASE_URL = 'https://static-maps.yandex.ru/v1?'
    
    def __init__(self, api_key: str):
        super()._apikey = api_key

    @property
    def base_url(self) -> str:
        return self._BASE_URL

    def get_map_fragment(self, coordinate: Coordinate) -> bytes:

        with Session() as s:

            response = s.get(

                url=f'{self._BASE_URL}apikey={self._apikey}&lang=ru_RU&ll={coordinate.latitude},{coordinate.longitude}&&spn=0.016457,0.00619'
            )

        return response.content
    
class HTTPGeocoderClient(IAPIClient, IGeocoder):

    _BASE_URL = 'https://geocode-maps.yandex.ru/1.x?'

    def __init__(self, api_key: str):
        super()._apikey = api_key

    def get_address(self, coordinates: Coordinate) -> Address:
        
        with Session() as s:

            response = s.get(

                url=f'{self._BASE_URL}apikey={self._apikey}&geocode={coordinates.longitude},{coordinates.latitude}&lang=ru_RU&format=json'
            )
        
        return response.json()
    
    def get_coordinates(self, address: str) -> Coordinate:
        
        with Session() as s:

            response = s.get(

                url=f'{self._BASE_URL}apikey={self._apikey}&geocode={self}&lang=ru_RU&format=json'
            )