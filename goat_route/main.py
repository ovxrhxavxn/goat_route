from os import getenv
from dotenv import load_dotenv

from src.api_clients.yandex_api_clients import HTTPGeocoderClient, StaticAPIClient
from src.api_clients.two_gis_api_clients import RoutingAPIClient
from src.geolocation import Address, Coordinate

def main():
    load_dotenv()

    address = Address('Россия', 'Челябинск', 'Братьев Кашириных', '129')

    geocoder = HTTPGeocoderClient(getenv('GEOCODER_API_KEY'))

    print(geocoder.get_coordinates(address))

if __name__ == '__main__':
    main()