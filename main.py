from player import Player
from field import Field
from ships import Ships


class StartSeaBattle:
    @staticmethod
    def start_game():
        print('******************************')
        print('*                            *')
        print('*  Добро пожаловать в игру   *')
        print('*--------МОРСКОЙ БОЙ!--------*')
        print('*                            *')
        print('* Обозначения на поле:       *')
        print('* Знак O - пустое поле       *')
        print('* Знак T - промах            *')
        print('* Знак X - попадание         *')
        print('* Знак + - подбитый корабль  *')
        print('*                            *')
        print('******************************')

        player = Player()
        player.field = Field()
        player.field.player_name = input('Введите имя игрока: ')
        player.field.field_size = input('Введите размер поля от 6 до 9 (оптимально 7): ')
        if player.field.field_size == 6:
            print(f'Вы выбрали размер поля, равный 6. Возможно придется немного подождать...')
        player.field.ships_coordinates, player.built_ships = Ships(player.field.field_size).get_coordinates()
        win_score = len(player.field.ships_coordinates)
        comp = Player()
        comp.field = Field()
        comp.field.player_name = 'Computer'
        comp.field.field_size = str(player.field.field_size)
        comp.field.ships_coordinates, comp.built_ships = Ships(comp.field.field_size).get_coordinates()
        selector_hide_ships = True  # Переключатель видимости поля игроков
        player.field.show_field()
        comp.field.show_field(hide_ships=selector_hide_ships)
        player_attack = player
        player_opponent = comp

        while True:
            repeat_move = False
            repeat_move = player_attack.turn(player_opponent)
            player.field.show_field()
            comp.field.show_field(hide_ships=selector_hide_ships)
            if player_attack.score == win_score:
                if player_attack == player:
                    print()
                    print()
                    print('****************************************************')
                    print(f'Поздравляем, {player_attack.field.player_name}, Вы победили!')
                    print('****************************************************')
                    input('Нажмите Enter для выхода\n')
                else:
                    print()
                    print()
                    print('****************************************************')
                    print(f'Искусственный интелект одержал верх над человеком!')
                    print(f'Не расстраивайтесь, {player.field.player_name}, в следуюший раз повезет!')
                    print('****************************************************')
                    input('Нажмите Enter для выхода\n')
                return False
            if not repeat_move:
                if player_attack == player:
                    player_attack = comp
                    player_opponent = player
                else:
                    player_attack = player
                    player_opponent = comp

