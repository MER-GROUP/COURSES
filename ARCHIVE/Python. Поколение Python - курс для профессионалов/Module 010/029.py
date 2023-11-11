'''
Функция matrix_by_elem()
Вам доступна генераторная функция matrix_by_elem(), которая принимает в качестве аргумента матрицу произвольной размерности и возвращает генератор, порождающий последовательность элементов переданной матрицы.

Перепишете данную функцию с использованием конструкции yield from, чтобы она выполняла ту же задачу.

Примечание 1. Под матрицей подразумеваются исключительно вложенные списки.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию matrix_by_elem(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640048/tests_3139057.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.5/Module_10.5.25

def matrix_by_elem(matrix):
    for row in matrix:
        for elem in row:
            yield elem

Sample Input:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(*matrix_by_elem(matrix))

Sample Output:
1 2 3 4 5 6 7 8 9
'''

from __future__ import annotations
from _collections_abc import Generator

# def matrix_by_elem(matrix):
#     for row in matrix:
#         for elem in row:
#             yield elem

def matrix_by_elem(matrix):
    for row in matrix:
        yield from row

def matrix_by_elem(matrix):
    yield from (el for elem in matrix for el in elem)
            
if __name__ == '__main__':
    matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    print(*matrix_by_elem(matrix))