'''
Функция alternating_sequence()
Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:

count — натуральное число, по умолчанию имеет значение None

Если count имеет значение None, функция должна возвращать генератор, порождающий бесконечный 
знакочередующийся ряд натуральных чисел.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, 
порождающий первые count чисел знакочередующегося ряда натуральных чисел, а затем возбуждающий 
исключение StopIteration.

Примечание 1. Знакочередующийся ряд натуральных чисел имеет вид:

1, -2, 3, -4, 5, -6, 7, -8, 9, -10, ...

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную  
функцию alternating_sequence(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640048/tests_2774515.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.5/Module_10.5.16

Sample Input 1:
generator = alternating_sequence()
print(next(generator))
print(next(generator))
Sample Output 1:
1
-2

Sample Input 2:
generator = alternating_sequence(10)
print(*generator)
Sample Output 2:
1 -2 3 -4 5 -6 7 -8 9 -10
'''
from __future__ import annotations
from _collections_abc import Generator

def alternating_sequence(count: int = None) -> Generator:
        index, num = 0, 1
        if count is None: count = float('inf')
        while index < count:
            yield (num, num*-1)[not num % 2]
            num += 1
            index += 1

if __name__ == '__main__':
    generator = alternating_sequence()
    print(next(generator))
    print(next(generator))

    generator = alternating_sequence(10)
    print(*generator)