import folium
import osmnx as ox

from pathlib import Path
from folium import Icon
from .geolocation import Coordinate
from ..tsp_solver import TSPSolver

class Map(folium.Map):
    
    def put_marker(self, coordinates: Coordinate) -> None:

        folium.Marker(
            
            location=[coordinates.latitude, coordinates.longitude]
            
        ).add_to(self)

    def put_tsp_markers(self, tsp_solution: TSPSolver.Solution):

        num = 0

        for node in tsp_solution.solved_nodes:

            coord: Coordinate = tsp_solution.coords_nodes.get(node)

            folium.Marker(

                location=[coord.latitude, coord.longitude],
                icon=Icon(icon=f'{num}', prefix='fa')

            ).add_to(self)

            num+=1

    def plot_tsp_route(self, solution: TSPSolver.Solution):

        for route in solution.route:
            ox.plot_route_folium(G=solution.graph, route=route, route_map=self)

    def save(self, path: str = 'views\\resources\\map.html'):
        
        super().save(Path(path).resolve())