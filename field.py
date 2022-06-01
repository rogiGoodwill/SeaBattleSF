class Field:
    '''Класс создания поля для игры'''

    def __init__(self):
        self.__player_name = None
        self.__field_size = None
        self.__ships_coordinates = None
        self.field = None

    @property
    def player_name(self):
        return self.__player_name

    @player_name.setter
    def player_name(self, value):
        if self.__player_name is None:
            self.__player_name = value

    @property
    def field_size(self):
        return self.__field_size

    @field_size.setter
    def field_size(self, value):
        if self.__field_size is None:
            while not self.__field_size:
                if not value.isdigit():
                    print(f'{value} - не число')
                    value = input(
                        'Введите размер поля от 6 до 9 (оптимально 7): ')
                elif not (6 <= int(value) <= 9):
                    print(f'Число {value} должно быть в диапазоне от 6 до 9')
                    value = input(
                        'Введите размер поля от 6 до 9 (оптимально 7): ')
                else:
                    self.__field_size = int(value)

    @property
    def ships_coordinates(self):
        return self.__ships_coordinates

    @ships_coordinates.setter
    def ships_coordinates(self, value):
        if self.__ships_coordinates is None:
            self.__ships_coordinates = value
            self.field = [
                ['O' for _ in range(self.__field_size)] for i in range(self.__field_size)]
            for dot in self.__ships_coordinates:
                self.field[dot[1] - 1][dot[0] - 1] = '■'

    def show_field(self, hide_ships=False):
        Field.__show_field(self, self.field, hide_ships)

    def __show_field(self, player_field, hide_ships):
        print()
        print(f'Поле игрока: {self.__player_name}')
        print('     ', end='')
        [print(i, end=' | ') for i in range(1, self.__field_size + 1)]
        print()
        print('--' * self.__field_size * 2 + '----')
        for i in range(self.__field_size):
            print(i + 1, end='  |')
            for j in range(self.__field_size):
                if hide_ships:
                    if player_field[i][j] == '■':
                        print(f' O ', end='|')
                    else:
                        print(f' {player_field[i][j]} ', end='|')
                else:
                    print(f' {player_field[i][j]} ', end='|')
            print()
