import json

from requests import Session, HTTPError, RequestException
from dataclasses import dataclass

from . api_client_interfaces import INavitelAPICLient, ITSPSolver
from .. geolocation import Address, Coordinate

class TSPAPIClient(INavitelAPICLient, ITSPSolver):

    @dataclass
    class Solution:
        pass 

    _BASE_ENDPOINT = 'https://webmapapi.navitel.ru/api/v1/calculateTSP/'

    @property
    def base_endpoint(self):
        return self._BASE_ENDPOINT
    
    def __make_body_for_tsp(self, waypoints: list[Coordinate]):
        pass
    
    def solve_tsp(self, waypoints: list[Coordinate]) -> Solution:

        body = self.__make_body_for_tsp(waypoints)

        headers = {

            'accept': 'application/json',

            'Api-Key': self._apikey,

            'Content-Type': 'application/json'
        }
