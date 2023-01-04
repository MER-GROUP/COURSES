'''
Двоичный логарифм
По данному натуральному числу N выведите такое наименьшее целое число k, что 2^k≥N.

Операцией возведения в степень пользоваться нельзя!

Входные данные
Вводится натуральное число N.

Выходные данные
Выведите ответ на задачу.

Sample Input:
7
Sample Output:
3
'''
n = int(input())
i = 1
count = 0
while i <= n:
    i += i 
    count += 1
    if i >= n:
        break
print(count)

# from math import ceil, log2
# print(ceil(log2(n)))