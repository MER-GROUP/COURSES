'''
Fruit

Дополните приведенный ниже код, чтобы он создал именованный 
кортеж Fruit с полями name, color и vitamins.

Примечание. Программа ничего не должна выводить.

from ____ import ____

Fruit = ____
'''
from collections import namedtuple

Fruit = namedtuple('Fruit', 'name,color,vitamins')