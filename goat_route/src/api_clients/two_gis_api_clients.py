from requests import Session, HTTPError
import json

from . api_client_interfaces import IGeocoder, I2GISAPIClient
from .. geolocation import Address, Coordinate

class RoutingAPIClient(I2GISAPIClient):
    
    @property
    def base_url(self):
        return self._BASE_URL
    

class PlacesAPICLient(I2GISAPIClient):
    pass
