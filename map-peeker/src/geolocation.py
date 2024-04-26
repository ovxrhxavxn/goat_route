class Coordinate:
    
    def __init__(self, latitude: float, longitude: float):

        self._latitude = latitude
        self._longitude = longitude

    @property
    def longitude(self):
        return self._longitude
    
    @property
    def latitude(self):
        return self._latitude
    
    
class Address:

    def __init__(self, country: str, city: str, street: str, house_number: int):

        self._country = country
        self._city = city
        self._street = street
        self._house_number = house_number

    @property
    def country(self) -> str:
        return self._country
    
    @property
    def city(self) -> str:
        return self._city
    
    @property
    def street(self) -> str:
        return self._street
    
    @property
    def house_number(self) -> int:
        return self._house_number