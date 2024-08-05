from os import getenv
from ctkmvc.model import ObservableModel

from core.api_clients.yandex_api_clients import HTTPGeocoderClient
from core.tsp_solver import TSPSolver
from core.mapping.geolocation import Address, Coordinate
from core.mapping.map import Map


class MainWindowModel(ObservableModel):

    def __init__(self) -> None:

        super().__init__()


    def _get_coordinates(self, addresses):

        geocoder = HTTPGeocoderClient(

            getenv('GEOCODER_API_KEY')
        )

        coords = []

        for address in addresses:

            addr = Address.convert_from(address)

            coords.append(geocoder.get_coordinates(addr))

        return coords
    

    def _solve_tsp(self, address: Address, coords: list[Coordinate], network_type):

        tsp_solver = TSPSolver()

        return tsp_solver.solve(address, coords, network_type)
    
    
    def _save_html_map(self, solution):

        map = Map()

        map.put_tsp_markers(solution)
        map.plot_tsp_route(solution)
        map.save()


    def generate_path(self, data: dict):

        addresses = data.get('addresses')
        network_type = data.get('network_type')
        
        coords = self._get_coordinates(addresses)

        solution = self._solve_tsp(Address.convert_from(addresses[0]), coords, network_type)

        self._save_html_map(solution)