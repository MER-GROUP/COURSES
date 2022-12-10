'''
Количество равных из трех

Входные данные
Даны три целых числа, записанных в отдельных строках. 
Определите, сколько среди них совпадающих.

Выходные данные
Программа должна вывести одно из чисел: 
3 (если все совпадают), 2 (если два совпадают) или 0 (если все числа различны).

Sample Input:
4
3
4
Sample Output:
2
'''
a, b, c = (int(input()) for _ in range(3))
if (a == b == c):
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)