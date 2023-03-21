'''
Ревью кода 3 😡
Требовалось написать программу, которая принимает на вход два целых числа a и b, 
каждое на отдельной строке, и выводит список всех целых чисел от a до b включительно, 
которые делятся на 7 без остатка. Программист торопился и написал программу неправильно.

Найдите и исправьте все ошибки, допущенные в этой программе (их ровно 5).

Примечание. Известно, что каждая ошибка затрагивает только одну строку 
и может быть исправлена без изменения других строк.

a = input()
b = input()
numbers = []

for i in range(a, b):
    if i // 7 == 0:
        numbers = numbers.append(i)

print(numbers)
'''
# a = int(input()) # 1
# b = int(input()) # 2
# numbers = []

# for i in range(a, b+1): # 3
#     if i % 7 == 0: # 4
#         numbers.append(i) # 5

# print(numbers)

import array
a,b = int(input()),int(input())
numbers = array.array('i',[])

for i in range(a, b+1):
    if i % 7 == 0:
        numbers.append(i)

print(list(numbers))