print('------------------')

import calendar

for name in calendar.day_name:
    print(name)

print('------------------')

import calendar, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

for name in calendar.day_name:
    print(name)

print('------------------')

import calendar

names = list(calendar.day_name)
print(names)

print('------------------')

import calendar

names = calendar.day_name
print(*names)

print('------------------')

import calendar, locale

for name in calendar.day_abbr:
    print(name)

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

for name in calendar.day_abbr:
    print(name)

print('------------------')

import calendar, locale

english_names = list(calendar.month_name)
print(english_names)

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

russian_names = list(calendar.month_name)
print(russian_names)

print('------------------')

import calendar, locale

english_names = list(calendar.month_abbr)
print(english_names)

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

russian_names = list(calendar.month_abbr)
print(russian_names)

print('------------------')

import calendar

print(calendar.MONDAY)
print(calendar.TUESDAY)
print(calendar.WEDNESDAY)
print(calendar.THURSDAY)
print(calendar.FRIDAY)
print(calendar.SATURDAY)
print(calendar.SUNDAY)

print('------------------')

import calendar

# эквивалентно calendar.setfirstweekday(6)
calendar.setfirstweekday(calendar.SUNDAY)     

print('------------------')

import calendar

print(calendar.firstweekday())
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.firstweekday())

print('------------------')

import calendar

print(calendar.isleap(2020))
print(calendar.isleap(2021))

print('------------------')

import calendar

print(calendar.leapdays(2020, 2025))

print('------------------')

import calendar

# среда
print(calendar.weekday(2021, 9, 1))  
# четверг   
print(calendar.weekday(2021, 9, 2))     

print('------------------')

import calendar

# январь 2022 года
print(calendar.monthrange(2022, 1)) 
# сентябрь 2021 года    
print(calendar.monthrange(2021, 9))     

print('------------------')

import calendar

print(*calendar.monthcalendar(2021, 9), sep='\n')

print('------------------')

import calendar

print(calendar.month(2021, 9))
print(calendar.month(2021, 10))
print(calendar.month(2021, 9, w=3))
print(calendar.month(2021, 9, l=2))
print(calendar.month(2021, 9, w=5, l=2))

print('------------------')

import calendar

print(calendar.calendar(2021))
print(calendar.calendar(2023))

print('------------------')

import calendar, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
print(calendar.calendar(2022, m=4))

print('------------------')

import calendar

calendar.prmonth(2021, 9)
calendar.prcal(2021)

print('------------------')