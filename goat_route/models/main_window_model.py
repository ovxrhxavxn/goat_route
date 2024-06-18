from os import getenv

from .interfaces import IModel
from utilities.observer import ModelObserver
from utilities.api_clients.yandex_api_clients import HTTPGeocoderClient
from utilities.tsp_solver import TSPSolver
from utilities.mapping.geolocation import Address, Coordinate
from utilities.mapping.map import Map

class MainWindowModel(IModel):

    def __init__(self) -> None:

        super().__init__()

        self._observers = []

    def add_observer(self, observer: ModelObserver):
        self._observers.append(observer)

    def remove_observer(self, observer: ModelObserver):
        self._observers.remove(observer)

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


    def notify_observers(self):

        for observer in self._observers:
            
            observer.model_is_changed()