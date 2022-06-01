from random import randrange
import time
from ship import Ship

class Ships:
    '''Класс создания кораблей на игровом поле'''

    # В списке ship_list задается длина и количество кораблей на поле
    ship_list = [3, 2, 2, 1, 1, 1, 1]

    def __init__(self, field_size):
        self._field_size = field_size
        self.coordinates, self.built_ships = Ships.get_coordinates(self)

    # Функция установки координат кораблей
    def get_coordinates(self):
        ships_coordinates = set()
        time_start = time.time()
        while len(ships_coordinates) != sum(Ships.ship_list):
            ships_coordinates.clear()
            built_ships = dict()
            key_num = 0
            for amount_decks in Ships.ship_list:
                key_num += 1
                flag = True
                while flag:
                    x = randrange(1, self._field_size + 1)
                    y = randrange(1, self._field_size + 1)
                    # расположение корабля: 1 - горизонталь, 2 - вертикаль
                    course = randrange(1, 3)

                    # Проверяем, чтобы длина корабля не выходила за размер поля
                    if (course == 1 and (y + amount_decks) <= self._field_size) or (
                            course == 2 and (x + amount_decks) <= self._field_size):
                        new_ship = Ship(amount_decks, x, y, course)

                        # Проверяем, что координаты нового корабля не пересекутся со старыми кораблями
                        # и что клетки вокруг корабля не заняты
                        if ships_coordinates.isdisjoint(new_ship.coordinates) and \
                                ships_coordinates.isdisjoint(new_ship.coordinates_around_ship):
                            ships_coordinates.update(new_ship.coordinates)
                            built_ships[key_num] = [list(new_ship.coordinates), new_ship.ship_health]
                            flag = False
                        else:
                            time_stop = time.time()
                            if time_stop - time_start > 0.5:
                                flag = False
        return [ships_coordinates, built_ships]