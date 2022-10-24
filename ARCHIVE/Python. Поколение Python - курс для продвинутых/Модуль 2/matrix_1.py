# создание матрицы
print('##########')
matrix  = [[2, -5, -11, 0],
           [-9, 4, 6, 13],
           [4, 7, 12, -2]]

print(matrix[1][2])

# Перебор элементов матрицы
# rows - количество строк, cols - количество столбцов
print('##########')
rows, cols = 3, 4
matrix  = [[2, 3, 1, 0],
           [9, 4, 6, 8],
           [4, 7, 2, 7]]

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()
 
# перебор элементов по столбцам
# rows - количество строк, cols - количество столбцов
print('##########')
rows, cols = 3, 4

matrix  = [[2, 3, 1, 0],
           [9, 4, 6, 8],
           [4, 7, 2, 7]]

for c in range(cols):
    for r in range(rows):
        print(matrix[r][c], end=' ')
    print()
    
# Функции ljust() и rjust()
# rows - количество строк, cols - количество столбцов
print('##########')
rows, cols = 3, 4

matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()
    
# Метод ljust()
print('##########')
print('a'.ljust(3)+'1')
print('ab'.ljust(3)+'1')
print('abc'.ljust(3)+'1')
print('abcdefg'.ljust(3)+'1')

print('a'.ljust(5, '*'))
print('ab'.ljust(5, '$'))
print('abc'.ljust(5, '#'))

# Метод rjust()
print('##########')
print('a'.rjust(3))
print('ab'.rjust(3))
print('abc'.rjust(3))
print('abcdefg'.rjust(3))

print('a'.rjust(5, '*'))
print('ab'.rjust(5, '$'))
print('abc'.rjust(5, '#'))

# выравнивание столбцов
print('##########')
rows, cols = 3, 4

matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]

for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(6), end='')
    print()
    
# элементы главной и побочной диагонали
print('##########')
n = 8
# создаем квадратную матрицу размером 8×8
matrix = [[0]*n for _ in range(n)]
# заполняем главную диагональ 1-цами, а побочную 2-ками
for i in range(n):
    matrix[i][i] = 1
    matrix[i][n-i-1] = 2
# выводим матрицу
for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
    
'''
Индексы i и j элементов на главной диагонали связаны соотношением i = j. 

Индексы i и j элементов на побочной диагонали связанны соотношением i + j + 1 = n (или  j = n - i - 1), где n — размерность матрицы

Заметим также, что:

если элемент находится выше главной диагонали, то i < j, если ниже, i > j.
если элемент находится выше побочной диагонали, то i + j + 1 < n, если ниже, i + j + 1 > n.
'''

# Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:
def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()
        
# Для считывания матрицы из n строк, заполненной числами, удобно использовать следующий код:
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)