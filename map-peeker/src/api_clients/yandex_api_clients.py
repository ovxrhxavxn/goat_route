from requests import Session, HTTPError
import json

from . api_client_interfaces import IGeocoder, IAPIClient
from .. geolocation import Address, Coordinate


class StaticAPIClient(IAPIClient):

    '''
    Класс для взаимодествия с Yandex Static API
    '''

    class MapImage:

        '''
        Вспомогательный класс, сохраняющий полученный фрагмент карты
        '''

        def save(self, image_bytes: bytes) -> bool:

            try:
            
                with open('map_fragment.png', 'wb') as map_fragment:

                    map_fragment.write(image_bytes)

            except Exception as e:
                print(e)

                return False
            
            else:
                return True


    _BASE_URL = 'https://static-maps.yandex.ru/v1?'

    def __init__(self, apikey: str):

        super().__init__(apikey=apikey)

        self._map_image = StaticAPIClient.MapImage()

    @property
    def base_url(self) -> str:
        return self._BASE_URL

    def get_map_fragment(self, coordinate: Coordinate) -> None:

        '''
        Получить PNG фрагмент карты по координатам
        '''

        with Session() as s:

            response = s.get(

                url=f'{self._BASE_URL}apikey={self._apikey}&lang=ru_RU&ll={coordinate.latitude},{coordinate.longitude}&z=15&size={650},{450}'
            )

        return self._map_image.save(response.content)

    
class HTTPGeocoderClient(IAPIClient, IGeocoder):

    '''
    Класс для взаимодействия с Yandex HTTP Geocoder 
    '''

    class Extractor:

        '''
        Вспомогательный класс-экстрактор для HTTPGeocoderClient
        '''

        @staticmethod
        def extract_coordinate(json_response: str) -> Coordinate:
            
            response = json.loads(json_response)

            pos = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]

            coordinates = str(pos).split(' ')

            return Coordinate(coordinates[0], coordinates[1])
        
        @staticmethod
        def extract_address(json_response: str) -> Address:

            response = json.loads(json_response)

            components = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']

            country_name = next((comp['name'] for comp in components if comp['kind'] == 'country'), None)
            locality_name = next((comp['name'] for comp in components if comp['kind'] == 'locality'), None)
            street_name = next((comp['name'] for comp in components if comp['kind'] == 'street'), None)
            house_number = next((comp['name'] for comp in components if comp['kind'] == 'house'), None)

            return Address(country_name, locality_name, street_name, house_number)

    _BASE_URL = 'https://geocode-maps.yandex.ru/1.x?'

    def __init__(self, apikey: str):

        super().__init__(apikey=apikey)

        self._deserializer = HTTPGeocoderClient.Extractor()

    @property
    def base_url(self):
        return self._BASE_URL

    def get_address(self, coordinates: Coordinate) -> Address:

        try:
        
            with Session() as s:

                response = s.get(

                    url=f'{self._BASE_URL}apikey={self._apikey}&geocode={coordinates.longitude},{coordinates.latitude}&lang=ru_RU&format=json'
                )      
        
        except HTTPError as e:
            print(e.response.status_code)

        else:
            return self._deserializer.extract_address(response.text)
    
    def get_coordinates(self, address: Address) -> Coordinate:

        try:
        
            with Session() as s:

                response = s.get(

                    url=f'{self._BASE_URL}apikey={self._apikey}' + 
                
                    f'&geocode={address.country}+{address.city}+{address.street}+{address.building_number}' + 
                
                    '&lang=ru_RU&format=json'
                )
        
        except HTTPError as e:
            print(e.response.status_code)
        
        else:
            return self._deserializer.extract_coordinate(response.text)