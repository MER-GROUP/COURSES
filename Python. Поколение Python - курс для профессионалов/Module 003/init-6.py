print('------------------')

import time

# получаем количество прошедших секунд в виде float числа
seconds = time.time()
print('Количество секунд с начала эпохи =', seconds)

print('------------------')

import time

# получаем количество прошедших секунд в виде float числа
seconds = time.time_ns()
print('Количество нано секунд с начала эпохи =', seconds)

print('------------------')

import time

seconds = 1630387918.354396
local_time = time.ctime(seconds)
print('Местное время:', local_time)

print('------------------')

import time

# вызов функции без аргумента
local_time = time.ctime()
print('Местное время:', local_time)

print('------------------')

import time

seconds = time.time()
local_time = time.ctime(seconds)
print('Местное время:', local_time)

print('------------------')

import time 

print('Before the sleep statement')
time.sleep(3)
print('After the sleep statement')

print('------------------')

import time 

print('Before the sleep statement')
time.sleep(0.7)
print('After the sleep statement')

print('------------------')

import time

for i in [0.7, 0.5, 1.0, 2.5, 3.3]:
    print(f'Waiting for {i} seconds')
    time.sleep(i)
print('The end')

print('------------------')