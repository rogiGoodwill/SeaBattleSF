from email import message
from main import *

class Messages:
    message_welcome = '''
    ******************************
    *                            *
    *  Добро пожаловать в игру   *
    *--------МОРСКОЙ БОЙ!--------*
    *                            *
    * Обозначения на поле:       *
    * Знак O - пустое поле       *
    * Знак T - промах            *
    * Знак X - попадание         *
    * Знак + - подбитый корабль  *
    *                            *
    *  Координаты вводятся       *
    *  через пробел:             *
    *  - x (горизонталь),        *
    *  - y (вертикаль)           *
    *                            *
    ******************************
    '''

    message_congrat_player = f'''
                
**************************
Поздравляем, Вы победили!
**************************

    '''

    message_congrat_comp = f'''
                
**************************************************
Искусственный интелект одержал верх над человеком!
Не расстраивайтесь, в следуюший раз повезет!
**************************************************

    '''

class MessageException:
    message_quantity_coordinate_exception = '''
---                                                              ---
--- Ошибка ввода координат! Нужно ввести два числа через пробел! ---
---                                                              ---    
    '''

    message_is_digital_coordinate_exception = '''
---                                                                        ---
--- Ошибка ввода координат! Одно из значений координат не является числом! ---
---                                                                        ---    
    '''

    message_coordinates_not_in_field = '''
---                                                  ---
--- Ошибка ввода координат! Выстрел за пределы поля! ---
---                                                  ---    
    '''

    message_repeat_coordinates = '''
---                                                      ---
--- Ошибка ввода координат! Вы уже стреляли в эту точку! ---
---                                                      ---    
    '''

