'''
Функция years_days()
Реализуйте генераторную функцию years_days(), которая принимает один аргумент:

year — натуральное число

Функция должна возвращать генератор, порождающий последовательность 
всех дат (тип date) в году year.

Примечание 1. Возьмем в качестве примера 2022 год. В январе этого года 31 день, 
в феврале — 28, в марте — 31, и так далее. Тогда генератор, полученный 
при вызове years_days(2022), должен порождать сначала все даты с 1 по 31 января, 
затем с 1 по 28 февраля, и так далее до 31 декабря.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию years_days(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/673155/tests_2785891.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.7/Module_10.7.9

Sample Input:
dates = years_days(2022)
print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))

Sample Output:
2022-01-01
2022-01-02
2022-01-03
2022-01-04
'''
from _collections_abc import Generator
from datetime import datetime, timedelta

def years_days(year: int) -> Generator:
    _datetime = datetime.strptime(str(year), '%Y').date()
    _days = datetime.strptime(str(year+1), '%Y').date().toordinal() - _datetime.toordinal()
    return (_datetime + timedelta(days=i) for i in range(_days))

if __name__ == '__main__':
    dates = years_days(2022)
    print(next(dates))
    print(next(dates))
    print(next(dates))
    print(next(dates))