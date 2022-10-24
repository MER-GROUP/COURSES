'''
Требовалось написать программу, которая:

преобразует список floats в список чисел, возведенных в квадрат и округленных 
с точностью до одного десятичного знака;
фильтрует список words  и оставляет только палиндромы длиной более 4 символов;
находит произведение чисел из списка numbers.
Программист торопился и написал программу неправильно. Доработайте его программу.
'''
# Решение
from functools import reduce 

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(round, map(lambda num: num**2, floats), [1] * len(floats)))
filter_result = list(filter(lambda name: name == name[::-1] and 4 < len(name), words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)

print(map_result)
print(filter_result)
print(reduce_result)
