'''
Удали пробелы
Дана строка, Вам требуется преобразовать все идущие подряд пробелы в один. 
Если пробелы есть в начале и в конце строки - их нужно убрать.

Входные данные
Длина строки не превосходит 1000.

Выходные данные
Выведите измененную строку.

Sample Input:
nz d urp lren s bwz  boom  t a   j    ho    vi
Sample Output:
nz d urp lren s bwz boom t a j ho vi
'''
import sys

# sys.stdin = open(file='020.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(
    map(
        str.strip,
        sys.stdin.readlines()
    )
)
# print(arr) # test

# print(arr[0].replace('  ', ' ').replace('  ', ' '))
print(' '.join(arr[0].split()))