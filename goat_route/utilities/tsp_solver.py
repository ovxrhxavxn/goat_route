import osmnx as ox
import networkx as nx

from networkx.algorithms.approximation.traveling_salesman import traveling_salesman_problem
from enum import StrEnum

from utilities.mapping.geolocation import Coordinate, Address

class TSPSolver:

    class Solution:

        def __init__(self, route, graph, solved_nodes, coords_nodes: dict):

            self.__route = route
            self.__graph = graph
            self.__solved_nodes = solved_nodes
            self.__coords_nodes = coords_nodes

        @property
        def route(self):
            return self.__route
        
        @property
        def graph(self):
            return self.__graph

        @property
        def solved_nodes(self):
            return self.__solved_nodes
    
        @property
        def coords_nodes(self):
            return self.__coords_nodes
        
    class NetworkType(StrEnum):

        WALK = 'walk',
        ALL = 'all',
        ALL_PUBLIC = 'all_public',
        DRIVE = 'drive',
        DRIVE_SERVICE = 'drive_service',
        BIKE = 'bike'

    def __init__(self) -> None:
        
        ox.config(use_cache=True)

    def __build_graph_from_city(self, address, network_type):

        return ox.graph_from_place(

            f'{address.country}, {address.city}', 
            network_type=network_type, 
            truncate_by_edge=True
            
            )
    
    def __get_nodes_to_visit(self, graph, coordinates: list[Coordinate]):

        return [ox.nearest_nodes(graph, coord.tuple[0], coord.tuple[1]) for coord in coordinates]
    
    def __fill_coords_nodes(self, coordinates, nodes):

        coords_nodes = {}

        for i, node in enumerate(nodes):

            coords_nodes[node] = coordinates[i]

        return coords_nodes
    
    def __get_nodes_subgraph(self, nodes_to_visit):

        return nx.complete_graph(nodes_to_visit, create_using=nx.MultiDiGraph)
    
    def __get_solved_nodes(self, subgraph):
        
        return traveling_salesman_problem(G=subgraph)
    
    def __get_route(self, graph, solved_nodes):

        routes = []

        for i in range(len(solved_nodes)-1):

            routes.append(nx.shortest_path(

                graph,
                solved_nodes[i],
                solved_nodes[i+1],
                weight='length'
            
                ))
            
        return routes

    def solve(self, address: Address, coordinates: list[Coordinate], network_type: NetworkType):

        graph = self.__build_graph_from_city(address, network_type)
        
        nodes_to_visit = self.__get_nodes_to_visit(graph, coordinates)

        subgraph_of_nodes: nx.MultiDiGraph = self.__get_nodes_subgraph(nodes_to_visit)
   
        solved_nodes = self.__get_solved_nodes(subgraph_of_nodes)

        route = self.__get_route(graph, solved_nodes)

        return self.Solution(route, graph, solved_nodes, self.__fill_coords_nodes(coordinates, nodes_to_visit))