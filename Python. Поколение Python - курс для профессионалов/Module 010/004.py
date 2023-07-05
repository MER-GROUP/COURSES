'''
Транспонированная матрица — матрица A^T, полученная из исходной матрицы A заменой строк на столбцы.
То есть для получения транспонированной матрицы из исходной нужно каждую строчку 
исходной матрицы записать в виде столбца в том же порядке.

Реализуйте функцию transpose() с использованием функции zip(), которая принимает один аргумент:

matrix — матрица произвольной размерности

Функция должна возвращать транспонированную матрицу matrix.

Примечание 1. Под матрицей подразумеваются исключительно вложенные списки.

Примечание 2. Функция должна возвращать новую матрицу, а не изменять переданную.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию transpose(), 
но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640044/tests_2768655.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.2/Module_10.2.21

Sample Input 1:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for row in transpose(matrix):
    print(row)
Sample Output 1:
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

Sample Input 2:
matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10]]
for row in transpose(matrix):
    print(row)
Sample Output 2:
[1, 6]
[2, 7]
[3, 8]
[4, 9]
[5, 10]
'''
def transpose(matrix: list) -> list:
    return list(map(list, zip(*matrix)))

if __name__ == '__main__':
    matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    for row in transpose(matrix):
        print(row)

    matrix = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10]]
    for row in transpose(matrix):
        print(row)