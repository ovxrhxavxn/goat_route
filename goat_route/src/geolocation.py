class Coordinate:

    '''
    Класс координат
    '''

    def __init__(self, latitude: float, longitude: float):

        self._latitude = latitude
        self._longitude = longitude

    def __str__(self) -> str:
        return f'{self.longitude}, {self.latitude}'

    @property
    def longitude(self) -> float:

        '''
        Значение долготы
        '''

        return self._longitude
    
    @property
    def latitude(self) -> float:
        
        '''
        Значение широты
        '''

        return self._latitude
    
    
class Address:

    '''
    Класс адреса
    '''

    def __init__(self, country: str, city: str, street: str, house_number: str | int):

        self._country = country
        self._city = city
        self._street = street
        self._house_number = house_number

    def __str__(self) -> str:
        return f'{self.country}, {self.city}, {self.street}, {self.building_number}'

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
    def building_number(self) -> int:
        return self._house_number