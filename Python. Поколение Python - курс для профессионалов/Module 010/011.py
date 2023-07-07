'''
Функция random_numbers()
Реализуйте функцию random_numbers(), которая принимает два аргумента:

left — целое число
right — целое число

Функция должна возвращать итератор, генерирующий бесконечную последовательность 
случайных целых чисел в диапазоне от left до right включительно.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый 
итератор random_numbers(), но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/668595/tests_2771229.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.3/Module_10.3.16


Sample Input 1:
iterator = random_numbers(1, 1)
print(next(iterator))
print(next(iterator))
Sample Output 1:
1
1

Sample Input 2:
iterator = random_numbers(1, 10)
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
Sample Output 2:
True
True
True
'''
from random import randint

def random_numbers(left: int, right: int):
    return iter(lambda: randint(left, right), 'inf')

if __name__ == '__main__':
    iterator = random_numbers(1, 1)
    print(next(iterator))
    print(next(iterator))

    iterator = random_numbers(1, 10)
    print(next(iterator) in range(1, 11))
    print(next(iterator) in range(1, 11))
    print(next(iterator) in range(1, 11))