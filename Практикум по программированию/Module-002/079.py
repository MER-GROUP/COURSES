'''
Минимальный делитель
Дано целое число, не меньшее 2. 
Выведите его наименьший натуральный делитель, отличный от 1.

Входные данные
Вводится натуральное число.

Выходные данные
Выведите ответ на задачу.

Sample Input:
122
Sample Output:
2
'''
# n = int(input())
# min = __import__('sys').maxsize
# i = 2
# while i <= n+1:
#     if not n % i and min > i:
#         min = i
#     i += 1
# print(min)

# n, i = int(input()), 2
# while n % i:
#     i += 1
# print(i)

# num = int(input())

# for i in range(2,num//2+2):
#     if num%i==0:
#         print(i)
#         break
# else:
#     print(num)

[next(print(i) for i in range(2, n + 1) if not n % i) for n in [int(input())]]