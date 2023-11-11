print('------------------')

from datetime import timedelta

delta = timedelta(days=7, hours=20, minutes=7, seconds=17)
print(delta)
print(type(delta))

print('------------------')

from datetime import timedelta

delta1 = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
delta2 = timedelta(weeks=1, hours=23, minutes=61)
delta3 = timedelta(hours=25)
delta4 = timedelta(minutes=300)

print(delta1, delta2, delta3, delta4, sep='\n')

print('------------------')

from datetime import timedelta

delta1 = timedelta(minutes=-40)
delta2 = timedelta(seconds=-10, weeks=-2)

print(delta1)
print(delta2)

print('------------------')

from datetime import timedelta

delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)

print('Количество дней =', delta.days)
print('Количество секунд =', delta.seconds)
print('Количество микросекунд =', delta.microseconds)

print('Общее количество секунд =', delta.total_seconds())

print('------------------')

from datetime import timedelta

def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60

delta = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)
hours, minutes = hours_minutes(delta)

print(delta)
print(hours)
print(minutes)

print('------------------')

from datetime import timedelta

delta1 = timedelta(weeks=1)
delta2 = timedelta(hours=24*7)
delta3 = timedelta(minutes=24*7*59)

print(delta1 == delta2)
print(delta1 != delta3)
print(delta1 < delta3)

print('------------------')

from datetime import timedelta

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)

print(delta1 != 57)
print(delta2 == '5')

print('------------------')

from datetime import timedelta

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)

print(delta2 > delta1) # тут все ок
# print(delta2 > 5)

print('------------------')

from datetime import timedelta

# 5 дней + 1 час
delta1 = timedelta(days=5) + timedelta(seconds=3600) 
# 5 дней - 1 час 
delta2 = timedelta(days=5) - timedelta(seconds=3600)  

print(delta1)
print(delta2)

print('------------------')

from datetime import timedelta

delta1 = 48 * timedelta(hours=1)
delta2 = timedelta(weeks=1) * (3/7)

print(delta1)
print(delta2)

print('------------------')

from datetime import timedelta

delta = timedelta(hours=1, minutes=6)
delta1 = delta / 2
delta2 = delta // 5

print(delta1)
print(delta2)

print('------------------')

from datetime import timedelta

# обычное деление, результат float
delta1 = timedelta(weeks=1) / timedelta(hours=5)  
# целочисленное деление, результат int     
delta2 = timedelta(weeks=1) // timedelta(hours=5)      

print(delta1)
print(delta2)

print('------------------')

from datetime import timedelta

delta1 = timedelta(weeks=1) % timedelta(hours=5) # 3 часа        
delta2 = timedelta(hours=1) % timedelta(minutes=7) # 4 минуты

print(delta1)
print(delta2)

print('------------------')

from datetime import timedelta

all_time = timedelta(days=3)
smena = timedelta(hours=7, minutes=30)

print(all_time // smena)
print(all_time % smena)

print('------------------')

from datetime import datetime, date, timedelta

my_datetime1 = datetime(2021, 1, 1, 12, 15, 20) + timedelta(weeks=1, hours=25)
my_datetime2 = datetime(2021, 1, 1, 12, 15, 20) - timedelta(weeks=1, hours=25)

my_date1 = date(2021, 1, 1) + timedelta(hours=49)
my_date2 = date(2021, 1, 1) - timedelta(hours=49)

print(my_datetime1, my_datetime2, my_date1, my_date2, sep='\n')

print('------------------')

from datetime import datetime, date, timedelta

delta1 = datetime(2021, 1, 1, 12, 15, 20) - datetime(2020, 5, 1, 10, 5, 10)
delta2 = date(2020, 2, 29) - date(2019, 9, 1)
delta3 = date(2019, 9, 1) - date(2020, 2, 29)

print(delta1)
print(delta2)
print(delta3)

print('------------------')

from datetime import timedelta

delta1 = timedelta(weeks=1, hours=23, minutes=61)
delta2 = timedelta(minutes=-300)

print(str(delta1), str(delta2), sep='\n')
print(repr(delta1), repr(delta2), sep='\n')

print('------------------')

from datetime import timedelta

delta = timedelta(days=-2, minutes=-300)
abs_delta = abs(delta)

print('Исходная:', delta.days, delta.seconds, delta, sep='\n')
print('С модулем:', abs_delta.days, abs_delta.seconds, abs_delta, sep='\n')

print('------------------')