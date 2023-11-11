'''
Функция sum_of_digits()

Реализуйте функцию sum_of_digits(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются натуральные числа

Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих 
в итерируемом объекте iterable.

Примечание 1. Рассмотрим набор чисел 13, 20, 41, 2, 2, 5 из первого теста. Сумма цифр 
всех представленных чисел будет равна:
1 + 3 + 2 + 0 + 4 + 1 + 2 + 2 + 5 = 20

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию sum_of_digits(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/674263/tests_2798509.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.10/Module_10.10.13

Sample Input 1:
print(sum_of_digits([13, 20, 41, 2, 2, 5]))
Sample Output 1:
20

Sample Input 2:
print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
Sample Output 2:
46

Sample Input 3:
print(sum_of_digits([123456789]))
Sample Output 3:
45
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

def sum_of_digits(iterable: Iterable):
    _chain = it.chain.from_iterable(map(str, iterable))
    return sum(map(int, _chain))

if __name__ == '__main__':
    print(sum_of_digits([13, 20, 41, 2, 2, 5]))

    print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

    print(sum_of_digits([123456789]))