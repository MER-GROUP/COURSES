'''
Функция ranges() 🌶️
Будем считать, что последовательность целых неотрицательных чисел можно преобразовать в отрезок, 
если разница между соседними элементами этой последовательности равна единице. Например, 
числа 3, 4, 5, 6, 7,8 можно преобразовать в отрезок [3;8]. Числа 1, 3, 5, 11, 15, 22 в отрезок 
преобразовать нельзя. Одиночное число преобразуется в отрезок, в котором и правой, 
и левой границей является оно само. Например, число 1 можно преобразовать в отрезок [1;1].

Реализуйте функцию ranges(), которая принимает один аргумент:

numbers — список различных натуральных чисел, расположенных в порядке возрастания

Функция должна преобразовывать числа из списка numbers в отрезки, представляя их в виде кортежей, 
где первый элемент кортежа является левой границей отрезка, второй элемент — правой границей отрезка. 
Полученные кортежи-отрезки функция должна возвращать в виде списка.

Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию ranges(), 
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/674986/tests_2807351.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.11/Module_10.11.15

Sample Input 1:
numbers = [1, 2, 3, 4, 7, 8, 10]
print(ranges(numbers))
Sample Output 1:
[(1, 4), (7, 8), (10, 10)]

Sample Input 2:
numbers = [1, 3, 5, 7]
print(ranges(numbers))
Sample Output 2:
[(1, 1), (3, 3), (5, 5), (7, 7)]

Sample Input 3:
numbers = [1, 2, 3, 4, 5, 6, 7]
print(ranges(numbers))
Sample Output 3:
[(1, 7)]
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

def ranges(numbers: int) -> list[tuple]:
    arr = list()
    numbers_it = iter(numbers)
    arr.append([next(numbers_it)])
    for el in numbers_it:
        if 1 == abs(arr[-1][-1] - el):
            arr[-1].extend([el])
        else:
            arr.append([el])

    return list(
        (t[0], t[-1]) 
        for t in arr
    )

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 7, 8, 10]
    print(ranges(numbers))

    numbers = [1, 3, 5, 7]
    print(ranges(numbers))

    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(ranges(numbers))