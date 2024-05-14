from dataclasses import dataclass

@dataclass
class Coordinate:

    '''
    Класс координат
    '''

    _longitude: float
    _latitude: float

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
    
@dataclass 
class Address:

    _country: str
    _city: str
    _street: str
    _house_number: int | str

    '''
    Класс адреса
    '''

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