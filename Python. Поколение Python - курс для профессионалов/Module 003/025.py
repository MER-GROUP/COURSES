'''
Количество дней
Дополните приведенный ниже код, чтобы он вывел 
количество дней (целое число) между датами today и birthday.

from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = ____

print(days)
'''
from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = birthday - today

print(days.days)