print('------------------')

# Приведенный ниже код:
from datetime import date
# тип date: год + месяц + день
my_date = date(1992, 10, 6)    
print(my_date)
print(type(my_date))

print('------------------')

from datetime import date

my_date = date(1992, 10, 6)
print('Год =', my_date.year)
print('Месяц =', my_date.month)
print('День =', my_date.day)

print('------------------')

from datetime import date

creation_date = date.today()
print(creation_date)

print('------------------')

from datetime import date

date1 = date(2022, 10, 15)
date2 = date(1999, 12, 26)
print(date1.weekday())
print(date2.weekday())

print('------------------')

from datetime import date

date1 = date(2022, 10, 15)
date2 = date(1999, 12, 26)
print(date1.isoweekday())
print(date2.isoweekday())

print('------------------')

from datetime import date

print(date.min)
print(date.max)

print('------------------')

# дата, соответствуюшая номеру дня 365
date1 = date.fromordinal(365)     
date2 = date(1999, 12, 26)
print(date1)
# номер дня, соответствующий дате 1999-12-26
print(date2.toordinal())  

print('------------------')

# Приведенный ниже код:
from datetime import time

# тип time: часы + минуты + секунды + микросекунды
my_time = time(11, 20, 54, 1234)    
print(my_time)
print(type(my_time))

print('------------------')

# Приведенный ниже код:
from datetime import time

time1 = time(11, 20, 54, 1234)
time2 = time(11, 20, 54)
time3 = time(11, 20)
time4 = time(11)
time5 = time()
time6 = time(minute=23, second=56)
print(time1, time2, time3, time4, time5, sep='\n')
print(time6)

print('------------------')

from datetime import time

my_time = time(11, 20, 54, 1234)
print('Часы =', my_time.hour)
print('Минуты =', my_time.minute)
print('Секунды =', my_time.second)
print('Микросекунды =', my_time.microsecond)

print('------------------')

# Приведенный ниже код:
from datetime import date, time

date1 = date(2022, 10, 15)
date2 = date(1999, 12, 26)
time1 = time(13, 10, 5)
time2 = time(21, 32, 59)
print(date1 < date2)
print(time1 < time2)

print('------------------')

# Приведенный ниже код:
from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(11, 20, 54)
print(my_date)
print(my_time)

print('------------------')

from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(11, 20, 54)

print(str(my_date))
print(str(my_time))

print('------------------')

# Приведенный ниже код:
from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(11, 20, 54)
print(repr(my_date))
print(repr(my_time))

print('------------------')

# Приведенный ниже код:
from datetime import date

# список дат
dates = [date(2021, 12, 31), date(2019, 10, 6), date(2022, 11, 8)]   
print(dates)

print('------------------')

# Приведенный ниже код:
from datetime import date

dates = [date(2021, 12, 31), date(2019, 10, 6), date(2022, 11, 8)]
print(*dates, sep='\n')

print('------------------')

# Приведенный ниже код:
from datetime import date

# множество
my_set = {date(2021, 12, 31), date(2019, 3, 19), date(2022, 5, 25)}         
 # словарь   
my_dict = {date(2021, 12, 31): 'Новый год', date(2030, 10, 6): 'День рождения'}    
print(my_set)
print(my_dict)

print('------------------')

# Приведенный ниже код:
from datetime import date, time

dates = [date(2021, 12, 31), date(2025, 3, 19), date(2017, 5, 25)]
print(min(dates))
print(max(dates))
print(sorted(dates))

print('------------------')

# Приведенный ниже код:
from datetime import date

date1 = date(1992, 10, 6)
# заменяем год  
date2 = date1.replace(year=1995)   
# заменяем месяц и число                  
date3 = date1.replace(month=12, day=17)     
print(date1)
print(date2)
print(date3)

print('------------------')

# Приведенный ниже код:
from datetime import time

time1 = time(17, 10, 6)
# заменяем час   
time2 = time1.replace(hour=21)   
# заменяем минуты и секунды                     
time3 = time1.replace(minute=48, second=59)     
print(time1)
print(time2)
print(time3)

print('------------------')

# Приведенный ниже код:
from datetime import date

# несуществующий месяц
my_date = date(2021, 19, 7)     
print(my_date)

print('------------------')