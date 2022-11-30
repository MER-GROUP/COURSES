print('------------------')

from datetime import datetime

# создаем полную дату-время
my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)  
# создаем дату-время с нулевой временной информацией  
only_date = datetime(2021, 12, 31)                       

print(my_datetime)
print(only_date)
print(type(my_datetime))

print('------------------')

from datetime import datetime

my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)

print('Год =', my_datetime.year)
print('Месяц =', my_datetime.month)
print('День =', my_datetime.day)
print('Часы =', my_datetime.hour)
print('Минуты =', my_datetime.minute)
print('Секунды =', my_datetime.second)
print('Микросекунды =', my_datetime.microsecond)

print('------------------')

from datetime import date, time, datetime

my_date = date(1992, 10, 6)
my_time = time(10, 45, 17)
my_datetime = datetime.combine(my_date, my_time)

print(my_datetime)

print('------------------')

from datetime import date, time, datetime

my_datetime = datetime(2022, 10, 7, 14, 15, 45)
# получаем только дату (тип date)
my_date = my_datetime.date()    
# получаем только время (тип time)                 
my_time = my_datetime.time()                     

print(my_datetime, type(my_datetime))
print(my_date, type(my_date))
print(my_time, type(my_time))

print('------------------')

from datetime import datetime

datetime_now = datetime.now()
datetime_utcnow = datetime.utcnow()
datetime_today = datetime.today()

# текущее локальное время (московское) на момент запуска программы
print(datetime_now) 
# текущее UTC время на момент запуска программы          
print(datetime_utcnow)     
# today
print(datetime_today)  

print('------------------')

from datetime import datetime

my_datetime = datetime(2021, 10, 13, 8, 10, 23)
print(my_datetime.timestamp())

print('------------------')

from datetime import datetime

my_datetime = datetime.fromtimestamp(1634101823.0)
print(my_datetime)

print('------------------')

from datetime import datetime

my_datetime = datetime(2021, 8, 10, 18, 20, 34)

# вывод в ISO формате
print(my_datetime)                                            
print(my_datetime.strftime('%d.%m.%y --- %H::%M::%S'))
print(my_datetime.strftime('%d/%m/%y'))
print(my_datetime.strftime('%A %d, %B %Y'))
print(my_datetime.strftime('%H:%M:%S'))

print('------------------')

from datetime import datetime

datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС ')

date_str, time_str = datetime_str.split(' ')

date_info = [int(i) for i in date_str.split('.')]
time_info = [int(i) for i in time_str.split(':')]

my_datetime = datetime(date_info[2], date_info[1], date_info[0], time_info[0], time_info[1], time_info[2])

print(my_datetime)

print('------------------')

from datetime import datetime

datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС ')
my_datetime = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M:%S')
print(my_datetime)

print('------------------')

from datetime import datetime

datetime0 = datetime.strptime('10.08.2034 13:55:59', '%d.%m.%Y %H:%M:%S')
datetime1 = datetime.strptime('10/08/21', '%d/%m/%y')
datetime2 = datetime.strptime('Tuesday 10, August 2021', '%A %d, %B %Y')
datetime3 = datetime.strptime('18.20.34', '%H.%M.%S')
datetime4 = datetime.strptime('2021/08/10', '%Y/%m/%d')
datetime5 = datetime.strptime('10.08.2021 (Tuesday, August)', '%d.%m.%Y (%A, %B)')
datetime6 = datetime.strptime('Year: 2021, Month: 08, Day: 10, Hour: 18.', 'Year: %Y, Month: %m, Day: %d, Hour: %H.')

print(datetime0, datetime1, datetime2, datetime3, datetime4, datetime5, datetime6, sep='\n')

print('------------------')

from datetime import datetime

my_datetime = datetime.strptime('10/08/2034 13:55:59', '%d.%m.%Y %H:%M:%S')
print(my_datetime)

print('------------------')

from datetime import datetime

datetime1 = datetime(1992, 10, 6, 10, 12, 45)
datetime2 = datetime1.replace(year=1995, month=12)         
datetime3 = datetime1.replace(day=17, hour=14, minute=37)

print(datetime1)
print(datetime2)
print(datetime3)

print('------------------')

from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
my_datetime = datetime(2021, 8, 10, 12, 34, 15)
print(my_datetime.strftime('%A %d, %B %Y, %H:%M:%S'))

print('------------------')

from datetime import datetime

my_datetime = datetime(1992, 10, 6, 10, 12, 45)

print(my_datetime.isoformat())
print(str(my_datetime))

print('------------------')