'''
Функция get_days_in_month()   
Реализуйте функцию get_days_in_month(), 
которая принимает два аргумента в следующем порядке:

year — натуральное число
month — полное название месяца на английском

Функция должна возвращать отсортированный по возрастанию список 
всех дат (тип date) месяца month и года year.

Примечание 1. Например, вызов:

get_days_in_month(2021, 'December')

должен вернуть список:

[datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ..., 
datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]

Примечание 2. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию get_days_in_month(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570049/tests_2575861.zip
'''
from datetime import datetime
from calendar import monthcalendar, month_name

def get_days_in_month(year: int, month: str) -> list[datetime.date]:
    month = list(month_name).index(month)
    month_days = [int(i) for i in sum(monthcalendar(year, month), []) if i]
    return [datetime(year=year, month=month, day=i).date() for i in month_days]

if __name__ == '__main__':
    print(get_days_in_month(2021, 'December'))