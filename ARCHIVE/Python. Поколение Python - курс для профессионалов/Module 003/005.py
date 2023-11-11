'''
Функция get_min_max()
Реализуйте функцию get_min_max(), которая принимает один аргумент:

dates — список дат (тип date)

Функция должна возвращать кортеж, первым элементом которого 
является минимальная дата из списка dates, вторым — максимальная 
дата из списка dates. Если список dates пуст, 
функция должна вернуть пустой кортеж.

Примечание 1. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию get_min_max(), 
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/609341/tests_2489841.zip

Sample Input 1:
dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
print(get_min_max(dates))
Sample Output 1:
(datetime.date(1992, 6, 10), datetime.date(2021, 10, 5))

Sample Input 2:
print(get_min_max([]))
Sample Output 2:
()
'''
from datetime import date

def get_min_max(arr: list) -> tuple:
    return (min(arr), max(arr)) if len(arr) else tuple()

if __name__ == '__main__':
    from datetime import date
    dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
    print(get_min_max(dates))
    print(get_min_max([]))