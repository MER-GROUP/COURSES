print('------------------')

import time

time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)
time_obj = time.struct_time(time_tuple)

print(time_obj)
print(type(time_obj))

print('------------------')

import time

result = time.localtime(1630387918)
print('Результат:', result)
print('Год:', result.tm_year)
print('Месяц:', result.tm_mon)
print('День:', result.tm_mday)
print('Час:', result.tm_hour)

print('------------------')

import time

result = time.localtime(1630387918)
print('Результат:', result)
print('Год:', result[0])
print('Месяц:', result[1])
print('День:', result[2])
print('Час:', result[3])

print('------------------')

import time

result = time.gmtime(1630387918)
print('Результат:', result)
print('Год:', result.tm_year)
print('Месяц:', result.tm_mon)
print('День:', result.tm_mday)
print('Час:', result.tm_hour)

print('------------------')

import time

time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)
time_obj = time.mktime(time_tuple)
print('Локальное время в секундах:', time_obj)

print('------------------')

import time

seconds = 1630377118

# возвращает struct_time
time_obj = time.localtime(seconds)            
print(time_obj)

# возвращает секунды из struct_time
time_seconds = time.mktime(time_obj)          
print(time_seconds)

print('------------------')

import time

time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)

result = time.asctime(time_tuple)
print('Результат:', result)

print('------------------')

import time

seconds = 1530377118
time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)

print(time.ctime(seconds))
print(time.asctime(time_tuple))

print('------------------')

import time

time_obj = time.localtime()
result = time.strftime('%d.%m.%Y, %H:%M:%S', time_obj)
print(result)

print('------------------')

import time

time_string = '1 September, 2021'
result = time.strptime(time_string, '%d %B, %Y')
print(result)

print('------------------')