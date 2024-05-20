import folium

from pathlib import Path

from .geolocation import Coordinate

class Map(folium.Map):
    
    def put_marker(self, coordinates: Coordinate) -> None:
        
        folium.Marker(
            
            location=[coordinates.latitude, coordinates.longitude]
            
        ).add_to(self)

    def put_line(self, coord_from: Coordinate, coord_to: Coordinate) -> None:

        folium.PolyLine(

            locations=[

                [coord_from.latitude, coord_from.longitude],

                [coord_to.latitude, coord_to.longitude]
            ]
        ).add_to(self)

    def save(self, path: str = 'views\\resources\\map.html'):

        super().save(Path(path).resolve())