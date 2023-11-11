'''
Функция get_all_mondays()
Реализуйте функцию get_all_mondays(), которая принимает один аргумент:

year — натуральное число

Функция должна возвращать отсортированный по возрастанию 
список всех дат (тип date) года year, выпадающих на понедельник.

Примечание 1. Например, вызов:

get_all_mondays(2021)

должен вернуть список:

[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., 
datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]

Примечание 2. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию get_all_mondays(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570049/tests_2575895.zip
'''
# from datetime import datetime, timedelta

# def get_all_mondays(year):
#     arr = list()
#     d = datetime(year=year, month=1, day=1)
#     while year == d.year:
#         if 1 == d.isoweekday():
#             arr.append(d.date())
#         d = d + timedelta(days=1)
#     return arr

# if __name__ == '__main__':
#     print(get_all_mondays(2021))

import calendar
from datetime import date

def get_all_mondays(year):
    mondays = []
    for month in range(1, 13):
        for week in calendar.monthcalendar(year, month):
            monday = week[0]
            if monday:
                mondays.append(date(year, month, monday))
    return mondays

if __name__ == '__main__':
    print(get_all_mondays(2021))