'''
Четные и нечетные числа
Даны три целых числа A, B, C. Определить, 
есть ли среди них хотя бы одно четное и хотя бы одно нечетное.

Входные данные
Числа A, B, C, не превышающие по модулю 10000.

Выходные данные
Одна строка – "YES" или "NO".

Sample Input:
3
4
5
Sample Output:
YES
'''
# arr = (int(input()) for _ in range(3)) # not work
arr = [int(input()) for _ in range(3)]
print(
    'YES' if any(map(lambda x: 0 == x % 2, arr))\
            and any(map(lambda x: 1 == x % 2, arr))\
            else 'NO'
)