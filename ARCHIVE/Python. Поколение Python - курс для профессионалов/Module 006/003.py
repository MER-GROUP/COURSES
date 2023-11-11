'''
Game

Вам доступен именованный кортеж Game. Дополните приведенный ниже код, 
чтобы он создал именованный кортеж типа ExtendedGame, имеющий те же поля, 
что и Game, а также два дополнительных поля — release_date и price.

Примечание. Программа ничего не должна выводить.

from collections import namedtuple

Game = namedtuple('Game', 'name developer publisher')

ExtendedGame = ____
'''
from collections import namedtuple

Game = namedtuple('Game', 'name developer publisher')

ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])