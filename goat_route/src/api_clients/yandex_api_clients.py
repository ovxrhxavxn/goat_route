import json

from requests import Session, HTTPError, RequestException

from . api_client_interfaces import IGeocoder, IYandexAPIClient
from .. geolocation import Address, Coordinate


class StaticAPIClient(IYandexAPIClient):

    '''
    Класс для взаимодествия с Yandex Static API.
    '''

    __BASE_ENDPOINT = 'https://static-maps.yandex.ru/v1'

    class MapImage:

        '''
        Вспомогательный класс, сохраняющий полученный фрагмент карты.
        '''
        @staticmethod
        def save(image_bytes: bytes) -> bool:

            try:
            
                with open('map_fragment.png', 'wb') as map_fragment:

                    map_fragment.write(image_bytes)

            except Exception as e:
                print(e)

                return False
            
            else:
                return True


    def __init__(self, apikey: str):

        super().__init__(apikey=apikey)
    
    @property
    def base_endpoint(self) -> str:
        return self.__BASE_ENDPOINT


    def get_map_fragment(self, coordinates: Coordinate) -> None:

        '''
        Получить PNG фрагмент карты по координатам.
        '''
        try:
            with Session() as s:

                response = s.get(

                    url=f'{self.__BASE_ENDPOINT}apikey={self._apikey}&lang=ru_RU&ll={coordinates.latitude},{coordinates.longitude}&z=15&size={650},{450}'
                )

        except HTTPError as e:
            print(e.response.text)

        except RequestException as e:
            print(e.response.text)

        else:

            try:
                return self.MapImage.save(response.content)
            
            except Exception as e:
                print('Что-то пошло не так... Повторите попытку позже.')

    
class HTTPGeocoderClient(IYandexAPIClient, IGeocoder):

    '''
    Класс для взаимодействия с Yandex HTTP Geocoder.
    '''

    __BASE_ENDPOINT = 'https://geocode-maps.yandex.ru/1.x/'

    class _Extractor:

        '''
        Вспомогательный класс-экстрактор для HTTPGeocoderClient.
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
        
    @property
    def base_endpoint(self):
        return self.__BASE_ENDPOINT

    def get_address(self, coordinates: Coordinate) -> Address:

        try:
        
            with Session() as s:

                response = s.get(

                    url=f'{self.__BASE_ENDPOINT}?apikey={self._apikey}&geocode={coordinates.longitude},{coordinates.latitude}&lang=ru_RU&format=json'
                )      
        
        except HTTPError as e:
            print(e.response.text)

        except RequestException as e:
            print(e.response.text)

        else:

            try:
                return self._Extractor.extract_address(response.text)
            
            except Exception as e:
                print('Что-то пошло не так... Повторите попытку позже.')

    def get_coordinates(self, address: Address) -> Coordinate:

        try:
        
            with Session() as s:

                response = s.get(

                    url=f'{self.__BASE_ENDPOINT}?apikey={self._apikey}' + 
                
                    f'&geocode={address.country}+{address.city}+{address.street}+{address.building_number}' + 
                
                    '&lang=ru_RU&format=json'
                )

        except HTTPError as e:
            print(e.response.text)

        except RequestException as e:
            print(e.response.text)
        
        else:

            try:
                return self._Extractor.extract_coordinate(response.content)
            
            except Exception as e:
                print('Что-то пошло не так... Повторите попытку позже.')