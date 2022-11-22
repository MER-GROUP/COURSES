'''
Alarm
Вам доступно время alarm. Дополните приведенный ниже код, 
чтобы он вывел следующие его компоненты:

количество часов в формате HH
количество минут в формате MM
количество секунд в формате SS

from datetime import time

alarm = time(7, 30, 25)

print('Часы:', alarm.____('____'))
print('Минуты:', alarm.____('____'))
print('Секунды:', alarm.____('____'))
'''
from datetime import time

alarm = time(7, 30, 25)

print('Часы:', alarm.strftime('%H'))
print('Минуты:', alarm.minute)
print('Секунды:', alarm.second)