'''
Симметричная ли матрица?
Проверьте, является ли двумерный массив симметричным относительно 
главной диагонали. Главная диагональ — та, которая идёт из левого 
верхнего угла двумерного массива в правый нижний.

Входные данные
Программа получает на вход число n, n ≤ 100, являющееся числом 
строк и столбцов в массиве. Далее во входном потоке идет n строк 
по nчисел, являющихся элементами массива.

Выходные данные
Программа должна выводить слово yes для симметричного массива 
и слово no для несимметричного.

Sample Input:
3
0 1 2
1 5 3
2 3 4
Sample Output:
yes
'''
import sys
# from array import array
# from copy import copy

# sys.stdin = open(file='042.csv', mode='rt', encoding='utf-8', newline='')
n, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
n = int(n)
# print(n) # test
arr = [ list(map(int, arr[i].split())) for i in range(n)]
# [print(*i) for i in arr]

# 1
if arr == list(map(list, zip(*arr))):
    print('yes')
else:
    print('no')

# 2
_exit = False
for coll in range(n):
    for row in range(n):
        if coll == row:
            continue
        elif arr[coll][row] == arr[row][coll]:
            continue
        else:
            print('no')
            _exit = True
            break
    if _exit:
        break
else:
    print('yes')