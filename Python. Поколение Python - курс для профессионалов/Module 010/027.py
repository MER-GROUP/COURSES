'''
Функция dates()
Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:

start — дата, тип date
count — натуральное число, по умолчанию имеет значение None

Если count имеет значение None, функция должна возвращать генератор, порождающий последовательность 
из максимально допустимого количества дат (тип date), начиная с даты start.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, 
порождающий последовательность из count дат (тип date), начиная с даты start, а затем возбуждающий 
исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую генераторную 
функцию dates(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640048/tests_2777686.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.5/Module_10.5.19

Sample Input 1:
generator = dates(date(2022, 3, 8))
print(next(generator))
print(next(generator))
print(next(generator))
Sample Output 1:
2022-03-08
2022-03-09
2022-03-10

Sample Input 2:
generator = dates(date(2022, 3, 8), 5
print(*generator)
Sample Output 2:
2022-03-08 2022-03-09 2022-03-10 2022-03-11 2022-03-12
'''
from __future__ import annotations
from _collections_abc import Generator
from datetime import datetime, date

def dates(start: date) -> Generator:
    ...
            
if __name__ == '__main__':
    generator = dates(date(2022, 3, 8))
    print(next(generator))
    print(next(generator))
    print(next(generator))

    generator = dates(date(2022, 3, 8), 5
    print(*generator)