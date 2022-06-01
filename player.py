from random import randrange
from myExceptions import *


class Player:
    def __init__(self):
        self.field = None
        self.destroyed_ships = set()
        self.score = 0
        self.shoots = set()

    def turn(self, opponent):

        if self.field.player_name == 'Computer':
            while True:
                x = randrange(1, self.field.field_size + 1)
                y = randrange(1, self.field.field_size + 1)
                comp_coordinates = [x, y]
                tmp = set()
                tmp.add(tuple(map(lambda a: int(a), comp_coordinates)))
                if not tmp.intersection(self.shoots):
                    return Player.shoot(self, opponent, comp_coordinates)

        else:
            try:
                input_coordinates = input(
                    f'Ходит игрок {self.field.player_name}. Введите координаты x, y через пробел или exit для выхода: ').split()
                if ''.join(input_coordinates) == 'exit':
                    quit()
                elif len(input_coordinates) != 2:
                    raise QuantityCoordinateException
                elif not input_coordinates[0].isdigit() or not input_coordinates[1].isdigit():
                    raise IsDigitalCoordinateException
                elif int(input_coordinates[0]) not in range(1, self.field.field_size + 1) or \
                        int(input_coordinates[1]) not in range(1, self.field.field_size + 1):
                    raise CoordinatesNotInField
                else:
                    tmp = set()
                    tmp.add(tuple(map(lambda a: int(a), input_coordinates)))
                    if tmp.intersection(self.shoots):
                        raise RepeatCoordinates
            except QuantityCoordinateException:
                print()
                print('!!!')
                print('Ошибка ввода координат! Нужно ввести два числа через пробел!')
                return True  # возвращаем True для того, чтобы ход не переходил сопернику
            except IsDigitalCoordinateException:
                print()
                print('!!!')
                print('Ошибка ввода координат! Одно из значений координат не является числом!')
                return True  # возвращаем True для того, чтобы ход не переходил сопернику
            except CoordinatesNotInField:
                print()
                print('!!!')
                print('Ошибка ввода координат! Выстрел за пределы поля!')
                return True  # возвращаем True для того, чтобы ход не переходил сопернику
            except RepeatCoordinates:
                print()
                print('!!!')
                print('Ошибка ввода координат! Вы уже стреляли в эту точку!')
                return True  # возвращаем True для того, чтобы ход не переходил сопернику
            else:
                return Player.shoot(self, opponent, input_coordinates)

    def shoot(self, opponent, input_coordinates):
        fire = set()
        fire.add(tuple(map(lambda a: int(a), input_coordinates)))
        tuple_fire = tuple(fire)[0]
        self.shoots.update(fire)
        if opponent.field.ships_coordinates.intersection(fire):
            print()
            print('Есть попадание!')
            self.score += 1
            opponent.field.field[tuple_fire[1] - 1][tuple_fire[0] - 1] = 'X'
            opponent.destroyed_ships.update(Player.rest_of_ships(opponent.built_ships, tuple_fire))

            if opponent.field.ships_coordinates.intersection(opponent.destroyed_ships):
                for dot in opponent.destroyed_ships:
                    opponent.field.field[dot[1] - 1][dot[0] - 1] = '+'
            return True
        else:
            opponent.field.field[tuple_fire[1] - 1][tuple_fire[0] - 1] = 'T'
        fire.clear()

    @staticmethod
    def rest_of_ships(ships, hit):
        for ship, status in ships.items():
            coords, health = status
            if hit in coords:
                ships[ship][1] -= 1
                if ships[ship][1] == 0:
                    # если здоровье = 0, то возвращаем координаты уничтоженного корабля
                    print(f'!!! Корабль размером <<{len(ships[ship][0])}>> уничтожен !!!')
                    return set(coords)
                else:
                    return set()
