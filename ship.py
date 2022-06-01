class Ship:
    '''Класс создания корабля'''

    def __init__(self, length, coord_x, coord_y, course):
        self.length = length
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.course = course
        self.coordinates = Ship.ship_coordinates(self)
        self.coordinates_around_ship = Ship.ship_coordinates_around(self)
        self.ship_health = length

    # Создание множества координат корабля
    def ship_coordinates(self):
        coordinates = set()
        if self.course == 1:
            for i in range(1, self.length + 1):
                coordinates.add((self.coord_x, self.coord_y + i))
        else:
            for i in range(1, self.length + 1):
                coordinates.add((self.coord_x + i, self.coord_y))
        return coordinates

    # Создание множества координат вокруг корабля
    def ship_coordinates_around(self):
        coordinates_around = set()
        for dot in self.coordinates:
            coordinates_around.add((dot[0] + 1, dot[1]))
            coordinates_around.add((dot[0] - 1, dot[1]))
            coordinates_around.add((dot[0], dot[1] + 1))
            coordinates_around.add((dot[0], dot[1] - 1))
            coordinates_around.add((dot[0] + 1, dot[1] + 1))
            coordinates_around.add((dot[0] - 1, dot[1] - 1))
            coordinates_around.add((dot[0] - 1, dot[1] + 1))
            coordinates_around.add((dot[0] + 1, dot[1] - 1))
        return coordinates_around
