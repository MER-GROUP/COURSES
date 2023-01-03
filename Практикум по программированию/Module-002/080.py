'''
Список степеней двойки
По данному числу N распечатайте все целые степени двойки, 
не превосходящие N, в порядке возрастания.

Операцией возведения в степень пользоваться нельзя!

Входные данные
Вводится натуральное число.

Выходные данные
Выведите ответ на задачу.

Sample Input:
50
Sample Output:
1 2 4 8 16 32
'''
n = int(input())
i = 1
while i <= n:
    print(i, end=' ')
    i += i 

# print()
# print('------')
# print(*range(int(__import__('math').log2(n)) + 1))
# print(1 << 0)
# print(1 << 1)
# print(1 << 2)
# print(1 << 3)
# print(1 << 4)
# print(1 << 5)

# print()
# print('------')
# print(int('1' + '0' * 0, 2))
# print(int('1' + '0' * 1, 2))
# print(int('1' + '0' * 2, 2))
# print(int('1' + '0' * 3, 2))
# print(int('1' + '0' * 4, 2))
# print(int('1' + '0' * 5, 2))

# print()
# print('------')
# print(int('1', 2))
# print(int('10', 2))
# print(int('100', 2))
# print(int('1000', 2))
# print(int('10000', 2))
# print(int('100000', 2))