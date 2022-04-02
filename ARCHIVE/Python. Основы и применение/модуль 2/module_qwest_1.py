# модуль datetime и методы date, timedelta
from datetime import date, timedelta

d = [int(i) for i in input().split()]

# хранение даты
my_date = date(*d)
#print(type(my_date))
#print(my_date)

days = int(input())

# хранкние количества дней
my_delta = timedelta(days)
#print(type(my_delta))
#print(my_delta)

# сумируем дату и дни
my_date += my_delta
#print(my_date)

res = str(my_date).replace('-', ' ')
arr = [str(int(i)) for i in res.split()]
print(' '.join(arr))