class Coordinate:
    
    def __init__(self, longitude: float, latitude: float):

        self.__longitude = longitude
        self.__latitude = latitude

    @property
    def longitude(self):
        return self.__longitude
    
    @property
    def latitude(self):
        return self.__latitude