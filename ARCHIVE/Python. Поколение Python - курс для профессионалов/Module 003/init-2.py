print('------------------')

from datetime import date, time

my_date = date(2021, 8, 10)
my_time = time(7, 18, 34)

# вывод в ISO формате
print(my_date)    
# вывод в ISO формате                         
print(my_time)  

# форматированный вывод даты
print(my_date.strftime('%d/%m/%y'))  
# форматированный вывод даты      
print(my_date.strftime('%A %d, %B %Y')) 
# форматированный вывод времени   
print(my_time.strftime('%H.%M.%S'))        

print('------------------')

from datetime import date, time

my_date = date(2021, 8, 10)
my_time = time(7, 18, 34)

print(my_date.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))
print(my_time.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))

print('------------------')

from datetime import date, time

given_date = date(2021, 7, 17)

print(given_date.strftime('%A %d %B %Y'))
print(given_date.strftime('%Y/%m/%d'))
print(given_date.strftime('%d.%m.%Y (%A, %B)'))
print(given_date.strftime('Day of year: %j, week number: %U'))

print('------------------')

from datetime import date, time

given_time = time(14, 4, 29)

print(given_time.strftime('Hours: %H, minutes: %M, seconds: %S.'))
print(given_time.strftime('%H:%M:%S'))
print(given_time.strftime('%I:%M:%S %p'))

print('------------------')

from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

my_date = date(2021, 8, 10)
# форматированный вывод даты в русской локализации
print(my_date.strftime("%A %d, %B %Y"))    

print('------------------')

from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(21, 15, 17)

print('Дата: ' + my_date.isoformat())
print('Время: ' + my_time.isoformat())

print('------------------')

from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(21, 15, 17)

print('Дата: ' + str(my_date))
print('Время: ' + str(my_time))

print('------------------')

from datetime import date
import locale

# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

my_date = date(2021, 8, 10)
# форматированный вывод даты в русской локализации
print(my_date.strftime("%A %d, %B %Y"))    

print('------------------')

import locale
print(locale.getlocale())

print('------------------')