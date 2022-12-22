print('------------------')

import time

start_time = time.time()

for i in range(5): 
    print(i)
    time.sleep(1)

end_time = time.time()

elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')

print('------------------')

import time

start_time = time.monotonic()

for i in range(5): 
    print(i)
    time.sleep(0.5)

end_time = time.monotonic()

elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')

print('------------------')

import time

start_time = time.perf_counter()

for i in range(5): 
    print(i)
    time.sleep(1)

end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')

print('------------------')

# функция из модуля math 
from math import factorial                       

# рекурсивная функция
def factorial_recurrent(n):                  
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)    

# итеративная функция
def factorial_classic(n):                    
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print('------------------')