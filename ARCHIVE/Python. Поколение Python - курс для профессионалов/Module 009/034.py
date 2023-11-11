'''
Функция matrix_to_dict()
Реализуйте функцию matrix_to_dict() с использованием аннотаций типов, 
которая принимает один аргумент:

matrix — матрица произвольной размерности, элементами которой 
являются целые или вещественные числа

Функция должна возвращать словарь, ключом в котором является 
номер строки матрицы, а значением — список элементов этой строки.

Примечание 1. Используйте встроенные типы (list, tuple, ...), 
а не типы из модуля typing. Также используйте нотацию |, а не тип Union из модуля typing.

Примечание 2. Под матрицей подразумеваются исключительно вложенные списки.

Примечание 3. Нумерация строк матрицы в возвращаемом функцией 
словаре должна начинаться с единицы.

Примечание 4. Элементы матрицы в списке должны располагаться 
в своем исходном порядке.

Примечание 5. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию matrix_to_dict(), но не код, вызывающий ее.

Примечание 6. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/655394/tests_2748227.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.6/Module_9.6.17

Sample Input 1:
matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
print(matrix_to_dict(matrix))
Sample Output 1:
{1: [5, 6, 7], 2: [8, 3, 2], 3: [4, 9, 8]}

Sample Input 2:
matrix = [[5.1, 6, 7.94]]
print(matrix_to_dict(matrix))
Sample Output 2:
{1: [5.1, 6, 7.94]}

Sample Input 3:
annotations = matrix_to_dict.__annotations__
print(annotations['return'])
Sample Output 3:
dict[int, list[int | float]]
'''
def matrix_to_dict(matrix: list[list[int|float]]) -> dict[int, list[int|float]]:
    return {i: v for i, v in enumerate(matrix, 1)}

if __name__ == '__main__':
    matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
    print(matrix_to_dict(matrix))

    matrix = [[5.1, 6, 7.94]]
    print(matrix_to_dict(matrix))

    annotations = matrix_to_dict.__annotations__
    print(annotations['return'])